from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

class NoneType(Type): pass

class Tools():
    def inferType(self, name, lst, type, isFunc = False):
        for env in lst:
            for sym in env:
                if sym.name == name and (type(sym.mtype) == MType) == isFunc:
                    if isFunc: sym.mtype.reType = type
                    else: sym.mtype = type
                    return type
                
    def isNoneType(self, type):
        return type(type) is NoneType or (type(type) is ArrayType and type(type.eleType) is NoneType)
    
    def inferNone(self, dstCtx, srcType, sym):
        if type(dstCtx) is Id:
            return self.inferType(dstCtx.name, sym, srcType)
        elif type(dstCtx) is CallExpr:
            return self.inferType(dstCtx.name.name, sym, srcType, True)
        elif type(dstCtx) is ArrayCell:
            type = srcType.eleType if type(srcType) is ArrayType else srcType
            dstName = dstCtx.arr.name if type(dstCtx.arr) is Id else dstCtx.arr.name.name
            isFunc = type(dstCtx.arr) is CallExpr
            for env in sym:
                for s in env:
                    if s.name == dstName and (type(s.mtype) is MType) == isFunc:
                        if isFunc:
                            if type(s.mtype.reType) is ArrayType:
                                s.mtype.reType.eleType = type
                            else:
                                s.mtype.reType = type
                        else:
                            if type(s.mtype) is ArrayType:
                                s.mtype.eleType = type
                            else:
                                s.mtype = type
        elif type(dstCtx) is ArrayLiteral:
            if len(srcType.size) == 0:
                srcType = srcType.eleType
            for expr in dstCtx.value:
                self.inferNone(expr, ArrayType(srcType.size[1:], srcType.eleType), sym)
    
    def findFunc(self, name, lst):
        for env in lst:
            for sym in env:
                if sym.name == name and type(sym.mtype) == MType:
                    return sym
        return None

