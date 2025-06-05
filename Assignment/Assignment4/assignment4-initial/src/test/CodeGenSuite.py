import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_number(self):
        input = """func main ()
        begin
            writeNumber(1)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test1(self):
            input = """
            func main()
            begin
                number b <- 2
                writeNumber(b)
            end
            """
            expect = "2.0"
            self.assertTrue(TestCodeGen.test(input, expect, 101))

    def test2(self):
        input = """number a <- 1
        number c <- 2
        func main()
        begin
            number b <- 3
            writeNumber(a)
            writeNumber(c)
            writeNumber(b)
        end
        """
        expect = "1.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 102))
    
    def test3(self):
        input = """number a <- 1
        func main()
        begin
            number b <- 2
            writeNumber(a + b)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 103))

    def test4(self): # expression (note)
        input = """
        func main()
        begin
            writeNumber(4 * 1 / 2 % 4)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 104))

    def test5(self): # expression (note)
        input = """
        func main()
        begin
            writeNumber(1 + 2 * 9 - 19 % 67 / 88)
        end
        """
        expect = "18.78409"
        self.assertTrue(TestCodeGen.test(input, expect, 105))

    def test6(self): # expression
        input = """
        number a <- (-3 * 10 + 3) / 10
        func main()
        begin
            writeNumber(a)
        end
        """
        expect = "-2.7"
        self.assertTrue(TestCodeGen.test(input, expect, 106))

    def test7(self): # expression
        input = """
        func main()
        begin
            writeBool(true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 107))
    
    def test8(self): # expression
        input = """
        func main()
        begin
            string a <- "abc"
            writeString(a)
        end
        """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input, expect, 108))

    def test9(self): # expression
        input = """
        func main()
        begin
            string a <- "abc"
            writeString(a ... "def")
        end
        """
        expect = "abcdef"
        self.assertTrue(TestCodeGen.test(input, expect, 109))
    
    def test10(self): # expression
        input = """
        func main()
        begin
            writeString(("abc" ... "a") ... "hhh")
        end
        """
        expect = "abcahhh"
        self.assertTrue(TestCodeGen.test(input, expect, 110))
    
    def test11(self): # expression
        input = """
        func main()
        begin
            writeBool(1 = 2)
            writeBool(1 != 2) 
        end
        """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 111))

    def test12(self): # expression
        input = """
        func main()
        begin
            writeBool(1 < 2)
            writeBool(1 <= 2)
        end
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 112))

    def test13(self): # expression
        input = """
        func main()
        begin
            writeBool(1 > 2)
            writeBool(1 >= 2)
        end
        """
        expect = "falsefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 113))

    def test14(self): # expression
        input = """
        func main()
        begin
            writeNumber(-1)
        end
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 114))
    
    def test15(self): # expression
        input = """
        func main()
        begin
            writeBool(not not true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 115))

    def test16(self): # for statement
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
            begin
                if (i = 4) break
            end
            writeNumber(i)
            
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 116))

    def test17(self): # for statement
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
            begin
                break
            end
            writeNumber(i)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 117))
    def test18(self): # for statement
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
            begin
                continue
            end
            writeNumber(i)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 118))

    def test19(self): # for statement
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
            begin
                if (i = 4) break
            end
            writeNumber(i)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 119))

    def test20(self): # assign statement
        input = """
        func main()
        begin
            string a <- "a"
            string b <- "b"
            string c
            c <- a ... b
          
            writeString(c)
        end
        """
        expect = "ab"
        self.assertTrue(TestCodeGen.test(input, expect, 120))

    def test21(self): # assign statement
        input = """
        func main()
        begin
            number i
            i <- 1
            writeBool(i = 1)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 121))

    def test22(self): # assign statement
        input = """
        func main()
        begin
            number a[2] <- [1, 2]
            number b <- a[0]
            writeNumber(b)
            writeString(";")
            writeNumber(a[1])
        end
        """
        expect = "1.0;2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 122))

    def test23(self): # assign statement
        input = """
        func main()
        begin
            number a[3] <- [1, 2, 3]
            number i <- 0
            for i until i > 2 by 1
            begin
                writeNumber(a[i])
                writeString(";")
            end
        end
        """
        expect = "1.0;2.0;3.0;"
        self.assertTrue(TestCodeGen.test(input, expect, 123))

    def test24(self): # assign statement
        input = """
        func main()
        begin
            var a <- 1
            writeNumber(a)
            var b <- "hi"
            writeString(b)
            var c <- true
            writeBool(c)
        end
        """
        expect = "1.0hitrue"
        self.assertTrue(TestCodeGen.test(input, expect, 124))

    def test25(self): # assign statement
        input = """
        number a <- 1
        number b <- 2
        func main()
        begin
            writeNumber(a) 
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 125))

    def test26(self): # assign statement
        input = """
        func f(number a) return 2 + a
        func main()
        begin
            writeNumber(f(2)) 
        end
        """
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 126))

    def test27(self): # assign statement
        input = """
        func f() return true
        func main()
        begin
            writeBool(f())
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 127))

    def test28(self): # assign statement
        input = """
        func f() return "vuongnguyen"
        func main()
        begin
            writeString(f())
        end
        """
        expect = "vuongnguyen"
        self.assertTrue(TestCodeGen.test(input, expect, 128))

    def test29(self): # assign statement
        input = """
        func f() return "vuongnguyen"
        func main()
        begin
            writeString(f())
        end
        """
        expect = "vuongnguyen"
        self.assertTrue(TestCodeGen.test(input, expect, 129))

    def test30(self): # assign statement
        input = """
        func f(number a) return a
        func main()
        begin
            writeNumber(f(1))
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 130))

    def test31(self): # assign statement
        input = """
        func f(number a, number b) return a + b - 1 
        func main()
        begin
            writeNumber(f(1, 2))
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 131))

    def test31(self): # assign statement
        input = """
        func f(number a, number b) return a + b - 1 
        func main()
        begin
            writeNumber(f(1, 2))
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 131))
    
    def test132(self):
        inputstr = """
        func concatString(string a, string b) return a ... b
        func main()
        begin
            writeString(concatString("1.0", "abc"))
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 132))

    def test133(self):
        inputstr = """
        func sum(number i, number j)
        begin
            number sum <- 0
            for i until i > j by 1
                sum <- sum + i
            return sum
        end
        func main()
        begin
            writeNumber(sum(1, 10))
        end
        """
        expectedoutput = "55.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 133))

    def test134(self):
        inputstr = """
        func isPrime(number n)
        begin
            if (n < 2) return false
            number i <- 2
            for i until i * i > n by 1
                if (n % i = 0) return false
            return true
        end
        func main()
        begin
            writeBool(isPrime(1))
            writeBool(isPrime(2))
            writeBool(isPrime(3))
            writeBool(isPrime(4))
        end
        """
        expectedoutput = "falsetruetruefalse"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 134))

    def test135(self):
        inputstr = """
        func compareString(string a, string b) return a == b
        func main()
        begin
            writeBool(compareString("1.0", "abc"))
        end
        """
        expectedoutput = "false"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 135))

    def test136(self):
        inputstr = """
        func compareString(string a, string b) return a == b
        func main()
        begin
            writeBool(compareString("abc", "abc"))
        end
        """
        expectedoutput = "true"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 136))

    def test137(self):
        inputstr = """
        func checkNumber(number a, number b) return a = b
        func main()
        begin
            writeBool(checkNumber(1, 1))
        end
        """
        expectedoutput = "true"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 137))

    def test138(self):
        inputstr = """
        func equation(number a, number b, number c)
            return (c - b) / a          
        func main()
        begin
            writeNumber(equation(1, 2, 5))
        end
        """
        expectedoutput = "3.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 138))

    def test139(self):
        inputstr = """
        func isOdd(number n)
        begin
            if (n % 2 = 0) return false
            return true
        end
        func main()
        begin
            writeBool(isOdd(1))
        end
        """
        expectedoutput = "true"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 139))

    def test140(self):
        inputstr = """
        func isEven(number n)
        begin
            if (n % 2 = 0) return true
            return false
        end
        func main()
        begin
            writeBool(isEven(1))
        end
        """
        expectedoutput = "false"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 140))

    def test141(self):
        inputstr = """
        func factorial(number n)
        begin
            if (n = 0) return 1
            number i <- 1
            number sum <- 1
            for i until i > n by 1
                sum <- sum * i
            return sum
        end
        func main()
        begin
            writeNumber(factorial(5))
        end
        """
        expectedoutput = "120.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 141))

    def test142(self):
        inputstr = """

        func main()
        begin
            writeNumber(1 + 2 * 3 / 4 % 5 )
        end
        """
        expectedoutput = "2.5"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 142))

    def test143(self):
        inputstr = """
        func main()
        begin
            writeBool(true and false and not true )
        end
        """
        expectedoutput = "false"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 143))

    def test144(self):
        inputstr = """
        func main()
        begin
            writeBool(true or false or not true or not false or not not false)
        end
        """
        expectedoutput = "true"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 144))

    def test145(self):
        inputstr = """
        func hello()
        begin
            writeString("hello")
        end
        func main()
        begin
            hello()
        end
        """
        expectedoutput = "hello"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 145))

    def test146(self):
        inputstr = """
        func main()
        begin
            writeNumber(23 * 2)
        end
        """
        expectedoutput = "46.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 146))

    def test147(self):
        inputstr = """
        func test(number c) return c * 2
        func main()
        begin
            writeNumber(test(1))
        end
        """
        expectedoutput = "2.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 147))

    def test148(self):
        inputstr = """

        func main()
        begin
            writeNumber(---------------------------------------1)
            
        end
        """
        expectedoutput = "-1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 148))

    def test149(self):
        inputstr = """
        func main()
        begin
            number b <- 3
            if (b = 2) writeNumber(1)
            elif (b = 3) writeString("abc")
            else writeNumber(2)
        end
        """
        expectedoutput = "abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 149))

    def test150(self):
        inputstr = """
        func calcAndPrint(number a, number b) 
        begin
            writeNumber(a + b)
        end
        func main()
        begin
            calcAndPrint(1, 2)
        end
        """
        expectedoutput = "3.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 150))

    def test151(self):
        inputstr = """
        func isOddOrEven(number n)
        begin
            if (n % 2 = 0) writeString("even")
            else writeString("odd")
        end
        func main()
        begin
            isOddOrEven(1)
        end
        """
        expectedoutput = "odd"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 151))

    def test152(self):
        inputstr = """
        func foo()
        begin
            number i <- 0
            for i until i > 10 by 1
            begin
                writeNumber(i)
                writeString("-")
            end

        end
        func main()
        begin
            foo()
        end
        """
        expectedoutput = "0.0-1.0-2.0-3.0-4.0-5.0-6.0-7.0-8.0-9.0-10.0-"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 152))

    def test153(self):
        inputstr = """
        func main()
        begin
            number b <- 1
            if (b = 1) writeNumber(1)
            elif (b = 2) writeNumber(2)
            elif (b = 3) writeNumber(3)
            elif (b = 4) writeNumber(4)
            else writeString("abc")

        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 153))

    def test154(self):
        inputstr = """
        func main()
        begin
            number a <- 1
            number b <- 2
            for a until a > b by 1
                if (a = 1) 
                begin
                    writeNumber(a)
                    break
                end
                elif (a = 2)
                begin
                    writeNumber(a)
                    break
                end
                elif (a = 3)
                begin
                    writeNumber(a)
                    break
                end
                else
                    writeString("abc")
        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 154))

    def test155(self):
        inputstr = """
        func test(number a) return a
        func test1()
        begin
            writeNumber(test(1))
        end
        func main()
        begin
            test1()
        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 155))

    def test156(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 156))

    def test157(self):
        inputstr = """
        func foo()
        begin 
            number i <- 0
            for i until i > 10 by 1
                if (i % 2 = 0) writeNumber(i)
        end
        func main()
        begin
            foo()
        end
        """
        expectedoutput = "0.02.04.06.08.010.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 157))

    def test158(self):
        inputstr = """
        func main()
        begin
            number a[2] <- [1, 2]
            writeNumber(a[0])

        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 158))

    def test159(self):
        inputstr = """
        func main()
        begin
            number a <- 5
            a <- a * a - a * a / a % 15 + a --- a
            writeNumber(a) 
        end
        """
        expectedoutput = "20.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 159))

    def test160(self):
        inputstr = """
        number a <- 5
        func main()
        begin
            number a <- 15
            number b <- 5
            writeNumber(a)

        end
        """
        expectedoutput = "15.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 160))

    def test161(self):
        inputstr = """
        number a <- 2
        func main()
        begin
            number a <- 1
            begin 
                writeNumber(a)
            end
        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 161))

    def test162(self):
        inputstr = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
                continue
            writeNumber(i)
        end
        """
        expectedoutput = "0.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 162))

    def test163(self):
        inputstr = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
                break
            writeNumber(i)
        end
        """
        expectedoutput = "0.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 163))

    def test164(self):
        inputstr = """
        func main()
        begin
            number i <- 0
            for i until i > 10 by 1
            begin
                writeNumber(i)
                for i until i > 10 by 1
                    continue
            end
            writeNumber(i)

        end
        """
        expectedoutput = "0.01.02.03.04.05.06.07.08.09.010.00.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 164))

    def test165(self):
        inputstr = """
        func main()
        begin
            var a <- 1
            writeNumber(a ------------------------------------- a)
        end
        """
        expectedoutput = "0.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 165))

    def test166(self):
        inputstr = """
        func main()
        begin
            writeBool(not not not not not not false and true or not true and false or true and not false)
        end
        """
        expectedoutput = "true"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 166))

    def test167(self):
        inputstr = """
        func foo (number a, string b)
        begin
            if (a = 1) return b
            return b ... "a"
        end
        func main()
        begin
            writeString(foo(2, "a"))
        end
        """
        expectedoutput = "aa"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 167))

    def test168(self):
        inputstr = """
        func printOdd(number n)
        begin
            for n until n > 10 by 1
                if (n % 2 = 1) writeNumber(n)
        end
        func main()
        begin
            printOdd(1)
        end
        """
        expectedoutput = "1.03.05.07.09.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 168))

    def test169(self):
        inputstr = """
        func cucu()
        begin
            writeString("Hello World")
        end
        func main()
        begin
            cucu()
        end
        """
        expectedoutput = "Hello World"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 169))

    def test170(self):
        inputstr = """
        func main()
        begin
            if (1 = 1) writeNumber(1)
        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 170))

    def test171(self):
        inputstr = """
        func main()
        begin
            number a[2] <- [1, 2]
            number b <- a[1]
            writeNumber(b)
        end
        """
        expectedoutput = "2.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 171))

    def test172(self):
        inputstr = """
        func main()
        begin
            number a[2] <- [15, 2]
            number b <- a[0]
            writeNumber(b)
        end
        """
        expectedoutput = "15.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 172))

    def test173(self):
        inputstr = """
        func main()
        begin
            string a[2] <- ["1.0", "abc"]
            writeString(a[0])
        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 173))

    def test174(self):
        inputstr = """
        func main()
        begin
            string a[2] <- ["abc", "def" ]
            writeString(a[0] ... a[1])
        end
        """
        expectedoutput = "abcdef"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 174))

    def test175(self):
        inputstr = """
        func main()
        begin
            string a[5] <- ["1.0", "abc", "def", "ghi", "jkl"]
            number i <- 0
            for i until i >= 5 by 1
                writeString(a[i])
        end
        """
        expectedoutput = "1.0abcdefghijkl"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 175))

    def test176(self):
        inputstr = """
        func main()
        begin
            string a[5] <- ["1.0", "abc", "def", "ghi", "jkl"]
            number i <- 0
            string result <- ""
            for i until i >= 5 by 1
                result <- result ... a[i]
            writeString(result)
        end
        """
        expectedoutput = "1.0abcdefghijkl"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 176))

    def test177(self):
        inputstr = """
        func main()
        begin
            bool a[2] <- [true, false]
            writeBool(a[0])
        end
        """
        expectedoutput = "true"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 177))

    def test178(self):
        inputstr = """
        func main()
        begin
            bool a[2] <- [true, false]
            number b[2] <- [1, 2]
            if (a[0]) writeNumber(b[0])
            elif (a[1]) writeNumber(b[1])
            else writeString("abc")
        end
        """
        expectedoutput = "1.0"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 178))

    def test179(self):
        inputstr = """
        func main()
        begin
            bool a[2] <- [true, false]
            if (a[0] and a[1]) writeNumber(1)
            else writeString("abc")
        end
        """
        expectedoutput = "abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 179))

    def test180(self):
        inputstr = """
        func haha()
        begin
            writeString("haha")
        end
        func main()
        begin
            haha()
        end
        """
        expectedoutput = "haha"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 180))

    def test181(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 181))

    def test182(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 182))

    def test183(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 183))

    def test184(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 184))

    def test185(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 185))

    def test186(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 186))

    def test187(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 187))

    def test188(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 188))

    def test189(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 189))

    def test190(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 190))

    def test191(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 191))

    def test192(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 192))

    def test193(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 193))

    def test194(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 194))

    def test195(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 195))

    def test196(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 196))

    def test197(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 197))

    def test198(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 198))

    def test199(self):
        inputstr = """
        func main()
        begin
            writeNumber(1)
            writeString("abc")
        end
        """
        expectedoutput = "1.0abc"
        self.assertTrue(TestCodeGen.test(inputstr, expectedoutput, 199))

    def test200(self):
        input = """
        func add(number a)
        begin
            if (a = 5) return 1
            else return 2
        end
        func main()
        begin
            number a <- 6
            writeNumber(add(a))
            if (a = 5) writeNumber(1)
            else writeNumber(0)
        end
        """
        expect = "2.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 200))
