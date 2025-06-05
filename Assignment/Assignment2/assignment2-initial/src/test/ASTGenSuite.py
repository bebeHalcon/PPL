import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    astTest = 299
    def test_ast_00(self):
        inp = \
"""number a
"""
        out = "Program([VarDecl(Id(a), NumberType, None, None)])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_01(self):
        inp = \
"""var str <- "Hello world!"
"""
        out = "Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_02(self):
        inp = \
"""var a <- bcd + 456
func foo(number x, string s)
begin
    y <- x + 4
    s <- concat(s,"s")
end
"""
        out = "Program([VarDecl(Id(a), None, var, BinaryOp(+, Id(bcd), NumLit(456.0))), FuncDecl(Id(foo), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(s), StringType, None, None)], Block([AssignStmt(Id(y), BinaryOp(+, Id(x), NumLit(4.0))), AssignStmt(Id(s), CallExpr(Id(concat), [Id(s), StringLit(s)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_03(self):
        inp = \
"""

func foo__(bool boo)
begin
    concat(boo,"s"* 74)
    s <- concat(s,-61.245)
end
var x__y <- [a,b,c] + 456
"""
        out = "Program([FuncDecl(Id(foo__), [VarDecl(Id(boo), BoolType, None, None)], Block([CallStmt(Id(concat), [Id(boo), BinaryOp(*, StringLit(s), NumLit(74.0))]), AssignStmt(Id(s), CallExpr(Id(concat), [Id(s), UnaryOp(-, NumLit(61.245))]))])), VarDecl(Id(x__y), None, var, BinaryOp(+, ArrayLit(Id(a), Id(b), Id(c)), NumLit(456.0)))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_04(self):
        inp = \
"""
func main(bool boo)
begin
    number arr[2.3,47] <- 1 + "6"
    s <- main(arr,2)
end
"""
        out = "Program([FuncDecl(Id(main), [VarDecl(Id(boo), BoolType, None, None)], Block([VarDecl(Id(arr), ArrayType([2.3, 47.0], NumberType), None, BinaryOp(+, NumLit(1.0), StringLit(6))), AssignStmt(Id(s), CallExpr(Id(main), [Id(arr), NumLit(2.0)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_05(self):
        inp = \
"""
func x(string arr[2,3,4])
begin
    number abc_dfg[2.3,47] <- arr
    main(6+  [4,arr])
end
"""
        out = "Program([FuncDecl(Id(x), [VarDecl(Id(arr), ArrayType([2.0, 3.0, 4.0], StringType), None, None)], Block([VarDecl(Id(abc_dfg), ArrayType([2.3, 47.0], NumberType), None, Id(arr)), CallStmt(Id(main), [BinaryOp(+, NumLit(6.0), ArrayLit(NumLit(4.0), Id(arr)))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_06(self):
        inp = \
"""## block in block
func ___(number arr[2])
begin
    number abc_dfg[2.3,47] <- arr(487,456,9,4*4,6-7,3 % 2)
    begin
        writeString(4+8+"abc"/true*__(abc_dfg))
    end

    x <- 6 - function(x[4,7.0])
end
"""
        out = "Program([FuncDecl(Id(___), [VarDecl(Id(arr), ArrayType([2.0], NumberType), None, None)], Block([VarDecl(Id(abc_dfg), ArrayType([2.3, 47.0], NumberType), None, CallExpr(Id(arr), [NumLit(487.0), NumLit(456.0), NumLit(9.0), BinaryOp(*, NumLit(4.0), NumLit(4.0)), BinaryOp(-, NumLit(6.0), NumLit(7.0)), BinaryOp(%, NumLit(3.0), NumLit(2.0))])), Block([CallStmt(Id(writeString), [BinaryOp(+, BinaryOp(+, NumLit(4.0), NumLit(8.0)), BinaryOp(*, BinaryOp(/, StringLit(abc), BooleanLit(True)), CallExpr(Id(__), [Id(abc_dfg)])))])]), AssignStmt(Id(x), BinaryOp(-, NumLit(6.0), CallExpr(Id(function), [ArrayCell(Id(x), [NumLit(4.0), NumLit(7.0)])])))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_07(self):
        inp = \
"""## test expression
func kid1412(number ranma1over2[2,8.1]) begin
    return (1 + 2.4) /  false * (3 -4 % (-6)) - arr([6,arr[6]],6,[6])
end
"""
        out = "Program([FuncDecl(Id(kid1412), [VarDecl(Id(ranma1over2), ArrayType([2.0, 8.1], NumberType), None, None)], Block([Return(BinaryOp(-, BinaryOp(*, BinaryOp(/, BinaryOp(+, NumLit(1.0), NumLit(2.4)), BooleanLit(False)), BinaryOp(-, NumLit(3.0), BinaryOp(%, NumLit(4.0), UnaryOp(-, NumLit(6.0))))), CallExpr(Id(arr), [ArrayLit(NumLit(6.0), ArrayCell(Id(arr), [NumLit(6.0)])), NumLit(6.0), ArrayLit(NumLit(6.0))])))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_08(self):
        inp = \
"""## more test expression
func kid1412(number ranma1over2[2,8.1]) begin
    dynamic A
    a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1)))))...(x !=y)
    return x
end
"""
        out = "Program([FuncDecl(Id(kid1412), [VarDecl(Id(ranma1over2), ArrayType([2.0, 8.1], NumberType), None, None)], Block([VarDecl(Id(A), None, dynamic, None), AssignStmt(Id(a), BinaryOp(..., BinaryOp(<=, BinaryOp(and, BinaryOp(or, Id(A), Id(B)), BinaryOp(+, Id(C), BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(3.0), NumLit(2.0)), NumLit(4.0)), NumLit(3.0)))), UnaryOp(not, BinaryOp(+, UnaryOp(-, NumLit(1.0)), CallExpr(Id(foo), [BinaryOp(+, Id(x), BinaryOp(*, Id(y), BinaryOp(-, Id(z), NumLit(1.0))))])))), BinaryOp(!=, Id(x), Id(y)))), Return(Id(x))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_09(self):
        inp = \
"""## return without block
func kid1412(number kuroba[14,12]) return kaitou
"""
        out = "Program([FuncDecl(Id(kid1412), [VarDecl(Id(kuroba), ArrayType([14.0, 12.0], NumberType), None, None)], Return(Id(kaitou)))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))


    def test_ast_10(self):
        inp = \
"""## multiple predeclarations
func a(string a)
func b(string b)
func c(string c)
func d(string d) return a
func e(string e) return b
func f(string f) return c
func g(string g) return d
func h(string h) begin
end
"""
        out = "Program([FuncDecl(Id(a), [VarDecl(Id(a), StringType, None, None)], None), FuncDecl(Id(b), [VarDecl(Id(b), StringType, None, None)], None), FuncDecl(Id(c), [VarDecl(Id(c), StringType, None, None)], None), FuncDecl(Id(d), [VarDecl(Id(d), StringType, None, None)], Return(Id(a))), FuncDecl(Id(e), [VarDecl(Id(e), StringType, None, None)], Return(Id(b))), FuncDecl(Id(f), [VarDecl(Id(f), StringType, None, None)], Return(Id(c))), FuncDecl(Id(g), [VarDecl(Id(g), StringType, None, None)], Return(Id(d))), FuncDecl(Id(h), [VarDecl(Id(h), StringType, None, None)], Block([]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_11(self):
        inp = \
