    def visitId(self,ctx,o):
        for i in o.sym:
            if i.name == ctx.name:
                if type(i.value.value) == type(int()):
                    #print(i.value)

                    #print(i.value.value)
                    code = self.emit.emitREADVAR(i.name, i.mtype, i.value.value, o.frame)
                    return (code , i.mtype)
                else: 
                    #print(i.value)
                    #print (StringType(i.value.value))
                    #print (i.mtype)
                    code = self.emit.emitGETSTATIC(i.value.value+"."+i.name,i.mtype, o.frame)
                    return (code , i.mtype)