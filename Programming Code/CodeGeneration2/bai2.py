    def visitId(self,ctx,o):
        sym = next(filter(lambda x: x.name == ctx.name, o.sym))
        if type(sym.value) is Index:
            if o.isLeft:
                code = self.emit.emitWRITEVAR(ctx.name, sym.mtype, sym.value.value,o.frame)
            else:
                code = self.emit.emitREADVAR(ctx.name, sym.mtype, sym.value.value,o.frame)
            return (code , sym.mtype)
        else:
            if o.isLeft:
                code = self.emit.emitPUTSTATIC(sym.value.value + "." + ctx.name, sym.mtype, o.frame)
            else:
                code = self.emit.emitGETSTATIC(sym.value.value + "." + ctx.name, sym.mtype, o.frame)
            return (code , sym.mtype)
            