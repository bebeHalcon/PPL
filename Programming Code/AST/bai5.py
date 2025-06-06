class ASTGeneration(MPVisitor):
#program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())
#exp: term ASSIGN exp | term;
    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.getChildCount()==1: return self.visit(ctx.term())
        return Binary(ctx.ASSIGN().getText(),self.visit(ctx.term()),self.visit(ctx.exp()))
        
#term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount()==1: return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)),self.visit(ctx.factor(1)))
#factor: factor ANDOR operand | operand; 
    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.getChildCount()==1: return self.visit(ctx.operand())
        return Binary(ctx.ANDOR().getText(),self.visit(ctx.factor()),self.visit(ctx.operand()))

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.INTLIT(): return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT(): return BooleanLiteral(True if ctx.BOOLIT().getText()=="True" else False)
        return self.visit(ctx.exp())