class Symbol:
    def __init__(self, name,mtyp):
        self.name=name
        self.mtyp=mtyp
class StaticCheck(Visitor): 
    def visitBlock(self,ctx,o):
        if type(o) is not list:
            o = [[]]
        result = 0
        maxBlock = 0
        cur = 0
        for stmt in ctx.ele:
            if type(stmt) is Block:
                env = [[]] + o
                cur = self.visit(stmt,env)
                if cur > maxBlock:
                    maxBlock = cur 
            else:
                cur = self.visit(stmt,o)
                result += cur
        return result + maxBlock
    def visitTypeDecl(self,ctx,o):
        o[0]+= [Symbol(ctx.name,ctx.rhs)]
        return 0
    def visitVarDecl(self,ctx,o):
        if type(ctx.typ) is IntType:
            return 2
        elif type(ctx.typ) is FloatType:
            return 6
        return self.visit(ctx.typ,o)
    def visitId(self,ctx,o):
        for scope in o:
            for sym in scope:
                if ctx.name == sym.name:
                    if type(sym.mtyp) is IntType:
                        return 2
                    elif type(sym.mtyp) is FloatType:
                        return 6

                    