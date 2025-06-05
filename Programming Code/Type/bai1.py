class Symbol:
    def __init__(self,name,type):
        self.name=name
        self.type=type

class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*']:
            if e1 == 3 or e2 == 3: raise TypeMismatchInExpression(ctx)
            if e1 == 2 or e2 == 2: return 2
            return 1
        elif ctx.op in ['<','>','==','!=']:
            if e1 != e2: raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op in ['&&','||']:
            if e1==3 and e2==3: return 3
            raise TypeMismatchInExpression(ctx)
        else:
            if e1 == 3 or e2 == 3: raise TypeMismatchInExpression(ctx)
            return 2
    def visitUnOp(self,ctx:UnOp,o):
        exp=self.visit(ctx.e,o)
        if ctx.op == '!':
            if exp!=3: raise TypeMismatchInExpression(ctx)
            return 3
        else:
            if exp==3: raise TypeMismatchInExpression(ctx)
            return exp

    def visitIntLit(self,ctx:IntLit,o): return 1

    def visitFloatLit(self,ctx,o): return 2

    def visitBoolLit(self,ctx,o): return 3