    def visitIf(self,ctx,o):
        if ctx.estmt == None:
            falseL = o.frame.getNewLabel()
            cod1, typ1 = self.visit(ctx.expr,Access(o.frame,o.sym,False))
            self.emit.printout(cod1)
            self.emit.printout(self.emit.emitIFFALSE(falseL,o.frame))
            self.visit(ctx.tstmt,o)
            self.emit.printout(self.emit.emitLABEL(falseL,o.frame))
        else:
            falseL = o.frame.getNewLabel()
            exitL = o.frame.getNewLabel()
            cod1, typ1=self.visit(ctx.expr,Access(o.frame,o.sym,False))
            self.emit.printout(cod1)
            self.emit.printout(self.emit.emitIFFALSE(falseL,o.frame))
            self.visit(ctx.tstmt,o)
            self.emit.printout(self.emit.emitGOTO(exitL,o.frame))
            self.emit.printout(self.emit.emitLABEL(falseL,o.frame))
            self.visit(ctx.estmt,o)
            self.emit.printout(self.emit.emitLABEL(exitL,o.frame))