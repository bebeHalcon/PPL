from functools import reduce
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext): 
        decl_list= [self.visit(ctx.vardecl(i)) for i in range(0,ctx.getChildCount()-1)]
        #print(decl_list[0][0])
        return Program(reduce(lambda x,y: x+y,decl_list,[]))
    
    def visitVardecl(self,ctx:MPParser.VardeclContext):  
        id_list=self.visit(ctx.ids())
        return list(map(lambda x: VarDecl(x,self.visit(ctx.mptype())),id_list))
    
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE(): return IntType()
        return FloatType()
    
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(ctx.getChild(i).getText()) for i in range(0,ctx.getChildCount()) if i%2==0]
        