# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u01da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\5\2t\n")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3}\n\3\3\4\3\4\3\4\3")
        buf.write("\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\5\6\u0089\n\6\3\7\3\7")
        buf.write("\3\7\5\7\u008e\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u0097")
        buf.write("\n\t\3\t\5\t\u009a\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\5\13\u00a5\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00ac\n")
        buf.write("\f\3\r\3\r\3\r\5\r\u00b1\n\r\3\16\5\16\u00b4\n\16\3\16")
        buf.write("\3\16\5\16\u00b8\n\16\3\16\3\16\5\16\u00bc\n\16\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00c2\n\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\5\21\u00c9\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00d4\n\22\3\23\3\23\3\23\5\23\u00d9\n\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u00e0\n\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00e9\n\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00f0\n\23\3\24\3\24\3\24\3\24\5\24\u00f6")
        buf.write("\n\24\3\24\3\24\3\25\3\25\3\25\5\25\u00fd\n\25\3\25\3")
        buf.write("\25\3\26\3\26\5\26\u0103\n\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\5\31\u010e\n\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u0119\n\32\3\33\3\33")
        buf.write("\3\33\5\33\u011e\n\33\3\33\3\33\3\34\3\34\3\34\5\34\u0125")
        buf.write("\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0134\n\36\3\36\3\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u013f\n\37\3\37\3\37\3 \3")
        buf.write(" \3!\3!\3\"\3\"\5\"\u0149\n\"\3#\3#\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\5%\u0158\n%\3&\3&\5&\u015c\n&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\5\'\u0163\n\'\3(\3(\3(\3(\3(\5(\u016a\n(")
        buf.write("\3)\3)\3)\3)\3)\5)\u0171\n)\3*\3*\3*\3*\3*\3*\7*\u0179")
        buf.write("\n*\f*\16*\u017c\13*\3+\3+\3+\3+\3+\3+\7+\u0184\n+\f+")
        buf.write("\16+\u0187\13+\3,\3,\3,\3,\3,\3,\7,\u018f\n,\f,\16,\u0192")
        buf.write("\13,\3-\3-\3-\5-\u0197\n-\3.\3.\3.\5.\u019c\n.\3/\3/\5")
        buf.write("/\u01a0\n/\3\60\3\60\5\60\u01a4\n\60\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01b1\n\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\5\65\u01c4\n\65\3\66\3")
        buf.write("\66\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u01ce\n\67\38\3")
        buf.write("8\38\38\39\39\39\39\59\u01d8\n9\39\2\5RTV:\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnp\2\7\5\2\34\34\36\"$$\3\2\25")
        buf.write("\26\3\2\27\30\3\2\31\33\3\2\3\5\2\u01de\2s\3\2\2\2\4|")
        buf.write("\3\2\2\2\6~\3\2\2\2\b\u0083\3\2\2\2\n\u0088\3\2\2\2\f")
        buf.write("\u008a\3\2\2\2\16\u008f\3\2\2\2\20\u0093\3\2\2\2\22\u009b")
        buf.write("\3\2\2\2\24\u00a4\3\2\2\2\26\u00ab\3\2\2\2\30\u00ad\3")
        buf.write("\2\2\2\32\u00bb\3\2\2\2\34\u00c1\3\2\2\2\36\u00c3\3\2")
        buf.write("\2\2 \u00c8\3\2\2\2\"\u00d3\3\2\2\2$\u00ef\3\2\2\2&\u00f1")
        buf.write("\3\2\2\2(\u00f9\3\2\2\2*\u0102\3\2\2\2,\u0104\3\2\2\2")
        buf.write(".\u0107\3\2\2\2\60\u010a\3\2\2\2\62\u0118\3\2\2\2\64\u011a")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u0128\3\2\2\2:\u012c\3\2\2")
        buf.write("\2<\u0137\3\2\2\2>\u0142\3\2\2\2@\u0144\3\2\2\2B\u0146")
        buf.write("\3\2\2\2D\u014a\3\2\2\2F\u014f\3\2\2\2H\u0157\3\2\2\2")
        buf.write("J\u015b\3\2\2\2L\u0162\3\2\2\2N\u0169\3\2\2\2P\u0170\3")
        buf.write("\2\2\2R\u0172\3\2\2\2T\u017d\3\2\2\2V\u0188\3\2\2\2X\u0196")
        buf.write("\3\2\2\2Z\u019b\3\2\2\2\\\u019f\3\2\2\2^\u01a3\3\2\2\2")
        buf.write("`\u01b0\3\2\2\2b\u01b2\3\2\2\2d\u01b7\3\2\2\2f\u01bc\3")
        buf.write("\2\2\2h\u01c3\3\2\2\2j\u01c5\3\2\2\2l\u01cd\3\2\2\2n\u01cf")
        buf.write("\3\2\2\2p\u01d7\3\2\2\2rt\5H%\2sr\3\2\2\2st\3\2\2\2tu")
        buf.write("\3\2\2\2uv\5\4\3\2vw\7\2\2\3w\3\3\2\2\2xy\5\6\4\2yz\5")
        buf.write("\4\3\2z}\3\2\2\2{}\5\6\4\2|x\3\2\2\2|{\3\2\2\2}\5\3\2")
        buf.write("\2\2~\177\5\b\5\2\177\u0080\5H%\2\u0080\7\3\2\2\2\u0081")
        buf.write("\u0084\5\n\6\2\u0082\u0084\5\22\n\2\u0083\u0081\3\2\2")
        buf.write("\2\u0083\u0082\3\2\2\2\u0084\t\3\2\2\2\u0085\u0089\5\20")
        buf.write("\t\2\u0086\u0089\5\16\b\2\u0087\u0089\5\f\7\2\u0088\u0085")
        buf.write("\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\13\3\2\2\2\u008a\u008b\7\b\2\2\u008b\u008d\7-\2\2\u008c")
        buf.write("\u008e\5.\30\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\r\3\2\2\2\u008f\u0090\7\7\2\2\u0090\u0091\7-\2")
        buf.write("\2\u0091\u0092\5.\30\2\u0092\17\3\2\2\2\u0093\u0094\5")
        buf.write("f\64\2\u0094\u0096\7-\2\2\u0095\u0097\5n8\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u009a\5.\30\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\21\3\2\2\2\u009b\u009c\7\t\2\2\u009c\u009d\7-\2")
        buf.write("\2\u009d\u009e\7%\2\2\u009e\u009f\5\24\13\2\u009f\u00a0")
        buf.write("\7&\2\2\u00a0\u00a1\5\32\16\2\u00a1\23\3\2\2\2\u00a2\u00a5")
        buf.write("\5\26\f\2\u00a3\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\25\3\2\2\2\u00a6\u00a7\5\30\r\2\u00a7")
        buf.write("\u00a8\7)\2\2\u00a8\u00a9\5\26\f\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00ac\5\30\r\2\u00ab\u00a6\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\27\3\2\2\2\u00ad\u00ae\5f\64\2\u00ae\u00b0")
        buf.write("\7-\2\2\u00af\u00b1\5n8\2\u00b0\u00af\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\31\3\2\2\2\u00b2\u00b4\5H%\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00bc\5B\"\2\u00b6\u00b8\5H%\2\u00b7\u00b6\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bc\5F$\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b3\3\2\2\2\u00bb\u00b7\3\2\2\2")
        buf.write("\u00bb\u00ba\3\2\2\2\u00bc\33\3\2\2\2\u00bd\u00be\5\36")
        buf.write("\20\2\u00be\u00bf\5\34\17\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00c2\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c2\35\3\2\2\2\u00c3\u00c4\5 \21\2\u00c4\u00c5\5H%")
        buf.write("\2\u00c5\37\3\2\2\2\u00c6\u00c9\5\"\22\2\u00c7\u00c9\5")
        buf.write("$\23\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9!")
        buf.write("\3\2\2\2\u00ca\u00d4\5\n\6\2\u00cb\u00d4\5,\27\2\u00cc")
        buf.write("\u00d4\5\60\31\2\u00cd\u00d4\5:\36\2\u00ce\u00d4\5> \2")
        buf.write("\u00cf\u00d4\5@!\2\u00d0\u00d4\5B\"\2\u00d1\u00d4\5D#")
        buf.write("\2\u00d2\u00d4\5F$\2\u00d3\u00ca\3\2\2\2\u00d3\u00cb\3")
        buf.write("\2\2\2\u00d3\u00cc\3\2\2\2\u00d3\u00cd\3\2\2\2\u00d3\u00ce")
        buf.write("\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4#\3\2\2\2\u00d5")
        buf.write("\u00d6\7\17\2\2\u00d6\u00d8\58\35\2\u00d7\u00d9\5H%\2")
        buf.write("\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\3")
        buf.write("\2\2\2\u00da\u00db\5 \21\2\u00db\u00f0\3\2\2\2\u00dc\u00dd")
        buf.write("\7\17\2\2\u00dd\u00df\58\35\2\u00de\u00e0\5H%\2\u00df")
        buf.write("\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\5\"\22\2\u00e2\u00e3\5\62\32\2\u00e3\u00e4")
        buf.write("\5&\24\2\u00e4\u00f0\3\2\2\2\u00e5\u00e6\7\17\2\2\u00e6")
        buf.write("\u00e8\58\35\2\u00e7\u00e9\5H%\2\u00e8\u00e7\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\5\"\22")
        buf.write("\2\u00eb\u00ec\5\62\32\2\u00ec\u00ed\5(\25\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00f0\5<\37\2\u00ef\u00d5\3\2\2\2\u00ef")
        buf.write("\u00dc\3\2\2\2\u00ef\u00e5\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0%\3\2\2\2\u00f1\u00f2\5H%\2\u00f2\u00f3\7\21\2\2")
        buf.write("\u00f3\u00f5\58\35\2\u00f4\u00f6\5H%\2\u00f5\u00f4\3\2")
        buf.write("\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8")
        buf.write("\5 \21\2\u00f8\'\3\2\2\2\u00f9\u00fa\5H%\2\u00fa\u00fc")
        buf.write("\7\20\2\2\u00fb\u00fd\5H%\2\u00fc\u00fb\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\5$\23\2")
        buf.write("\u00ff)\3\2\2\2\u0100\u0103\7-\2\2\u0101\u0103\5d\63\2")
        buf.write("\u0102\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103+\3\2\2")
        buf.write("\2\u0104\u0105\5*\26\2\u0105\u0106\5.\30\2\u0106-\3\2")
        buf.write("\2\2\u0107\u0108\7\35\2\2\u0108\u0109\5N(\2\u0109/\3\2")
        buf.write("\2\2\u010a\u010b\7\17\2\2\u010b\u010d\58\35\2\u010c\u010e")
        buf.write("\5H%\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\u0110\5\"\22\2\u0110\u0111\5\62\32\2\u0111")
        buf.write("\u0112\5\66\34\2\u0112\61\3\2\2\2\u0113\u0114\5H%\2\u0114")
        buf.write("\u0115\5\64\33\2\u0115\u0116\5\62\32\2\u0116\u0119\3\2")
        buf.write("\2\2\u0117\u0119\3\2\2\2\u0118\u0113\3\2\2\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119\63\3\2\2\2\u011a\u011b\7\21\2\2\u011b\u011d")
        buf.write("\58\35\2\u011c\u011e\5H%\2\u011d\u011c\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\5\"\22\2\u0120")
        buf.write("\65\3\2\2\2\u0121\u0122\5H%\2\u0122\u0124\7\20\2\2\u0123")
        buf.write("\u0125\5H%\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0127\5\"\22\2\u0127\67\3\2\2\2\u0128")
        buf.write("\u0129\7%\2\2\u0129\u012a\5N(\2\u012a\u012b\7&\2\2\u012b")
        buf.write("9\3\2\2\2\u012c\u012d\7\n\2\2\u012d\u012e\7-\2\2\u012e")
        buf.write("\u012f\7\13\2\2\u012f\u0130\5N(\2\u0130\u0131\7\f\2\2")
        buf.write("\u0131\u0133\5N(\2\u0132\u0134\5H%\2\u0133\u0132\3\2\2")
        buf.write("\2\u0133\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136")
        buf.write("\5\"\22\2\u0136;\3\2\2\2\u0137\u0138\7\n\2\2\u0138\u0139")
        buf.write("\7-\2\2\u0139\u013a\7\13\2\2\u013a\u013b\5N(\2\u013b\u013c")
        buf.write("\7\f\2\2\u013c\u013e\5N(\2\u013d\u013f\5H%\2\u013e\u013d")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0141\5$\23\2\u0141=\3\2\2\2\u0142\u0143\7\r\2\2\u0143")
        buf.write("?\3\2\2\2\u0144\u0145\7\16\2\2\u0145A\3\2\2\2\u0146\u0148")
        buf.write("\7\6\2\2\u0147\u0149\5N(\2\u0148\u0147\3\2\2\2\u0148\u0149")
        buf.write("\3\2\2\2\u0149C\3\2\2\2\u014a\u014b\7-\2\2\u014b\u014c")
        buf.write("\7%\2\2\u014c\u014d\5J&\2\u014d\u014e\7&\2\2\u014eE\3")
        buf.write("\2\2\2\u014f\u0150\7\22\2\2\u0150\u0151\5H%\2\u0151\u0152")
        buf.write("\5\34\17\2\u0152\u0153\7\23\2\2\u0153G\3\2\2\2\u0154\u0155")
        buf.write("\7.\2\2\u0155\u0158\5H%\2\u0156\u0158\7.\2\2\u0157\u0154")
        buf.write("\3\2\2\2\u0157\u0156\3\2\2\2\u0158I\3\2\2\2\u0159\u015c")
        buf.write("\5L\'\2\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015cK\3\2\2\2\u015d\u015e\5N(\2\u015e")
        buf.write("\u015f\7)\2\2\u015f\u0160\5L\'\2\u0160\u0163\3\2\2\2\u0161")
        buf.write("\u0163\5N(\2\u0162\u015d\3\2\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("M\3\2\2\2\u0164\u0165\5P)\2\u0165\u0166\7#\2\2\u0166\u0167")
        buf.write("\5P)\2\u0167\u016a\3\2\2\2\u0168\u016a\5P)\2\u0169\u0164")
        buf.write("\3\2\2\2\u0169\u0168\3\2\2\2\u016aO\3\2\2\2\u016b\u016c")
        buf.write("\5R*\2\u016c\u016d\t\2\2\2\u016d\u016e\5R*\2\u016e\u0171")
        buf.write("\3\2\2\2\u016f\u0171\5R*\2\u0170\u016b\3\2\2\2\u0170\u016f")
        buf.write("\3\2\2\2\u0171Q\3\2\2\2\u0172\u0173\b*\1\2\u0173\u0174")
        buf.write("\5T+\2\u0174\u017a\3\2\2\2\u0175\u0176\f\4\2\2\u0176\u0177")
        buf.write("\t\3\2\2\u0177\u0179\5T+\2\u0178\u0175\3\2\2\2\u0179\u017c")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("S\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\b+\1\2\u017e")
        buf.write("\u017f\5V,\2\u017f\u0185\3\2\2\2\u0180\u0181\f\4\2\2\u0181")
        buf.write("\u0182\t\4\2\2\u0182\u0184\5V,\2\u0183\u0180\3\2\2\2\u0184")
        buf.write("\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186U\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u0189\b,\1\2")
        buf.write("\u0189\u018a\5X-\2\u018a\u0190\3\2\2\2\u018b\u018c\f\4")
        buf.write("\2\2\u018c\u018d\t\5\2\2\u018d\u018f\5X-\2\u018e\u018b")
        buf.write("\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191W\3\2\2\2\u0192\u0190\3\2\2\2\u0193")
        buf.write("\u0194\7\24\2\2\u0194\u0197\5X-\2\u0195\u0197\5Z.\2\u0196")
        buf.write("\u0193\3\2\2\2\u0196\u0195\3\2\2\2\u0197Y\3\2\2\2\u0198")
        buf.write("\u0199\7\30\2\2\u0199\u019c\5Z.\2\u019a\u019c\5\\/\2\u019b")
        buf.write("\u0198\3\2\2\2\u019b\u019a\3\2\2\2\u019c[\3\2\2\2\u019d")
        buf.write("\u01a0\5^\60\2\u019e\u01a0\5`\61\2\u019f\u019d\3\2\2\2")
        buf.write("\u019f\u019e\3\2\2\2\u01a0]\3\2\2\2\u01a1\u01a4\7-\2\2")
        buf.write("\u01a2\u01a4\5b\62\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3")
        buf.write("\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7\'\2\2\u01a6\u01a7")
        buf.write("\5h\65\2\u01a7\u01a8\7(\2\2\u01a8_\3\2\2\2\u01a9\u01b1")
        buf.write("\7-\2\2\u01aa\u01b1\5p9\2\u01ab\u01b1\5b\62\2\u01ac\u01ad")
        buf.write("\7%\2\2\u01ad\u01ae\5N(\2\u01ae\u01af\7&\2\2\u01af\u01b1")
        buf.write("\3\2\2\2\u01b0\u01a9\3\2\2\2\u01b0\u01aa\3\2\2\2\u01b0")
        buf.write("\u01ab\3\2\2\2\u01b0\u01ac\3\2\2\2\u01b1a\3\2\2\2\u01b2")
        buf.write("\u01b3\7-\2\2\u01b3\u01b4\7%\2\2\u01b4\u01b5\5J&\2\u01b5")
        buf.write("\u01b6\7&\2\2\u01b6c\3\2\2\2\u01b7\u01b8\7-\2\2\u01b8")
        buf.write("\u01b9\7\'\2\2\u01b9\u01ba\5h\65\2\u01ba\u01bb\7(\2\2")
        buf.write("\u01bbe\3\2\2\2\u01bc\u01bd\t\6\2\2\u01bdg\3\2\2\2\u01be")
        buf.write("\u01bf\5N(\2\u01bf\u01c0\7)\2\2\u01c0\u01c1\5h\65\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c4\5N(\2\u01c3\u01be\3\2\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4i\3\2\2\2\u01c5\u01c6\7\'\2\2\u01c6")
        buf.write("\u01c7\5L\'\2\u01c7\u01c8\7(\2\2\u01c8k\3\2\2\2\u01c9")
        buf.write("\u01ca\7*\2\2\u01ca\u01cb\7)\2\2\u01cb\u01ce\5l\67\2\u01cc")
        buf.write("\u01ce\7*\2\2\u01cd\u01c9\3\2\2\2\u01cd\u01cc\3\2\2\2")
        buf.write("\u01cem\3\2\2\2\u01cf\u01d0\7\'\2\2\u01d0\u01d1\5l\67")
        buf.write("\2\u01d1\u01d2\7(\2\2\u01d2o\3\2\2\2\u01d3\u01d8\7*\2")
        buf.write("\2\u01d4\u01d8\7,\2\2\u01d5\u01d8\7+\2\2\u01d6\u01d8\5")
        buf.write("j\66\2\u01d7\u01d3\3\2\2\2\u01d7\u01d4\3\2\2\2\u01d7\u01d5")
        buf.write("\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8q\3\2\2\2\60s|\u0083")
        buf.write("\u0088\u008d\u0096\u0099\u00a4\u00ab\u00b0\u00b3\u00b7")
        buf.write("\u00bb\u00c1\u00c8\u00d3\u00d8\u00df\u00e8\u00ef\u00f5")
        buf.write("\u00fc\u0102\u010d\u0118\u011d\u0124\u0133\u013e\u0148")
        buf.write("\u0157\u015b\u0162\u0169\u0170\u017a\u0185\u0190\u0196")
        buf.write("\u019b\u019f\u01a3\u01b0\u01c3\u01cd\u01d7")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'return'", 
                     "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", 
                     "')'", "'['", "']'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "BOOL", "STRING", "RETURN", 
                      "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "EQ", "ASSIGN", "NEQ", "LESS", "LEQ", "GREATER", "GEQ", 
                      "CONCAT", "STR_EQ", "LP", "RP", "LSB", "RSB", "CM", 
                      "NUM_LIT", "BOOL_LIT", "STR_LIT", "ID", "NEWLINE", 
                      "WS", "COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl_mem = 2
    RULE_decl = 3
    RULE_var_decl = 4
    RULE_dyn_decl = 5
    RULE_v_decl = 6
    RULE_type_decl = 7
    RULE_func_decl = 8
    RULE_param_list = 9
    RULE_param_prime = 10
    RULE_param = 11
    RULE_func_body = 12
    RULE_stmt_list = 13
    RULE_stmt_mem = 14
    RULE_stmt = 15
    RULE_match_stmt = 16
    RULE_unmatch_stmt = 17
    RULE_elif_stmt = 18
    RULE_else_unmatch_stmt = 19
    RULE_lhs = 20
    RULE_assign_stmt = 21
    RULE_as_expr = 22
    RULE_if_match_stmt = 23
    RULE_elif_match_list = 24
    RULE_elif_match_stmt = 25
    RULE_else_match_stmt = 26
    RULE_cond_expr = 27
    RULE_for_stmt = 28
    RULE_for_unmatch_stmt = 29
    RULE_break_stmt = 30
    RULE_continue_stmt = 31
    RULE_return_stmt = 32
    RULE_func_call_stmt = 33
    RULE_block_stmt = 34
    RULE_newline_list = 35
    RULE_expr_list = 36
    RULE_expr_prime = 37
    RULE_expr = 38
    RULE_rel_expr = 39
    RULE_and_expr = 40
    RULE_add_expr = 41
    RULE_mul_expr = 42
    RULE_not_expr = 43
    RULE_sign_expr = 44
    RULE_idx_expr = 45
    RULE_elem_expr = 46
    RULE_operand = 47
    RULE_func_call_expr = 48
    RULE_arr_elem = 49
    RULE_types = 50
    RULE_idx_op = 51
    RULE_arr_lit = 52
    RULE_dim_list = 53
    RULE_arr_dim = 54
    RULE_literal = 55

    ruleNames =  [ "program", "decl_list", "decl_mem", "decl", "var_decl", 
                   "dyn_decl", "v_decl", "type_decl", "func_decl", "param_list", 
                   "param_prime", "param", "func_body", "stmt_list", "stmt_mem", 
                   "stmt", "match_stmt", "unmatch_stmt", "elif_stmt", "else_unmatch_stmt", 
                   "lhs", "assign_stmt", "as_expr", "if_match_stmt", "elif_match_list", 
                   "elif_match_stmt", "else_match_stmt", "cond_expr", "for_stmt", 
                   "for_unmatch_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "func_call_stmt", "block_stmt", "newline_list", "expr_list", 
                   "expr_prime", "expr", "rel_expr", "and_expr", "add_expr", 
                   "mul_expr", "not_expr", "sign_expr", "idx_expr", "elem_expr", 
                   "operand", "func_call_expr", "arr_elem", "types", "idx_op", 
                   "arr_lit", "dim_list", "arr_dim", "literal" ]

    EOF = Token.EOF
    NUMBER=1
    BOOL=2
    STRING=3
    RETURN=4
    VAR=5
    DYNAMIC=6
    FUNC=7
    FOR=8
    UNTIL=9
    BY=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSE=14
    ELIF=15
    BEGIN=16
    END=17
    NOT=18
    AND=19
    OR=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    ASSIGN=27
    NEQ=28
    LESS=29
    LEQ=30
    GREATER=31
    GEQ=32
    CONCAT=33
    STR_EQ=34
    LP=35
    RP=36
    LSB=37
    RSB=38
    CM=39
    NUM_LIT=40
    BOOL_LIT=41
    STR_LIT=42
    ID=43
    NEWLINE=44
    WS=45
    COMMENT=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    ERROR_TOKEN=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 112
                self.newline_list()


            self.state = 115
            self.decl_list()
            self.state = 116
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_mem(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_memContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.decl_mem()
                self.state = 119
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.decl_mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_mem" ):
                return visitor.visitDecl_mem(self)
            else:
                return visitor.visitChildren(self)




    def decl_mem(self):

        localctx = ZCodeParser.Decl_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.decl()
            self.state = 125
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.var_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.func_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Type_declContext,0)


        def v_decl(self):
            return self.getTypedRuleContext(ZCodeParser.V_declContext,0)


        def dyn_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Dyn_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.type_decl()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.v_decl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.dyn_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dyn_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def as_expr(self):
            return self.getTypedRuleContext(ZCodeParser.As_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dyn_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDyn_decl" ):
                return visitor.visitDyn_decl(self)
            else:
                return visitor.visitChildren(self)




    def dyn_decl(self):

        localctx = ZCodeParser.Dyn_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dyn_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ZCodeParser.DYNAMIC)
            self.state = 137
            self.match(ZCodeParser.ID)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 138
                self.as_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def as_expr(self):
            return self.getTypedRuleContext(ZCodeParser.As_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_v_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitV_decl" ):
                return visitor.visitV_decl(self)
            else:
                return visitor.visitChildren(self)




    def v_decl(self):

        localctx = ZCodeParser.V_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_v_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.VAR)
            self.state = 142
            self.match(ZCodeParser.ID)
            self.state = 143
            self.as_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(ZCodeParser.TypesContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def arr_dim(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_dimContext,0)


        def as_expr(self):
            return self.getTypedRuleContext(ZCodeParser.As_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_type_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = ZCodeParser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.types()
            self.state = 146
            self.match(ZCodeParser.ID)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 147
                self.arr_dim()


            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 150
                self.as_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.FUNC)
            self.state = 154
            self.match(ZCodeParser.ID)
            self.state = 155
            self.match(ZCodeParser.LP)
            self.state = 156
            self.param_list()
            self.state = 157
            self.match(ZCodeParser.RP)
            self.state = 158
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.param_prime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_prime" ):
                return visitor.visitParam_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_prime)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.param()
                self.state = 165
                self.match(ZCodeParser.CM)
                self.state = 166
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(ZCodeParser.TypesContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def arr_dim(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_dimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.types()
            self.state = 172
            self.match(ZCodeParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 173
                self.arr_dim()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 176
                    self.newline_list()


                self.state = 179
                self.return_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 180
                    self.newline_list()


                self.state = 183
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_mem(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_memContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_list)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.stmt_mem()
                self.state = 188
                self.stmt_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_mem" ):
                return visitor.visitStmt_mem(self)
            else:
                return visitor.visitChildren(self)




    def stmt_mem(self):

        localctx = ZCodeParser.Stmt_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.stmt()
            self.state = 194
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_stmtContext,0)


        def unmatch_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Unmatch_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.unmatch_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Match_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_match_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_match_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch_stmt" ):
                return visitor.visitMatch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def match_stmt(self):

        localctx = ZCodeParser.Match_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_match_stmt)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.if_match_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.func_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 208
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unmatch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def cond_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_exprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_stmtContext,0)


        def elif_match_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_match_listContext,0)


        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def else_unmatch_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_unmatch_stmtContext,0)


        def for_unmatch_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_unmatch_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_unmatch_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnmatch_stmt" ):
                return visitor.visitUnmatch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def unmatch_stmt(self):

        localctx = ZCodeParser.Unmatch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unmatch_stmt)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(ZCodeParser.IF)
                self.state = 212
                self.cond_expr()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 213
                    self.newline_list()


                self.state = 216
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(ZCodeParser.IF)
                self.state = 219
                self.cond_expr()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 220
                    self.newline_list()


                self.state = 223
                self.match_stmt()
                self.state = 224
                self.elif_match_list()
                self.state = 225
                self.elif_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(ZCodeParser.IF)
                self.state = 228
                self.cond_expr()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 229
                    self.newline_list()


                self.state = 232
                self.match_stmt()
                self.state = 233
                self.elif_match_list()
                self.state = 234
                self.else_unmatch_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.for_unmatch_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def cond_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_exprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.newline_list()
            self.state = 240
            self.match(ZCodeParser.ELIF)
            self.state = 241
            self.cond_expr()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 242
                self.newline_list()


            self.state = 245
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_unmatch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def unmatch_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Unmatch_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_unmatch_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_unmatch_stmt" ):
                return visitor.visitElse_unmatch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_unmatch_stmt(self):

        localctx = ZCodeParser.Else_unmatch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_else_unmatch_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.newline_list()
            self.state = 248
            self.match(ZCodeParser.ELSE)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 249
                self.newline_list()


            self.state = 252
            self.unmatch_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def arr_elem(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_elemContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.arr_elem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def as_expr(self):
            return self.getTypedRuleContext(ZCodeParser.As_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.lhs()
            self.state = 259
            self.as_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_as_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAs_expr" ):
                return visitor.visitAs_expr(self)
            else:
                return visitor.visitChildren(self)




    def as_expr(self):

        localctx = ZCodeParser.As_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_as_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ZCodeParser.ASSIGN)
            self.state = 262
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_match_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def cond_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_exprContext,0)


        def match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_stmtContext,0)


        def elif_match_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_match_listContext,0)


        def else_match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_match_stmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_match_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_match_stmt" ):
                return visitor.visitIf_match_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_match_stmt(self):

        localctx = ZCodeParser.If_match_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_match_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ZCodeParser.IF)
            self.state = 265
            self.cond_expr()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 266
                self.newline_list()


            self.state = 269
            self.match_stmt()
            self.state = 270
            self.elif_match_list()
            self.state = 271
            self.else_match_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_match_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def elif_match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_match_stmtContext,0)


        def elif_match_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_match_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_match_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_match_list" ):
                return visitor.visitElif_match_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_match_list(self):

        localctx = ZCodeParser.Elif_match_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elif_match_list)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.newline_list()
                self.state = 274
                self.elif_match_stmt()
                self.state = 275
                self.elif_match_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_match_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def cond_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Cond_exprContext,0)


        def match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_stmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_match_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_match_stmt" ):
                return visitor.visitElif_match_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_match_stmt(self):

        localctx = ZCodeParser.Elif_match_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elif_match_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.ELIF)
            self.state = 281
            self.cond_expr()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 282
                self.newline_list()


            self.state = 285
            self.match_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_match_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_match_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_match_stmt" ):
                return visitor.visitElse_match_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_match_stmt(self):

        localctx = ZCodeParser.Else_match_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_else_match_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.newline_list()
            self.state = 288
            self.match(ZCodeParser.ELSE)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 289
                self.newline_list()


            self.state = 292
            self.match_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_cond_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_expr" ):
                return visitor.visitCond_expr(self)
            else:
                return visitor.visitChildren(self)




    def cond_expr(self):

        localctx = ZCodeParser.Cond_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_cond_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.LP)
            self.state = 295
            self.expr()
            self.state = 296
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def match_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_stmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(ZCodeParser.FOR)
            self.state = 299
            self.match(ZCodeParser.ID)
            self.state = 300
            self.match(ZCodeParser.UNTIL)
            self.state = 301
            self.expr()
            self.state = 302
            self.match(ZCodeParser.BY)
            self.state = 303
            self.expr()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 304
                self.newline_list()


            self.state = 307
            self.match_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_unmatch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def unmatch_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Unmatch_stmtContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_unmatch_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_unmatch_stmt" ):
                return visitor.visitFor_unmatch_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_unmatch_stmt(self):

        localctx = ZCodeParser.For_unmatch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_unmatch_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZCodeParser.FOR)
            self.state = 310
            self.match(ZCodeParser.ID)
            self.state = 311
            self.match(ZCodeParser.UNTIL)
            self.state = 312
            self.expr()
            self.state = 313
            self.match(ZCodeParser.BY)
            self.state = 314
            self.expr()
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 315
                self.newline_list()


            self.state = 318
            self.unmatch_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.RETURN)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.STR_LIT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 325
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(ZCodeParser.ID)
            self.state = 329
            self.match(ZCodeParser.LP)
            self.state = 330
            self.expr_list()
            self.state = 331
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.BEGIN)
            self.state = 334
            self.newline_list()
            self.state = 335
            self.stmt_list()
            self.state = 336
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_newline_list)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(ZCodeParser.NEWLINE)
                self.state = 339
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr_list)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.expr_prime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_prime" ):
                return visitor.visitExpr_prime(self)
            else:
                return visitor.visitChildren(self)




    def expr_prime(self):

        localctx = ZCodeParser.Expr_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr_prime)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.expr()
                self.state = 348
                self.match(ZCodeParser.CM)
                self.state = 349
                self.expr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Rel_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Rel_exprContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.rel_expr()
                self.state = 355
                self.match(ZCodeParser.CONCAT)
                self.state = 356
                self.rel_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.rel_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.And_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.And_exprContext,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def STR_EQ(self):
            return self.getToken(ZCodeParser.STR_EQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LEQ(self):
            return self.getToken(ZCodeParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(ZCodeParser.GEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_rel_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_expr" ):
                return visitor.visitRel_expr(self)
            else:
                return visitor.visitChildren(self)




    def rel_expr(self):

        localctx = ZCodeParser.Rel_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_rel_expr)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.and_expr(0)
                self.state = 362
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LEQ) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GEQ) | (1 << ZCodeParser.STR_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.and_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.and_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(ZCodeParser.And_exprContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_and_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 373
                    self.add_expr(0) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 382
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 383
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 384
                    self.mul_expr(0) 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Not_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_exprContext,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_mul_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 393
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 394
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 395
                    self.not_expr() 
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def not_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Not_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_not_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expr" ):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)




    def not_expr(self):

        localctx = ZCodeParser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_not_expr)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(ZCodeParser.NOT)
                self.state = 402
                self.not_expr()
                pass
            elif token in [ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def idx_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_sign_expr)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(ZCodeParser.SUB)
                self.state = 407
                self.sign_expr()
                pass
            elif token in [ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.idx_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Elem_exprContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idx_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_expr" ):
                return visitor.visitIdx_expr(self)
            else:
                return visitor.visitChildren(self)




    def idx_expr(self):

        localctx = ZCodeParser.Idx_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_idx_expr)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.elem_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elem_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def idx_op(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elem_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem_expr" ):
                return visitor.visitElem_expr(self)
            else:
                return visitor.visitChildren(self)




    def elem_expr(self):

        localctx = ZCodeParser.Elem_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elem_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 415
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 416
                self.func_call_expr()
                pass


            self.state = 419
            self.match(ZCodeParser.LSB)
            self.state = 420
            self.idx_op()
            self.state = 421
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_operand)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.func_call_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
                self.match(ZCodeParser.LP)
                self.state = 427
                self.expr()
                self.state = 428
                self.match(ZCodeParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_expr" ):
                return visitor.visitFunc_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def func_call_expr(self):

        localctx = ZCodeParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(ZCodeParser.ID)
            self.state = 433
            self.match(ZCodeParser.LP)
            self.state = 434
            self.expr_list()
            self.state = 435
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def idx_op(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem" ):
                return visitor.visitArr_elem(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem(self):

        localctx = ZCodeParser.Arr_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arr_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(ZCodeParser.ID)
            self.state = 438
            self.match(ZCodeParser.LSB)
            self.state = 439
            self.idx_op()
            self.state = 440
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = ZCodeParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def idx_op(self):
            return self.getTypedRuleContext(ZCodeParser.Idx_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idx_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_op" ):
                return visitor.visitIdx_op(self)
            else:
                return visitor.visitChildren(self)




    def idx_op(self):

        localctx = ZCodeParser.Idx_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_idx_op)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.expr()
                self.state = 445
                self.match(ZCodeParser.CM)
                self.state = 446
                self.idx_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = ZCodeParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.LSB)
            self.state = 452
            self.expr_prime()
            self.state = 453
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def dim_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dim_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_list" ):
                return visitor.visitDim_list(self)
            else:
                return visitor.visitChildren(self)




    def dim_list(self):

        localctx = ZCodeParser.Dim_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_dim_list)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(ZCodeParser.NUM_LIT)
                self.state = 456
                self.match(ZCodeParser.CM)
                self.state = 457
                self.dim_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_dimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def dim_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_listContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim" ):
                return visitor.visitArr_dim(self)
            else:
                return visitor.visitChildren(self)




    def arr_dim(self):

        localctx = ZCodeParser.Arr_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arr_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(ZCodeParser.LSB)
            self.state = 462
            self.dim_list()
            self.state = 463
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(ZCodeParser.STR_LIT)
                pass
            elif token in [ZCodeParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
                self.arr_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[40] = self.and_expr_sempred
        self._predicates[41] = self.add_expr_sempred
        self._predicates[42] = self.mul_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




