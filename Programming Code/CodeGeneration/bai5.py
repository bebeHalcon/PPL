    def  visitBinExpr(self,ctx,o):
        cod1,typ1= self.visit(ctx.e1,o)
        cod2,typ2= self.visit(ctx.e2,o)
        if ctx.op in ['+', '-']:
            if (type(typ1) is FloatType or type(typ2) is FloatType):
                if type(typ1) is IntType:
                    cod1 += self.emit.emitI2F(o.frame)
                if type(typ2) is IntType:
                    cod2 += self.emit.emitI2F(o.frame)
                cod = self.emit.emitADDOP(ctx.op,FloatType(),o.frame)
                return (cod1+cod2+cod,FloatType())
            else:
                cod = self.emit.emitADDOP(ctx.op,IntType(),o.frame)
                return (cod1+cod2+cod,IntType())
        elif ctx.op in ['*', '/']:
            
            if ctx.op == '/' or (type(typ1) is FloatType or type(typ2) is FloatType):
                if type(typ1) is IntType:
                    cod1 += self.emit.emitI2F(o.frame)
                if type(typ2) is IntType:
                    cod2 += self.emit.emitI2F(o.frame)
                cod = self.emit.emitMULOP(ctx.op,FloatType(),o.frame)
                
                #print(cod1+cod2+cod)
                return (cod1+cod2+cod,FloatType())
            else:
                cod = self.emit.emitMULOP(ctx.op,IntType(),o.frame)
                return (cod1+cod2+cod,IntType())
            
        else:
            if type(typ1) != type(typ2):
                cod = self.emit.emitREOP(ctx.op,FloatType(),o.frame)
                if type(typ1) is IntType:
                    cod1 += self.emit.emitI2F(o.frame)
                if type(typ2) is IntType:
                    cod2 += self.emit.emitI2F(o.frame)
            else:
                cod = self.emit.emitREOP(ctx.op,typ1,o.frame)
            
            #print (cod1+cod2+cod)
            return(cod1+cod2+cod,BoolType())
      