from functools import reduce 
class IntType: pass
class FloatType: pass
class BoolType: pass
class NoneType: pass
class Symbol: 
    def __init__(self,name,type):
        self.name=name
        self.type=type
class Utils:
    def setTypeForId(name,type,o):
        for i in o:
            for id in i:
                if id.name==name:
                    id.type=type
                    return
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o=[[]]
        for i in ctx.decl:
            self.visit(i,o)
        for i in ctx.stmts:
            self.visit(i,o)
    def visitVarDecl(self,ctx:VarDecl,o): 
        for i in o[0]:
            if i.name==ctx.name:
                raise Redeclared(ctx)
        o[0]+=[Symbol(ctx.name,NoneType())]
    def visitFuncDecl(self,ctx:FuncDecl,o):
        for id in o[0]:
            if id.name == ctx.name:
                raise Redeclared(ctx)
        o[0]+=[Symbol(ctx.name,[])]
        o1=[[]]+o
        for i in ctx.param:
            self.visit(i,o1)
        for i in o[0]:
            if i.name == ctx.name:
                i.type= o1[0]
        for i in ctx.local:
            self.visit(i,o1)
        


        for i in ctx.stmts:
            self.visit(i,o1)
        for item in o[0]:
            if item.name == ctx.name:
                for temp in range(0,len(item.type)):
                    if type(o1[0][temp].type) is not NoneType:
                        item.type[temp].type = o1[0][temp].type
        
        
        
            

    def visitCallStmt(self,ctx:CallStmt,o):
        args = [self.visit(i,o) for i in ctx.args]
        para=False
        for i in o:
            for item in i:
                if item.name == ctx.name:
                    para=item.type
                if type(para) is list:
                    break
        if type(para) is not list:
            raise UndeclaredIdentifier(ctx.name)
        if len(args) != len(para):
            raise TypeMismatchInStatement(ctx)
        for i in range(0, len(args)):
            if type(args[i]) is NoneType and type(para[i].type) is NoneType:
                raise TypeCannotBeInferred(ctx)
            elif type(para[i].type) is NoneType:
                for item in o:
                    for name in item:
                        flag=False
                        if name.name == ctx.name:
                            if type(name.type) is list: 
                                flag=True
                                name.type[i].type=args[i]
                                break
                        if flag: break
            elif type(args[i]) is NoneType:
                Utils.setTypeForId(ctx.args[i].name,para[i].type,o)
            elif type(args[i]) != type(para[i].type):
                raise TypeMismatchInStatement(ctx)

    def visitAssign(self,ctx:Assign,o): 
        rhs=self.visit(ctx.rhs,o)
        lhs=self.visit(ctx.lhs,o)
        
        if type(rhs) is NoneType and type(lhs) is NoneType:
            TypeCannotBeInferred(ctx)
        elif type(rhs) is NoneType:
            Utils.setTypeForId(ctx.rhs.name,lhs,o)
        elif type(lhs) is NoneType:
      
            Utils.setTypeForId(ctx.lhs.name,rhs,o)
        elif type(lhs) != type(rhs):
            raise  TypeMismatchInStatement(ctx)

    def visitIntLit(self,ctx:IntLit,o): return IntType() 

    def visitFloatLit(self,ctx,o): return FloatType()

    def visitBoolLit(self,ctx,o): return BoolType()

    def visitId(self,ctx,o): 
        for i in o:
            for id in i:
                if id.name == ctx.name:
                    return id.type
        raise UndeclaredIdentifier