"""## multiple empty blocks
func main(number x, bool b) begin
begin
end
begin
begin
end
begin
end
end
begin
end
end
"""
        out = "Program([FuncDecl(Id(main), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(b), BoolType, None, None)], Block([Block([]), Block([Block([]), Block([])]), Block([])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_12(self):
        inp = \
"""## multiple global variable declarations
var x <- 6
var y <- "7"
var z <- true

func main(number x, bool b) begin
    print(x,y,z,t)
end

var t <- foo(x,y,z)
"""
        out = "Program([VarDecl(Id(x), None, var, NumLit(6.0)), VarDecl(Id(y), None, var, StringLit(7)), VarDecl(Id(z), None, var, BooleanLit(True)), FuncDecl(Id(main), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(b), BoolType, None, None)], Block([CallStmt(Id(print), [Id(x), Id(y), Id(z), Id(t)])])), VarDecl(Id(t), None, var, CallExpr(Id(foo), [Id(x), Id(y), Id(z)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_13(self):
        inp = \
"""## 
number x <- 1
func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx..."") 

xy<-    xy
        elif (1 + 2 == 3) return 0
        else if ( a- n < 6) number c
        var foo <- (54 + 1)*(4 / True[6,2])
        bool arr <- arr[-7] 
        return not -1

end 
"""
        out = "Program([VarDecl(Id(x), NumberType, None, NumLit(1.0)), FuncDecl(Id(True), [VarDecl(Id(_), NumberType, None, None)], Block([If((BinaryOp(==, BinaryOp(<=, Id(x), BinaryOp(and, Id(_), CallExpr(Id(f), [Id(z)]))), BinaryOp(or, BooleanLit(True), ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))), If((BinaryOp(..., BinaryOp(==, ArrayLit(UnaryOp(-, NumLit(2.0)), NumLit(3.0)), Id(yx)), StringLit()), AssignStmt(Id(xy), Id(xy))), [(BinaryOp(==, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), Return(NumLit(0.0)))], If((BinaryOp(<, BinaryOp(-, Id(a), Id(n)), NumLit(6.0)), VarDecl(Id(c), NumberType, None, None)), [], None))), [], None), VarDecl(Id(foo), None, var, BinaryOp(*, BinaryOp(+, NumLit(54.0), NumLit(1.0)), BinaryOp(/, NumLit(4.0), ArrayCell(Id(True), [NumLit(6.0), NumLit(2.0)])))), VarDecl(Id(arr), BoolType, None, ArrayCell(Id(arr), [UnaryOp(-, NumLit(7.0))])), Return(UnaryOp(not, UnaryOp(-, NumLit(1.0))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_14(self):
        inp = \
"""## trick about function declaration and global variable declaration
func foo(string str)
var x <- 7 + (t - false)
"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(str), StringType, None, None)], None), VarDecl(Id(x), None, var, BinaryOp(+, NumLit(7.0), BinaryOp(-, Id(t), BooleanLit(False))))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_15(self):
        inp = \
"""## random testcase
func main()  
    begin
        var x <- const* (4 + -12)
    x <- 7 and 1
number arr[3] <- [const,n[8],  getVar(6,true)]

end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), None, var, BinaryOp(*, Id(const), BinaryOp(+, NumLit(4.0), UnaryOp(-, NumLit(12.0))))), AssignStmt(Id(x), BinaryOp(and, NumLit(7.0), NumLit(1.0))), VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(Id(const), ArrayCell(Id(n), [NumLit(8.0)]), CallExpr(Id(getVar), [NumLit(6.0), BooleanLit(True)])))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_16(self):
        inp = \
"""## multi-dimensional array declaration check
func foo(number a) return a+1
number a[2,3] <- [[1+2,3,"abc",foo(4)],[true,false,true]]

"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0), StringLit(abc), CallExpr(Id(foo), [NumLit(4.0)])), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True))))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_17(self):
        inp = \
"""## array assignment with string
func foo(number a) begin
    string arr[7]
    arr[6] <- "'4+6'""
end

"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(arr), ArrayType([7.0], StringType), None, None), AssignStmt(ArrayCell(Id(arr), [NumLit(6.0)]), StringLit('4+6'\"))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_18(self):
        inp = \
"""## string with escaped sequences
func foo(number a) begin
    var arr <- 612
    arr[6] <- "dr.Stone\\r\\b  \\n\\t\\f' "
end

"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(arr), None, var, NumLit(612.0)), AssignStmt(ArrayCell(Id(arr), [NumLit(6.0)]), StringLit(dr.Stone\\r\\b  \\n\\t\\f' ))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_19(self):
        inp = \
"""func bar(number arr,bool b ) ## Day la comment giua chung
begin
x[2,8] <- foo([1,2,"abcd",154/4])
number x <- readString()
number x[6] <- [1,2,3]
## Day la comment ben trong


end

## Day la comment ben ngoai
"""
        out = "Program([FuncDecl(Id(bar), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(b), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(x), [NumLit(2.0), NumLit(8.0)]), CallExpr(Id(foo), [ArrayLit(NumLit(1.0), NumLit(2.0), StringLit(abcd), BinaryOp(/, NumLit(154.0), NumLit(4.0)))])), VarDecl(Id(x), NumberType, None, CallExpr(Id(readString), [])), VarDecl(Id(x), ArrayType([6.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_20(self):
        inp = \
"""## multiple function declarations with empty parameter list
func main()
func main1()
func main2()
func main3() begin
end
func main4()
"""
        out = "Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main1), [], None), FuncDecl(Id(main2), [], None), FuncDecl(Id(main3), [], Block([])), FuncDecl(Id(main4), [], None)])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_21(self):
        inp = \
"""## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if__(var_)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), CallStmt(Id(if__), [Id(var_)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_22(self):
        inp = \
"""## just another random testcase
func main()
begin 
    var new <- __init__(self,x,y)
    dynamic x <- 6
end
number xxx
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(new), None, var, CallExpr(Id(__init__), [Id(self), Id(x), Id(y)])), VarDecl(Id(x), None, dynamic, NumLit(6.0))])), VarDecl(Id(xxx), NumberType, None, None)])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_23(self):
        inp = \
"""## check case-sensitive identifiers
func True(number _) begin       
if (x <= _ and f(z) + true or _) 
        falSe(a,2,"b")

end
"""
        out = "Program([FuncDecl(Id(True), [VarDecl(Id(_), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), BinaryOp(or, BinaryOp(and, Id(_), BinaryOp(+, CallExpr(Id(f), [Id(z)]), BooleanLit(True))), Id(_))), CallStmt(Id(falSe), [Id(a), NumLit(2.0), StringLit(b)])), [], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_24(self):
        inp = \
"""func bar(string str)   
begin ## begin
var x <- y + "abc\\'x"...6
end