class MType:
    def __init__(self, parType, reType):
        self.parType = parType
        self.reType = reType

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[Symbol("readNumber", MType([], NumberType()), CName(self.libName)),
                Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType([], BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType([], StringType()), CName(self.libName)),
                Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName))
                ]]

    def gen(self, ast, path):
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = 'ZCodeClass'
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.glbVarFrame = Frame("<clinit>", VoidType())
        self.reType = NoneType()

    def visitProgram(self, ast, o):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        o = SubBody(None, self.env)
        varLst = []
        funcLst = []
        for decl in ast.decl:
            if type(decl) is VarDecl:
                varLst += [decl]
            else:
                funcLst += [decl]
        self.genVAR(varLst, o)
        
        for decl in funcLst:
            self.visit(decl, o)
        self.emit.emitEPILOG()
        return o

    def genVAR(self, varLst, o):
        for decl in varLst:
            type = NoneType() if decl.varType is None else decl.varType
            code = self.emit.emitATTRIBUTE(decl.name.name, type, False, None)
            self.emit.printout(code)
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, self.glbVarFrame))
        for decl in varLst:
            val = CName(self.className)
            if decl.varInit is not None:    
                code, type = self.visit(decl.varInit, Access(self.glbVarFrame, o.sym, False))
                self.emit.printout(code)
                self.emit.printout(self.emit.emitPUTSTATIC(self.className + '/' + decl.name.name, type, self.glbVarFrame))
            o.sym[0] = [Symbol(decl.name.name, type, val)] + o.sym[0]
        self.emit.printout(self.emit.emitRETURN(VoidType(), self.glbVarFrame))
        self.emit.printout(self.emit.emitENDMETHOD(self.glbVarFrame))

    def genMETHOD(self, ast, o, frame):
        isMain = ast.name.name == "main" and len(ast.param) == 0 and type(self.reType) is VoidType
        returnType = self.reType if not isMain else VoidType()
        methodName = ast.name.name
        inType = [ArrayType([1], StringType())] if isMain else [x.varType for x in ast.param]
        mtype = MType(inType, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, True, frame))
        frame.enterScope(True)
        glenv = o
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                [1], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        if ast.param != []:
            temp = o[0][::-1]
            for x in temp:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), x.name, x.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        body = ast.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if body:
            self.emit.printout(self.visit(body, SubBody(frame, glenv)))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        self.reType = NoneType()
        temp = o.sym
        o.sym[0] = [Symbol(ast.name.name, MType([x.varType for x in ast.param], self.reType), CName(self.className))] + o.sym[0]
        if ast.body is not None:
            temp = [[]] + o.sym
            for x in ast.param:
                temp[0] = [Symbol(x.name.name, x.varType, Index(self.glbVarFrame.getNewIndex()))] + temp[0]
            if len(ast.param) == 0: temp = temp[1:]
            _ = self.visit(ast.body, SubBody(self.glbVarFrame, temp))
            if type(self.reType) is NoneType:
                self.reType = VoidType()
        frame = Frame(ast.name.name, VoidType())
        self.genMETHOD(ast, temp, frame)
        o.sym[0][0] = Symbol(ast.name.name, MType([x.varType for x in ast.param], self.reType), CName(self.className))

    def visitVarDecl(self, ast, o):
        reCode = ""
        type = NoneType() if ast.varType is None else ast.varType
        index = o.frame.getNewIndex()
        code = self.emit.emitVAR(index, ast.name.name, type, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        reCode += code
        val = Index(index)
        if ast.varInit is not None:
            code, type = self.visit(ast.varInit, Access(o.frame, o.sym, False))
            reCode += code + self.emit.emitWRITEVAR(ast.name.name, type, index, o.frame)
        o.sym[0] = [Symbol(ast.name.name, type, val)] + o.sym[0]
        return reCode

    def visitAssign(self, ast, o):
        reCode = ""
        rCode, rType = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        lCode, lType = self.visit(ast.lhs, Access(o.frame, o.sym, True))
        if Tools().isNoneType(rType):
            Tools().inferNone(ast.rhs, lType, o.sym)
            rCode, rType = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        if Tools().isNoneType(lType):
            Tools().inferNone(ast.lhs, rType, o.sym)
            lCode, lType = self.visit(ast.lhs, Access(o.frame, o.sym, True))
        if type(lCode) is list:
            reCode += lCode[0] + rCode + lCode[1]
        else:
            reCode += rCode + lCode
        return reCode

    def visitIf(self, ast, o):
        reCode = ""
        exprCode, _ = self.visit(ast.expr, Access(o.frame, o.sym, False))
        reCode += exprCode
        labels = []
        for expr, stmt in ast.elifStmt:
            nextLabel = o.frame.getNewLabel()
            labels.append(nextLabel)
        if ast.elseStmt is not None:
            nextLabel = o.frame.getNewLabel()
            labels.append(nextLabel)
        nextLabel = o.frame.getNewLabel()
        labels.append(nextLabel)
        reCode += self.emit.emitIFFALSE(labels[0], o.frame)
        reCode += self.visit(ast.thenStmt, o)
        reCode += self.emit.emitGOTO(labels[-1], o.frame)
        for i in range(len(ast.elifStmt)):
            reCode += self.emit.emitLABEL(labels[i], o.frame)
            exprCode, _ = self.visit(ast.elifStmt[i][0], Access(o.frame, o.sym, False))
            reCode += exprCode + self.emit.emitIFFALSE(labels[i+1], o.frame)
            reCode += self.visit(ast.elifStmt[i][1], o)
            reCode += self.emit.emitGOTO(labels[-1], o.frame)
        if ast.elseStmt is not None:
            reCode += self.emit.emitLABEL(labels[-2], o.frame)
            reCode += self.visit(ast.elseStmt, o)
        reCode += self.emit.emitLABEL(labels[-1], o.frame)
        return reCode

    def visitFor(self, ast, o):
        reCode = ""
        frame = o.frame
        rIndex, _ = self.visit(ast.name, Access(frame, o.sym, False))
        reCode += rIndex
        newLabel = frame.getNewLabel()
        frame.enterLoop()
        reCode += self.emit.emitLABEL(newLabel, frame)
        condCode, _ = self.visit(ast.condExpr, Access(frame, o.sym, False))
        reCode += condCode
        brkLabel = frame.getBreakLabel()
        code = self.emit.emitIFTRUE(brkLabel, frame)
        reCode += code
        reCode += self.visit(ast.body, o)
        contLabel = frame.getContinueLabel()
        code = self.emit.emitLABEL(contLabel, frame)
        reCode += code
        updCode, _ = self.visit(ast.updExpr, Access(frame, o.sym, False))
        reCode += updCode
        rIndex, _ = self.visit(ast.name, Access(frame, o.sym, False))
        reCode += rIndex
        upd = self.emit.emitADDOP('+', NumberType(), frame)
        lIndex, _ = self.visit(ast.name, Access(frame, o.sym, True))
        reCode += upd + lIndex
        code = self.emit.emitGOTO(newLabel, frame)
        reCode += code
        code = self.emit.emitLABEL(brkLabel, frame)
        reCode += code
        frame.exitLoop()
        lIndex, _ = self.visit(ast.name, Access(frame, o.sym, True))
        reCode += lIndex
        return reCode

    def visitBreak(self, ast, o):
        reCode = ""
        brkLabel = o.frame.getBreakLabel()
        reCode += self.emit.emitGOTO(brkLabel, o.frame)
        return reCode

    def visitContinue(self, ast, o):
        reCode = ""
        contLabel = o.frame.getContinueLabel()
        reCode += self.emit.emitGOTO(contLabel, o.frame)
        return reCode

    def visitReturn(self, ast, o):
        reCode = ""
        if ast.expr is not None:
            code, type = self.visit(ast.expr, Access(o.frame, o.sym, False))
            reCode += code + self.emit.emitRETURN(type, o.frame)
            self.reType = type
        else:
            reCode += self.emit.emitRETURN(VoidType(), o.frame)
            self.reType = VoidType()
        return reCode

    def visitCallStmt(self, ast, o):
        reCode = ""
        sym = Tools().findFunc(ast.name.name, o.sym)
        cname = sym.value.value
        ctype = sym.mtype
        for i in range(len(ast.args)):
            argCode, argType = self.visit(ast.args[i], Access(o.frame, o.sym, False))
            if Tools().isNoneType(argType):
                Tools().inferNone(ast.args[i], ctype.parType[i], o.sym)
                argCode, argType = self.visit(ast.args[i], Access(o.frame, o.sym, False))
            reCode += argCode
        if ast.name.name == 'writeNumber':
            reCode += self.emit.emitINVOKESTATIC("io/writeNumber", MType([NumberType()], VoidType()), o.frame)
        elif ast.name.name == 'writeBool':
            reCode += self.emit.emitINVOKESTATIC("io/writeBool", MType([BoolType()], VoidType()), o.frame)
        elif ast.name.name == 'writeString':
            reCode += self.emit.emitINVOKESTATIC("io/writeString", MType([StringType()], VoidType()), o.frame)
        else:
            reCode += self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, o.frame)
        return reCode

    def visitBlock(self, ast, o):
        reCode = ""
        newEnv = [[]] + o.sym
        o.frame.enterScope(False)
        sLabel = o.frame.getStartLabel()
        reCode += self.emit.emitLABEL(sLabel, o.frame)
        for stmt in ast.stmt:
            reCode += self.visit(stmt, SubBody(o.frame, newEnv))
        eLabel = o.frame.getEndLabel()
        reCode += self.emit.emitLABEL(eLabel, o.frame)
        o.frame.exitScope()
        return reCode

    def visitBinaryOp(self, ast, o):
        lCode, lType = self.visit(ast.left, o)
        rCode, rType = self.visit(ast.right, o)
        type = NoneType()
        if ast.op in ['+', '-', '*', '/', '%', '<', '<=', '>', '>=', '=', '!=']:
            type = NumberType()
        elif ast.op in ['and', 'or']:
            type = BoolType()
        elif ast.op in ['==', '...']:
            type = StringType()
        if Tools().isNoneType(lType):
            Tools().inferNone(ast.left, type, o.sym)
            lCode, lType = self.visit(ast.left, o)
        if Tools().isNoneType(rType):
            Tools().inferNone(ast.right, type, o.sym)
            rCode, rType = self.visit(ast.right, o)
        if ast.op in ['+', '-']:
            return lCode + rCode + self.emit.emitADDOP(ast.op, NumberType(), o.frame), NumberType()
        elif ast.op in ['*', '/']:
            return lCode + rCode + self.emit.emitMULOP(ast.op, NumberType(), o.frame), NumberType()
        elif ast.op == '%':
            return lCode + rCode + self.emit.emitMOD(o.frame), NumberType()
        elif ast.op in ['<', '<=', '>', '>=', '=', '!=']:
            return lCode + rCode + self.emit.emitREOP(ast.op, NumberType(), o.frame), BoolType()
        elif ast.op == 'and':
            return lCode + rCode + self.emit.emitANDOP(o.frame), BoolType()
        elif ast.op == 'or':
            return lCode + rCode + self.emit.emitOROP(o.frame), BoolType()
        elif ast.op == '==':
            return lCode + rCode + self.emit.emitINVOKEVIRTUAL('java/lang/String/equals', MType([object()], BoolType()), o.frame), BoolType()
        elif ast.op == '...':
            return lCode + rCode + self.emit.emitINVOKEVIRTUAL('java/lang/String/concat', MType([StringType()], StringType()), o.frame), StringType()

    def visitUnaryOp(self, ast, o):
        opCode, opType = self.visit(ast.operand, o)
        type = BoolType() if ast.op == 'not' else NumberType()
        if Tools().isNoneType(opType):
            Tools().inferNone(ast.operand, type, o.sym)
            opCode, opType = self.visit(ast.operand, o)
        if ast.op == 'not':
            return opCode + self.emit.emitNOT(BoolType(), o.frame), BoolType()
        elif ast.op == '-':
            return opCode + self.emit.emitNEGOP(NumberType(), o.frame), NumberType()

    def visitCallExpr(self, ast, o):
        if ast.name.name == 'readNumber':
            return self.emit.emitINVOKESTATIC("io/readNumber", MType([], NumberType()), o.frame), NumberType()
        elif ast.name.name == 'readBool':
            return self.emit.emitINVOKESTATIC("io/readBool", MType([], BoolType()), o.frame), BoolType()
        elif ast.name.name == 'readString':
            return self.emit.emitINVOKESTATIC("io/readString", MType([], StringType()), o.frame), StringType()
        sym = Tools().findFunc(ast.name.name, o.sym)
        cname = sym.value.value
        ctype = sym.mtype
        code = ""
        reType = ctype.reType
        for i in range(len(ast.args)):
            argCode, argType = self.visit(ast.args[i], Access(o.frame, o.sym, False))
            if Tools().isNoneType(argType):
                argType = Tools().inferNone(ast.args[i], ctype.parType[i], o.sym)
                argCode, argType = self.visit(ast.args[i], Access(o.frame, o.sym, False))
            code += argCode
        return code + self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, o.frame), reType

    def visitId(self, ast, o):
        sym = None
        for env in o.sym:
            for s in env:
                if s.name == ast.name and type(s.mtype) is not MType:
                    sym = s
                    break
            if sym is not None:
                break
        if o.isLeft:
            if type(sym.value) is Index:
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o.frame), sym.mtype
            else:
                return self.emit.emitPUTSTATIC(self.className + '/' + ast.name, sym.mtype, o.frame), sym.mtype
        else:
            if type(sym.value) is Index:
                return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o.frame), sym.mtype
            else:
                return self.emit.emitGETSTATIC(self.className + '/' + ast.name, sym.mtype, o.frame), sym.mtype
    
    def visitArrayCell(self, ast, o):
        arrCode, arrType = self.visit(ast.arr, Access(o.frame, o.sym, False))
        if len(ast.idx) == len(arrType.size):
            arrType = arrType.eleType
        elif len(ast.idx) < len(arrType.size):
            arrType = ArrayType(arrType.size[len(ast.idx):], arrType.eleType)
        for i in range(len(ast.idx)):
            if i != 0:
                code = self.emit.emitALOAD(StringType(), o.frame)
                arrCode += code
            idxCode, idxType = self.visit(ast.idx[i], Access(o.frame, o.sym, False))
            if Tools().isNoneType(idxType):
                Tools().inferNone(ast.idx[i], NumberType(), o.sym)
                idxCode, idxType = self.visit(ast.idx[i], Access(o.frame, o.sym, False))
            arrCode += idxCode + self.emit.emitF2I(o.frame)
        if o.isLeft:
            return [arrCode, self.emit.emitASTORE(arrType, o.frame)], arrType
        else:
            return arrCode + self.emit.emitALOAD(arrType, o.frame), arrType
    
    def visitArrayLiteral(self, ast, o):
        dim = len(ast.value)
        arrType = NoneType()
        maxDim = []
        for expr in ast.value:
            _, eleType = self.visit(expr, o)
            if type(eleType) is ArrayType:
                maxDim = eleType.size if len(eleType.size) > len(maxDim) else maxDim
                arrType = eleType.eleType
            else:
                arrType = eleType
            if not Tools().isNoneType(arrType):
                break
        code = self.emit.emitPUSHICONST(dim, o.frame)
        if len(maxDim) > 0:
            code += self.emit.emitANEWARRAY(self.emit.getFullType(ArrayType(maxDim, arrType)), o.frame)
        else:
            code += self.emit.emitNEWARRAY(arrType, o.frame)
        for i in range(dim):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            eCode, eType = self.visit(ast.value[i], Access(o.frame, o.sym, False))
            if Tools().isNoneType(eType):
                Tools().inferNone(ast.value[i], arrType, o.sym)
                eCode, eType = self.visit(ast.value[i], Access(o.frame, o.sym, False))
            code += eCode
            code += self.emit.emitASTORE(eType, o.frame)
        return code, ArrayType([dim] + maxDim, arrType)

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()