class GetEnv(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o = self.visit(decl,o)
        return o

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        env = []
        for decl in ctx.mem:
            env = self.visit(decl,env)
        return o + [(ctx.name,ctx.parent,env)]

    def visitVarDecl(self,ctx:VarDecl,o:object):
        for decl in o:
            if decl.name == ctx.name : raise RedeclaredField(ctx.name)
        return o + [ctx]
        
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        for decl in o:
            if decl.name == ctx.name : raise RedeclaredMethod(ctx.name)
        return o + [ctx]
        
class StaticCheck(Visitor):
        # class x {
        #     foo(){
        #         x m ;
        #         m.a;
        #         m.b; ERROR here
        #     }
        #     int a
        # } (khai bao bien a sau van chap nhan)
        
    def visitProgram(self,ctx:Program,o:object): 
        #duyet lan dau de lay thong tin so bo o = ["x","",[FuncDecl("foo"),VarDecl("a")]]
        o = GetEnv().visit(ctx,o)
        # duyet lan hai de check
        for decl in ctx.decl:
            self.visit(decl,o)

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        #di lai funcdecl de kiem tra moi truong cuc bo
        for decl in ctx.mem:
            if type(decl) is FuncDecl:
                self.visit(decl,o)
            
    def visitVarDecl(self,ctx:VarDecl,o:object):pass

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        local = ctx.param + ctx.body[0]
        # local ["",m, type(x)] : moi truong cuc bo
        for expr in ctx.body[1]:
            #kiem tra tinh hop le cua m nen can truyen local, o de kiem tra bien hop le cua doi tuong m
            self.visit(expr,(local,o))
            
    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitClassType(self,ctx:ClassType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        for decl in o[0]:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)

    # class FieldAccess(Expr): #exp:Expr,field:str
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        typ = self.visit(ctx.exp,o) # m.a <- ClassType(x)
        if type(typ) is ClassType:
            #kiem tra class m va bien a
            type_info = None
            found = False
            for classDecl in o[1]:
                if typ.name == classDecl[0]:
                    type_info = classDecl
                    found = True
                    break
            if not found: raise UndeclaredClass(typ.name)
            for mem in type_info[2]:
                if ctx.field == mem.name:
                    return mem.typ
            raise UndeclaredField(ctx.field)