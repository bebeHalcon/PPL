from functools import reduce
class Symbol:
    def __init__(self,id:str, assigned=False):
        self.id=id
        self.assigned=assigned
class StaticCheck(Visitor): 
    def visitProgram(self,ctx,o):
        o=[]
        for i in ctx.decls:
            self.visit(i,o)
    def visitBlock(self,ctx,o):
        
        reduce(lambda x,y: self.visit(y,x),ctx.local,o)
        #print("o: ",o)
        reduce(lambda x,y: self.visit(y,x),ctx.body,o)
        
    def visitVarDecl(self,ctx,o):
        o+=[Symbol(ctx.name)]
        return o
    def visitAssign(self,ctx,o):
        self.visit(ctx.lhs,o)
        return o
    def visitId(self,ctx,o):
        #print(o)
        for i in range(len(o)):
            if (o[i].id==ctx.name):
                o[i].assigned=True
                break
            if (o[i].assigned==False):
                raise  UnassignedVariable(ctx)
            