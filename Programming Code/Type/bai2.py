from functools import reduce
class Symbol:
    def __init__(self,name,type):
        self.name=name
        self.type=type
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o=[]
        reduce (lambda acc,cur: self.visit(cur,acc),ctx.decl,o)
        self.visit(ctx.exp,o)
    def visitVarDecl(self,ctx:VarDecl,o): 
        sym = Symbol(ctx.name,ctx.typ)
        o+=[sym]
        return o
    def visitIntType(self,ctx:IntType,o):pass

    def visitFloatType(self,ctx:FloatType,o):pass

    def visitBoolType(self,ctx:BoolType,o):pass

    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*']:
            if type(e1) is BoolType or type(e2) is BoolType:
                raise TypeMismatchInExpression(ctx)
            if type(e1) is FloatType or type(e2) is FloatType:
                return FloatType()
            return IntType()
        elif ctx.op == '/':
            if type(e1) is BoolType or type(e2) is BoolType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif ctx.op in ['&&','||']:
            if type(e1) is not BoolType or type(e2) is not BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        else:
            if type(e1) != type(e2): 
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        e=self.visit(ctx.e,o)
        if ctx.op == '-':
            if type(e) is BoolType: raise TypeMismatchInExpression(ctx)
            return e
        else:
            if type(e) is not BoolType: raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitIntLit(self,ctx:IntLit,o): return IntType() 

    def visitFloatLit(self,ctx,o): return FloatType()

    def visitBoolLit(self,ctx,o): return BoolType()

    def visitId(self,ctx,o): 
        for i in o:
            if i.name == ctx.name:
                return i.type
        raise  UndeclaredIdentifier(ctx.name)