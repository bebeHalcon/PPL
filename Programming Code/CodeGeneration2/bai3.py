    def visitAssign(self,ctx,o):
        rcod,rtyp=self.visit(ctx.rhs,Access(o.frame,o.sym,False))
        #print(rcod)
        self.emit.printout(rcod)
        lcod,ltyp=self.visit(ctx.lhs,Access(o.frame,o.sym,True))
        
        self.emit.printout(lcod)