number arr[7]
"""
        out = "Program([FuncDecl(Id(bar), [VarDecl(Id(str), StringType, None, None)], Block([VarDecl(Id(x), None, var, BinaryOp(..., BinaryOp(+, Id(y), StringLit(abc\\'x)), NumLit(6.0)))])), VarDecl(Id(arr), ArrayType([7.0], NumberType), None, None)])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_25(self):
        inp = \
""" ## simply check if-statement
func main(number x)   
begin 
var y <- [0,1,2]
    if (12 +((x + 7) >= 9- 6*  9)) begin
        readNumber(y)
    end
end
"""
        out = "Program([FuncDecl(Id(main), [VarDecl(Id(x), NumberType, None, None)], Block([VarDecl(Id(y), None, var, ArrayLit(NumLit(0.0), NumLit(1.0), NumLit(2.0))), If((BinaryOp(+, NumLit(12.0), BinaryOp(>=, BinaryOp(+, Id(x), NumLit(7.0)), BinaryOp(-, NumLit(9.0), BinaryOp(*, NumLit(6.0), NumLit(9.0))))), Block([CallStmt(Id(readNumber), [Id(y)])])), [], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_26(self):
        inp = \
""" ## another simply check if-statement
func main(number x)   
begin 
    if (true and true) x <- 6 + 7*True(x)
    else begin
        writeBool(x)
    end
end
"""
        out = "Program([FuncDecl(Id(main), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(and, BooleanLit(True), BooleanLit(True)), AssignStmt(Id(x), BinaryOp(+, NumLit(6.0), BinaryOp(*, NumLit(7.0), CallExpr(Id(True), [Id(x)]))))), [], Block([CallStmt(Id(writeBool), [Id(x)])]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_27(self):
        inp = \
""" ## multiple consecutive if-statements without elif and else
func main()   
begin 
    if (a) 
    if (b)
    if (c)
    if (d)
    if (e)
    if (f)
    begin
    end
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), Block([])), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_28(self):
        inp = \
""" ## multiple consecutive elif-statements
func main()   
begin 
    if (a) begin
    end
    elif (b) begin
    end
    elif (c) begin
    end
    elif (d) begin
    end
    elif (e) begin
    end
    elif (f) begin
    end
    else begin
    end
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((Id(a), Block([])), [(Id(b), Block([])), (Id(c), Block([])), (Id(d), Block([])), (Id(e), Block([])), (Id(f), Block([]))], Block([]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_29(self):
        inp = \
""" ## if in if (1)
func main()   
begin 
    if (1) if (b) writeNumber(b)
    elif (c) writeNumber(c)
    elif (d) writeNumber(d)
    elif (e) writeNumber(e)
    else writeNumber(1)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((Id(b), CallStmt(Id(writeNumber), [Id(b)])), [(Id(c), CallStmt(Id(writeNumber), [Id(c)])), (Id(d), CallStmt(Id(writeNumber), [Id(d)])), (Id(e), CallStmt(Id(writeNumber), [Id(e)]))], CallStmt(Id(writeNumber), [NumLit(1.0)]))), [], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_30(self):
        inp = \
