# Trần Thiện Nhân
# 2111913

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class NoneType(Type): pass

class FuncType(Type):
    def __init__(self, returnType = NoneType(), paramType = [], body = False):
        self.returnType = returnType
        self.paramType = paramType
        self.body = body

class Symbol:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Tools:
    def inferType(self, name, lst, type, isFunc = False):
        for env in lst:
            for sym in env:
                if sym.name == name and (type(sym.type) == FuncType) == isFunc:
                    if isFunc: sym.type.returnType = type
                    else: sym.type = type
                    return type

    def isNoneType(self, type):
        return type(type) is NoneType or (type(type) is ArrayType and self.isNoneType(type.eleType))

    def inferNone(self, dstCtx, dstType, srcType, stmt, o):
        if type(dstType) is NoneType:
            if type(dstCtx) is Id: return self.inferType(dstCtx.name, o, srcType)
            else: return self.inferType(dstCtx.name.name, o, srcType, True)
        else:
            raise TypeCannotBeInferred(stmt)

    def sizeIn(self, src, dst):
        if len(src) > len(dst): return False
        for i in range(len(src)):
            if src[i] != dst[i]: return False
        return True

    def isEqualParam(self, src, dst):
        if len(src) != len(dst): return False
        for i in range(len(src)):
            if not self.isEquivalentType(src[i], dst[i]): return False
        return True
    
    def isEquivalentType(self, src, dst):
        if type(src) is ArrayType and type(dst) is ArrayType:
            return self.isEquivalentType(src.eleType, dst.eleType) and self.sizeIn(src.size, dst.size) and self.sizeIn(dst.size, src.size)
        return type(src) is type(dst)

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.inFunc = None
        self.inLoop = 0
        self.curStmt = None
        self.haveReturn = False

    def check(self):
        self.visit(self.ast, [[]])
        return ""

    def visitProgram(self, ctx, o):
        o = [[
            Symbol("readNumber", FuncType(NumberType(), [], True)),
            Symbol("writeNumber", FuncType(VoidType(), [NumberType()], True)),
            Symbol("readBool", FuncType(BoolType(), [], True)),
            Symbol("writeBool", FuncType(VoidType(), [BoolType()], True)),
            Symbol("readString", FuncType(StringType(), [], True)),
            Symbol("writeString", FuncType(VoidType(), [StringType()], True))
        ]]
        for x in ctx.decl:
            self.visit(x, o)
        for sym in o[0]:
            if type(sym.type) is FuncType and sym.type.body is False:
                raise NoDefinition(sym.name)
        flag = False
        for sym in o[0]:
            if sym.name == 'main' and type(sym.type) is FuncType and type(sym.type.returnType) is VoidType and len(sym.type.paramType) == 0:
                flag = True
                break
        if not flag: raise NoEntryPoint()

    def visitFuncDecl(self, ctx, o):
        self.curStmt = ctx
        self.haveReturn = False
        funcType = FuncType(NoneType(), [x.varType for x in ctx.param], ctx.body is not None)
        env = [[]]
        if funcType.body is True:
            temp = [[]]
            try:
                for x in ctx.param:
                    self.visit(x, temp)
            except Redeclared as e:
                raise Redeclared(Parameter(), e.name)
            env = temp + o
        isInO = False
        for en in o:
            for sym in en:
                if sym.name == ctx.name.name and type(sym.type) is FuncType:
                    if Tools().isEqualParam(sym.type.paramType, funcType.paramType) and sym.type.body is False:
                        if funcType.body is True:
                            isInO = True
                            sym.type.body = True
                            funcType = sym.type
                            break
                    raise Redeclared(Function(), ctx.name.name)
        if not isInO:
            o[0].append(Symbol(ctx.name.name, funcType))
        if funcType.body is True:
            self.inFunc = Symbol(ctx.name.name, funcType)
            self.visit(ctx.body, env)
            for env in o:
                for sym in env:
                    if sym.name == ctx.name.name and type(sym.type) is FuncType:
                        if type(sym.type.returnType) is NoneType:
                            Tools().inferType(ctx.name.name, o, VoidType(), True)
                            self.inFunc = None
                            break
                        elif type(sym.type.returnType) is not VoidType and not self.haveReturn:
                            raise TypeMismatchInStatement(ctx.body)

    def visitVarDecl(self, ctx, o):
        self.curStmt = ctx
        for sym in o[0]:
            if sym.name == ctx.name.name and type(sym.type) is not FuncType:
                raise Redeclared(Variable(), ctx.name.name)
        type = NoneType() if ctx.varType is None else ctx.varType
        o[0].append(Symbol(ctx.name.name, type))
        if ctx.varInit is not None:
            initType = self.visit(ctx.varInit, o)
            type = self.visit(ctx.name, o)
            self.assignType(ctx, ctx.name, type, ctx.varInit, initType, o, True)

    def visitAssign(self, ctx, o):
        self.curStmt = ctx
        rType = self.visit(ctx.rhs, o)
        lType = self.visit(ctx.lhs, o)
        self.assignType(ctx, ctx.lhs, lType, ctx.rhs, rType, o, True)

    def visitIf(self, ctx, o):
        self.curStmt = ctx
        exprType = self.visit(ctx.expr, o)
        if Tools().isNoneType(exprType):
            exprType = Tools().inferNone(ctx.expr, exprType, BoolType(), self.curStmt, o)
        elif type(exprType) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt, o)
        self.curStmt = ctx
        if ctx.elifStmt is not None:
            for (expr, stmt) in ctx.elifStmt:
                exprType = self.visit(expr, o)
                if Tools().isNoneType(exprType):
                    exprType = Tools().inferNone(expr, exprType, BoolType(), self.curStmt, o)
                elif type(exprType) is not BoolType:
                    raise TypeMismatchInStatement(ctx)
                self.visit(stmt, o)
                self.curStmt = ctx
        if ctx.elseStmt is not None:
            self.visit(ctx.elseStmt, o)

    def visitFor(self, ctx, o):
        self.curStmt = ctx
        varType = self.visit(ctx.name, o)
        if Tools().isNoneType(varType):
            varType = Tools().inferNone(ctx.name, varType, NumberType(), self.curStmt, o)
        elif type(varType) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        condType = self.visit(ctx.condExpr, o)
        if Tools().isNoneType(condType):
            condType = Tools().inferNone(ctx.condExpr, condType, BoolType(), self.curStmt, o)
        elif type(condType) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        updType = self.visit(ctx.updExpr, o)
        if Tools().isNoneType(updType):
            updType = Tools().inferNone(ctx.updExpr, updType, NumberType(), self.curStmt, o)
        elif type(updType) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        self.inLoop +=  1
        self.visit(ctx.body, o)
        self.inLoop -=  1

    def visitBreak(self, ctx, o):
        if self.inLoop == 0: raise MustInLoop(ctx)

    def visitContinue(self, ctx, o):
        if self.inLoop == 0: raise MustInLoop(ctx)

    def visitReturn(self, ctx, o):
        self.curStmt = ctx
        if ctx.expr is not None:
            reType = self.visit(ctx.expr, o)
            self.assignType(ctx, CallStmt(Id(self.inFunc.name),[]), self.inFunc.type.returnType, ctx.expr, reType, o, True)
        else:
            if type(self.inFunc.type.returnType) is NoneType:
                self.inFunc.type.returnType = Tools().inferType(self.inFunc.name, o, VoidType(), True)
            elif type(self.inFunc.type.returnType) is not VoidType:
                raise TypeMismatchInStatement(ctx)
        self.haveReturn = True

    def visitCallStmt(self, ctx, o):
        self.curStmt = ctx
        type = None
        for env in o:
            for sym in env:
                if sym.name == ctx.name.name and type(sym.type) is FuncType:
                    type = sym.type
                    break
            if type is not None: break
        if type is None: raise Undeclared(Function(), ctx.name.name)
        if len(type.paramType) !=  len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        if type(type.returnType) is NoneType:
            Tools().inferType(ctx.name.name, o, VoidType(), True)
        if type(type.returnType) is not VoidType:
            raise TypeMismatchInStatement(ctx)
        for i in range(len(ctx.args)):
            argType = self.visit(ctx.args[i], o)
            self.assignType(ctx, ctx.args[i], argType, None, type.paramType[i], o, True)

    def visitBlock(self, ctx, o):
        env = [[]] + o
        for stm in ctx.stmt:
            self.visit(stm, env)

    def visitBinaryOp(self, ctx, o):
        e1type = self.visit(ctx.left, o)
        if ctx.op in ['+', '-', '*', '/', '%', '=', '!=', '>', '<', '>=', '<=']:
            if Tools().isNoneType(e1type):
                e1type = Tools().inferNone(ctx.left, e1type, NumberType(), self.curStmt, o)
            e2type = self.visit(ctx.right, o)
            if Tools().isNoneType(e2type):
                e2type = Tools().inferNone(ctx.right, e2type, NumberType(), self.curStmt, o)
            if [type(e1type), type(e2type)] != [NumberType, NumberType]:
                raise TypeMismatchInExpression(ctx)
            if ctx.op in ['+', '-', '*', '/', '%']:
                return NumberType()
            else:
                return BoolType()
        elif ctx.op in ['and', 'or']:
            if Tools().isNoneType(e1type):
                e1type = Tools().inferNone(ctx.left, e1type, BoolType(), self.curStmt, o)
            e2type = self.visit(ctx.right, o)
            if Tools().isNoneType(e2type):
                e2type = Tools().inferNone(ctx.right, e2type, BoolType(), self.curStmt, o)
            if [type(e1type), type(e2type)] != [BoolType, BoolType]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif ctx.op == '==':
            if Tools().isNoneType(e1type):
                e1type = Tools().inferNone(ctx.left, e1type, StringType(), self.curStmt, o)
            e2type = self.visit(ctx.right, o)
            if Tools().isNoneType(e2type):
                e2type = Tools().inferNone(ctx.right, e2type, StringType(), self.curStmt, o)
            if [type(e1type), type(e2type)] != [StringType, StringType]:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif ctx.op == '...':
            if Tools().isNoneType(e1type):
                e1type = Tools().inferNone(ctx.left, e1type, StringType(), self.curStmt, o)
            e2type = self.visit(ctx.right, o)
            if Tools().isNoneType(e2type):
                e2type = Tools().inferNone(ctx.right, e2type, StringType(), self.curStmt, o)
            if [type(e1type), type(e2type)] != [StringType, StringType]:
                raise TypeMismatchInExpression(ctx)
            return StringType()

    def visitUnaryOp(self, ctx, o):
        type = self.visit(ctx.operand, o)
        if ctx.op == 'not':
            if Tools().isNoneType(type):
                type = Tools().inferNone(ctx.operand, type, BoolType(), self.curStmt, o)
            if type(type) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif ctx.op == '-':
            if Tools().isNoneType(type):
                type = Tools().inferNone(ctx.operand, type, NumberType(), self.curStmt, o)
            if type(type) is not NumberType:
                raise TypeMismatchInExpression(ctx)
            return NumberType()

    def visitCallExpr(self, ctx, o):
        type = None
        for env in o:
            for sym in env:
                if sym.name == ctx.name.name and type(sym.type) is FuncType:
                    type = sym.type
                    break
            if type is not None: break
        if type is None: raise Undeclared(Function(), ctx.name.name)
        if type(type.returnType) is VoidType: raise TypeMismatchInExpression(ctx)
        if len(type.paramType) != len(ctx.args):
            raise TypeMismatchInExpression(ctx)
        for i in range(len(ctx.args)):
            argType = self.visit(ctx.args[i], o)
            self.assignType(ctx, ctx.args[i], argType, None, type.paramType[i], o)
        return type.returnType

    def visitId(self, ctx, o):
        for env in o:
            for sym in env:
                if sym.name == ctx.name and type(sym.type) is not FuncType:
                    return sym.type
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx, o):
        type = self.visit(ctx.arr, o)
        if type(type) is NoneType:
            raise TypeCannotBeInferred(self.curStmt)
        elif type(type) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        if len(ctx.idx) > len(type.size):
            raise TypeMismatchInExpression(ctx)
        else:
            for exp in ctx.idx:
                idxType = self.visit(exp, o)
                if Tools().isNoneType(idxType):
                    idxType = Tools().inferNone(exp, idxType, NumberType(), self.curStmt, o)
                if type(idxType) is not NumberType:
                    raise TypeMismatchInExpression(ctx)
            if len(ctx.idx) < len(type.size):
                return ArrayType(type.size[len(ctx.idx):], type.eleType)
            else: return type.eleType

    def visitArrayLiteral(self, ctx, o):
        dim = len(ctx.value)
        arrType = NoneType()
        maxDim = []
        for exp in ctx.value:
            type = self.visit(exp, o)
            if type(type) is not NoneType:
                if type(type) is ArrayType and len(type.size) > len(maxDim):
                    maxDim = type.size
                if type(arrType) is NoneType:
                    if type(type) is ArrayType:
                        if type(type.eleType) is not NoneType:
                            arrType = type.eleType
                            break
                    else:
                        arrType = type
                        break
        if type(arrType) is NoneType:
            for exp in ctx.value:
                type = self.visit(exp, o)
                try:
                    self.inferElem(maxDim, NoneType(), type.size if type(type) is ArrayType else [], NoneType(), exp, o)
                except TypeMismatchInExpression as e:
                    raise TypeMismatchInExpression(ctx)
            return ArrayType([dim] + maxDim, NoneType())
        self.inferArray([dim] + maxDim, arrType, ctx, o)
        return ArrayType([dim] + maxDim, arrType)

    def visitNumberLiteral(self, ctx, o): return NumberType()
    
    def visitStringLiteral(self, ctx, o): return StringType()
    
    def visitBooleanLiteral(self, ctx, o): return BoolType()

    def inferArray(self, srcDim, srcType, ctx, o):
        if srcDim[0] != len(ctx.value):
            raise TypeMismatchInExpression(ctx)
        for exp in ctx.value:
            temp = srcDim[1:]
            type = self.visit(exp, o)
            if type(type) is NoneType:
                if len(temp) == 0:
                    type = Tools().inferNone(exp, type, srcType, self.curStmt, o)
                else:
                    type = Tools().inferNone(exp, type, ArrayType(temp, srcType), self.curStmt, o)
            elif type(type) is ArrayType:
                if not Tools().sizeIn(type.size, temp):
                    raise TypeMismatchInExpression(ctx)
                if type(type.eleType) is NoneType:
                    self.inferElem(temp, srcType, type.size, type.eleType, exp, o)
                elif type(type.eleType) is not type(srcType):
                    raise TypeMismatchInExpression(ctx)
            else:
                if not Tools().isEquivalentType(type, srcType) or len(temp) != 0:
                    raise TypeMismatchInExpression(ctx)
    
    def inferElem(self, srcDim, srcType, dstDim, dstType, ctx, o):
        if len(dstDim) > len(srcDim):
            raise TypeMismatchInExpression(ctx)
        if len(dstDim) != 0:
            if dstDim[0] != srcDim[0]:
                raise TypeMismatchInExpression(ctx)
            if type(ctx) is ArrayLiteral:
                for exp in ctx.value:
                    self.inferElem(srcDim[1:], srcType, dstDim[1:], dstType, exp, o)
            else:
                Tools().inferNone(ctx, NoneType(), ArrayType(srcDim, srcType), self.curStmt, o)
        else:
            if len(srcDim) != 0:
                Tools().inferNone(ctx, NoneType(), ArrayType(srcDim, srcType), self.curStmt, o)
            else:
                if type(dstType) is NoneType:
                    Tools().inferNone(ctx, NoneType(), srcType, self.curStmt, o)
                else:
                    if type(srcType) is not type(dstType):
                        raise TypeMismatchInExpression(ctx)

    def assignType(self, ctx, lCtx, lType, rCtx, rType, o, isStmt = False):
        if type(lType) is ArrayType and len(lType.size) == 0:
            lType = lType.eleType
        if type(rType) is ArrayType and len(rType.size) == 0:
            rType = rType.eleType
        if Tools().isNoneType(lType) and Tools().isNoneType(rType):
            raise TypeCannotBeInferred(self.curStmt)
        elif type(lType) is NoneType:
            lType = Tools().inferNone(lCtx, lType, rType, self.curStmt, o)
        elif type(rType) is NoneType:
            rType = Tools().inferNone(rCtx, rType, lType, self.curStmt, o)
        elif type(lType) is ArrayType and type(lType.eleType) is NoneType:
            if type(rType) is ArrayType:
                if not Tools().sizeIn(lType.size, rType.size):
                    raise TypeCannotBeInferred(self.curStmt)
                else:
                    if type(lCtx) is ArrayLiteral:
                        lType = ArrayType(lType.size[1:], lType.eleType)
                        rType = ArrayType(rType.size[1:], rType.eleType)
                        for exp in lCtx.value:
                            self.assignType(ctx, exp, lType, None, rType, o, isStmt)
                    else:
                        Tools().inferNone(lCtx, NoneType(), ArrayType(rType.size, rType.eleType), self.curStmt, o)
            else:
                raise TypeCannotBeInferred(self.curStmt)
        elif type(rType) is ArrayType and type(rType.eleType) is NoneType:
            if type(lType) is ArrayType:
                if not Tools().sizeIn(rType.size, lType.size):
                    raise TypeCannotBeInferred(self.curStmt)
                else:
                    if type(rCtx) is ArrayLiteral:
                        lType = ArrayType(lType.size[1:], lType.eleType)
                        rType = ArrayType(rType.size[1:], rType.eleType)
                        for exp in rCtx.value:
                            self.assignType(ctx, None, lType, exp, rType, o, isStmt)
                    else:
                        Tools().inferNone(rCtx, NoneType(), ArrayType(lType.size, lType.eleType), self.curStmt, o)
            else:
                raise TypeCannotBeInferred(self.curStmt)
        elif not Tools().isEquivalentType(lType, rType):
            if isStmt: raise TypeMismatchInStatement(self.curStmt)
            else: raise TypeMismatchInExpression(ctx)