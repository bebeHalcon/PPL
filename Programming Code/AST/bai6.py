from functools import reduce
class ASTGeneration(MPVisitor):

#program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())
#exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):
        temp = int((ctx.getChildCount()-1)/2)
        term_list=[(ctx.ASSIGN(i).getText(),self.visit(ctx.term(i))) for i in range(0,temp)]
        term_list.reverse()
        #print(term_list[1])
        return reduce(lambda acc,ele:Binary(ele[0],ele[1],acc),term_list,self.visit(ctx.getChild(ctx.getChildCount()-1)))

#term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount()==1: return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)),self.visit(ctx.factor(1)))
#factor: operand (ANDOR operand)*;  
    def visitFactor(self,ctx:MPParser.FactorContext):
        temp = int((ctx.getChildCount()-1)/2)
        operand_list = [(ctx.ANDOR(i-1).getText(),self.visit(ctx.operand(i))) for i in range(1,temp+1)]
        if len(operand_list) ==0: return self.visit(ctx.operand(0))
        return reduce(lambda acc,ele: Binary(ele[0],acc,ele[1]),operand_list,self.visit(ctx.operand(0)))
    
#operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT(): return BooleanLiteral(ctx.BOOLIT().getText()=='True' )
        return self.visit(ctx.exp())



