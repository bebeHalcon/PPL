    def visitBinExpr(self,ctx,o):
        (cod1,typ1)= self.visit(ctx.e1,o)
        (cod2,typ2) = self.visit(ctx.e2,o)
        if ctx.op in [ '+', '-' ]:
            code = self.emit.emitADDOP(ctx.op,IntType(),o.frame)
            return (cod1 + cod2 + code, IntType())
        elif ctx.op in ['*','/']:
            code = self.emit.emitMULOP(ctx.op,IntType(),o.frame)
            return (cod1 + cod2 + code, IntType())
        elif ctx.op in ['+.','-.']:
            op = ''
            if ctx.op == '+.':
                op = '+' 
            else: op = '-'
            code = self.emit.emitADDOP(op,FloatType(),o.frame)
            return (cod1 + cod2 + code, FloatType())
        elif ctx.op in ['*.','/.']:
            op = ''
            if ctx.op == '*.':
                op = '*' 
            else:
                op = '/'
            code = self.emit.emitMULOP(op,FloatType(),o.frame)
            return (cod1 + cod2 + code, FloatType())
            
                