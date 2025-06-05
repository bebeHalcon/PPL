import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    ######---------- Test Keywords, Operators, Separators ----------######
    def test001(self):
        """testcase 1: Keywords, operators, separators (No comment)"""
        input = """, bool + func > true if >= == and <= else 
        ... until string for * ) <- number by ] var dynamic % begin - [ < return continue or elif ( != break false /"""
        expect = ",,bool,+,func,>,true,if,>=,==,and,<=,else,\n,...,until,string,for,*,),<-,number,by,],var,dynamic,%,begin,-,[,<,return,continue,or,elif,(,!=,break,false,/,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,1))

    def test002(self):
        """testcase 2: Keywords, operators, separators (With comment)"""
        input = """break if - by until else ##Comment return % >= <= / 
        ... number var and , ) false ## begin end not and"""
        expect = "break,if,-,by,until,else,\n,...,number,var,and,,,),false,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,2))


    ######---------- Test Identifiers ----------######
    def test003(self):
        """testcase 3: Normal Identifiers"""
        input = """nhatTruong HoangNhat4869 n4H8a6T9
        truong*hoang*nhat abc/def/ghi"""
        expect = "nhatTruong,HoangNhat4869,n4H8a6T9,\n,truong,*,hoang,*,nhat,abc,/,def,/,ghi,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,3))

    def test004(self):
        """testcase 4: Identifiers start with underscore"""
        input = """_beginend hoangnhat_truong _underscore_123
        _principle_of_programming_language_assignment_1"""
        expect = "_beginend,hoangnhat_truong,_underscore_123,\n,_principle_of_programming_language_assignment_1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,4))

    def test005(self):
        """testcase 5: Identifiers start with number"""
        input = """NHAT4869 != 4869nhat_Truong 268_LyThuongKiet_District_10_HCMC"""
        expect = "NHAT4869,!=,4869,nhat_Truong,268,_LyThuongKiet_District_10_HCMC,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,5))

    def test006(self):
        """testcase 6: Identifiers with comments"""
        input = """_HoangNhat4869 ____OK____ ## This is not an identifier
        Newline... #############
        __main__ testcase006"""
        expect = "_HoangNhat4869,____OK____,\n,Newline,...,\n,__main__,testcase006,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,6))
    
    
    ######---------- Literals ----------######
    def test007(self):
        """testcase 7: Boolean and number literals"""
        input = """0 0022 18 true 02 000 0.10e03 4E-90 10. 3e0 false
        00.4869E+10 ##Comment
        _02main_"""
        expect = "0,0022,18,true,02,000,0.10e03,4E-90,10.,3e0,false,\n,00.4869E+10,\n,_02main_,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,7))

    def test008(self):
        """testcase 8: Number in program"""
        input = """
        number fib[50] <- [0, 1]
        func createFib()
        begin
            var i <- 2
            for i until i < 50 by 1
                fib[i] <- fib[i - 1] + fib[i - 2]
            end
        end
        """
        expect = "\n,number,fib,[,50,],<-,[,0,,,1,],\n,func,createFib,(,),\n,begin,\n,var,i,<-,2,\n,for,i,until,i,<,50,by,1,\n,fib,[,i,],<-,fib,[,i,-,1,],+,fib,[,i,-,2,],\n,end,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,8))

    def test009(self):
        """testcase 9: String literals"""
        input = """truefalse 0.23E+09 "String"
        "a" < "b" < "c" ##"""
        expect = "truefalse,0.23E+09,String,\n,a,<,b,<,c,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,9))

    def test010(self):
        """testcase 10: String with escape characters"""
        input = r""""This is a string containing escape characters: \n \t \b \r \f \' \\" a + b = 0.02E-14 ##__OK__"""
        expect = "This is a string containing escape characters: \\n \\t \\b \\r \\f \\' \\\\,a,+,b,=,0.02E-14,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,10))

    def test011(self):
        """testcase 11: String with special characters"""
        input = "\"Testcase 11: Nhat's \t string.%^*#*$...\"##__Testcase 10__"
        expect = "Testcase 11: Nhat's \t string.%^*#*$...,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,11))

    def test012(self):
        """testcase 12: Distinguish whitespace and escape sequence"""
        input = r""""Truong"_"Hoang_Nhat"##__Testcase 12__
        4869.0310E2003 _"N"*##009.0989 "String\r"
        "Newline: \n" "Tab: \t" "Backspace: \b" "Formfeed: \f" "Backslash: \\" "Single quote: \'" """
        expect = "Truong,_,Hoang_Nhat,\n,4869.0310E2003,_,N,*,\n,Newline: \\n,Tab: \\t,Backspace: \\b,Formfeed: \\f,Backslash: \\\\,Single quote: \\\',<EOF>"
        self.assertTrue(TestLexer.test(input,expect,12))

    def test013(self):
        """testcase 13"""
        input = """string str <- "This is " ## String str
        string newstr <- abc ... "Nhat's testcase." ##__Testcase 13__"""
        expect = "string,str,<-,This is ,\n,string,newstr,<-,abc,...,Nhat's testcase.,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,13))

    def test014(self):
        """testcase 14: Double quote in string"""
        input = """"BK@HCMUT"" * % CSE'"'"PPL"
        ##__Testcase 14__"""
        expect = "BK@HCMUT, * % CSE'\"'\"PPL,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,14))


    ######---------- Test Newline, Comment ----------######
    def test015(self):
        """testcase 15: Comments"""
        input = """## Comment 1
        ## Comment 2
        ## Comment 3
        """
        expect = "\n,\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,15))

    def test016(self):
        """testcase 16: Comment in line"""
        input = """Testcase 16 <- Comments ## This is a comment ## Comment???"""
        expect = "Testcase,16,<-,Comments,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,16))

    def test017(self):
        """testcase 17: Newline with \n character"""
        input = "\n\n\n\n"
        expect = "\n,\n,\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,17))

    def test018(self):
        """testcase 18: Newline with 'enter' button"""
        input = """
        ## ^^ :)))

        """
        expect = "\n,\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,18))

    def test019(self):
        """testcase 19: Comment in string"""
        input = """string str <- "testcase19 ## Comment in string" ##__Testcase 19__"""
        expect = "string,str,<-,testcase19 ## Comment in string,<EOF>"   
        self.assertTrue(TestLexer.test(input,expect,19))

    def test020(self):
        """testcase 20: Comments"""
        input = """######
        01######### number
        true + false / div [ begin,######## keyword
        "\\\\"###
        """
        expect = "\n,01,\n,true,+,false,/,div,[,begin,,,\n,\\\\,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,20))


    ######---------- Test Error ----------######
    def test021(self):
        """testcase 21: Error Token"""
        input = """and
        continue > break not % <- $ ... [ >= or ! <= - end + { bool ] ) # ? , by * true ="""
        expect = "and,\n,continue,>,break,not,%,<-,Error Token $"
        self.assertTrue(TestLexer.test(input,expect,21))

    def test022(self):
        """testcase 22: Error Token"""
        input = """bool not continue true ... by until ( var < for if ] return begin , = and func <- == TruongHoangNhat != # % [ string @ >= false dynamic /"""
        expect = "bool,not,continue,true,...,by,until,(,var,<,for,if,],return,begin,,,=,and,func,<-,==,TruongHoangNhat,!=,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,22))

    def test023(self):
        """testcase 23: Error Token"""
        input = """(-_-)(>_<)(^_^)"""
        expect = "(,-,_,-,),(,>,_,<,),(,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,23))

    def test024(self):
        """testcase 24: Error Token"""
        input = """string number a = 0.02E+19 + c and not -2 or .48e-69
        b <- c + a - e ... d"""
        expect = "string,number,a,=,0.02E+19,+,c,and,not,-,2,or,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,24))

    def test025(self):
        """testcase 25: Error Token"""
        input = """
        import math
        def area(r):
            return math.pi * (r ** 2)
        """
        expect = "\n,import,math,\n,def,area,(,r,),Error Token :"
        self.assertTrue(TestLexer.test(input,expect,25))

    def test026(self):
        """testcase 26: Unclosed String"""
        input = "\"'Truong Hoang Nhat'\""
        expect = "Unclosed String: 'Truong Hoang Nhat'\""
        self.assertTrue(TestLexer.test(input,expect,26))

    def test027(self):
        """testcase 27: Unclosed String"""
        input = r""""Truong Hoang Nhat\'\n\b\t"""
        expect = "Unclosed String: Truong Hoang Nhat\\'\\n\\b\\t"
        self.assertTrue(TestLexer.test(input,expect,27))

    def test028(self):
        """testcase 28: Unclosed String"""
        input = """ "Truong Hoang
        Nhat" """
        expect = "Unclosed String: Truong Hoang"
        self.assertTrue(TestLexer.test(input,expect,28))

    def test029(self):
        """testcase 29: Unclosed String"""
        input = r""" "principle of programming language \'" " """
        expect = "principle of programming language \\',Unclosed String:  "
        self.assertTrue(TestLexer.test(input,expect,29))

    def test030(self):
        """testcase 30: Unclosed String"""
        input = """ "Faded - 'Alan Walker'" """
        expect = "Unclosed String: Faded - 'Alan Walker'\" "
        self.assertTrue(TestLexer.test(input,expect,30))

    def test031(self):
        """testcase 31: Unclosed String"""
        input = "\"This is newline character: \n\""
        expect = "Unclosed String: This is newline character: "
        self.assertTrue(TestLexer.test(input,expect,31))

    def test032(self):
        """testcase 32: Unclosed String"""
        input = """ \"'''''''''''\" """
        expect = "Unclosed String: '''''''''''\" "
        self.assertTrue(TestLexer.test(input,expect,32))

    def test033(self):
        """testcase 33: Unclosed String"""
        input = """"Distinguish between \\n and \n" """
        expect = "Unclosed String: Distinguish between \\n and "
        self.assertTrue(TestLexer.test(input,expect,33))
    
    def test034(self):
        """testcase 34: Unclosed String"""
        input = """// ## Comment
        "Testcase34\\\\" ## Comment
        "\n" ## Comment
        """
        expect = "/,/,\n,Testcase34\\\\,\n,Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,34))

    def test035(self):
        """testcase 35: Unclosed String"""
        input = """
        func main()
        begin
            print("Unclosed String: \n)
        end
        """
        expect = "\n,func,main,(,),\n,begin,\n,print,(,Unclosed String: Unclosed String: "
        self.assertTrue(TestLexer.test(input,expect,35))
    
    def test036(self):
        """testcase 36: Illegal Escape In String"""
        input = r""" "Illegal Escape In String: \a" """
        expect = "Illegal Escape In String: Illegal Escape In String: \\a"
        self.assertTrue(TestLexer.test(input,expect,36))

    def test037(self):
        """testcase 37: Illegal Escape In String"""
        input = r""""Truong Hoang Nhat \s" """
        expect = "Illegal Escape In String: Truong Hoang Nhat \\s"
        self.assertTrue(TestLexer.test(input,expect,37))

    def test038(self):
        """testcase 38: Illegal Escape In String"""
        input = r"""string str <- "Escape character: \1 \2 \3 \4 \5 \6 \7 \8" """
        expect = "string,str,<-,Illegal Escape In String: Escape character: \\1"
        self.assertTrue(TestLexer.test(input,expect,38))

    def test039(self):
        """testcase 39: Illegal Escape In String"""
        input = """ "\\t\\n\\b\\r\\f\\\'\\\\\\h\\o\\a\\n\\g\\n\\h\\a\\t" """
        expect = "Illegal Escape In String: \\t\\n\\b\\r\\f\\\'\\\\\\h"
        self.assertTrue(TestLexer.test(input,expect,39))
        
    def test040(self):
        """testcase 40: Illegal Escape In String"""
        input = r""""Truong Hoang \" Nhat"""
        expect = "Illegal Escape In String: Truong Hoang \\\""
        self.assertTrue(TestLexer.test(input,expect,40))

    def test041(self):
        """testcase 41: Illegal Escape In String"""
        input = r""""Happy \ New \ Year \ 2024" """
        expect = "Illegal Escape In String: Happy \\ "
        self.assertTrue(TestLexer.test(input,expect,41))
        
    def test042(self):
        """testcase 42: Illegal Escape In String"""
        input = r""""Illegal Escape In String: \x \y \z" """
        expect = "Illegal Escape In String: Illegal Escape In String: \\x"
        self.assertTrue(TestLexer.test(input,expect,42))


    ######---------- Test All (43-100) ----------######
    def test043(self):
        """testcase 43"""
        input = """
        ## Testcase 43
        func main()
            var a <- 1
            var b <- 2
            a <- a + b
            print(a)
        end
        """
        expect = "\n,\n,func,main,(,),\n,var,a,<-,1,\n,var,b,<-,2,\n,a,<-,a,+,b,\n,print,(,a,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,43))

    def test044(self):
        """testcase 44"""
        input = "-10e-10 22.e+3 3.eh2 0.000e0.1"
        expect = "-,10e-10,22.e+3,3.,eh2,0.000e0,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,44))

    def test045(self):
        """testcase 45"""
        input = "Ho Chi Minh University of Technology, VNU-HCM"
        expect = "Ho,Chi,Minh,University,of,Technology,,,VNU,-,HCM,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,45))

    def test046(self):
        """testcase 46"""
        input = """ "He said: '"I'll give you $100'"" """
        expect = "He said: '\"I'll give you $100'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,46))

    def test047(self):
        """testcase 47"""
        input = "\nhello"
        expect = "\n,hello,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,47))

    def test048(self):
        """testcase 48"""
        input = """
        number a
        func factorial(number n)
        begin
            if n = 0 return 1
            else return n * factorial(n - 1)
        end
        """
        expect = "\n,number,a,\n,func,factorial,(,number,n,),\n,begin,\n,if,n,=,0,return,1,\n,else,return,n,*,factorial,(,n,-,1,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,48))

    def test049(self):
        """testcase 49"""
        input = """a <- 1 ## Assign 1 to a
        #This is not a comment"""
        expect = "a,<-,1,\n,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,49))

    def test050(self):
        """testcase 50"""
        input = r"""___Underscore___,1234__4321,TruongHoangNhat
        "ABC\n"..."DEF" + string a for if and ()[]()
        ///***123123....."""
        expect = "___Underscore___,,,1234,__4321,,,TruongHoangNhat,\n,ABC\\n,...,DEF,+,string,a,for,if,and,(,),[,],(,),\n,/,/,/,*,*,*,123123.,...,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,50))

    def test051(self):
        """testcase 51"""
        input = """
        func main()
        begin
            string str <- "Happy" ... "New" ... "Year"
            print(a)
        end
        """
        expect = "\n,func,main,(,),\n,begin,\n,string,str,<-,Happy,...,New,...,Year,\n,print,(,a,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,51))

    def test052(self):
        """testcase 52"""
        input = """if9,/begin-]O(untilI*uSl7string>#breakby$r?hcevarfV;2\<k^."s4A...hoangnhat|end&5
        _iNJ@q"""
        expect = "if9,,,/,begin,-,],O,(,untilI,*,uSl7string,>,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,52))

    def test053(self):
        """testcase 53"""
        input = """&Truong#&$hoa@ngnhat):$*4869& Nhat\\ ## @@.@@
        2114303@HCMUT**&"""
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input,expect,53))

    def test054(self):
        """testcase 54"""
        input = """ "'It isn't'" """
        expect = "Unclosed String: 'It isn't'\" "
        self.assertTrue(TestLexer.test(input,expect,54))

    def test055(self):
        """testcase 55"""
        input = "nhat.truongttbn2710@hcmut.edu.vn ## Email"
        expect = "nhat,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,55))

    def test056(self):
        """testcase 56"""
        input = "\"String 1 ##Comment\",\"String 2\"##Comment\n,\"String 3'\""
        expect = "String 1 ##Comment,,,String 2,\n,,,Unclosed String: String 3'\""
        self.assertTrue(TestLexer.test(input,expect,56))

    def test057(self):
        """testcase 57"""
        input = r""""'"'"$\w'" "
        """  
        expect =  "Illegal Escape In String: '\"'\"$\\w"
        self.assertTrue(TestLexer.test(input, expect, 57))
    
    def test058(self):
        """testcase 58"""
        input = """..."..."..."..." """
        expect = "...,...,...,...,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,58))

    def test059(self):
        """testcase 59"""
        input = """0123 00.520E-01 02. 00000.00000E+00000 number if ("@") ?"""
        expect = "0123,00.520E-01,02.,00000.00000E+00000,number,if,(,@,),Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,59))    

    def test060(self):
        """testcase 60"""
        input = """"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,60))

    def test061(self):
        """testcase 61"""
        input = """\"VSCode is the best IDE :)))))\""""
        expect = "VSCode is the best IDE :))))),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,61))
        
    def test062(self):
        """testcase 62"""
        input = """
        func main()
        begin
            print("This is illegal escape sequence: \\a")
        end
        """
        expect = "\n,func,main,(,),\n,begin,\n,print,(,Illegal Escape In String: This is illegal escape sequence: \\a"
        self.assertTrue(TestLexer.test(input,expect,62))

    def test063(self):
        """testcase 63"""
        input = """"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,63))

    def test064(self):
        """testcase 64"""
        input = """ "\\n"/"\\" """
        expect = "\\n,/,Illegal Escape In String: \\\""
        self.assertTrue(TestLexer.test(input,expect,64))
        
    def test065(self):
        """testcase 65"""
        input = """(True(1),False(0)){1,2,3,4,5}"""
        expect = "(,True,(,1,),,,False,(,0,),),Error Token {"
        self.assertTrue(TestLexer.test(input,expect,65))
        
    def test066(self):
        """testcase 66"""
        input = """K2 091 3.e4-21 007 09xxxxxxxx
        00k## {1,2,3,4,5} $%%@%
        ,)-*#"""
        expect = "K2,091,3.e4,-,21,007,09,xxxxxxxx,\n,00,k,\n,,,),-,*,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,66))
        
    def test067(self):
        """testcase 67"""
        input = """
        number a <- foo(c) + 1 + _4869 and not )
        
        string str <- "Hello
        world" ##
        
        """
        expect = "\n,number,a,<-,foo,(,c,),+,1,+,_4869,and,not,),\n,\n,string,str,<-,Unclosed String: Hello"
        self.assertTrue(TestLexer.test(input,expect,67))

    def test068(self):
        """testcase 68"""
        input = """## string a <- "Hello", b <- "World"
        ANTLR PPL
        0094
        *(()!=)
        """
        expect = "\n,ANTLR,PPL,\n,0094,\n,*,(,(,),!=,),\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,68))
        
    def test069(self):
        """testcase 69"""
        input = "09E-23009E3.-348e+84.38E488-+e9E.0"
        expect = "09E-23009,E3,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,69))

    def test070(self):
        """testcase 70"""
        input = """_1_2_3_4_5_6_7_8_9_"""
        expect = "_1_2_3_4_5_6_7_8_9_,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,70))

    def test071(self):
        """testcase 71"""
        input = """"'"TruongHoangNhat*...begin",##,???"""
        expect = "'\"TruongHoangNhat*...begin,,,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,71))

    def test072(self):
        """testcase 72"""
        input = """	

            ==	func
            >= var
            ...	break	not 105 <-	=	]	string "abcd" ] until	<
            begin ) "abcd" != continue


            "abcd" number >=	break var bool end , < break end	- 33.53e324	!= not

                ]
            string (
            bool [ number
            ==	(
            begin
            by	if -	if	>=
            24.69	false +	/ not continue	and ]	]
            <= end bool	<-	continue
            (
            bool else not ==
            begin for
            if true	=	func begin ...
            ( * or	for until elif	[
            ) for
        """
        expect = "\n,\n,==,func,\n,>=,var,\n,...,break,not,105,<-,=,],string,abcd,],until,<,\n,begin,),abcd,!=,continue,\n,\n,\n,abcd,number,>=,break,var,bool,end,,,<,break,end,-,33.53e324,!=,not,\n,\n,],\n,string,(,\n,bool,[,number,\n,==,(,\n,begin,\n,by,if,-,if,>=,\n,24.69,false,+,/,not,continue,and,],],\n,<=,end,bool,<-,continue,\n,(,\n,bool,else,not,==,\n,begin,for,\n,if,true,=,func,begin,...,\n,(,*,or,for,until,elif,[,\n,),for,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,72))

    def test073(self):
        """testcase 73"""
        input = """string str <-- "Testcase 73" ##String """
        expect = "string,str,<-,-,Testcase 73,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,73))

    def test074(self):
        """testcase 74"""
        input = r"""string str <-- "Testcase \74" ##Unclosed String """
        expect = "string,str,<-,-,Illegal Escape In String: Testcase \\7"
        self.assertTrue(TestLexer.test(input,expect,74))

    def test075(self):
        """testcase 75"""
        input = """string str <-- "Testcase
        75" ##Unclosed String """
        expect = "string,str,<-,-,Unclosed String: Testcase"
        self.assertTrue(TestLexer.test(input,expect,75))

    def test076(self):
        """testcase 76"""
        input = """76 Quang Ngai * 76X2-4288"""
        expect = "76,Quang,Ngai,*,76,X2,-,4288,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,76))

    def test077(self):
        """testcase 77"""
        input = """##,##,##,##,##,##,#,#,#,#,#,#,"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,77))

    def test078(self):
        """testcase 78"""
        input = """string str <---- "##Comment?'\""
        func begin          hello
                    2ee+33 cccc 00009.0004e-222
        ## Testcase 78"""
        expect = "string,str,<-,-,-,-,##Comment?'\",\n,func,begin,hello,\n,2,ee,+,33,cccc,00009.0004e-222,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,78))

    def test079(self):
        """testcase 79"""
        input = """Despacito
        Quiero respirar tu cuello despacito
        Deja que te diga cosas al oido
        Para que te acuerdes si no estas conmigo
        Despacito
        Quiero desnudarte a besos despacito
        Firmar las paredes de tu laberinto
        Y hacer de tu cuerpo todo un manuscrito (sube, sube, sube)"""
        expect = "Despacito,\n,Quiero,respirar,tu,cuello,despacito,\n,Deja,que,te,diga,cosas,al,oido,\n,Para,que,te,acuerdes,si,no,estas,conmigo,\n,Despacito,\n,Quiero,desnudarte,a,besos,despacito,\n,Firmar,las,paredes,de,tu,laberinto,\n,Y,hacer,de,tu,cuerpo,todo,un,manuscrito,(,sube,,,sube,,,sube,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,79))

    def test080(self):
        """testcase 80"""
        input = """4869aptx4869__aptx4869"""
        expect = "4869,aptx4869__aptx4869,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,80))

    def test081(self):
        """testcase 81"""
        input = """
        ##include <iostream>
        using namespace std;
        int main() {
            cout << "Hello, World!";
            return 0;
        }
        """
        expect = "\n,\n,using,namespace,std,Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,81))

    def test082(self):
        """testcase 82"""
        input = """
        func main()
        begin
            number a <- 5
            if (a < 10) print("a is less than 10")
            else print("a is greater than or equal to 10")
        end
        """
        expect = "\n,func,main,(,),\n,begin,\n,number,a,<-,5,\n,if,(,a,<,10,),print,(,a is less than 10,),\n,else,print,(,a is greater than or equal to 10,),\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,82))

    def test083(self):
        """testcase 83"""
        input = """begin end (---) + ///''"""
        expect = "begin,end,(,-,-,-,),+,/,/,/,Error Token '"
        self.assertTrue(TestLexer.test(input,expect,83))

    def test084(self):
        """testcase 84"""
        input = """eIosf/8{>"$,+qreturnPcHuntil.#%h]!=Xfuncw?;|DpL\3>=numbertz@(B`
        Tg*beginZ1Ghoangnhat0bool5&4A"""
        expect = "eIosf,/,8,Error Token {"
        self.assertTrue(TestLexer.test(input,expect,84))

    def test085(self):
        """testcase 85"""
        input = """number/string/bool-main/begin"""
        expect = "number,/,string,/,bool,-,main,/,begin,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,85))

    def test086(self):
        """testcase 86"""
        input = """10 e-10 22.e+3 3.eh2 0.000e0.1"""
        expect = "10,e,-,10,22.e+3,3.,eh2,0.000e0,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,86))

    def test087(self):
        """testcase 87"""
        input = """a + c - 9 + 0.02E0
        ________-----_______"""
        expect = "a,+,c,-,9,+,0.02E0,\n,________,-,-,-,-,-,_______,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,87))

    def test088(self):
        """testcase 88"""
        input = """"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,88))

    def test089(self):
        """testcase 89"""
        input = """dynamic b <- "nnnnn"/////////\\\\\\\\"""
        expect = "dynamic,b,<-,nnnnn,/,/,/,/,/,/,/,/,/,Error Token \\"
        self.assertTrue(TestLexer.test(input,expect,89))

    def test090(self):
        """testcase 90"""
        input = """C:\\Users\\minx\\OneDrive\\Documents\\Curriculums\\Junior\\HK232\\PPL\\Assignment\\Assignment_1\\assignment1\\src>"""
        expect = "C,Error Token :"
        self.assertTrue(TestLexer.test(input,expect,90))

    def test091(self):
        """testcase 91"""
        input = """,,,...,,,..."""
        expect = ",,,,,,...,,,,,,,...,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,91))

    def test092(self):
        """testcase 92"""
        input = """
            =	begin + dynamic 
            -	*
            return	/ - break
            = 14 return else return 
            <-
            or *	+	elif	string >	bool	continue	77E5776 a1 or
            <- == or continue	true /	continue	continue func
            string	break "abcd"
            >=	==
            until	-	/ bool	begin
            <- ( 
            ) ==	by
            and and	!=	if false
            a1 >=	<=	(
            %	not dynamic
            * until	continue
            for return	return	] <-	end	func <=	var or	> if	dynamic
            break	begin dynamic	continue	127e-6561	begin
        """
        expect = "\n,=,begin,+,dynamic,\n,-,*,\n,return,/,-,break,\n,=,14,return,else,return,\n,<-,\n,or,*,+,elif,string,>,bool,continue,77E5776,a1,or,\n,<-,==,or,continue,true,/,continue,continue,func,\n,string,break,abcd,\n,>=,==,\n,until,-,/,bool,begin,\n,<-,(,\n,),==,by,\n,and,and,!=,if,false,\n,a1,>=,<=,(,\n,%,not,dynamic,\n,*,until,continue,\n,for,return,return,],<-,end,func,<=,var,or,>,if,dynamic,\n,break,begin,dynamic,continue,127e-6561,begin,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,92))

    def test093(self):
        """testcase 93"""
        input = """([3[)33]433[45)(34)]]"""
        expect = "(,[,3,[,),33,],433,[,45,),(,34,),],],<EOF>"
        self.assertTrue(TestLexer.test(input,expect,93))

    def test094(self):
        """testcase 94"""
        input = """<EOF>"""
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,94))

    def test095(self):
        """testcase 95"""
        input = """ "Truong""Hoang""'""Nhat" """
        expect = "Truong,Hoang,'\",Nhat,Unclosed String:  "
        self.assertTrue(TestLexer.test(input,expect,95))

    def test096(self):
        """testcase 96"""
        input = """
        ######
        0101
        ######
        00010010
        """
        expect = "\n,\n,0101,\n,\n,00010010,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,96))

    def test097(self):
        """testcase 97"""
        input = """?kiytyw(36)__+hwe now"""
        expect = "Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,97))

    def test098(self):
        """testcase 98"""
        input = r""""Escape: \\ \' \n \"","""
        expect = "Illegal Escape In String: Escape: \\\\ \\' \\n \\\""
        self.assertTrue(TestLexer.test(input,expect,98))

    def test099(self):
        """testcase 99"""
        input = """
        test -> Lexer | Parser | AST | Semantic | CodeGen
        """
        expect = "\n,test,-,>,Lexer,Error Token |"
        self.assertTrue(TestLexer.test(input,expect,99))

    def test100(self):
        """testcase 100"""
        input = """This is the final testcase, I hope it will pass all the tests and I will get 10/10 for this assignment"""
        expect = "This,is,the,final,testcase,,,I,hope,it,will,pass,all,the,tests,and,I,will,get,10,/,10,for,this,assignment,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))