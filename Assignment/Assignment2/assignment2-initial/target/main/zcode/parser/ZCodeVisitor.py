# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_mem.
    def visitDecl_mem(self, ctx:ZCodeParser.Decl_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dyn_decl.
    def visitDyn_decl(self, ctx:ZCodeParser.Dyn_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#v_decl.
    def visitV_decl(self, ctx:ZCodeParser.V_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_decl.
    def visitType_decl(self, ctx:ZCodeParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_prime.
    def visitParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_body.
    def visitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_mem.
    def visitStmt_mem(self, ctx:ZCodeParser.Stmt_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#match_stmt.
    def visitMatch_stmt(self, ctx:ZCodeParser.Match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#unmatch_stmt.
    def visitUnmatch_stmt(self, ctx:ZCodeParser.Unmatch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_unmatch_stmt.
    def visitElse_unmatch_stmt(self, ctx:ZCodeParser.Else_unmatch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#as_expr.
    def visitAs_expr(self, ctx:ZCodeParser.As_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_match_stmt.
    def visitIf_match_stmt(self, ctx:ZCodeParser.If_match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_match_list.
    def visitElif_match_list(self, ctx:ZCodeParser.Elif_match_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_match_stmt.
    def visitElif_match_stmt(self, ctx:ZCodeParser.Elif_match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_match_stmt.
    def visitElse_match_stmt(self, ctx:ZCodeParser.Else_match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cond_expr.
    def visitCond_expr(self, ctx:ZCodeParser.Cond_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_unmatch_stmt.
    def visitFor_unmatch_stmt(self, ctx:ZCodeParser.For_unmatch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_prime.
    def visitExpr_prime(self, ctx:ZCodeParser.Expr_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#rel_expr.
    def visitRel_expr(self, ctx:ZCodeParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#and_expr.
    def visitAnd_expr(self, ctx:ZCodeParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_expr.
    def visitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mul_expr.
    def visitMul_expr(self, ctx:ZCodeParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#not_expr.
    def visitNot_expr(self, ctx:ZCodeParser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#idx_expr.
    def visitIdx_expr(self, ctx:ZCodeParser.Idx_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elem_expr.
    def visitElem_expr(self, ctx:ZCodeParser.Elem_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_expr.
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_elem.
    def visitArr_elem(self, ctx:ZCodeParser.Arr_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#types.
    def visitTypes(self, ctx:ZCodeParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#idx_op.
    def visitIdx_op(self, ctx:ZCodeParser.Idx_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_lit.
    def visitArr_lit(self, ctx:ZCodeParser.Arr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dim_list.
    def visitDim_list(self, ctx:ZCodeParser.Dim_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_dim.
    def visitArr_dim(self, ctx:ZCodeParser.Arr_dimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)



del ZCodeParser