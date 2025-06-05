from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,cur:  self.visit(cur,acc),ctx.decl,[[]]) 

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        #if ctx.name!= 'a': 
        #    print(o[0])
        #    print("cur: ",ctx.name)
        o[0]+=[ctx.name]
        return o
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0]+=[ctx.name]
        return o
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        o[0]+=[ctx.name]
        
        o2 = [[]]+o
        #if (ctx.name == 'foo'):print(o)
        o1 = reduce(lambda acc,cur:self.visit(cur,acc), ctx.param + ctx.body[0] ,o2)
        
        for i in ctx.body[1]:
            self.visit(i,o1)
        return o
        

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        flag=0
        #print(o)
       
        #if (ctx.name=='z'): print (o)
        for i in o:
        #    print("num of stack: ", len(o))
            for j in i:
        #        print("num of current: ", len(o[i]))
                if ctx.name==j: 
                    flag=1
                    break
            if flag == 1: break
        if (flag==0): raise UndeclaredIdentifier(ctx.name)
        