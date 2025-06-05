from functools import reduce
class Symbol:
    def __init__(self,name,assigned=False):
        self.name=name
        self.assigned=assigned
class StaticCheck(Visitor): 
    def visitProgram(self,ctx,o):
        o = []
        reduce(lambda x,y: self.visit(y,x),ctx.decls,o)
    def visitBlock(self,ctx,o):
        env = o
        reduce(lambda x,y: self.visit(y,x),ctx.local + ctx.body, env)
        unass_vars = []
        for i in env:
            if i.assigned == False:
                unass_vars += [Id(i.name)]
        if len(unass_vars) > 0 :
            raise UnassignedVariables(unass_vars)
        return o
    def visitVarDecl(self,ctx,o):
        o+= [Symbol(ctx.name)]
        return o
    def visitAssign(self,ctx,o):
        self.visit(ctx.rhs,o)
        self.visit(ctx.lhs,o)
        return o
    def visitId(self,ctx,o):
        for i in range(len(o)):
            if o[i].name == ctx.name:
                o[i].assigned=True
                break
    def visitNumLit(self,ctx,o): pass