""" ## if in if (2)
func main()   
begin 
    if (1) begin 
        if (b) writeNumber(b)
        elif (c) writeNumber(c)
        elif (d) writeNumber(d)
    end
    elif (e) writeNumber(e)
    else writeNumber(1)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), Block([If((Id(b), CallStmt(Id(writeNumber), [Id(b)])), [(Id(c), CallStmt(Id(writeNumber), [Id(c)])), (Id(d), CallStmt(Id(writeNumber), [Id(d)]))], None)])), [(Id(e), CallStmt(Id(writeNumber), [Id(e)]))], CallStmt(Id(writeNumber), [NumLit(1.0)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_31(self):
        inp = \
""" ## if in if (3)
func main()   
begin 
    if (1) begin 
        if (b) writeNumber(b)
        elif (c) writeNumber(c)
        elif (d) writeNumber(d)
    end
    elif (2) if (b) writeNumber(b)
        elif (c) writeNumber(c)
        elif (d) writeNumber(d)
    else writeNumber(2)
    else writeNumber(3)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), Block([If((Id(b), CallStmt(Id(writeNumber), [Id(b)])), [(Id(c), CallStmt(Id(writeNumber), [Id(c)])), (Id(d), CallStmt(Id(writeNumber), [Id(d)]))], None)])), [(NumLit(2.0), If((Id(b), CallStmt(Id(writeNumber), [Id(b)])), [(Id(c), CallStmt(Id(writeNumber), [Id(c)])), (Id(d), CallStmt(Id(writeNumber), [Id(d)]))], CallStmt(Id(writeNumber), [NumLit(2.0)])))], CallStmt(Id(writeNumber), [NumLit(3.0)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_32(self):
        inp = \
""" ## if in if (4)
func main()   
begin 
    if (a) a()
    elif (b) b()
    elif (c) c()
    else if (d) d()
    elif (e) e()
    elif (f) f()
    else g()
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((Id(a), CallStmt(Id(a), [])), [(Id(b), CallStmt(Id(b), [])), (Id(c), CallStmt(Id(c), []))], If((Id(d), CallStmt(Id(d), [])), [(Id(e), CallStmt(Id(e), [])), (Id(f), CallStmt(Id(f), []))], CallStmt(Id(g), [])))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_33(self):
        inp = \
""" ## if in if (5)
func main()   
begin 
    if (1) if (2) if (3) if (4) if (5) if (6) if (7) if (8) if (9) if (10) CallStmt(11)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), If((NumLit(3.0), If((NumLit(4.0), If((NumLit(5.0), If((NumLit(6.0), If((NumLit(7.0), If((NumLit(8.0), If((NumLit(9.0), If((NumLit(10.0), CallStmt(Id(CallStmt), [NumLit(11.0)])), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_34(self):
        inp = \
""" ## random testcase
func main()
begin 
    writeString("Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), If((NumLit(3.0), If((NumLit(4.0), If((NumLit(5.0), If((NumLit(6.0), If((NumLit(7.0), If((NumLit(8.0), If((NumLit(9.0), If((NumLit(10.0), CallStmt(Id(CallStmt), [NumLit(11.0)])), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])")
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(writeString), [StringLit(Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), If((NumLit(3.0), If((NumLit(4.0), If((NumLit(5.0), If((NumLit(6.0), If((NumLit(7.0), If((NumLit(8.0), If((NumLit(9.0), If((NumLit(10.0), CallStmt(Id(CallStmt), [NumLit(11.0)])), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))]))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_35(self):
        inp = \
""" ## if in for
func ___(number _) begin       
if (x <= _) begin 
        foo(a,2,"b")
    end
for ____ until ____ * 2 by "abc" 
if (_) begin   
    end
    _(boolean,_) 
    begin

    _(___,__,_____ ) 
    __ <- ____ * _ + __ - _(__,___)[_,[__,8],____]
end
end
"""
        out = "Program([FuncDecl(Id(___), [VarDecl(Id(_), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), Id(_)), Block([CallStmt(Id(foo), [Id(a), NumLit(2.0), StringLit(b)])])), [], None), For(Id(____), BinaryOp(*, Id(____), NumLit(2.0)), StringLit(abc), If((Id(_), Block([])), [], None)), CallStmt(Id(_), [Id(boolean), Id(_)]), Block([CallStmt(Id(_), [Id(___), Id(__), Id(_____)]), AssignStmt(Id(__), BinaryOp(-, BinaryOp(+, BinaryOp(*, Id(____), Id(_)), Id(__)), ArrayCell(CallExpr(Id(_), [Id(__), Id(___)]), [Id(_), ArrayLit(Id(__), NumLit(8.0)), Id(____)])))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_36(self):
        inp = \
"""## find max in array
func max(number a[100], number length)
begin
    if (length <= 0)
        return -1e9 ## Represent negative infinity
    var max <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] > max) max <- a[i]
    return max
end
"""
        out = "Program([FuncDecl(Id(max), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<=, Id(length), NumLit(0.0)), Return(UnaryOp(-, NumLit(1000000000.0)))), [], None), VarDecl(Id(max), None, var, ArrayCell(Id(a), [NumLit(0.0)])), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), If((BinaryOp(>, ArrayCell(Id(a), [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(Id(a), [Id(i)]))), [], None)), Return(Id(max))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_37(self):
        inp = \
"""## Float number literal
func main()
begin
    writeNumber(12.75e8)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [NumLit(1275000000.0)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_38(self):
        inp = \
"""## Float number literal
func main()
begin
    writeNumber(-12.75E-8)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [UnaryOp(-, NumLit(1.275e-07))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_39(self):
        inp = \
"""## Float number literal
func main()
begin
    writeNumber(126.E-4)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [NumLit(0.0126)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_40(self):
        inp = \
"""## Float number literal
func main()
begin
    writeNumber(00876.12e0004)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [NumLit(8761200.0)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_41(self):
        inp = \
"""## Float number literal
func main()
begin
    writeNumber(1.e+5)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [NumLit(100000.0)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_42(self):
        inp = \
"""## consecutive same function decl with return-statements
func main() return 1
func main() return 2
func main() return 3
func main() return 4
func main() return 5
"""
        out = "Program([FuncDecl(Id(main), [], Return(NumLit(1.0))), FuncDecl(Id(main), [], Return(NumLit(2.0))), FuncDecl(Id(main), [], Return(NumLit(3.0))), FuncDecl(Id(main), [], Return(NumLit(4.0))), FuncDecl(Id(main), [], Return(NumLit(5.0)))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_43(self):
        inp = \
"""## for in elif
func min(number a, string b)
begin  
if (x <= false)
begin 
main(a,2,"b")
x <- 8*8
end
elif (abc > "abc") 

for id until id >= 4 by 1 loop1(arr[a(b),b(a)])
loop2(arr[a(b)],b[2])

func1(x) 
begin
func2(y)
end
end
"""
        out = "Program([FuncDecl(Id(min), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, None)], Block([If((BinaryOp(<=, Id(x), BooleanLit(False)), Block([CallStmt(Id(main), [Id(a), NumLit(2.0), StringLit(b)]), AssignStmt(Id(x), BinaryOp(*, NumLit(8.0), NumLit(8.0)))])), [(BinaryOp(>, Id(abc), StringLit(abc)), For(Id(id), BinaryOp(>=, Id(id), NumLit(4.0)), NumLit(1.0), CallStmt(Id(loop1), [ArrayCell(Id(arr), [CallExpr(Id(a), [Id(b)]), CallExpr(Id(b), [Id(a)])])])))], None), CallStmt(Id(loop2), [ArrayCell(Id(arr), [CallExpr(Id(a), [Id(b)])]), ArrayCell(Id(b), [NumLit(2.0)])]), CallStmt(Id(func1), [Id(x)]), Block([CallStmt(Id(func2), [Id(y)])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_44(self):
        inp = \
"""## if if else else 
func main() begin 
bool a<-true 
bool b<-false 
if (not a) 
    if (b) writeString("b is correct")
    else writeString("b is not correct")
else writeString("a is correct")
return
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), VarDecl(Id(b), BoolType, None, BooleanLit(False)), If((UnaryOp(not, Id(a)), If((Id(b), CallStmt(Id(writeString), [StringLit(b is correct)])), [], CallStmt(Id(writeString), [StringLit(b is not correct)]))), [], CallStmt(Id(writeString), [StringLit(a is correct)])), Return()]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_45(self):
        inp = \
"""## if elif if elif elif else 
func main()
begin 
if(1) return 
elif (2) 
    if (3) return 
    elif (4) return 
    elif (5) return 
    else return
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), Return()), [(NumLit(2.0), If((NumLit(3.0), Return()), [(NumLit(4.0), Return()), (NumLit(5.0), Return())], Return()))], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_46(self):
        inp = \
"""##declare in statement without block
func main() 
begin 
    if (1) string a[3,2] <- [[1,2],[3,4],[5,6]]
    else number b[4,4,4]
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], StringType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], VarDecl(Id(b), ArrayType([4.0, 4.0, 4.0], NumberType), None, None))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_47(self):
        inp = \
"""## simple for-statement
func main() 
begin 
    for id until id >= 4 by 1.5555 
    loop(arr[a(b),b[a]])
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([For(Id(id), BinaryOp(>=, Id(id), NumLit(4.0)), NumLit(1.5555), CallStmt(Id(loop), [ArrayCell(Id(arr), [CallExpr(Id(a), [Id(b)]), ArrayCell(Id(b), [Id(a)])])]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_48(self):
        inp = \
"""## simple for-statement
func main() 
begin 
    for id until id >= 4 by 1.5555 if (6) b <- 7 + a
        elif (7) if (8) return
        elif (9) begin
            if (10) var x <- true
            else print(abc)
            return
        end
        elif (11) return 7
        else return 8
    else return 9

    
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([For(Id(id), BinaryOp(>=, Id(id), NumLit(4.0)), NumLit(1.5555), If((NumLit(6.0), AssignStmt(Id(b), BinaryOp(+, NumLit(7.0), Id(a)))), [(NumLit(7.0), If((NumLit(8.0), Return()), [(NumLit(9.0), Block([If((NumLit(10.0), VarDecl(Id(x), None, var, BooleanLit(True))), [], CallStmt(Id(print), [Id(abc)])), Return()])), (NumLit(11.0), Return(NumLit(7.0)))], Return(NumLit(8.0))))], Return(NumLit(9.0))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_49(self):
        inp = \
"""## string using ## 
func main()
begin 
    string s<-"this test case is to check if it is work normally if ## in the string"
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(s), StringType, None, StringLit(this test case is to check if it is work normally if ## in the string))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_50(self):
        inp = \
"""## exmaple of block in Zcode specification page 12
func main() begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, None), AssignStmt(Id(r), NumLit(2.0)), VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), ArrayType([5.0], NumberType), None, None), AssignStmt(Id(s), BinaryOp(*, BinaryOp(*, Id(r), Id(r)), NumLit(3.14))), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), Id(s))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_51(self):
        inp = \
"""func main() begin
if (1) writeString("1")
elif (2) if(3) writeString("1")
elif (4) writeString("1")
else writeString("1")
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_52(self):
        inp = \
"""func main()
begin
    var i <- 0
    number j <- 0
    for i until i <= 10 by 2
    begin
        for j until j <= 20 by 4
            writeNumber(i*j)
    end
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_53(self):
        inp = \
"""func main() begin
if (1)
	if (2)
		b()
	elif (3)
		if (4)
			c()
		elif (5)
			d()
		else e()
	elif(6)
		f()
	else g()
elif (7) h()
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), CallStmt(Id(b), [])), [(NumLit(3.0), If((NumLit(4.0), CallStmt(Id(c), [])), [(NumLit(5.0), CallStmt(Id(d), []))], CallStmt(Id(e), []))), (NumLit(6.0), CallStmt(Id(f), []))], CallStmt(Id(g), []))), [(NumLit(7.0), CallStmt(Id(h), []))], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_54(self):
        inp = \
"""func main() begin
if (1)
	if (2)
		b()
	elif (3)
		if (4)
			c()
		elif (5)
			d()
		else e()
	elif(6)
		f()
	else g()
elif (7) h()
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), CallStmt(Id(b), [])), [(NumLit(3.0), If((NumLit(4.0), CallStmt(Id(c), [])), [(NumLit(5.0), CallStmt(Id(d), []))], CallStmt(Id(e), []))), (NumLit(6.0), CallStmt(Id(f), []))], CallStmt(Id(g), []))), [(NumLit(7.0), CallStmt(Id(h), []))], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_55(self):
        inp = \
"""## expresion in array lit 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)+3
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(4)*foo(foo(3))]]
"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(+, BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])), NumLit(3.0)))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [NumLit(4.0)])), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])])))))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_56(self):
        inp = \
"""## Merge sort with zcode
func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if ((i < n1) and (j >= n2) or (L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end
"""
        out = "Program([FuncDecl(Id(merge), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(mid), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), VarDecl(Id(k), NumberType, None, None), VarDecl(Id(n1), NumberType, None, BinaryOp(+, BinaryOp(-, Id(mid), Id(left)), NumLit(1.0))), VarDecl(Id(n2), NumberType, None, BinaryOp(-, Id(right), Id(mid))), VarDecl(Id(L), ArrayType([100.0], NumberType), None, None), VarDecl(Id(R), ArrayType([100.0], NumberType), None, None), For(Id(i), BinaryOp(<, Id(i), Id(n1)), NumLit(1.0), AssignStmt(ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(left), Id(i))]))), For(Id(j), BinaryOp(<, Id(j), Id(n2)), NumLit(1.0), AssignStmt(ArrayCell(Id(R), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, BinaryOp(+, Id(mid), NumLit(1.0)), Id(j))]))), AssignStmt(Id(i), NumLit(0.0)), AssignStmt(Id(j), NumLit(0.0)), AssignStmt(Id(k), Id(left)), For(Id(k), BinaryOp(<=, Id(k), Id(right)), NumLit(1.0), Block([If((BinaryOp(or, BinaryOp(and, BinaryOp(<, Id(i), Id(n1)), BinaryOp(>=, Id(j), Id(n2))), BinaryOp(<=, ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(R), [Id(j)]))), Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(L), [Id(i)])), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), [], Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(R), [Id(j)])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0)))]))]))])), FuncDecl(Id(mergeSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(<, Id(left), Id(right)), Block([VarDecl(Id(mid), NumberType, None, BinaryOp(/, BinaryOp(+, Id(left), Id(right)), NumLit(2.0))), CallStmt(Id(mergeSort), [Id(arr), Id(left), Id(mid)]), CallStmt(Id(mergeSort), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(right)]), CallStmt(Id(merge), [Id(arr), Id(left), Id(mid), Id(right)])])), [], None)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_57(self):
        inp = \
"""##if in for
func main() begin
    number i<-0 
    for i until i>0 by 1
        if (1) 
            for i until i<0 by 1
                if (2) continue
                else break
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), NumLit(0.0)), NumLit(1.0), If((NumLit(1.0), For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), NumLit(1.0), If((NumLit(2.0), Continue), [], Break))), [], None))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_58(self):
        inp = \
"""## fibonanci
number res[100]

func fib(number n)
begin
    if (res[n] != -1) return res[n]
    res[n] <- fib(n - 1) + fib(n - 2)
    return res[n]
end

func main() begin
    res[0] <- 0
    res[1] <- 1
    
    var i <- 2
    for i until i = 100 by 1 res[i] <- -1
    
    writeNumber(fib(5))
    writeNumber(fib(10))
    writeNumber(fib(50))
end
"""
        out = "Program([VarDecl(Id(res), ArrayType([100.0], NumberType), None, None), FuncDecl(Id(fib), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(!=, ArrayCell(Id(res), [Id(n)]), UnaryOp(-, NumLit(1.0))), Return(ArrayCell(Id(res), [Id(n)]))), [], None), AssignStmt(ArrayCell(Id(res), [Id(n)]), BinaryOp(+, CallExpr(Id(fib), [BinaryOp(-, Id(n), NumLit(1.0))]), CallExpr(Id(fib), [BinaryOp(-, Id(n), NumLit(2.0))]))), Return(ArrayCell(Id(res), [Id(n)]))])), FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(res), [NumLit(0.0)]), NumLit(0.0)), AssignStmt(ArrayCell(Id(res), [NumLit(1.0)]), NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(res), [Id(i)]), UnaryOp(-, NumLit(1.0)))), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(5.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(50.0)])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_59(self):
        inp = \
"""## fibonanci
number res[100]
func res(number x)
    number res[99]
func res(number y) begin
    number res[98]
end
func res(number y) return res
"""
        out = "Program([VarDecl(Id(res), ArrayType([100.0], NumberType), None, None), FuncDecl(Id(res), [VarDecl(Id(x), NumberType, None, None)], None), VarDecl(Id(res), ArrayType([99.0], NumberType), None, None), FuncDecl(Id(res), [VarDecl(Id(y), NumberType, None, None)], Block([VarDecl(Id(res), ArrayType([98.0], NumberType), None, None)])), FuncDecl(Id(res), [VarDecl(Id(y), NumberType, None, None)], Return(Id(res)))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_60(self):
        inp = \
"""## multiple nested for-statements
func main() 
begin
    for i until i = 100 by 1 for j until j = 100 by 1 for k until k = 100 by 1 for m until m = 100 by 1 for n until n = 100 by 1 return
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), For(Id(j), BinaryOp(=, Id(j), NumLit(100.0)), NumLit(1.0), For(Id(k), BinaryOp(=, Id(k), NumLit(100.0)), NumLit(1.0), For(Id(m), BinaryOp(=, Id(m), NumLit(100.0)), NumLit(1.0), For(Id(n), BinaryOp(=, Id(n), NumLit(100.0)), NumLit(1.0), Return())))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_61(self):
        inp = \
"""## multiple nested for- and if-statements
func main() 
begin
    for i until i = 100 by 1 for j until j = 100 by 1 for k until k = 100 by 1 if (i) if (j) if (k) return
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), For(Id(j), BinaryOp(=, Id(j), NumLit(100.0)), NumLit(1.0), For(Id(k), BinaryOp(=, Id(k), NumLit(100.0)), NumLit(1.0), If((Id(i), If((Id(j), If((Id(k), Return()), [], None)), [], None)), [], None))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_62(self):
        inp = \
"""## another testcase with if
func main() 
begin
    if (1) 
    if (2) 
    if (3) break
    else continue
    else break
    else continue

end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), If((NumLit(3.0), Break), [], Continue)), [], Break)), [], Continue)]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_63(self):
        inp = \
"""## another testcase with if
func main() 
begin
    if (1) number a <- 1
    else number a <- 2
    if (2) number a <- 2
    else number a <- 3
    if (3) number a <- 3
    else number a <- 4
    
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), NumberType, None, NumLit(1.0))), [], VarDecl(Id(a), NumberType, None, NumLit(2.0))), If((NumLit(2.0), VarDecl(Id(a), NumberType, None, NumLit(2.0))), [], VarDecl(Id(a), NumberType, None, NumLit(3.0))), If((NumLit(3.0), VarDecl(Id(a), NumberType, None, NumLit(3.0))), [], VarDecl(Id(a), NumberType, None, NumLit(4.0)))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_64(self):
        inp = \
"""## another for in if
func main() 
begin
    if (1) number a <- 1
    else for i until true by a if (1) number a <- 1
    else for i until true by a if (1) number a <- 1
    else for i until true by a if (1) number a <- 1
    
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), NumberType, None, NumLit(1.0))), [], For(Id(i), BooleanLit(True), Id(a), If((NumLit(1.0), VarDecl(Id(a), NumberType, None, NumLit(1.0))), [], For(Id(i), BooleanLit(True), Id(a), If((NumLit(1.0), VarDecl(Id(a), NumberType, None, NumLit(1.0))), [], For(Id(i), BooleanLit(True), Id(a), If((NumLit(1.0), VarDecl(Id(a), NumberType, None, NumLit(1.0))), [], None)))))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_65(self):
        inp = \
"""func min(number a, string b) begin       
if (x <= false) begin 
        foo(a,2,"b")
    end
for kaitou_kid until id >= 4 by 1 
if (x <= false) begin 
        writeBool(xyz)
    end
end
"""
        out = "Program([FuncDecl(Id(min), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, None)], Block([If((BinaryOp(<=, Id(x), BooleanLit(False)), Block([CallStmt(Id(foo), [Id(a), NumLit(2.0), StringLit(b)])])), [], None), For(Id(kaitou_kid), BinaryOp(>=, Id(id), NumLit(4.0)), NumLit(1.0), If((BinaryOp(<=, Id(x), BooleanLit(False)), Block([CallStmt(Id(writeBool), [Id(xyz)])])), [], None))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_66(self):
        inp = \
"""## this check continue statement 
func main() begin 
var i<-0
for i until i=10 by 1
    begin 
        var j<--0.87e-4
        i <- i*j
        continue
    end
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(j), None, var, UnaryOp(-, NumLit(8.7e-05))), AssignStmt(Id(i), BinaryOp(*, Id(i), Id(j))), Continue]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_67(self):
        inp = \
"""func isPrime(number x)
func main()
begin
    number x <- readNumber()
    if (isPrime(x)) printString("Yes")
    else printString("No")
end
func isPrime(number x)
begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false
    end
return true
for i until i > x / 2 by 1 + 1 var c <- 1
end
"""
        out = "Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), BinaryOp(+, NumLit(1.0), NumLit(1.0)), VarDecl(Id(c), None, var, NumLit(1.0)))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_68(self):
        inp = \
"""## return before another statements
func predeclaration(number x)
func main()
begin
    return x
    var x <- Number(x)
end
"""
        out = "Program([FuncDecl(Id(predeclaration), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([Return(Id(x)), VarDecl(Id(x), None, var, CallExpr(Id(Number), [Id(x)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_69(self):
        inp = \
"""## check multi-dimensional array literal
func main()
begin
    x <- [[[[[[[[[[[1,2],[3],4],5],6],7],8],9],10],11],12]]
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(x), ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0)), NumLit(4.0)), NumLit(5.0)), NumLit(6.0)), NumLit(7.0)), NumLit(8.0)), NumLit(9.0)), NumLit(10.0)), NumLit(11.0)), NumLit(12.0))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_70(self):
        inp = \
"""## check multi-dimensional array literal
func main()
begin
    bool x <- [[[[[[[[[[[1,2],[3],4],5],6],7],8],9],10],11],12]] + "[[[[[[[[[[[1,2],[3],4],5],6],7],8],9],10],11],12]]" 
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), BoolType, None, BinaryOp(+, ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0)), NumLit(4.0)), NumLit(5.0)), NumLit(6.0)), NumLit(7.0)), NumLit(8.0)), NumLit(9.0)), NumLit(10.0)), NumLit(11.0)), NumLit(12.0))), StringLit([[[[[[[[[[[1,2],[3],4],5],6],7],8],9],10],11],12]])))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_71(self):
        inp = \
"""func main()
begin
    number b<-1
    var a<- --------[1,2]*----------------b
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, ArrayLit(NumLit(1.0), NumLit(2.0)))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_71(self):
        inp = \
"""func super_saiyan()
begin
    super_saiyan()
    super_saiyan(super_saiyan())
    super_saiyan(super_saiyan(super_saiyan()))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan())))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan()))))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan())))))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan()))))))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan())))))))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan()))))))))
    super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan(super_saiyan())))))))))

end
"""
        out = "Program([FuncDecl(Id(super_saiyan), [], Block([CallStmt(Id(super_saiyan), []), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])])])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])])])])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])])])])])])]), CallStmt(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [CallExpr(Id(super_saiyan), [])])])])])])])])])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_72(self):
        inp = \
"""var pi <- 3.141592653589793238462643383279502884197
"""
        out = "Program([VarDecl(Id(pi), None, var, NumLit(3.141592653589793))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_73(self):
        inp = \
"""## super boolean expression
func tion() return not not not ----a and b + 6 ----5 +8 or not not not x / true and 6 or not not (not y and 7 % false or "1+2")
"""
        out = "Program([FuncDecl(Id(tion), [], Return(BinaryOp(or, BinaryOp(and, BinaryOp(or, BinaryOp(and, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(a)))))))), BinaryOp(+, BinaryOp(-, BinaryOp(+, Id(b), NumLit(6.0)), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(5.0))))), NumLit(8.0))), BinaryOp(/, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(x)))), BooleanLit(True))), NumLit(6.0)), UnaryOp(not, UnaryOp(not, BinaryOp(or, BinaryOp(and, UnaryOp(not, Id(y)), BinaryOp(%, NumLit(7.0), BooleanLit(False))), StringLit(1+2)))))))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_74(self):
        inp = \
"""func a() 
begin
    for doo until (doo <= 2) by "hello'""...l
        for doo until (doo <= 2) by "hello'""...l
            for doo until (doo <= 2) by "hello'""...l
                if (a) 
                    for doo until (doo <= 2) by "hello'""...l
                        return
                elif (b) 
                    for doo until (doo <= 2) by "hello'""...l
                        return
                else no()
end
"""
        out = """Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), If((Id(a), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), Return())), [(Id(b), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello'"), Id(l)), Return()))], CallStmt(Id(no), [])))))]))])"""
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_75(self):
        inp = \
""" ## nested function calls
func a(number x) 
begin
    return a(a(a(a(a(a(a(a(a(a(a(a(0))))))))))))
end
"""
        out = "Program([FuncDecl(Id(a), [VarDecl(Id(x), NumberType, None, None)], Block([Return(CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [NumLit(0.0)])])])])])])])])])])])]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_76(self):
        inp = \
""" ## nested function calls
func a(number x) 
begin
    a(a(a(a(a(a(a(a(a(a(a(a(0))))))))))))
end
"""
        out = "Program([FuncDecl(Id(a), [VarDecl(Id(x), NumberType, None, None)], Block([CallStmt(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [CallExpr(Id(a), [NumLit(0.0)])])])])])])])])])])])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))
    
    def test_ast_77(self):
        inp = \
""" ## function call but looks like output
func main() 
begin
    Program([VarDecl(Id(str), None, "var", StringLit("Hello world!"))])
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(Program), [ArrayLit(CallExpr(Id(VarDecl), [CallExpr(Id(Id), [Id(str)]), Id(None), StringLit(var), CallExpr(Id(StringLit), [StringLit(Hello world!)])]))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_78(self):
        inp = \
"""## array declaration check
func foo(number a) return a+1
number a[2,3] <- [[1+2,3,"abc",foo(4)],[true,false,true]]
"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0), StringLit(abc), CallExpr(Id(foo), [NumLit(4.0)])), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True))))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_79(self):
        inp = \
"""## something
func alo_alo_1_2_3_4(string x) begin
    if (1 + 8 == 2) return
    else if (true or True and not TRUE) continue
    elif (false or False and not FALSE) break
    else return
    return
end
"""
        out = "Program([FuncDecl(Id(alo_alo_1_2_3_4), [VarDecl(Id(x), StringType, None, None)], Block([If((BinaryOp(==, BinaryOp(+, NumLit(1.0), NumLit(8.0)), NumLit(2.0)), Return()), [], If((BinaryOp(and, BinaryOp(or, BooleanLit(True), Id(True)), UnaryOp(not, Id(TRUE))), Continue), [(BinaryOp(and, BinaryOp(or, BooleanLit(False), Id(False)), UnaryOp(not, Id(FALSE))), Break)], Return())), Return()]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_80(self):
        inp = \
"""## ANTLR-like check
func antlr() begin
    print("(ID | func_call_expr) OPEN_IDX expr_prime CLOSE_IDX;")
end
"""
        out = "Program([FuncDecl(Id(antlr), [], Block([CallStmt(Id(print), [StringLit((ID | func_call_expr) OPEN_IDX expr_prime CLOSE_IDX;)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_81(self):
        inp = \
"""############################################################################################################################
func comment(string comment) 
begin
    print("############################################################################################################################"..."")
end
"""
        out = "Program([FuncDecl(Id(comment), [VarDecl(Id(comment), StringType, None, None)], Block([CallStmt(Id(print), [BinaryOp(..., StringLit(############################################################################################################################), StringLit())])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_82(self):
        inp = \
"""func min(number a, string b)
begin  
if (x <= false)
    begin 
        main(a,2,"b")
        begin
        end
    end
else 
    for id until (abc > "abc") by 1 

        loop1(arr[a(b),b(a)])
        loop2(arr[a(b)],b[2])

end
"""
        out = "Program([FuncDecl(Id(min), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, None)], Block([If((BinaryOp(<=, Id(x), BooleanLit(False)), Block([CallStmt(Id(main), [Id(a), NumLit(2.0), StringLit(b)]), Block([])])), [], For(Id(id), BinaryOp(>, Id(abc), StringLit(abc)), NumLit(1.0), CallStmt(Id(loop1), [ArrayCell(Id(arr), [CallExpr(Id(a), [Id(b)]), CallExpr(Id(b), [Id(a)])])]))), CallStmt(Id(loop2), [ArrayCell(Id(arr), [CallExpr(Id(a), [Id(b)])]), ArrayCell(Id(b), [NumLit(2.0)])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_83(self):
        inp = \
"""func main() begin 
number a<- readNumber()
if (a<0) 
    if (-a%2 = 0) 
        begin
        end
    else if (a<50) return
        elif (a<100) return
        else return 
elif (a>10) 
    begin 
    end 
else return
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, CallExpr(Id(readNumber), [])), If((BinaryOp(<, Id(a), NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, UnaryOp(-, Id(a)), NumLit(2.0)), NumLit(0.0)), Block([])), [], If((BinaryOp(<, Id(a), NumLit(50.0)), Return()), [(BinaryOp(<, Id(a), NumLit(100.0)), Return())], Return()))), [(BinaryOp(>, Id(a), NumLit(10.0)), Block([]))], Return())]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_84(self):
        inp = \
"""func main() 

begin 



## Several newlines


newline <- newline(0)


return
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(newline), CallExpr(Id(newline), [NumLit(0.0)])), Return()]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_85(self):
        inp = \
"""## An LMS testcase
number a <- 100

func sum(number n)
begin
    if (n = 0) return 0
    return n + sum(n - 1)
end

func main()
begin
    writeNumber(sum(a))
end
"""
        out = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_86(self):
        inp = \
"""
number a <- 100


func main()
begin
    if (false) return false
    else for id until 10 by true
    return a
    return a
end
"""
        out = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(main), [], Block([If((BooleanLit(False), Return(BooleanLit(False))), [], For(Id(id), NumLit(10.0), BooleanLit(True), Return(Id(a)))), Return(Id(a))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_87(self):
        inp = \
"""## 
number a <- 100

func mod(number a, number b) return a % b
func div (number a, number b) return a / b

func main()
begin
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    v()
    return mod(10,2)
    return div(10,2)
end
"""
        out = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(mod), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Return(BinaryOp(%, Id(a), Id(b)))), FuncDecl(Id(div), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Return(BinaryOp(/, Id(a), Id(b)))), FuncDecl(Id(main), [], Block([Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), CallStmt(Id(v), []), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_87(self):
        inp = \
"""## 
number a <- 100

func mod(number a, number b) return a % b
func div (number a, number b) return a / b

func main()
begin
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    return mod(10,2)
    return div(10,2)
    v()
    return mod(10,2)
    return div(10,2)
end
"""
        out = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(mod), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Return(BinaryOp(%, Id(a), Id(b)))), FuncDecl(Id(div), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Return(BinaryOp(/, Id(a), Id(b)))), FuncDecl(Id(main), [], Block([Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)])), CallStmt(Id(v), []), Return(CallExpr(Id(mod), [NumLit(10.0), NumLit(2.0)])), Return(CallExpr(Id(div), [NumLit(10.0), NumLit(2.0)]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_88(self):
        inp = \
"""## number check
func main()
begin
    v(000.00E+0013+-66.4789e-1)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(v), [BinaryOp(+, NumLit(0.0), UnaryOp(-, NumLit(6.64789)))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_89(self):
        inp = \
"""## number check
func main()
begin
    v(001.01E+0017+-66.4789e-8)
end
"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(v), [BinaryOp(+, NumLit(1.01e+17), UnaryOp(-, NumLit(6.64789e-07)))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_90(self):
        inp = \
"""## a testcase from ParserSuite
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
number a<- arr[foo(1),foo(3)%3]*(-1)
return
end
"""
        out = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])]))))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, BinaryOp(*, ArrayCell(Id(arr), [CallExpr(Id(foo), [NumLit(1.0)]), BinaryOp(%, CallExpr(Id(foo), [NumLit(3.0)]), NumLit(3.0))]), UnaryOp(-, NumLit(1.0)))), Return()]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_91(self):
        inp = \
"""## a testcase from ParserSuite
number x <- 1
func True(number _) begin       
if ((x <= _ and f(z)) == true or arr[1,2,3]) if ([-2,  3] ==yx...\"...\") 

xy<-    xy
        else if ( a- n < 6) number c

        var foo <- (54 + 1)*(4 / true)+foo(x)[3]
        bool arr <- arr[-7]
        return not -1

end
"""
        out = "Program([VarDecl(Id(x), NumberType, None, NumLit(1.0)), FuncDecl(Id(True), [VarDecl(Id(_), NumberType, None, None)], Block([If((BinaryOp(==, BinaryOp(<=, Id(x), BinaryOp(and, Id(_), CallExpr(Id(f), [Id(z)]))), BinaryOp(or, BooleanLit(True), ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))), If((BinaryOp(..., BinaryOp(==, ArrayLit(UnaryOp(-, NumLit(2.0)), NumLit(3.0)), Id(yx)), StringLit(...)), AssignStmt(Id(xy), Id(xy))), [], If((BinaryOp(<, BinaryOp(-, Id(a), Id(n)), NumLit(6.0)), VarDecl(Id(c), NumberType, None, None)), [], None))), [], None), VarDecl(Id(foo), None, var, BinaryOp(+, BinaryOp(*, BinaryOp(+, NumLit(54.0), NumLit(1.0)), BinaryOp(/, NumLit(4.0), BooleanLit(True))), ArrayCell(CallExpr(Id(foo), [Id(x)]), [NumLit(3.0)]))), VarDecl(Id(arr), BoolType, None, ArrayCell(Id(arr), [UnaryOp(-, NumLit(7.0))])), Return(UnaryOp(not, UnaryOp(-, NumLit(1.0))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_92(self):
        inp = \
"""## an anime quotes
func True(number _) begin       
    writeString("I won't say you'll definitely be able to do it if you don't give up. But if you do, then there'll definitely be nothing.")
end
"""
        out = "Program([FuncDecl(Id(True), [VarDecl(Id(_), NumberType, None, None)], Block([CallStmt(Id(writeString), [StringLit(I won't say you'll definitely be able to do it if you don't give up. But if you do, then there'll definitely be nothing.)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_93(self):
        inp = \
"""## mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain
func mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain(number main) begin       
    main("mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain"...mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain)
end
"""
        out = "Program([FuncDecl(Id(mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain), [VarDecl(Id(main), NumberType, None, None)], Block([CallStmt(Id(main), [BinaryOp(..., StringLit(mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain), Id(mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmain))])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_94(self):
        inp = \
"""## 
func boku_wa_kimi_no_koto_ga_suki_da_kedo_kimi_wa_boku_wo_betsu_ni_suki_janai_mitai(number main) begin       
end
func Dragon_Ball_Z(number Akira_Toriyama) 
return "Son Goku"
"""
        out = "Program([FuncDecl(Id(boku_wa_kimi_no_koto_ga_suki_da_kedo_kimi_wa_boku_wo_betsu_ni_suki_janai_mitai), [VarDecl(Id(main), NumberType, None, None)], Block([])), FuncDecl(Id(Dragon_Ball_Z), [VarDecl(Id(Akira_Toriyama), NumberType, None, None)], Return(StringLit(Son Goku)))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_95(self):
        inp = \
"""## 
func main() 
begin 
    number a[4,6,7,8]
    a[3,2,1,ahahaha(4)] <- 1
end

"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_96(self):
        inp = \
"""## 
func main() 
begin 
    number a[2e1,3e2,4e3,5e4,6e5] <- a[b[c[d[e[f[g[h]]]]]]]
    a[b[c[d[e[f[g[h]]]]]]] <- a(b(c(d(e(f(g(h)))))))
end

"""
        out = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([20.0, 300.0, 4000.0, 50000.0, 600000.0], NumberType), None, ArrayCell(Id(a), [ArrayCell(Id(b), [ArrayCell(Id(c), [ArrayCell(Id(d), [ArrayCell(Id(e), [ArrayCell(Id(f), [ArrayCell(Id(g), [Id(h)])])])])])])])), AssignStmt(ArrayCell(Id(a), [ArrayCell(Id(b), [ArrayCell(Id(c), [ArrayCell(Id(d), [ArrayCell(Id(e), [ArrayCell(Id(f), [ArrayCell(Id(g), [Id(h)])])])])])])]), CallExpr(Id(a), [CallExpr(Id(b), [CallExpr(Id(c), [CallExpr(Id(d), [CallExpr(Id(e), [CallExpr(Id(f), [CallExpr(Id(g), [Id(h)])])])])])])]))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_97(self):
        inp = \
"""## block in block
func main() 
begin 
    begin
        begin
            begin
                begin
                    begin
                        begin
                            begin
                                begin
                                    print("Hello World!")
                                end
                            end
                        end
                    end
                end
            end
        end
    end    
end

"""
        out = "Program([FuncDecl(Id(main), [], Block([Block([Block([Block([Block([Block([Block([Block([Block([CallStmt(Id(print), [StringLit(Hello World!)])])])])])])])])])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_98(self):
        inp = \
"""## another expression
func xor(bool a, bool b) return (a and not b) or (not a and b)
func main() 
begin 
    
    bool a<- xor(true,false) or xor(false,true) or not (xor(true,true))
end

"""
        out = "Program([FuncDecl(Id(xor), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), BoolType, None, None)], Return(BinaryOp(or, BinaryOp(and, Id(a), UnaryOp(not, Id(b))), BinaryOp(and, UnaryOp(not, Id(a)), Id(b))))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BinaryOp(or, BinaryOp(or, CallExpr(Id(xor), [BooleanLit(True), BooleanLit(False)]), CallExpr(Id(xor), [BooleanLit(False), BooleanLit(True)])), UnaryOp(not, CallExpr(Id(xor), [BooleanLit(True), BooleanLit(True)]))))]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))

    def test_ast_99(self):
        inp = \
"""## an amazing quote
func main() 
begin 
    cout("Your skin isn't paper, don't cut it. Your neck isn't a coat, don't hang it. Your body isn't a book, don't judge it. Your life isn't a movie, don't end it. Your heart isn't a door, don't lock it. Remember to always love yourself no matter what you come against!")
    thank_you_for_using_my_bad_testcases(from_Dat)
end

"""
        out = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(cout), [StringLit(Your skin isn't paper, don't cut it. Your neck isn't a coat, don't hang it. Your body isn't a book, don't judge it. Your life isn't a movie, don't end it. Your heart isn't a door, don't lock it. Remember to always love yourself no matter what you come against!)]), CallStmt(Id(thank_you_for_using_my_bad_testcases), [Id(from_Dat)])]))])"
        ASTGenSuite.astTest += 1
        self.assertTrue(TestAST.test(inp, out, ASTGenSuite.astTest))