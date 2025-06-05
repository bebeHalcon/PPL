from functools import reduce
class IntType: pass
class FloatType: pass
class BoolType: pass
class Symbol:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    
class StaticCheck(Visitor):
    def setTypeOfId(self,name,type,o):
        for i in o:
            if i.name==name:
                i.type=type
                return
        
    def visitProgram(self,ctx:Program,o):
        o= reduce (lambda acc,cur: self.visit(cur,acc),ctx.decl,[])
        for i in ctx.stmts:
            self.visit(i,o)

    def visitVarDecl(self,ctx:VarDecl,o): 
        o+=[Symbol(ctx.name, None)]
        return o

    def visitAssign(self,ctx:Assign,o): 
        rhs = self.visit(ctx.rhs,o)
        lhs = self.visit(ctx.lhs,o)
        if type(rhs) == type(lhs) :
            if rhs == None: raise  TypeCannotBeInferred(ctx)
        else:
            if rhs != None and lhs != None:
                raise TypeMismatchInStatement(ctx)
            if rhs == None:
                self.setTypeOfId(ctx.rhs.name,lhs,o)
            if lhs == None:
                self.setTypeOfId(ctx.lhs.name,rhs,o)
            

    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*','/']:
            if type(e1) in [FloatType,BoolType] or type(e2) in [FloatType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if e1 == None:
                self.setTypeOfId(ctx.e1.name,IntType(),o)
            if e2 == None:
                self.setTypeOfId(ctx.e2.name,IntType(),o)
            return IntType()
        elif ctx.op in ['+.','-.','*.','/.']:
            if type(e1) in [IntType,BoolType] or type(e2) in [IntType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if e1 == None:
                self.setTypeOfId(ctx.e1.name,FloatType(),o)
            if e2 == None:
                self.setTypeOfId(ctx.e2.name,FloatType(),o)
            return FloatType()
        elif ctx.op in ['>','=']:
            if type(e1) in [FloatType,BoolType] or type(e2) in [FloatType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if e1 == None:
                self.setTypeOfId(ctx.e1.name,IntType(),o)
            if e2 == None:
                self.setTypeOfId(ctx.e2.name,IntType(),o)
            return BoolType()
        elif ctx.op in ['>.','=.']:
            if type(e1) in [IntType,BoolType] or type(e2) in [IntType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if e1 == None:
                self.setTypeOfId(ctx.e1.name,FloatType(),o)
            if e2 == None:
                self.setTypeOfId(ctx.e2.name,FloatType(),o)
            return BoolType()
        else:
            if type(e1) in [IntType,FloatType] or type(e2) in [IntType,FloatType]:
                raise TypeMismatchInExpression(ctx)
            if e1 == None:
                self.setTypeOfId(ctx.e1.name,BoolType(),o)
            if e2 == None:
                self.setTypeOfId(ctx.e2.name,BoolType(),o)
            
            return BoolType()
    def visitUnOp(self,ctx:UnOp,o):
        e= self.visit(ctx.e,o)
        if ctx.op == '-':
            if e == None: 
                self.setTypeOfId(ctx.e.name,IntType(),o)
                return IntType()
            if type(e) is not IntType: raise TypeMismatchInExpression(ctx)
            return IntType()
        elif ctx.op =='-.':
            if e == None: 
                self.setTypeOfId(ctx.e.name,FloatType(),o)
                return FloatType()
            if type(e) is not FloatType: raise TypeMismatchInExpression(ctx)
            return FloatType()
        elif ctx.op =='!':
            if e == None: 
                self.setTypeOfId(ctx.e.name,BoolType(),o)
                return BoolType()
            if type(e) is not BoolType: raise TypeMismatchInExpression(ctx)
            return BoolType()
        elif ctx.op =='i2f':
            if e == None: 
                self.setTypeOfId(ctx.e.name,IntType(),o)
                return FloatType()
            if type(e) is not IntType: raise TypeMismatchInExpression(ctx)
            return FloatType()
        else:
            if e == None: 
                self.setTypeOfId(ctx.e.name,FloatType(),o)
                return FloatType()
            if type(e) is not FloatType: raise TypeMismatchInExpression(ctx)
            return IntType()
    def visitIntLit(self,ctx:IntLit,o): return IntType() 

    def visitFloatLit(self,ctx,o): return FloatType()

    def visitBoolLit(self,ctx,o): return BoolType()

    def visitId(self,ctx,o): 
        for i in o:
            if i.name == ctx.name:
                return i.type
        raise UndeclaredIdentifier(ctx.name)