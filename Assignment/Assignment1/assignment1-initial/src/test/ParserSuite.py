import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test101(self):
        """testcase 101"""
        input = """
            func main()
            begin
                number a
                number b <- 2
                a <- 3 + 2 + -1 - 5
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))

    def test102(self):
        """testcase 102"""
        input = """
            func main()
            begin
                number a[2, 3] <- [[1, 2, 3], [4, 5, 6]]
                ## array a
                string b <- "Hello world"
                var i <- 1
                for i until i >= 10 by 1
                begin
                    printString(b)
                    if (i > 5) break
                    else continue

                end
                number e
                e <- a[1, 2] - 3 * a[2, 1] + not a[2, 2]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 102))
    
    def test103(self):
        """testcase 103"""
        input = """
            number a
            func factorial(number n)
            begin
                if (n = 0) return 1
                else return n * factorial(n - 1)       ## recursive
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 103))

    def test104(self):
        """testcase 104"""
        input = """
            func isPrime(number x)
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
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 104))

    def test105(self):
        """testcase 105"""
        input = """
            number a[5] <- [0, 2, 4, 6, 8]
            func main()
            begin
                var i = 2
                for i = 1 until i < 5 by 1
                begin
                    print(a[i])
                end
            end
        """
        expect = "Error on line 5 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 105))

    def test106(self):
        """testcase 106"""
        input = """
            number a[true, "abc"] <- [[1, 2, 3], [4, 5, 6]]
            func main()
            begin
                print(a[1])
            end
        """
        expect = "Error on line 2 col 21: true"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test107(self):
        """testcase 107"""
        input = """
            bool a[2, 3] <- [[true, false, true], [false, true, false]] ## array a
            number b[2, 3] <- [[1, 2, 3], [4, 5, 6]] ## array b
            string str <- "Hello world" ## string str
            func main()
            begin
                print(a[1, 2])
                print(b[1, 2])
                print(str)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test108(self):
        """testcase 108"""
        input = """
            func main()
            begin
                var a <- 1
                var b <- 2
                var c <- 3
                if ((a < b) and (b < c)) printString("a < b < c")
                elif ((a < c) and (c < b)) printString("a < c < b")
                elif ((b < a) and (a < c)) printString("b < a < c")
                elif ((b < c) and (c < a)) printString("b < c < a")
                elif ((c < a) and (a < b)) printString("c < a < b")
                elif (c < b) and (b < a) printString("c < b < a")
                else printString("a = b = c")
            end
        """
        expect = "Error on line 12 col 29: and"
        self.assertTrue(TestParser.test(input, expect, 108))

    def test109(self):
        """testcase 109"""
        input = """
            number a[5] <- [1, 3, 5, 7, 9]
            number n <- (a[5])[2]
            func main()
            begin
                print(n)
            end
        """
        expect = "Error on line 3 col 30: ["
        self.assertTrue(TestParser.test(input, expect, 109))

    def test110(self):
        """testcase 110"""
        input = """
            func gcd(number a, number b)
            begin
                if (a > b) return gcd(b, a%b)
                elif (a < b) return gcd(b%a, a)
                else return a
            end



            func main()
            begin
                number a <- readNumber()
                number b <- readNumber()
                print(gcd(a, b))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 110))

    def test111(self):
        """testcase 111"""
        input = """
            number num <- readNumber()
            func main()
            begin
                if (num = 1)
                if (num = 2)
                if (num = 3)
                if (num = 4) printString("num = 4")
                elif (num = 5) printString("num = 5")
                else printString("num = 3")
                else printString("num = 2")
                else printString("num = 1")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 111))

    def test112(self):
        """testcase 112"""
        input = """
            func main()
            begin
                number a
                a <- a * b - c + not 1 and 2 + 3 ... c
                var m

            end
        """
        expect = "Error on line 6 col 21: \n"
        self.assertTrue(TestParser.test(input, expect, 112))

    def test113(self):
        """testcase 113"""
        input = """func main()
                begin
                    number u <- 1e4
                    for u until u < 0 by -1
                    begin
                        if (u % 5 = 0) writeString(u ... " is even")
                        elif writeString(u ... " is odd")
                        else break
                    end
                end
        """
        expect = "Error on line 7 col 29: writeString"
        self.assertTrue(TestParser.test(input,expect,113))

    def test114(self):
        """testcase 114"""
        input = """
            func foo(number a) begin
                if ((a=1) or (a=0)) return 1
                return a*foo(a)
            end

            number arr[2,3] <- [[1,2,3],[4.E+5 + 6.e-7 * foo(8) and 9]]

            func main()
            begin
                number a <- arr[foo(0) = 1,foo(2)%3-4]*(not foo(5) and foo(6))
                return
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,114))

    def test115(self):
        """testcase 115"""
        input = """
            func foo()
            begin
                number arr[2,3,4] <- [[1,2,3],["abc","def","ghi"],[false,true,false]]
                return arr
            end
            func main()
            begin
                foo()[2,3,4] <- 5
            end
        """
        expect = "Error on line 9 col 21: ["
        self.assertTrue(TestParser.test(input,expect,115))

    def test116(self):
        """testcase 116"""
        input = """
            func main()
            begin
                number a <- 5
                if (a < 10) print("a is less than 10")
                else print("a is greater than or equal to 10")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,116))

    def test117(self):
        """testcase 117"""
        input = """
            dynamic num
            var a <- 1
            string b <- [[2]]
            func main()
            begin
                foo(2)
                c <- not 3 and foo()
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,117))

    def test118(self):
        """testcase 118"""
        input = """
            var number <- 1
            func main()

        """
        expect = "Error on line 2 col 16: number"
        self.assertTrue(TestParser.test(input,expect,118))

    def test119(self):
        """testcase 119"""
        input = """
            func main()
            begin
                number a[] <- [1, 2, 3]
                print(a[1])
            end
        """
        expect = "Error on line 4 col 25: ]"
        self.assertTrue(TestParser.test(input,expect,119))

    def test120(self):
        """testcase 120"""
        input = """
            string str
            func main()
            begin
                number a <- [[1, 2, 3], [4, 5, 6]] + not 2 = 3
                if (a) printString()


                else printString(str)
            end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,120))

    def test121(self):
        """testcase 121"""
        input = """
            func main() begin end
        """
        expect = "Error on line 2 col 30: end"
        self.assertTrue(TestParser.test(input,expect,121))

    def test122(self):
        """testcase 122"""
        input = """
            func _1() return

            
            func 2() return ## invalid function name
            func main() return


        """
        expect = "Error on line 5 col 17: 2"
        self.assertTrue(TestParser.test(input,expect,122))

    def test123(self):
        """testcase 123"""
        input = """
            func main()


            ## Hihi this is a comment



            begin





            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,123))

    def test124(self):
        """testcase 124"""
        input = """## Start program
            bool flag <- true
            func main()
            begin
                if (flag) printString("Hello world")
                else printString("Goodbye world")
                else return
            end
        """
        expect = "Error on line 7 col 16: else"
        self.assertTrue(TestParser.test(input,expect,124))

    def test125(self):
        """testcase 125"""
        input = """
            string str1 <- "Hoang" ... "Nhat"
            string str2 <- "Hoang" ... "Nhat" ... "Truong"

            func main()
            begin
                print(str1)
                print(str2)
            end
        """
        expect = "Error on line 3 col 46: ..."
        self.assertTrue(TestParser.test(input,expect,125))

    def test126(self):
        """testcase 126"""
        input = """
            ## Testcase 126
            func main()
            begin
                number n1 <- not printString("Hello world")
                number n2 <- peint("Nhat") + print("Truong")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,126))

    def test127(self):
        """testcase 127"""
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 127))

    def test128(self):
        """testcase 128"""
        input = """
            func foo(number n)
            begin
                if (n != 1 and foo(n - 1) = 0) return n*foo(n-1) ## != and = are unasociated
                else return 1 + false ## Comment

            end
            number n <- foo(5)

        """
        expect = "Error on line 4 col 42: ="
        self.assertTrue(TestParser.test(input, expect, 128))

    def test129(self):
        """testcase 129"""
        input = """ 
            var arr[3] <- [1, 2, 3]
        """
        expect = "Error on line 2 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 129))

    def test130(self):
        """testcase 130"""
        input = """
            number f["Hello", 2] <- foo(0)
            func main()
            begin
                print(f["true", 2])
            end
        """
        expect = "Error on line 2 col 21: Hello"
        self.assertTrue(TestParser.test(input, expect, 130))

    def test131(self):
        """testcase 131"""
        input = """
            number fib[50] <- [0, 1]
            func createFib()
            begin
                var i <- 2
                for i until i < 50 by 1
                    fib[i] <- fib[i - 1] + fib[i - 2]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 131))

    def test132(self):
        """testcase 132"""
        input = """
            Func main()
            begin
                print("Testcase 132")
            end
        """
        expect = "Error on line 2 col 12: Func"
        self.assertTrue(TestParser.test(input, expect, 132))

    def test133(self):
        """testcase 133"""
        input = """
            

            func main() begin print("Hi") end
        """
        expect = "Error on line 4 col 30: print"
        self.assertTrue(TestParser.test(input, expect, 133))

    def test134(self):
        """testcase 134"""
        input = """
            var True <- true
            var False <- false
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 134))

    def test135(self):
        """testcase 135"""
        input = """
            func main()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 135))

    def test136(self):
        """testcase 136"""
        input = """
                    func        comb(number n, number k)
            begin
                if ((k = 0) or (k = n)) 
                    return 1
                else 
                    return comb(n - 1, k - 1) + comb(n - 1, k)
            end
                    
                    
                var n <- readNumber()

                var k <- readNumber()
                print(comb(n, k))
        """
        expect = "Error on line 14 col 16: print"
        self.assertTrue(TestParser.test(input, expect, 136))

    def test137(self):
        """testcase 137"""
        input = """
            bool b <- foo(foo(foo(2)*2)*3)*4 and "Hoang"..."Nhat"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 137))

    def test138(self):
        """testcase 138"""
        input = """
            func main() begin
                f(2) <- 3

            end
        
        """
        expect = "Error on line 3 col 21: <-"
        self.assertTrue(TestParser.test(input, expect, 138))

    def test139(self):
        """testcase 139"""
        input = """

            ## Testcase 139

            number n <- "abc" ... "def" = "fed" ... "cba"   ## Assoc check
        """
        expect = "Error on line 5 col 48: ..."
        self.assertTrue(TestParser.test(input, expect, 139))

    def test140(self):
        """testcase 140"""
        input = """
            func bubbleSort(number arr, number n)
            begin
                var i <- 0
                for i until i < n - 1 by 1
                begin
                    var j <- 0
                    for j until j < n - i - 1 by 1
                    begin
                        if (arr[j] > arr[j + 1]) 
                        begin
                            var temp <- arr[j]
                            arr[j] <- arr[j + 1]
                            arr[j + 1] <- temp
                        end
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 140))

    def test141(self):
        """testcase 141"""
        input = """
            var i ## Comment
            func main()
        """
        expect = "Error on line 2 col 28: \n"
        self.assertTrue(TestParser.test(input, expect, 141))

    def test142(self):
        """testcase 142"""
        input = """
            func    main()
            begin
                var     a <- [1, 2, 3]
                var b    <- [4, 5, 6]
                var c[2] <-     a + b
            end
        """
        expect = "Error on line 6 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 142))

    def test143(self):
        """testcase 143"""
        input = """
            bool ar[true, 2] <- [[true, false], false, true]
        """
        expect = "Error on line 2 col 20: true"
        self.assertTrue(TestParser.test(input, expect, 143))

    def test144(self):
        """testcase 144"""
        input = """
            func foo(var a, number b)
            begin
                if (a = 1) return 1
                else return a*foo(a)
            end
        """
        expect = "Error on line 2 col 21: var"
        self.assertTrue(TestParser.test(input, expect, 144))

    def test145(self):
        """testcase 145"""
        input = """
            func main()     ## Main 1
            func main()     ## Main 2
            func main()     ## Main 3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 145))

    def test146(self):
        """testcase 146"""
        input = """
            func main()
            begin
                number a <- readNumber()
                if (a = 1)
                if (a = 2) 
                    printString("a = 2")
                else if (a = 3) printString("a = 3") 
                else 
                    printString("a = 1")   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 146))

    def test147(self):
        """testcase 147"""
        input = """
            func testcase147()
            begin
                for i until i < 10 by 1
                for j until j < 10 by 1
                for k until k < 10 by 1
            end
        """
        expect = "Error on line 7 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 147))

    def test148(self):
        """testcase 148"""
        input = """
            func main()
            if (true) print("true")
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 148))

    def test149(self):
        """testcase 149"""
        input = """
            func test149()
            begin
                input <- "\\n func test149() \\n begin \\n ## testcase 149 \\n ...(something)... \\n end"
                expected <- "successful"
                self->assertTrue(TestParser->test(input, expected, 149))
            end
        """
        expect = "Error on line 6 col 20: -"
        self.assertTrue(TestParser.test(input, expect, 149))

    def test150(self):
        """testcase 150"""
        input = """
            func test150()
            begin
                ## testcase 150
                input <- "\\n func test150() \\n begin \\n ## testcase 150 \\n ...(something)... \\n end"
                expected <- "successful"
                selfAssertTrue(TestParsertest(input, expected, 150))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 150))

    def test151(self):
        """testcase 151"""
        input = """
            func main()
            begin
                number a <- 1
                if (a < 10)
                    print("a is less than 10")
                    a <- a + 10
                else
                    print("a is greater than or equal to 10")
                    a <- a - 10
            end
        """
        expect = "Error on line 8 col 16: else"
        self.assertTrue(TestParser.test(input, expect, 151))

    def test152(self):
        """testcase 152"""
        input = """
            func main()
            begin
                3 + 2 + -1 <- 4
            end
        """
        expect = "Error on line 4 col 16: 3"
        self.assertTrue(TestParser.test(input, expect, 152))

    def test153(self):
        """testcase 153"""
        input = """
            string str <- foo()[2, 3, 4]
            number a <- str[2][4]
        """
        expect = "Error on line 3 col 30: ["
        self.assertTrue(TestParser.test(input, expect, 153))

    def test154(self):
        """testcase 154"""
        input = """
            string str <- foo(a and b ... "\\n\\\\" + ("\\\''\"" ... true * not false))[2,2] ## String str
            func main() begin ## Begin
            end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 154))

    def test155(self):
        """testcase 155"""
        input = """
            func foo(number a[], bool b) return
        """
        expect = "Error on line 2 col 30: ]"
        self.assertTrue(TestParser.test(input, expect, 155))

    def test156(self):
        """testcase 156"""
        input = """
            ## This testcase does not have any declaration
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 156))

    def test157(self):
        """testcase 157"""
        input = """ 
            func foo(number a) begin
                if (a=1 or a=0) return 1
                return a*foo(a)
            end

            number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]

            func main()
            begin
                number a<- arr[foo(1),foo(3)%3]
                return
            end
        """
        expect = "Error on line 3 col 28: ="
        self.assertTrue(TestParser.test(input, expect, 157))

    def test158(self):
        """testcase 158"""
        input = """
            func main()
            begin
                var __ <- __
                for __ until _+_*_/_...not_ by __
                    __ <- __
                if  (_-_) return
                elif (_-_) return
                else return
            end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 158))

    def test159(self):
        """testcase 159"""
        input = """
            func main()
            begin
                while(1)
                ## "while(1)" is a function call
                begin
                    print("Hello world")
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 159))

    def test160(self):
        """testcase 160"""
        input = """
            func _()
            begin
                continue
                break
                return
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 160))

    def test161(self):
        """testcase 161"""
        input = """
            func _()
            begin
                Break <- Continue()
                [2] <- 3
            end
        """
        expect = "Error on line 5 col 16: ["
        self.assertTrue(TestParser.test(input, expect, 161))

    def test162(self):
        """testcase 162"""
        input = """
            var a <- (((((((((((2)))))))))))
            number b[2] <- [a, [1, 2]]
            dynamic c[2, 3] <- [[a, b, 3], [true, foo(2), "abc"]]
            func main()
        """
        expect = "Error on line 4 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 162))

    def test163(self):
        """testcase 163"""
        input = """
            func _1()
            number _1
            func _2()
            string _2
            func _3()
            bool _3
            var result <- _1 + _2 + _3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test164(self):
        """testcase 164"""
        input = """
            return
        """
        expect = "Error on line 2 col 12: return"
        self.assertTrue(TestParser.test(input, expect, 164))

    def test165(self):
        """testcase 165"""
        input = """
            func
            main
            (
            )
            begin
            end
        """
        expect = "Error on line 2 col 16: \n"
        self.assertTrue(TestParser.test(input, expect, 165))

    def test166(self):
        """testcase 166"""
        input = """
            func elif()
            begin
                print("elif")
            end
        """
        expect = "Error on line 2 col 17: elif"
        self.assertTrue(TestParser.test(input, expect, 166))

    def test167(self):
        """testcase 167"""
        input = """
            func main()

            begin
                if (c = 1)
                if (c = 2) c(2)
                elif (c = 3) c(3)
                elif (c = 4)
                if (c = 5)
                if (c = 6) c(6)
                else return
            
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 167))

    def test168(self):
        """testcase 168"""
        input = """
            func main()     ## testcase 168

            begin
                if (c = 1)
                if (c = 2) return
                elif (c = 3)
                elif (c = 4) return
                if (c = 5)
                if (c = 6) return
                else return
            
            end
        """
        expect = "Error on line 8 col 16: elif"
        self.assertTrue(TestParser.test(input, expect, 168))

    def test169(self):
        """testcase 169"""
        input = """
            func main() return
            begin
                number a <- 5
                foo(a = 5)
            end
        """
        expect = "Error on line 3 col 12: begin"
        self.assertTrue(TestParser.test(input, expect, 169))

    def test170(self):
        """testcase 170"""
        input = """
        ## Testcase 170
        func main() begin


            var a <- 1
            var b <- 2
            a <- a + b
            print(a)
        end


        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))

    def test171(self):
        """testcase 171"""
        input = """
            func isPrime(number x)
            
            func main()
            begin
                number x <- readNumber()
                if (isPrime(x)) writeString("Yes")
                else writeString("No")
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
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 171))

    def test172(self):
        """testcase 172"""
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))

            func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 172))

    def test173(self):
        """testcase 173"""
        input = """
            ## comment func main()
            begin
                return
            end
        """
        expect = "Error on line 3 col 12: begin"
        self.assertTrue(TestParser.test(input, expect, 173))

    def test174(self):
        """testcase 174"""
        input = """
            number pi <- 3.14159265358979323
            func area(number r)
            begin
                return pi * r * r
            end

            func main()
            begin
                number r <- readNumber()
                print(area(r))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 174))

    def test175(self):
        """testcase 175"""
        input = """
            func main()

            begin

                var a <- 1
                variable <- - b <= c and foo([2] + e*p0 - 4%m) % 3 or c[2] ... "hi" > 3
                error <- --c + not not not a <= b * [c, foo*(2-foo(1))] / 2 == false
            end

        """
        expect = "Error on line 8 col 76: =="
        self.assertTrue(TestParser.test(input, expect, 175))

    def test176(self):
        """testcase 176"""
        input = """
            number a[3,3] <- [[0.0E-1, "76QuangNgai", false], [-1, -2, -3], foo(5)*7/5%9 and not 11]
            ## Testcase 176
            func main()
            begin
                print(a[1, 2], a[2, 1], a[3, 3])
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 176))

    def test177(self):
        """testcase 177"""
        input = """
            ## Testcase 177
            dynamic i
            func main()
            begin
                print(i + 2 % 3 - not 2 = _ / (2.3E-19 * n))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 177))

    def test178(self):
        """testcase 178"""
        input = """
            func atom_val(string atom)
            begin
                if (atom = "H") return 1
                elif (atom = "He") return 2
                elif (atom = "Li") return 3
                elif (atom = "Be") return 4
                elif (atom = "B") return 5
                elif (atom = "C") return 6
                elif (atom = "N") return 7
                elif (atom = "O") return 8
                elif (atom = "F") return 9
                elif (atom = "Ne") return 10
                elif (atom = "Na") return 11
                elif (atom = "Mg") return 12
                elif (atom = "Al") return 13
                elif (atom = "Si") return 14
                elif (atom = "P") return 15
                elif (atom = "S") return 16
                elif (atom = "Cl") return 17
                elif (atom = "Ar") return 18
                elif (atom = "K") return 19
                elif (atom = "Ca") return 20
                elif (atom = "Sc") return 21
                elif (atom = "Ti") return 22
                elif (atom = "V") return 23
                elif (atom = "Cr") return 24
                elif (atom = "Mn") return 25
                elif (atom = "Fe") return 26
                elif (atom = "Co") return 27
                elif (atom = "Ni") return 28
                elif (atom = "Cu") return 29
                elif (atom = "Zn") return 30
                elif (atom = "Ga") return 31
                elif (atom = "Ge") return 32
                elif (atom = "As") return 33
                elif (atom = "Se") return 34
                elif (atom = "Br") return 35
                elif (atom = "Kr") return 36
                elif (atom = "Rb") return 37
                elif (atom = "Sr") return 38
                elif (atom = "Y") return 39
                elif (atom = "Zr") return 40
                elif (atom = "Nb") return 41
                elif (atom = "Mo") return 42
                elif (atom = "Tc") return 43
                elif (atom = "Ru") return 44
                elif (atom = "Rh") return 45
                elif (atom = "Pd") return 46
                elif (atom = "Ag") return 47
                elif (atom = "Cd") return 48
                elif (atom = "In") return 49
                elif (atom = "Sn") return 50
                elif (atom = "Sb") return 51
                elif (atom = "Te") return 52
                elif (atom = "I") return 53
                elif (atom = "Xe") return 54
                elif (atom = "Cs") return 55
                elif (atom = "Ba") return 56
                elif (atom = "La") return 57
                elif (atom = "Ce") return 58
                elif (atom = "Pr") return 59
                elif (atom = "Nd") return 60
                elif (atom = "Pm") return 61
                elif (atom = "Sm") return 62
                elif (atom = "Eu") return 63
                elif (atom = "Gd") return 64
                elif (atom = "Tb") return 65
                elif (atom = "Dy") return 66
                elif (atom = "Ho") return 67
                elif (atom = "Er") return 68
                elif (atom = "Tm") return 69
                elif (atom = "Yb") return 70
                elif (atom = "Lu") return 71
                elif (atom = "Hf") return 72
                elif (atom = "Ta") return 73
                elif (atom = "W") return 74
                elif (atom = "Re") return 75
                elif (atom = "Os") return 76
                elif (atom = "Ir") return 77
                elif (atom = "Pt") return 78
                elif (atom = "Au") return 79
                elif (atom = "Hg") return 80
                elif (atom = "Tl") return 81
                elif (atom = "Pb") return 82
                elif (atom = "Bi") return 83
                elif (atom = "Po") return 84
                elif (atom = "At") return 85
                elif (atom = "Rn") return 86
                elif (atom = "Fr") return 87
                elif (atom = "Ra") return 88
                elif (atom = "Ac") return 89
                elif (atom = "Th") return 90
                elif (atom = "Pa") return 91
                elif (atom = "U") return 92
                elif (atom = "Np") return 93
                elif (atom = "Pu") return 94
                elif (atom = "Am") return 95
                elif (atom = "Cm") return 96
                elif (atom = "Bk") return 97
                elif (atom = "Cf") return 98
                elif (atom = "Es") return 99
                elif (atom = "Fm") return 100
                elif (atom = "Md") return 101
                elif (atom = "No") return 102
                elif (atom = "Lr") return 103
                elif (atom = "Rf") return 104
                elif (atom = "Db") return 105
                elif (atom = "Sg") return 106
                elif (atom = "Bh") return 107
                elif (atom = "Hs") return 108
                elif (atom = "Mt") return 109
                elif (atom = "Ds") return 110
                elif (atom = "Rg") return 111
                elif (atom = "Cn") return 112
                elif (atom = "Nh") return 113
                elif (atom = "Fl") return 114
                elif (atom = "Mc") return 115
                elif (atom = "Lv") return 116
                elif (atom = "Ts") return 117
                elif (atom = "Og") return 118
                else return 0
            end

            func calc_PTK(string formula)
            begin
                number PTK <- 0
                number aval
                number idx
                for i until i < len(formula) by 1
                begin
                    if (isUpper(formula[i]))
                    begin
                        var atom <- formula[i]
                        if (i + 1 < len(formula) and isLower(formula[i + 1]))
                        begin
                            atom <- atom + formula[i + 1]
                            i <- i + 1
                        end
                        aval <- atom_val(atom)
                        if (aval = 0) return 0
                    end
                    else if (isDigit(formula[i]))
                    begin
                        idx <- 0
                        for i until (i < len(formula) and isDigit(formula[i])) by 1
                        begin
                            idx <- idx * 10 + (formula[i] - "0")
                            i <- i + 1
                        end
                        if (idx = 0) return 0
                        else PTK <- PTK + aval * idx
                    end
                end
                return PTK
            end

            func main()
            begin
                string formula <- readString()
                print(calc_PTK(formula))
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 178))
    def test179(self):
        """testcase 179"""
        input = """
            func main()
            begin
                number a[0] <- []

            end
        """
        expect = "Error on line 4 col 32: ]"
        self.assertTrue(TestParser.test(input, expect, 179))

    def test180(self):
        """testcase 180"""
        input = """
            number arr[0.3, 3e+9] <- Nhat
            func main()
            begin
                if (arr[0.3]..."Huhu test 178 dai qua") print("Sorry thay")
                else break
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 180))

    def test181(self):
        """testcase 181"""
        input = """
            func main()
            begin
                bool a <- a[not not - - (a[a[a[a[a[a[0]]]]]]), 2 + 3/4, [1,2,3,4]]
            end
            var b <- a(1,2)[1,2,3 ... 2] + true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 181))

    def test182(self):
        """testcase 182"""
        input = """
            var i <- 0
            var j <- i
            var k <- j
            func main()
            begin
                for i until i < 10 by 1 for j until j < i by 1 for k until k < j by 1 return
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 182))

    def test183(self):
        """testcase 183"""
        input = """
            number n <- not(a + b (foo(b, c, d)/true ... 1) - continue)
            func main() return
        """
        expect = "Error on line 2 col 62: continue"
        self.assertTrue(TestParser.test(input, expect, 183))

    def test184(self):
        """testcase 184"""
        input = """
            func            main()

            begin   
                        dynamic n
            n <-    ((A or B and C + 10/2%3+1) <= (not(-1+foo(a+k+(p2-1)))))...(true != false)
                    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 184))

    def test185(self):
        """testcase 185"""
        input = """
            func main()
            func 0()
            return
        """
        expect = "Error on line 3 col 17: 0"
        self.assertTrue(TestParser.test(input, expect, 185))

    def test186(self):
        """testcase 186"""
        input = """
            func a+b()
            begin
                return
            end
        """
        expect = "Error on line 2 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 186))

    def test187(self):
        """testcase 187"""
        input = """
            string str <- "Testcase"        ... "187"
            func main()
            begin
                print(not [1,2,foo()] + 0 ... str - "" % 3 != 7)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 187))

    def test188(self):
        """testcase 188"""
        input = """
            number a <- (not 3%2)[0]
            var b <- 1
        """
        expect = "Error on line 2 col 33: ["
        self.assertTrue(TestParser.test(input, expect, 188))

    def test189(self):
        """testcase 189"""
        input = """
            func main() begin
                return end
        """
        expect = "Error on line 3 col 23: end"
        self.assertTrue(TestParser.test(input, expect, 189))

    def test190(self):
        """testcase 190"""
        input = """
            func main() begin
                return
            end func main() begin
                return
            end
        """
        expect = "Error on line 4 col 16: func"
        self.assertTrue(TestParser.test(input, expect, 190))

    def test191(self):
        """testcase 191"""
        input = """
            func foo(number a,
            string str) return
        
        """
        expect = "Error on line 2 col 30: \n"
        self.assertTrue(TestParser.test(input, expect, 191))

    def test192(self):
        """testcase 192"""
        input = """
            bool b <- getBool(foo(1), foo(getBool(foo(2), foo()), getBool(1)), getBool(foo(1), getBool(foo(1))))

            dynamic a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 192))

    def test193(self):
        """testcase 193"""
        input = """
            func main()
            begin
                begin
                    begin
                        begin
                            begin
                                begin
                                end
                            end
                        end
                    end
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 193))

    def test194(self):
        """testcase 194"""
        input = """
            string b <- -___-___-___-___-__
            number a <- (p*-----------id---------q)

            func main()
                return a+b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 194))

    def test195(self):
        """testcase 195"""
        input = """number a <- (a[1]*[1]) ---- 3"""
        expect = "Error on line 1 col 29: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 195))

    def test196(self):
        """testcase 196"""
        input = """
            string a <- "Hoang '" Nhat ... " ... 4869"--"
            func main()
            begin
                print(a)
            end
        """
        expect = "Error on line 2 col 53: --"
        self.assertTrue(TestParser.test(input, expect, 196))

    def test197(self):
        """testcase 197"""
        input = """
            ## Testcase 197
            func testcase197(number a, number b)

                    func main()

            begin
                str <- foo(null, "...")...foo(1, 2, 3)
            end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 197))

    def test198(self):
        """testcase 198"""
        input = """
            var a <- [hehe, (0), 2*3]
            ## Testcase 198
            var m <- a[2, 3, 1][0]
        """
        expect = "Error on line 4 col 31: ["
        self.assertTrue(TestParser.test(input, expect, 198))

    def test199(self):
        """testcase 199"""
        input = """
            func ## Comment main() ## Comment begin
                number a <- 1
            end
        """
        expect = "Error on line 2 col 51: \n"
        self.assertTrue(TestParser.test(input, expect, 199))

    def test200(self):
        """testcase 200"""
        input = """
            string testcase200 <- "This is the final testcase, I don't know where I could put the \\r character"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))