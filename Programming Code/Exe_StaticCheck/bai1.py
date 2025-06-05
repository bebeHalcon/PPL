from functools import reduce
class StaticCheck(Visitor): 
    def visitBlock(self,ctx,o):
        if type(o) is not list: 
            o=[[]]
        for stmt in ctx.ele:
            if type(stmt) is Block:
                env = [[]]+o
                self.visit(stmt,env)
            else:
                self.visit(stmt,o)
        
    def visitTypeDecl(self,ctx,o):
        o[0]+= [ctx.name] 
    def visitVarDecl(self,ctx,o): 
        #print(o)
        if (type(ctx.typ) is Id):
            self.visit(ctx.typ,o)

    def visitId(self, ctx,o):
        for scope in o: 
            if ctx.name in scope:
                return
        raise UndeclaredType(ctx.name)
    def visitIntType(self,ctx,o): pass
    def visitFloatType(self,ctx,o): pass
