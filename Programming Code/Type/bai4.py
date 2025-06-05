from functools import reduce 
class IntType: pass
class FloatType: pass
class BoolType: pass
class NoneType: pass
class Symbol: 
    def __init__(self,name,type):
        self.name=name
        self.type=type
class Utils:
    def setTypeForId(name,type,o):
        for i in o:
            for id in i:
                if id.name==name:
                    id.type=type
                    return
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o=[[]]
        for i in ctx.decl:
            self.visit(i,o)
        for i in ctx.stmts:
            self.visit(i,o)

    def visitVarDecl(self,ctx:VarDecl,o): 
        for id in o[0]:
            if id.name == ctx.name:
                raise Redeclared(ctx)
        o[0]+=[Symbol(ctx.name,NoneType())]

    def visitBlock(self,ctx:Block,o): 
        o=[[]] + o
        for i in ctx.decl:
            self.visit(i,o)
        for i in ctx.stmts:
            self.visit(i,o)

    def visitAssign(self,ctx:Assign,o): 
        rhs=self.visit(ctx.rhs,o)
        lhs=self.visit(ctx.lhs,o)
        if type(rhs) is NoneType and type(lhs) is NoneType:
            raise TypeCannotBeInferred(ctx)
        elif type(rhs) is NoneType:
            Utils.setTypeForId(ctx.rhs.name,lhs,o)
        elif type(lhs) is NoneType:
            Utils.setTypeForId(ctx.lhs.name,rhs,o)
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*','/']:
            if type(e1) not in [NoneType,IntType] or type(e2) not in [NoneType,IntType]:
                raise TypeMismatchInExpression(ctx)
            if type(e1) is NoneType:
                Utils.setTypeForId(ctx.e1.name,IntType(),o)
            if type(e2) is NoneType:
                Utils.setTypeForId(ctx.e2.name,IntType(),o)
            return IntType()
        elif ctx.op in ['+.','-.','*.','/.']:
            if type(e1) not in [NoneType,FloatType] or type(e2) not in [NoneType,FloatType]:
                raise TypeMismatchInExpression(ctx)
            if type(e1) is NoneType:
                Utils.setTypeForId(ctx.e1.name,FloatType(),o)
            if type(e2) is NoneType:
                Utils.setTypeForId(ctx.e2.name,FloatType(),o)
            return FloatType()
        elif ctx.op in ['=','>']:
            if type(e1) not in [NoneType,IntType] or type(e2)  not in [NoneType,IntType]:
                raise TypeMismatchInExpression(ctx)
            if type(e1) is NoneType:
                Utils.setTypeForId(ctx.e1.name,IntType(),o)
            if type(e2) is NoneType:
                Utils.setTypeForId(ctx.e2.name,IntType(),o)
            return BoolType()
        elif ctx.op in ['=.','>.']:
            if type(e1)  not in [NoneType,FloatType] or type(e2) not in [NoneType,FloatType]:
                raise TypeMismatchInExpression(ctx)
            if type(e1) is NoneType:
                Utils.setTypeForId(ctx.e1.name,FloatType(),o)
            if type(e2) is NoneType:
                Utils.setTypeForId(ctx.e2.name,FloatType(),o)
            return BoolType()
        else:
            if type(e1)  not in [NoneType,BoolType] or type(e2) not in [NoneType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if type(e1) is NoneType:
                Utils.setTypeForId(ctx.e1.name,BoolType(),o)
            if type(e2) is NoneType:
                Utils.setTypeForId(ctx.e2.name,BoolType(),o)
            return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e,o)
        if ctx.op == '-':
            if type(e)  not in [NoneType,IntType]:
                raise TypeMismatchInExpression(ctx)
            if type(e) is NoneType:
                Utils.setTypeForId(ctx.e.name,IntType(),o)
            return IntType()
        elif ctx.op == '-.':
            if type(e)  not in [NoneType,FloatType]:
                raise TypeMismatchInExpression(ctx)
            if type(e) is NoneType:
                Utils.setTypeForId(ctx.e.name,FloatType(),o)
            return FloatType()
        elif ctx.op == '!':
            if type(e) not in [NoneType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if type(e) is NoneType:
                Utils.setTypeForId(ctx.e.name,BoolType(),o)
            return BoolType()
        elif ctx.op == 'i2f':
            if type(e)  not in [NoneType,IntType]:
                raise TypeMismatchInExpression(ctx)
            if type(e) is NoneType:
                Utils.setTypeForId(ctx.e.name,IntType(),o)
            return FloatType()
        else:
            if type(e)  not in [NoneType,FloatType]:
                raise TypeMismatchInExpression(ctx)
            if type(e) is NoneType:
                Utils.setTypeForId(ctx.e.name,FloatType(),o)
            return IntType() 
        

    def visitIntLit(self,ctx:IntLit,o): return IntType() 

    def visitFloatLit(self,ctx,o): return FloatType()

    def visitBoolLit(self,ctx,o): return BoolType()

    def visitId(self,ctx,o): 
        for i in o:
            for item in i:
                if item.name== ctx.name:
                    return item.type
        raise UndeclaredIdentifier(ctx.name)