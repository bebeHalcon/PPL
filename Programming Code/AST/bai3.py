class ASTGeneration(MPVisitor):
    #program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

    # vardecls:vardecl vardecltail
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) 
        
    #vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount()==0): return [];
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) 
        
    # vardecl: mptype ids SM;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return [VarDecl(i,self.visit(ctx.mptype())) for i in self.visit(ctx.ids())]
   
    #mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()
    #ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        if (ctx.getChildCount()==1):
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        