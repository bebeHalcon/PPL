from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    
    # program: newline_list? decl_list EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))

    # decl_list: decl_mem decl_list | decl_mem;
    def visitDecl_list(self, ctx: ZCodeParser.Decl_listContext):
        return self.visit(ctx.decl_mem()) + self.visit(ctx.decl_list()) if ctx.decl_list() else self.visit(ctx.decl_mem())
    
    # decl_mem: decl newline_list;
    def visitDecl_mem(self, ctx: ZCodeParser.Decl_memContext):
        return self.visit(ctx.decl())
    
    # decl: var_decl | func_decl;	
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        return [self.visit(ctx.var_decl())] if ctx.var_decl() else [self.visit(ctx.func_decl())]
    
    # var_decl: type_decl | v_decl | dyn_decl;
    def visitVar_decl(self, ctx: ZCodeParser.Var_declContext):
        if ctx.type_decl():
            return self.visit(ctx.type_decl())
        elif ctx.v_decl():
            return self.visit(ctx.v_decl())
        else:
            return self.visit(ctx.dyn_decl())
        
    # dyn_decl: DYNAMIC ID as_expr?;	
    def visitDyn_decl(self, ctx: ZCodeParser.Dyn_declContext):
        varInit = self.visit(ctx.as_expr()) if ctx.as_expr() else None
        return VarDecl(Id(ctx.ID().getText()), None, 'dynamic', varInit)
            
    # v_decl: VAR ID as_expr;
    def visitV_decl(self, ctx: ZCodeParser.V_declContext):
        return VarDecl(Id(ctx.ID().getText()), None, 'var', self.visit(ctx.as_expr()))
    
    # type_decl: types ID arr_dim? as_expr?;	
    def visitType_decl(self, ctx: ZCodeParser.Type_declContext):
        varInit = self.visit(ctx.as_expr()) if ctx.as_expr() else None
        if ctx.arr_dim():
            return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.arr_dim()), self.visit(ctx.types())), None, varInit)
        else:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.types()), None, varInit)
    
    # func_decl: FUNC ID LP param_list RP func_body;	
    def visitFunc_decl(self, ctx: ZCodeParser.Func_declContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.param_list()), self.visit(ctx.func_body()))
    
    # param_list: param_prime | ;	
    def visitParam_list(self, ctx: ZCodeParser.Param_listContext):
        return self.visit(ctx.param_prime()) if ctx.param_prime() else []
    
    # param_prime: param CM param_prime | param;
    def visitParam_prime(self, ctx: ZCodeParser.Param_primeContext):
        return [self.visit(ctx.param())] + self.visit(ctx.param_prime()) if ctx.param_prime() else [self.visit(ctx.param())]

    # param: types ID arr_dim?;	
    def visitParam(self, ctx: ZCodeParser.ParamContext):
        varType = ArrayType(self.visit(ctx.arr_dim()), self.visit(ctx.types())) if ctx.arr_dim() else self.visit(ctx.types())
        return VarDecl(Id(ctx.ID().getText()), varType)

    # func_body: newline_list? return_stmt | newline_list? block_stmt | ;
    def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
        if ctx.getChildCount() == 0:
            return None
        else:
            return self.visit(ctx.return_stmt()) if ctx.return_stmt() else self.visit(ctx.block_stmt())
        
    # stmt_list: stmt_mem stmt_list | ;	
    def visitStmt_list(self, ctx: ZCodeParser.Stmt_listContext):
        return [self.visit(ctx.stmt_mem())] + self.visit(ctx.stmt_list()) if ctx.getChildCount() == 2 else []

    # stmt_mem: stmt newline_list;
    def visitStmt_mem(self, ctx: ZCodeParser.Stmt_memContext):
        return self.visit(ctx.stmt())

    # stmt: match_stmt | unmatch_stmt;
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        return self.visit(ctx.match_stmt()) if ctx.match_stmt() else self.visit(ctx.unmatch_stmt())

    # match_stmt: var_decl
    #     | assign_stmt 
    #     | if_match_stmt 
    #     | for_stmt 
    #     | break_stmt 
    #     | continue_stmt 
    #     | return_stmt 
    #     | func_call_stmt
    #     | block_stmt;
    def visitMatch_stmt(self, ctx: ZCodeParser.Match_stmtContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_match_stmt():
            return self.visit(ctx.if_match_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.func_call_stmt():
            return self.visit(ctx.func_call_stmt())
        else:
            return self.visit(ctx.block_stmt())

    # unmatch_stmt: IF cond_expr newline_list? stmt
	# 		| IF cond_expr newline_list? match_stmt elif_match_list elif_stmt
	# 		| IF cond_expr newline_list? match_stmt elif_match_list else_unmatch_stmt
    #       | for_unmatch_stmt;
    def visitUnmatch_stmt(self, ctx: ZCodeParser.Unmatch_stmtContext):
        if ctx.for_unmatch_stmt():
            return self.visit(ctx.for_unmatch_stmt())
        elif ctx.else_unmatch_stmt():
            return If(self.visit(ctx.cond_expr()), self.visit(ctx.match_stmt()), self.visit(ctx.elif_match_list()), self.visit(ctx.else_unmatch_stmt()))
        elif ctx.elif_stmt():
            elifList = self.visit(ctx.elif_match_list()) + [self.visit(ctx.elif_stmt())]
            return If(self.visit(ctx.cond_expr()), self.visit(ctx.match_stmt()), elifList)
        else:
            return If(self.visit(ctx.cond_expr()), self.visit(ctx.stmt()), [])
        
    # elif_stmt: newline_list ELIF cond_expr newline_list? stmt;
    def visitElif_stmt(self, ctx: ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.cond_expr()), self.visit(ctx.stmt()))
    
    # else_unmatch_stmt: newline_list ELSE newline_list? unmatch_stmt;
    def visitElse_unmatch_stmt(self, ctx: ZCodeParser.Else_unmatch_stmtContext):
        return self.visit(ctx.unmatch_stmt())
    
    # lhs: ID | arr_elem;
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.arr_elem())
        
    # assign_stmt: lhs as_expr;
    def visitAssign_stmt(self, ctx: ZCodeParser.Assign_stmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.as_expr()))
     
    # as_expr: ASSIGN expr;	
    def visitAs_expr(self, ctx: ZCodeParser.As_exprContext):
        return self.visit(ctx.expr())
    
    # if_match_stmt: IF cond_expr newline_list? match_stmt elif_match_list else_match_stmt;
    def visitIf_match_stmt(self, ctx: ZCodeParser.If_match_stmtContext):
        return If(self.visit(ctx.cond_expr()), self.visit(ctx.match_stmt()), self.visit(ctx.elif_match_list()), self.visit(ctx.else_match_stmt()))
    
    # elif_match_list: newline_list elif_match_stmt elif_match_list | ;
    def visitElif_match_list(self, ctx: ZCodeParser.Elif_match_listContext):
        return [self.visit(ctx.elif_match_stmt())] + self.visit(ctx.elif_match_list()) if ctx.elif_match_list() else []
    
    # elif_match_stmt: ELIF cond_expr newline_list? match_stmt;
    def visitElif_match_stmt(self, ctx: ZCodeParser.Elif_match_stmtContext):
        return (self.visit(ctx.cond_expr()), self.visit(ctx.match_stmt()))

    # else_match_stmt: newline_list ELSE newline_list? match_stmt;
    def visitElse_match_stmt(self, ctx: ZCodeParser.Else_match_stmtContext):
        return self.visit(ctx.match_stmt())
    
    # cond_expr: LP expr RP;	
    def visitCond_expr(self, ctx: ZCodeParser.Cond_exprContext):
        return self.visit(ctx.expr())
        
    # for_stmt: FOR ID UNTIL expr BY expr newline_list? match_stmt;	
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.match_stmt()))
    
    # break_stmt: BREAK;
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()
    
    # continue_stmt: CONTINUE;
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()
    
    # return_stmt: RETURN expr?;
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        return Return(self.visit(ctx.expr())) if ctx.expr() else Return()
    
    # func_call_stmt: ID LP expr_list RP;	
    def visitFunc_call_stmt(self, ctx: ZCodeParser.Func_call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))
    
    # block_stmt: BEGIN newline_list stmt_list END;
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.stmt_list()))
    
    # expr_list: expr_prime | ;
    def visitExpr_list(self, ctx: ZCodeParser.Expr_listContext):
        return self.visit(ctx.expr_prime()) if ctx.expr_prime() else []

    # expr_prime: expr CM expr_prime | expr;
    def visitExpr_prime(self, ctx: ZCodeParser.Expr_primeContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_prime()) if ctx.expr_prime() else [self.visit(ctx.expr())]

    # expr: rel_expr CONCAT rel_expr | rel_expr;
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        return BinaryOp('...', self.visit(ctx.rel_expr(0)), self.visit(ctx.rel_expr(1))) if ctx.CONCAT() else self.visit(ctx.rel_expr(0))

    # rel_expr: and_expr (EQ|STR_EQ|NEQ|LESS|GREATER|LEQ|GEQ) and_expr | and_expr;
    def visitRel_expr(self, ctx: ZCodeParser.Rel_exprContext):
        op = '=' if ctx.EQ() else '==' if ctx.STR_EQ() else '!=' if ctx.NEQ() else '<' if ctx.LESS() else '>' if ctx.GREATER() else '<=' if ctx.LEQ() else '>='
        return BinaryOp(op, self.visit(ctx.and_expr(0)), self.visit(ctx.and_expr(1))) if ctx.getChildCount() == 3 else self.visit(ctx.and_expr(0))

    # and_expr: and_expr (AND|OR) add_expr | add_expr;
    def visitAnd_expr(self, ctx: ZCodeParser.And_exprContext):
        op = 'and' if ctx.AND() else 'or'
        return BinaryOp(op, self.visit(ctx.and_expr()), self.visit(ctx.add_expr())) if ctx.getChildCount() == 3 else self.visit(ctx.add_expr())

    # add_expr: add_expr (ADD|SUB) mul_expr | mul_expr;
    def visitAdd_expr(self, ctx: ZCodeParser.Add_exprContext):
        op = '+' if ctx.ADD() else '-'
        return BinaryOp(op, self.visit(ctx.add_expr()), self.visit(ctx.mul_expr())) if ctx.getChildCount() == 3 else self.visit(ctx.mul_expr())

    # mul_expr: mul_expr (MUL|DIV|MOD) not_expr | not_expr;
    def visitMul_expr(self, ctx: ZCodeParser.Mul_exprContext):
        op = '*' if ctx.MUL() else '/' if ctx.DIV() else '%'
        return BinaryOp(op, self.visit(ctx.mul_expr()), self.visit(ctx.not_expr())) if ctx.getChildCount() == 3 else self.visit(ctx.not_expr())

    # not_expr: NOT not_expr | sign_expr;
    def visitNot_expr(self, ctx: ZCodeParser.Not_exprContext):
        return UnaryOp('not', self.visit(ctx.not_expr())) if ctx.NOT() else self.visit(ctx.sign_expr())

    # sign_expr: SUB sign_expr | idx_expr;													
    def visitSign_expr(self, ctx: ZCodeParser.Sign_exprContext):
        return UnaryOp('-', self.visit(ctx.sign_expr())) if ctx.SUB() else self.visit(ctx.idx_expr())

    # idx_expr: elem_expr | operand;
    def visitIdx_expr(self, ctx: ZCodeParser.Idx_exprContext):
        return self.visit(ctx.elem_expr()) if ctx.elem_expr() else self.visit(ctx.operand())

    # elem_expr: (ID | func_call_expr) LSB idx_op RSB;
    def visitElem_expr(self, ctx: ZCodeParser.Elem_exprContext):
        arr = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.func_call_expr())
        return ArrayCell(arr, self.visit(ctx.idx_op()))
    
    # operand: ID | literal | func_call_expr | LP expr RP;
    def visitOperand(self, ctx: ZCodeParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.func_call_expr():
            return self.visit(ctx.func_call_expr())
        else:
            return self.visit(ctx.expr())
    
    # func_call_expr: ID LP expr_list RP;
    def visitFunc_call_expr(self, ctx: ZCodeParser.Func_call_exprContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))

    # arr_elem: ID LSB idx_op RSB;
    def visitArr_elem(self, ctx: ZCodeParser.Arr_elemContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.idx_op()))
    
    # for_unmatch_stmt: FOR ID UNTIL expr BY expr newline_list? unmatch_stmt;
    def visitFor_unmatch_stmt(self, ctx: ZCodeParser.For_unmatch_stmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.unmatch_stmt()))
        
    # types: NUMBER | BOOL | STRING;
    def visitTypes(self, ctx: ZCodeParser.TypesContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return StringType()
        
    # idx_op: expr CM idx_op | expr;
    def visitIdx_op(self, ctx: ZCodeParser.Idx_opContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.idx_op()) if ctx.idx_op() else [self.visit(ctx.expr())]
        
    # arr_lit: LSB expr_prime RSB;
    def visitArr_lit(self, ctx: ZCodeParser.Arr_litContext):
        return ArrayLiteral(self.visit(ctx.expr_prime()))
    
    # dim_list: NUM_LIT CM dim_list | NUM_LIT;
    def visitDim_list(self, ctx: ZCodeParser.Dim_listContext):
        return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.dim_list()) if ctx.dim_list() else [float(ctx.NUM_LIT().getText())]

    # arr_dim: LSB dim_list RSB;
    def visitArr_dim(self, ctx: ZCodeParser.Arr_dimContext):
        return self.visit(ctx.dim_list())

    # literal: NUM_LIT | STR_LIT | BOOL_LIT | arr_lit;
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.NUM_LIT():
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif ctx.BOOL_LIT():
            return BooleanLiteral(True) if ctx.BOOL_LIT().getText() == "true" else BooleanLiteral(False)
        elif ctx.STR_LIT():
            return StringLiteral(ctx.STR_LIT().getText())
        elif ctx.arr_lit():
            return self.visit(ctx.arr_lit())