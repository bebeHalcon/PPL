from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = []
        reduce(lambda acc,cur: acc + self.visit(cur,acc),ctx.decl,[])
    

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return [ctx.name]           

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise  RedeclaredConstant(ctx.name)
        return [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass