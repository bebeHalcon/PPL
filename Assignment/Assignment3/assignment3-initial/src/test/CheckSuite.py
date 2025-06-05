import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test301(self):
        input = """
            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,301))

    def test302(self):
        input = """
            func foo(number a, number a)
            func main()
            begin
                dynamic a
                var b <- a * a + foo(a, a)
            end
            func foo(number a, number b)
            begin
                return a + b
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,302))

    def test303(self):
        input = """
        number arr[1,2,3]
        func main()
        begin
            var a <- arr[1,2]
            number b <- a[1] ... true
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., ArrayCell(Id(a), [NumLit(1.0)]), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,303))

    def test304(self):
        input = """
        func foo(number a, string a)
        begin
            return a
        end
        func main()
        begin
            foo(1, "1")
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,304))

    def test305(self):
        input = """
        number c <- 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,305))

    def test306(self):
        input = """
        func foo(number a, string a)
        func main()
        begin
            foo(1, "1")
        end
        func foo(number a, string b)
        begin
            return a
        end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,306))

    def test307(self):
        input = """
        func foo()
        func foo(number a, string b)
        func main()
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,307))

    def test308(self):
        input = """
        func foo()
        begin
            return 1
        end
        func main()
        begin
            foo()
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input,expect,308))

    def test309(self):
        input = """
        func main()
        begin
            dynamic a
            var b <- a[0] + 1
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, BinaryOp(+, ArrayCell(Id(a), [NumLit(0.0)]), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,309))

    def test310(self):
        input = """
        func factorial(number n)
        begin
            if (n = 0)
                return 1
            else
                return n * factorial(n - 1)
        end
        func main()
        begin
            number n <- 5
            number result <- factorial(n)
            writeNumber(result)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,310))

    def test311(self):
        input = """
        func main()
        begin
            for i until i > 10 by 1
            begin
                writeNumber(i)
            end
        end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,311))

    def test312(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i >= 10 by 1
            begin
                writeNumber(i)
            end
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,312))

    def test313(self):
        input = """
        func f(number x[2, 3]) return x

        func main()
        begin
            dynamic x <- f([[1, 2, 3], [4, 5, 6]])
            var y <- x[0, 0]
            writeString(y)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"
        self.assertTrue(TestChecker.test(input,expect,313))

    def test314(self):
        input = """
        func f(number x[2, 3]) return x

        func main()
        begin
            dynamic x <- f([[1, 2, 3], [4, 5, 6]])
            var y <- x[0, 0]
            writeNumber(y)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,314))

    def test315(self):
        input = """
        func main() begin
        end

        func readNumber()
        begin
            return 1
        end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input,expect,315))

    def test316(self):
        input = """
        func foo()
        func foo1()
        func foo()
        func foo1() return
        func main()
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,316))

    def test317(self):
        input = """
        func foo() return 1
        func foo() return 2
        func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,317))

    def test318(self):
        input = """
        func main()
        begin
            bool a <- (1 > 2) and (3 < 4)
            writeBool(a)
            return a
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,318))

    def test319(self):
        input = """
        dynamic x
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            dynamic d
            dynamic e
            x <- [a, [b], [[1,2,3]], [[c,d,e]]]
            number arr1[1,3] <- a
            dynamic arr2 <- b
            arr2 <- [2.5, 3.5, 4.5]
            dynamic f <- d
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,319))

    def test320(self):
        input = """
        func main()
        begin
            var i <- 1
            for i until 2 < 3 by 1
                for i until 2 < 3 by 1
                    break
            break
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,320))

    def test321(self):
        input = """
        func main()
        begin
            var i <- 1
            for i until 2 < 3 by 1
            begin
                break
                continue
                break
                continue
            end
            var x <- (1 > 2) and true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,321))

    def test322(self):
        input = """
        func main()
        begin
            var x <- (1 > 2) and true
            var y <- x or false
            var z <- y and true
            var t <- z or false
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,322))

    def test323(self):
        input = """
            number a
            func main()
            begin
                number a
                begin
                    number a
                    begin
                        string a
                    end
                end
                begin
                    number a
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,323))

    def test324(self):
        input = """
            number a
            var x <- [a, [a], [[a,a,a]]]
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(Id(a)), ArrayLit(ArrayLit(Id(a), Id(a), Id(a))))"
        self.assertTrue(TestChecker.test(input,expect,324))

    def test325(self):
        input = """
        number a <- a * 2
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,325))

    def test326(self):
        input = """
        func main()
        begin
            dynamic a
            var b <- a[1] + 1
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, BinaryOp(+, ArrayCell(Id(a), [NumLit(1.0)]), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,326))

    def test327(self):
        input = """
        func main()
        begin
            dynamic a
            string x <- [a]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,327))

    def test328(self):
        input = """
        func foo() begin
            number a
            return 1
            return a ... "hi"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), StringLit(hi))"
        self.assertTrue(TestChecker.test(input,expect,328))

    def test329(self):
        input = """
        func main()
        begin
            dynamic a
            string x[1] <- [a,a]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([1.0], StringType), None, ArrayLit(Id(a), Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,329))

    def test330(self):
        input = """
        func foo(number x, string y)
        func foo(number x, number x) return
        func main() return
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,330))

    def test331(self):
        input = """
        func main()
        func foo()
        begin
            number a <- main()
        end
        func main() return
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,331))

    def test332(self):
        input = """
        func main()
        begin
            dynamic x
            x <- (x = 1) or ("hi" == "hi")
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(hi), StringLit(hi))))"
        self.assertTrue(TestChecker.test(input,expect,332))

    def test333(self):
        input = """
        dynamic a
        func foo() return a
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,333))

    def test334(self):
        input = """
        func foo(number a) return 1
        func main()
        begin
            dynamic x
            number a <- foo([x])
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, CallExpr(Id(foo), [ArrayLit(Id(x))]))"
        self.assertTrue(TestChecker.test(input,expect,334))

    def test335(self):
        input = """
        func main() return
        func foo()
        begin
            return 1
            return "a"
        end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(a))"
        self.assertTrue(TestChecker.test(input,expect,335))

    def test336(self):
        input = """
        func main()
        begin
            dynamic a <- a
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, Id(a))"
        self.assertTrue(TestChecker.test(input,expect,336))

    def test337(self):
        input = """
        func main()
        func foo()
        begin
            dynamic x
            number a[3,2] <- [[0.0, 0], [x,x], [x, x - 3]]
            x <- main()
        end
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input,expect,337))

    def test338(self):
        input = """
        dynamic x
        number a[3] <- [1, [x,x]]
        func main()
        begin
            x <- 1
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,338))

    def test339(self):
        input = """
        func main()
        begin
            dynamic a
            var c <- a == a + 2
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,339))

    def test340(self):
        input = """
        func foo(number a, bool b)
        dynamic x
        func main()
        begin
            foo(x, x, x, x)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(x), Id(x), Id(x), Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,340))

    def test341(self):
        input = """
        func foo(number a, bool b)
        dynamic x
        func main()
        begin
            foo(x, x)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(x), Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,341))

    def test342(self):
        input = """
        number x <- 10
        func f(number x)
        begin
            number x <- x + 20
            writeNumber(x)
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,342))

    def test343(self):
        input = """
        func test1()
        func test2()
        func test3()
        func test(number test1, string test2, bool test3)
        begin
            return (test1 > test1()) and (test2 == test2()) or (test3 and test3())
        end
        func main()
        begin
            return test(1,"abc",true)
        end

        """
        expect = "No Function Definition: test1"
        self.assertTrue(TestChecker.test(input,expect,343))

    def test344(self):
        input = """
        func a1(number a,number b, number c)
        func main()
        begin
            number a <- 1
            a1(1,2,3)
        end
        func a(number a,number b, number c)
        begin
            a <- a1(a,b,c)
            return "lo ve du"
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a1), [Id(a), Id(b), Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,344))

    def test345(self):
        input = """
        dynamic x
        number a[2,2] <- [x,[x,x]]
        func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,345))

    def test346(self):
        input = """
        func foo() return
        func main()
        begin
            number a <- foo()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input,expect,346))

    def test347(self):
        input = """
        func main()
            begin
                dynamic num
                bool arr <- num and (num > num)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input,expect,347))

    def test348(self):
        input = """
        func main() return
        func foo()
        begin
            dynamic a
            return 1
            return a
            dynamic b <- a
            b <- b and 1
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(b), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input,expect,348))

    def test349(self):
        input = """
        func main() return
        func foo()
        begin
            dynamic a
            return 1
            return [a]
        end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,349))

    def test350(self):
        input = """
        func main()
        func foo()
        begin
            var a <- main()

        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input,expect,350))

    def test351(self):
        input = """
        func main() return
        func foo()
        begin
            dynamic a
            return a
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,351))

    def test352(self):
        input = """
        dynamic x
        func main()
        begin
            number a[2,2] <- [[x,x]]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input,expect,352))

    def test353(self):
        input = """
        func test()
        begin
            dynamic a
            return a
        end
        func main()
        begin
            test()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,353))

    def test354(self):
        input = """
        dynamic x
        dynamic a <- [[x,x], [x,x,x]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(x), Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,354))

    def test355(self):
        input = """
        func main()
        begin
            dynamic a
            var b <- a[1] + 1
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, BinaryOp(+, ArrayCell(Id(a), [NumLit(1.0)]), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,355))

    def test356(self):
        input = """
        dynamic x
        dynamic a <- [[1,2], [x,x,x]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(Id(x), Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,356))

    def test357(self):
        input = """
        dynamic x
        number a[2,2] <- [[x,x], [x,x]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,357))

    def test358(self):
        input = """
        dynamic x
        dynamic y
        number a[2,2] <- [[y,y], [x,x]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,358))

    def test359(self):
        input = """
        dynamic x
        dynamic y
        number a[2,2] <- [[y,y,y], [x,x]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), Id(y), Id(y)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,359))

    def test360(self):
        input = """
        func test()
        begin
            dynamic a
            if (1 = 2) return 1
            elif (1 = 3) return a
        end
        func main()
        begin
            test()
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(test), [])"
        self.assertTrue(TestChecker.test(input,expect,360))

    def test361(self):
        input = """
            func foo(number a[2,3],number x[2,3])

            func main()
            begin
                dynamic b
                dynamic c
                number a[2,3]
                number x <- foo(a, c)
            end
            func foo(number a[2,3],number x[2,3])
            begin
                dynamic a
                return a
                return true
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,361))

    def test362(self):
        input = """
            func foo()
            begin
                begin
                    dynamic x
                dynamic y
                number a[2,3] <- [[x,x,x], [y,y,y]]
                number b[3] <- a[1]
                return b
                end
            end
            func main()
            begin
                number a <- foo()[2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,362))

    def test363(self):
        input = """
            func foo()
            begin
                dynamic x
                dynamic y
                number a[2,3] <- [[x,x,x], [y,y,y]]
                number b[3] <- a[1]
                return b[0]
            end
            func main()
            begin
                number a <- foo()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,363))

    def test364(self):
        input = """
            func foo()
            begin
                if (1 = 2) return 1
                elif (1 = 3) return 2
                else return true
                dynamic i
                for i until 2 < 3 by 1
                begin
                    string b <- "hi"
                    return b
                end
            end
            func main()
            begin
                number a <- foo()
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,364))

    def test365(self):
        input = """
            dynamic a
            number b <- [a] + 1
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), NumberType, None, BinaryOp(+, ArrayLit(Id(a)), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,365))

    def test366(self):
        input = """
            dynamic a
            func main()
            begin
                if ([a]) writeNumber(1)
            end
        """
        expect = "Type Cannot Be Inferred: If((ArrayLit(Id(a)), CallStmt(Id(writeNumber), [NumLit(1.0)])), [], None)"
        self.assertTrue(TestChecker.test(input,expect,366))

    def test367(self):
        input = """
            func foo()
            begin
                if (1 = 2) return 1
                elif (1 = 3) return "hi"
                else
                begin
                    return true
                    return 1
                end
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(hi))"
        self.assertTrue(TestChecker.test(input,expect,367))

    def test368(self):
        input = """
            func foo()
            begin
                dynamic x
                number a[2,2] <- [[x], [x]]
            end
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x)), ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input,expect,368))

    def test369(self):
        input = """
            dynamic a
            dynamic b
            dynamic c
            number x[5] <- [a,b,c,b,a]
            number y <- x[a] + b - c
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,369))

    def test370(self):
        input = """
            func foo(string a, number b)
            begin
                var i <- 1
                for i until i < 10 by 2
                begin
                    if (i = 5) break
                    else return i
                end
            end
            func main()
            begin
                dynamic x
                dynamic y
                number arr[2] <- [4.8, 6.9]
                dynamic a <- foo(x, arr[y])
                arr[0] <- y
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,370))

    def test371(self):
        input = """
        func foo()
        func main()
        begin
        number a[1,2,3]
        a[0] <- foo()
        end
        func foo()
        begin
        if (true)
        return [[2,2,2],[3,3,3]]
        elif (false) return foo()
        else return [[3,3,3,3],[3,3,3,3]]
        end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(NumLit(3.0), NumLit(3.0), NumLit(3.0), NumLit(3.0)), ArrayLit(NumLit(3.0), NumLit(3.0), NumLit(3.0), NumLit(3.0))))"
        self.assertTrue(TestChecker.test(input,expect,371))

    def test372(self):
        input = """
        func foo() return 1
        func main() return foo()
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,372))

    def test373(self):
        input = """
        func main() begin
            var i <- 2
            for i until true by 1
            begin
                break
                continue
                begin
                    break
                    continue
                end

                for i until true by 1
                begin
                    break
                    continue
                end
                break
                continue
            end
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,373))

    def test374(self):
        input = """
        number a
        string b
        number c

        func foo( number a, number b[1,2])
        func main()
        begin
        end
        func foo( number a, number b[1,2,3])
        return 1
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,374))

    def test375(self):
        input = """
        func main()
        begin
        dynamic a
        dynamic b
        dynamic c
        if (true) dynamic a
        elif (false) dynamic b
        else dynamic c
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,375))

    def test376(self):
        input = """
        number foo
        func main()
            begin
                foo()
            end
        func foo() return
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,376))

    def test377(self):
        input = """
        dynamic x
        func main() begin
        if (true) return
        elif ([x]) return
        end
        """
        expect = "Type Cannot Be Inferred: If((BooleanLit(True), Return()), [(ArrayLit(Id(x)), Return())], None)"
        self.assertTrue(TestChecker.test(input,expect,377))


    def test378(self):
        input = """
        func f(number x[2, 3]) return x
        func main()
        begin
            dynamic x <- [[1, 2, 3], [4, 5, 6]]
            var y <- f(x)
            writeString(y)
        end
        """
        expect = """Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,378))

    def test379(self):
        input = """
        dynamic x
        func main() begin
        string a[1] <- [x,x]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([1.0], StringType), None, ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,379))

    def test380(self):
        input = """
        dynamic x
        func main() begin
        string a[1] <- [x,x,2]
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], StringType), None, ArrayLit(Id(x), Id(x), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input,expect,380))

    def test381(self):
        input = """
            func foo1()
            dynamic x
            number a[2,3] <- [[x, foo1(), x], [foo1(), x, foo1()]]
            func foo2()
            dynamic y
            string b[2,3] <- foo2()
            func foo1() return 1
            func main()
            begin
                y <- [b[1,2], b[2,1], foo2()[0,0]]
                b[2,2] <- y[foo1()]
            end
        """
        expect = "No Function Definition: foo2"
        self.assertTrue(TestChecker.test(input,expect,381))

    def test382(self):
        input = """
            func foo(number a[2,2], string x[2,2])
            begin
                return x[1]
            end
            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                dynamic d
                dynamic e
                dynamic f
                dynamic x <- foo([[1,2],[3,4]], [[a,b],[c,d]])
                x[1] <- foo([[1,2],[3,4]], [[e,f],[c,d]])[0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,382))

    def test383(self):
        input = """
            func foo(string a)
            func main()
            begin
                dynamic x
                dynamic y
                writeNumber(foo(x))
                writeString(foo(y))
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [CallExpr(Id(foo), [Id(y)])])"
        self.assertTrue(TestChecker.test(input,expect,383))

    def test384(self):
        input = """
            func foo(string a)
            func main()
            begin
                dynamic x
                dynamic y
                writeNumber(foo(x))
                var i <- foo([y])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(i), None, var, CallExpr(Id(foo), [ArrayLit(Id(y))]))"
        self.assertTrue(TestChecker.test(input,expect,384))

    def test385(self):
        input = """
            string x
            func foo(number x)
            begin
                return x
            end
            func main()
            begin
                dynamic a <- foo(x)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,385))

    def test386(self):
        input = """
            dynamic x
            number a <- [[1,2,3], [x,x]]
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input,expect,386))

    def test387(self):
        input = """
            dynamic x
            var a <- [x, [x], [[x,x,x]]]
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x)), ArrayLit(ArrayLit(Id(x), Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input,expect,387))

        
    def test388(self):
        input = """
        dynamic a
        string x[1] <- [a]
        func main() begin
            a<-7
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(7.0))"
        self.assertTrue(TestChecker.test(input, expect, 388))

    def test389(self):
        input = """
        func foo(number a[1]) return 1
        dynamic x
        number a <- foo([x])
        func main() begin 
            x <- true
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 389))
        
    def test390(self):
        input = """
        dynamic x
        number b <- -[x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), NumberType, None, UnaryOp(-, ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 390))

    def test391(self):
        input = """
        func main()
        func foo()
        begin
            number a <- main()
        end
        func main() return
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 391))
    
    def test392(self):
        input = """
        func foo()
        begin
            number a <- 3
        end
        func foo()
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 392))
  
    def test393(self):
        input = """
        func main()
        begin
            dynamic num
            bool arr <- num and (num > num)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 393))
        
    def test394(self):
        input = """
        func mul(number a, number b) return a*b
        func main()
        begin
            var a <- mul(a,5)
            var c <- mul(b,2)
        end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 394))
    
    def test395(self):
        input = """func f()
        return true
        func main()
        begin
            number a
            number b[5]
            a <- b[f()]
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [CallExpr(Id(f), [])])"
        self.assertTrue(TestChecker.test(input, expect, 395))
    
    def test396(self):
        input = """func f()
        begin
            number a <- 5
            return a
        end
        func main()
        begin
            number a
            a <- f()[1]
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), []), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 396))

    def test397(self):
        input = """func main()
        begin
            number a[3] <- [1,2,3]
            number b[3] <- [4,5,6]
            number c <- a[b[1]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 397))
    
    def test398(self):
        input = """
        func main() begin 
            dynamic i
            for i until i == "abc" by 1 continue
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(i), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 398))
    
    def test399(self):
        input = """## type mismatch 
        func main() begin 
            var a<- (1=2) or ("abc"..."abc'"dfe")
        end 
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, BinaryOp(=, NumLit(1.0), NumLit(2.0)), BinaryOp(..., StringLit(abc), StringLit(abc'\"dfe)))"
        self.assertTrue(TestChecker.test(input, expect, 399))
    
    def test400(self):
        input = """
            string s1 <- "this"
            string s2 <- "is"
            string s3 <- "the final testcase, "
            string s4 <- "i hope that i will pass all of the tests."
            func concat(string a, string a)
            func main()
            begin
                writeString(concat(concat(concat(s1,s2),s3),s4))
            end
            func concat(string a, string b) return a...b
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test401(self):
        input = """
            func test(number a, string b)
            func main()
            begin
                dynamic a
                dynamic b
                a <- test(test(a,b), test(a,b))
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(test), [CallExpr(Id(test), [Id(a), Id(b)]), CallExpr(Id(test), [Id(a), Id(b)])])"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test402(self):
        input = """
        dynamic a
        dynamic b
        number c[2,3] <- [[a,a,a], [b,b]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), Id(a), Id(a)), ArrayLit(Id(b), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test403(self):
        input = """
        dynamic a <- [1,2,3]
        dynamic b <- [4,5,6]
        dynamic c <- a + b
        func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test404(self):
        input = """
        string a <- [1,2,3]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), StringType, None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test405(self):
        input = """
        string a[1,2] <- [["a","b"]]
        string b[2,2] <- [["a","b"]]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2.0, 2.0], StringType), None, ArrayLit(ArrayLit(StringLit(a), StringLit(b))))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test406(self):
        input = """
        func foo() return
        func main()
        begin
            dynamic a <- not foo()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 406))