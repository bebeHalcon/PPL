    def visitVarDecl(self,ctx,o):
        if  o.frame != None:
            fromLabel = o.frame.getStartLabel()
            toLabel = o.frame.getEndLabel()
            curIndex = o.frame.getCurrIndex()
            o.frame.setCurrIndex(curIndex+1)
            code = self.emit.emitVAR(curIndex, ctx.name, ctx.typ,fromLabel, toLabel)
            self.emit.printout(code)
            return Symbol(ctx.name,ctx.typ,Index(curIndex))
        else:
            code = self.emit.emitATTRIBUTE(ctx.name,ctx.typ, False)
            self.emit.printout(code)
            return Symbol(ctx.name,ctx.typ,CName(self.className))