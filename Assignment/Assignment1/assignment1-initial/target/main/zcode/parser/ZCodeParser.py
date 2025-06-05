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
        buf.write("\u01cc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\5\2r\n\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3{\n\3\3\4\3\4\3\4\3\5\3\5")
        buf.write("\5\5\u0082\n\5\3\6\3\6\3\6\5\6\u0087\n\6\3\7\3\7\3\7\5")
        buf.write("\7\u008c\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u0095\n\t")
        buf.write("\3\t\5\t\u0098\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\5\13\u00a3\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00aa\n\f")
        buf.write("\3\r\3\r\3\r\5\r\u00af\n\r\3\16\5\16\u00b2\n\16\3\16\3")
        buf.write("\16\5\16\u00b6\n\16\3\16\3\16\5\16\u00ba\n\16\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c0\n\17\3\20\3\20\3\20\3\21\3\21\5")
        buf.write("\21\u00c7\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00d2\n\22\3\23\3\23\3\23\5\23\u00d7\n\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00de\n\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00e7\n\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00ed\n\23\3\24\3\24\3\24\3\24\5\24\u00f3\n\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\5\25\u00fa\n\25\3\25\3\25\3")
        buf.write("\26\3\26\5\26\u0100\n\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\5\31\u010b\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u0116\n\32\3\33\3\33\3\33")
        buf.write("\5\33\u011b\n\33\3\33\3\33\3\34\3\34\3\34\5\34\u0122\n")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0131\n\36\3\36\3\36\3\37\3\37\3")
        buf.write(" \3 \3!\3!\5!\u013b\n!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\5$\u014a\n$\3%\3%\5%\u014e\n%\3&\3&\3&\3")
        buf.write("&\3&\5&\u0155\n&\3\'\3\'\3\'\3\'\3\'\5\'\u015c\n\'\3(")
        buf.write("\3(\3(\3(\3(\5(\u0163\n(\3)\3)\3)\3)\3)\3)\7)\u016b\n")
        buf.write(")\f)\16)\u016e\13)\3*\3*\3*\3*\3*\3*\7*\u0176\n*\f*\16")
        buf.write("*\u0179\13*\3+\3+\3+\3+\3+\3+\7+\u0181\n+\f+\16+\u0184")
        buf.write("\13+\3,\3,\3,\5,\u0189\n,\3-\3-\3-\5-\u018e\n-\3.\3.\5")
        buf.write(".\u0192\n.\3/\3/\5/\u0196\n/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\5\60\u01a3\n\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u01b6\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\5\66\u01c0\n\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\58\u01ca\n8\38\2\5PRT9\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjln\2\7\5\2\34\34\36\"$$\3\2\25\26\3\2")
        buf.write("\27\30\3\2\31\33\3\2\3\5\2\u01cf\2q\3\2\2\2\4z\3\2\2\2")
        buf.write("\6|\3\2\2\2\b\u0081\3\2\2\2\n\u0086\3\2\2\2\f\u0088\3")
        buf.write("\2\2\2\16\u008d\3\2\2\2\20\u0091\3\2\2\2\22\u0099\3\2")
        buf.write("\2\2\24\u00a2\3\2\2\2\26\u00a9\3\2\2\2\30\u00ab\3\2\2")
        buf.write("\2\32\u00b9\3\2\2\2\34\u00bf\3\2\2\2\36\u00c1\3\2\2\2")
        buf.write(" \u00c6\3\2\2\2\"\u00d1\3\2\2\2$\u00ec\3\2\2\2&\u00ee")
        buf.write("\3\2\2\2(\u00f6\3\2\2\2*\u00ff\3\2\2\2,\u0101\3\2\2\2")
        buf.write(".\u0104\3\2\2\2\60\u0107\3\2\2\2\62\u0115\3\2\2\2\64\u0117")
        buf.write("\3\2\2\2\66\u011e\3\2\2\28\u0125\3\2\2\2:\u0129\3\2\2")
        buf.write("\2<\u0134\3\2\2\2>\u0136\3\2\2\2@\u0138\3\2\2\2B\u013c")
        buf.write("\3\2\2\2D\u0141\3\2\2\2F\u0149\3\2\2\2H\u014d\3\2\2\2")
        buf.write("J\u0154\3\2\2\2L\u015b\3\2\2\2N\u0162\3\2\2\2P\u0164\3")
        buf.write("\2\2\2R\u016f\3\2\2\2T\u017a\3\2\2\2V\u0188\3\2\2\2X\u018d")
        buf.write("\3\2\2\2Z\u0191\3\2\2\2\\\u0195\3\2\2\2^\u01a2\3\2\2\2")
        buf.write("`\u01a4\3\2\2\2b\u01a9\3\2\2\2d\u01ae\3\2\2\2f\u01b5\3")
        buf.write("\2\2\2h\u01b7\3\2\2\2j\u01bf\3\2\2\2l\u01c1\3\2\2\2n\u01c9")
        buf.write("\3\2\2\2pr\5F$\2qp\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\5\4\3")
        buf.write("\2tu\7\2\2\3u\3\3\2\2\2vw\5\6\4\2wx\5\4\3\2x{\3\2\2\2")
        buf.write("y{\5\6\4\2zv\3\2\2\2zy\3\2\2\2{\5\3\2\2\2|}\5\b\5\2}~")
        buf.write("\5F$\2~\7\3\2\2\2\177\u0082\5\n\6\2\u0080\u0082\5\22\n")
        buf.write("\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\t\3\2\2")
        buf.write("\2\u0083\u0087\5\20\t\2\u0084\u0087\5\16\b\2\u0085\u0087")
        buf.write("\5\f\7\2\u0086\u0083\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\13\3\2\2\2\u0088\u0089\7\b\2\2\u0089")
        buf.write("\u008b\7-\2\2\u008a\u008c\5.\30\2\u008b\u008a\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\r\3\2\2\2\u008d\u008e\7\7\2")
        buf.write("\2\u008e\u008f\7-\2\2\u008f\u0090\5.\30\2\u0090\17\3\2")
        buf.write("\2\2\u0091\u0092\5d\63\2\u0092\u0094\7-\2\2\u0093\u0095")
        buf.write("\5l\67\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u0098\5.\30\2\u0097\u0096\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\21\3\2\2\2\u0099\u009a\7\t")
        buf.write("\2\2\u009a\u009b\7-\2\2\u009b\u009c\7%\2\2\u009c\u009d")
        buf.write("\5\24\13\2\u009d\u009e\7&\2\2\u009e\u009f\5\32\16\2\u009f")
        buf.write("\23\3\2\2\2\u00a0\u00a3\5\26\f\2\u00a1\u00a3\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\25\3\2\2\2\u00a4")
        buf.write("\u00a5\5\30\r\2\u00a5\u00a6\7)\2\2\u00a6\u00a7\5\26\f")
        buf.write("\2\u00a7\u00aa\3\2\2\2\u00a8\u00aa\5\30\r\2\u00a9\u00a4")
        buf.write("\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\27\3\2\2\2\u00ab\u00ac")
        buf.write("\5d\63\2\u00ac\u00ae\7-\2\2\u00ad\u00af\5l\67\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\31\3\2\2\2\u00b0")
        buf.write("\u00b2\5F$\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00ba\5@!\2\u00b4\u00b6\5F$\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00ba\5D#\2\u00b8\u00ba\3\2\2\2\u00b9\u00b1\3\2")
        buf.write("\2\2\u00b9\u00b5\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\33")
        buf.write("\3\2\2\2\u00bb\u00bc\5\36\20\2\u00bc\u00bd\5\34\17\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bb\3\2\2\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00c0\35\3\2\2\2\u00c1\u00c2\5 \21")
        buf.write("\2\u00c2\u00c3\5F$\2\u00c3\37\3\2\2\2\u00c4\u00c7\5\"")
        buf.write("\22\2\u00c5\u00c7\5$\23\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7!\3\2\2\2\u00c8\u00d2\5\n\6\2\u00c9\u00d2")
        buf.write("\5,\27\2\u00ca\u00d2\5\60\31\2\u00cb\u00d2\5:\36\2\u00cc")
        buf.write("\u00d2\5<\37\2\u00cd\u00d2\5> \2\u00ce\u00d2\5@!\2\u00cf")
        buf.write("\u00d2\5B\"\2\u00d0\u00d2\5D#\2\u00d1\u00c8\3\2\2\2\u00d1")
        buf.write("\u00c9\3\2\2\2\u00d1\u00ca\3\2\2\2\u00d1\u00cb\3\2\2\2")
        buf.write("\u00d1\u00cc\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d1\u00ce\3")
        buf.write("\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2#")
        buf.write("\3\2\2\2\u00d3\u00d4\7\17\2\2\u00d4\u00d6\58\35\2\u00d5")
        buf.write("\u00d7\5F$\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\5 \21\2\u00d9\u00ed\3\2\2\2")
        buf.write("\u00da\u00db\7\17\2\2\u00db\u00dd\58\35\2\u00dc\u00de")
        buf.write("\5F$\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e0\5\"\22\2\u00e0\u00e1\5\62\32\2\u00e1")
        buf.write("\u00e2\5&\24\2\u00e2\u00ed\3\2\2\2\u00e3\u00e4\7\17\2")
        buf.write("\2\u00e4\u00e6\58\35\2\u00e5\u00e7\5F$\2\u00e6\u00e5\3")
        buf.write("\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9")
        buf.write("\5\"\22\2\u00e9\u00ea\5\62\32\2\u00ea\u00eb\5(\25\2\u00eb")
        buf.write("\u00ed\3\2\2\2\u00ec\u00d3\3\2\2\2\u00ec\u00da\3\2\2\2")
        buf.write("\u00ec\u00e3\3\2\2\2\u00ed%\3\2\2\2\u00ee\u00ef\5F$\2")
        buf.write("\u00ef\u00f0\7\21\2\2\u00f0\u00f2\58\35\2\u00f1\u00f3")
        buf.write("\5F$\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\5 \21\2\u00f5\'\3\2\2\2\u00f6\u00f7")
        buf.write("\5F$\2\u00f7\u00f9\7\20\2\2\u00f8\u00fa\5F$\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\5$\23\2\u00fc)\3\2\2\2\u00fd\u0100\7-\2\2\u00fe")
        buf.write("\u0100\5b\62\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2")
        buf.write("\u0100+\3\2\2\2\u0101\u0102\5*\26\2\u0102\u0103\5.\30")
        buf.write("\2\u0103-\3\2\2\2\u0104\u0105\7\35\2\2\u0105\u0106\5L")
        buf.write("\'\2\u0106/\3\2\2\2\u0107\u0108\7\17\2\2\u0108\u010a\5")
        buf.write("8\35\2\u0109\u010b\5F$\2\u010a\u0109\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\5\"\22\2\u010d")
        buf.write("\u010e\5\62\32\2\u010e\u010f\5\66\34\2\u010f\61\3\2\2")
        buf.write("\2\u0110\u0111\5F$\2\u0111\u0112\5\64\33\2\u0112\u0113")
        buf.write("\5\62\32\2\u0113\u0116\3\2\2\2\u0114\u0116\3\2\2\2\u0115")
        buf.write("\u0110\3\2\2\2\u0115\u0114\3\2\2\2\u0116\63\3\2\2\2\u0117")
        buf.write("\u0118\7\21\2\2\u0118\u011a\58\35\2\u0119\u011b\5F$\2")
        buf.write("\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\3")
        buf.write("\2\2\2\u011c\u011d\5\"\22\2\u011d\65\3\2\2\2\u011e\u011f")
        buf.write("\5F$\2\u011f\u0121\7\20\2\2\u0120\u0122\5F$\2\u0121\u0120")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0124\5\"\22\2\u0124\67\3\2\2\2\u0125\u0126\7%\2\2\u0126")
        buf.write("\u0127\5L\'\2\u0127\u0128\7&\2\2\u01289\3\2\2\2\u0129")
        buf.write("\u012a\7\n\2\2\u012a\u012b\7-\2\2\u012b\u012c\7\13\2\2")
        buf.write("\u012c\u012d\5L\'\2\u012d\u012e\7\f\2\2\u012e\u0130\5")
        buf.write("L\'\2\u012f\u0131\5F$\2\u0130\u012f\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\5 \21\2\u0133")
        buf.write(";\3\2\2\2\u0134\u0135\7\r\2\2\u0135=\3\2\2\2\u0136\u0137")
        buf.write("\7\16\2\2\u0137?\3\2\2\2\u0138\u013a\7\6\2\2\u0139\u013b")
        buf.write("\5L\'\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("A\3\2\2\2\u013c\u013d\7-\2\2\u013d\u013e\7%\2\2\u013e")
        buf.write("\u013f\5H%\2\u013f\u0140\7&\2\2\u0140C\3\2\2\2\u0141\u0142")
        buf.write("\7\22\2\2\u0142\u0143\5F$\2\u0143\u0144\5\34\17\2\u0144")
        buf.write("\u0145\7\23\2\2\u0145E\3\2\2\2\u0146\u0147\7.\2\2\u0147")
        buf.write("\u014a\5F$\2\u0148\u014a\7.\2\2\u0149\u0146\3\2\2\2\u0149")
        buf.write("\u0148\3\2\2\2\u014aG\3\2\2\2\u014b\u014e\5J&\2\u014c")
        buf.write("\u014e\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014eI\3\2\2\2\u014f\u0150\5L\'\2\u0150\u0151\7)\2\2")
        buf.write("\u0151\u0152\5J&\2\u0152\u0155\3\2\2\2\u0153\u0155\5L")
        buf.write("\'\2\u0154\u014f\3\2\2\2\u0154\u0153\3\2\2\2\u0155K\3")
        buf.write("\2\2\2\u0156\u0157\5N(\2\u0157\u0158\7#\2\2\u0158\u0159")
        buf.write("\5N(\2\u0159\u015c\3\2\2\2\u015a\u015c\5N(\2\u015b\u0156")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015cM\3\2\2\2\u015d\u015e")
        buf.write("\5P)\2\u015e\u015f\t\2\2\2\u015f\u0160\5P)\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u0163\5P)\2\u0162\u015d\3\2\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0163O\3\2\2\2\u0164\u0165\b)\1\2\u0165\u0166")
        buf.write("\5R*\2\u0166\u016c\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169")
        buf.write("\t\3\2\2\u0169\u016b\5R*\2\u016a\u0167\3\2\2\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("Q\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\b*\1\2\u0170")
        buf.write("\u0171\5T+\2\u0171\u0177\3\2\2\2\u0172\u0173\f\4\2\2\u0173")
        buf.write("\u0174\t\4\2\2\u0174\u0176\5T+\2\u0175\u0172\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178S\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\b+\1\2")
        buf.write("\u017b\u017c\5V,\2\u017c\u0182\3\2\2\2\u017d\u017e\f\4")
        buf.write("\2\2\u017e\u017f\t\5\2\2\u017f\u0181\5V,\2\u0180\u017d")
        buf.write("\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183U\3\2\2\2\u0184\u0182\3\2\2\2\u0185")
        buf.write("\u0186\7\24\2\2\u0186\u0189\5V,\2\u0187\u0189\5X-\2\u0188")
        buf.write("\u0185\3\2\2\2\u0188\u0187\3\2\2\2\u0189W\3\2\2\2\u018a")
        buf.write("\u018b\7\30\2\2\u018b\u018e\5X-\2\u018c\u018e\5Z.\2\u018d")
        buf.write("\u018a\3\2\2\2\u018d\u018c\3\2\2\2\u018eY\3\2\2\2\u018f")
        buf.write("\u0192\5\\/\2\u0190\u0192\5^\60\2\u0191\u018f\3\2\2\2")
        buf.write("\u0191\u0190\3\2\2\2\u0192[\3\2\2\2\u0193\u0196\7-\2\2")
        buf.write("\u0194\u0196\5`\61\2\u0195\u0193\3\2\2\2\u0195\u0194\3")
        buf.write("\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\7\'\2\2\u0198\u0199")
        buf.write("\5f\64\2\u0199\u019a\7(\2\2\u019a]\3\2\2\2\u019b\u01a3")
        buf.write("\7-\2\2\u019c\u01a3\5n8\2\u019d\u01a3\5`\61\2\u019e\u019f")
        buf.write("\7%\2\2\u019f\u01a0\5L\'\2\u01a0\u01a1\7&\2\2\u01a1\u01a3")
        buf.write("\3\2\2\2\u01a2\u019b\3\2\2\2\u01a2\u019c\3\2\2\2\u01a2")
        buf.write("\u019d\3\2\2\2\u01a2\u019e\3\2\2\2\u01a3_\3\2\2\2\u01a4")
        buf.write("\u01a5\7-\2\2\u01a5\u01a6\7%\2\2\u01a6\u01a7\5H%\2\u01a7")
        buf.write("\u01a8\7&\2\2\u01a8a\3\2\2\2\u01a9\u01aa\7-\2\2\u01aa")
        buf.write("\u01ab\7\'\2\2\u01ab\u01ac\5f\64\2\u01ac\u01ad\7(\2\2")
        buf.write("\u01adc\3\2\2\2\u01ae\u01af\t\6\2\2\u01afe\3\2\2\2\u01b0")
        buf.write("\u01b1\5L\'\2\u01b1\u01b2\7)\2\2\u01b2\u01b3\5f\64\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b6\5L\'\2\u01b5\u01b0\3\2\2\2")
        buf.write("\u01b5\u01b4\3\2\2\2\u01b6g\3\2\2\2\u01b7\u01b8\7\'\2")
        buf.write("\2\u01b8\u01b9\5J&\2\u01b9\u01ba\7(\2\2\u01bai\3\2\2\2")
        buf.write("\u01bb\u01bc\7*\2\2\u01bc\u01bd\7)\2\2\u01bd\u01c0\5j")
        buf.write("\66\2\u01be\u01c0\7*\2\2\u01bf\u01bb\3\2\2\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01c0k\3\2\2\2\u01c1\u01c2\7\'\2\2\u01c2\u01c3")
        buf.write("\5j\66\2\u01c3\u01c4\7(\2\2\u01c4m\3\2\2\2\u01c5\u01ca")
        buf.write("\7*\2\2\u01c6\u01ca\7,\2\2\u01c7\u01ca\7+\2\2\u01c8\u01ca")
        buf.write("\5h\65\2\u01c9\u01c5\3\2\2\2\u01c9\u01c6\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01cao\3\2\2\2/qz\u0081")
        buf.write("\u0086\u008b\u0094\u0097\u00a2\u00a9\u00ae\u00b1\u00b5")
        buf.write("\u00b9\u00bf\u00c6\u00d1\u00d6\u00dd\u00e6\u00ec\u00f2")
        buf.write("\u00f9\u00ff\u010a\u0115\u011a\u0121\u0130\u013a\u0149")
        buf.write("\u014d\u0154\u015b\u0162\u016c\u0177\u0182\u0188\u018d")
        buf.write("\u0191\u0195\u01a2\u01b5\u01bf\u01c9")
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
    RULE_match_if_stmt = 23
    RULE_elif_match_list = 24
    RULE_elif_match_stmt = 25
    RULE_else_match_stmt = 26
    RULE_cond_expr = 27
    RULE_for_stmt = 28
    RULE_break_stmt = 29
    RULE_continue_stmt = 30
    RULE_return_stmt = 31
    RULE_func_call_stmt = 32
    RULE_block_stmt = 33
    RULE_newline_list = 34
    RULE_expr_list = 35
    RULE_expr_prime = 36
    RULE_expr = 37
    RULE_rel_expr = 38
    RULE_and_expr = 39
    RULE_add_expr = 40
    RULE_mul_expr = 41
    RULE_not_expr = 42
    RULE_sign_expr = 43
    RULE_idx_expr = 44
    RULE_elem_expr = 45
    RULE_operand = 46
    RULE_func_call_expr = 47
    RULE_arr_elem = 48
    RULE_types = 49
    RULE_idx_op = 50
    RULE_arr_lit = 51
    RULE_dim_list = 52
    RULE_arr_dim = 53
    RULE_literal = 54

    ruleNames =  [ "program", "decl_list", "decl_mem", "decl", "var_decl", 
                   "dyn_decl", "v_decl", "type_decl", "func_decl", "param_list", 
                   "param_prime", "param", "func_body", "stmt_list", "stmt_mem", 
                   "stmt", "match_stmt", "unmatch_stmt", "elif_stmt", "else_unmatch_stmt", 
                   "lhs", "assign_stmt", "as_expr", "match_if_stmt", "elif_match_list", 
                   "elif_match_stmt", "else_match_stmt", "cond_expr", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "func_call_stmt", 
                   "block_stmt", "newline_list", "expr_list", "expr_prime", 
                   "expr", "rel_expr", "and_expr", "add_expr", "mul_expr", 
                   "not_expr", "sign_expr", "idx_expr", "elem_expr", "operand", 
                   "func_call_expr", "arr_elem", "types", "idx_op", "arr_lit", 
                   "dim_list", "arr_dim", "literal" ]

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
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 110
                self.newline_list()


            self.state = 113
            self.decl_list()
            self.state = 114
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.decl_mem()
                self.state = 117
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
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
            self.state = 122
            self.decl()
            self.state = 123
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
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.var_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.type_decl()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.v_decl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
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
            self.state = 134
            self.match(ZCodeParser.DYNAMIC)
            self.state = 135
            self.match(ZCodeParser.ID)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 136
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
            self.state = 139
            self.match(ZCodeParser.VAR)
            self.state = 140
            self.match(ZCodeParser.ID)
            self.state = 141
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
            self.state = 143
            self.types()
            self.state = 144
            self.match(ZCodeParser.ID)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 145
                self.arr_dim()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 148
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
            self.state = 151
            self.match(ZCodeParser.FUNC)
            self.state = 152
            self.match(ZCodeParser.ID)
            self.state = 153
            self.match(ZCodeParser.LP)
            self.state = 154
            self.param_list()
            self.state = 155
            self.match(ZCodeParser.RP)
            self.state = 156
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.param()
                self.state = 163
                self.match(ZCodeParser.CM)
                self.state = 164
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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
            self.state = 169
            self.types()
            self.state = 170
            self.match(ZCodeParser.ID)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 171
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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 174
                    self.newline_list()


                self.state = 177
                self.return_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 178
                    self.newline_list()


                self.state = 181
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
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.stmt_mem()
                self.state = 186
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
            self.state = 191
            self.stmt()
            self.state = 192
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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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


        def match_if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Match_if_stmtContext,0)


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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.match_if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 202
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 203
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 204
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 205
                self.func_call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 206
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
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(ZCodeParser.IF)
                self.state = 210
                self.cond_expr()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 211
                    self.newline_list()


                self.state = 214
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(ZCodeParser.IF)
                self.state = 217
                self.cond_expr()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 218
                    self.newline_list()


                self.state = 221
                self.match_stmt()
                self.state = 222
                self.elif_match_list()
                self.state = 223
                self.elif_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(ZCodeParser.IF)
                self.state = 226
                self.cond_expr()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 227
                    self.newline_list()


                self.state = 230
                self.match_stmt()
                self.state = 231
                self.elif_match_list()
                self.state = 232
                self.else_unmatch_stmt()
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
            self.state = 236
            self.newline_list()
            self.state = 237
            self.match(ZCodeParser.ELIF)
            self.state = 238
            self.cond_expr()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 239
                self.newline_list()


            self.state = 242
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
            self.state = 244
            self.newline_list()
            self.state = 245
            self.match(ZCodeParser.ELSE)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 246
                self.newline_list()


            self.state = 249
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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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
            self.state = 255
            self.lhs()
            self.state = 256
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
            self.state = 258
            self.match(ZCodeParser.ASSIGN)
            self.state = 259
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Match_if_stmtContext(ParserRuleContext):
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
            return ZCodeParser.RULE_match_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch_if_stmt" ):
                return visitor.visitMatch_if_stmt(self)
            else:
                return visitor.visitChildren(self)




    def match_if_stmt(self):

        localctx = ZCodeParser.Match_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_match_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ZCodeParser.IF)
            self.state = 262
            self.cond_expr()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 263
                self.newline_list()


            self.state = 266
            self.match_stmt()
            self.state = 267
            self.elif_match_list()
            self.state = 268
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
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.newline_list()
                self.state = 271
                self.elif_match_stmt()
                self.state = 272
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
            self.state = 277
            self.match(ZCodeParser.ELIF)
            self.state = 278
            self.cond_expr()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 279
                self.newline_list()


            self.state = 282
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
            self.state = 284
            self.newline_list()
            self.state = 285
            self.match(ZCodeParser.ELSE)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 286
                self.newline_list()


            self.state = 289
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
            self.state = 291
            self.match(ZCodeParser.LP)
            self.state = 292
            self.expr()
            self.state = 293
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

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


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
            self.state = 295
            self.match(ZCodeParser.FOR)
            self.state = 296
            self.match(ZCodeParser.ID)
            self.state = 297
            self.match(ZCodeParser.UNTIL)
            self.state = 298
            self.expr()
            self.state = 299
            self.match(ZCodeParser.BY)
            self.state = 300
            self.expr()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 301
                self.newline_list()


            self.state = 304
            self.stmt()
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
        self.enterRule(localctx, 58, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
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
        self.enterRule(localctx, 60, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
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
        self.enterRule(localctx, 62, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(ZCodeParser.RETURN)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.STR_LIT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 311
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
        self.enterRule(localctx, 64, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ZCodeParser.ID)
            self.state = 315
            self.match(ZCodeParser.LP)
            self.state = 316
            self.expr_list()
            self.state = 317
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
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.BEGIN)
            self.state = 320
            self.newline_list()
            self.state = 321
            self.stmt_list()
            self.state = 322
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
        self.enterRule(localctx, 68, self.RULE_newline_list)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(ZCodeParser.NEWLINE)
                self.state = 325
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
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
        self.enterRule(localctx, 70, self.RULE_expr_list)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
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
        self.enterRule(localctx, 72, self.RULE_expr_prime)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.expr()
                self.state = 334
                self.match(ZCodeParser.CM)
                self.state = 335
                self.expr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
        self.enterRule(localctx, 74, self.RULE_expr)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.rel_expr()
                self.state = 341
                self.match(ZCodeParser.CONCAT)
                self.state = 342
                self.rel_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
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
        self.enterRule(localctx, 76, self.RULE_rel_expr)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.and_expr(0)
                self.state = 348
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LEQ) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GEQ) | (1 << ZCodeParser.STR_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 349
                self.and_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_and_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 359
                    self.add_expr(0) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 370
                    self.mul_expr(0) 
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 381
                    self.not_expr() 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_not_expr)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(ZCodeParser.NOT)
                self.state = 388
                self.not_expr()
                pass
            elif token in [ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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
        self.enterRule(localctx, 86, self.RULE_sign_expr)
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(ZCodeParser.SUB)
                self.state = 393
                self.sign_expr()
                pass
            elif token in [ZCodeParser.LP, ZCodeParser.LSB, ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
        self.enterRule(localctx, 88, self.RULE_idx_expr)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.elem_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
        self.enterRule(localctx, 90, self.RULE_elem_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 401
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 402
                self.func_call_expr()
                pass


            self.state = 405
            self.match(ZCodeParser.LSB)
            self.state = 406
            self.idx_op()
            self.state = 407
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
        self.enterRule(localctx, 92, self.RULE_operand)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.func_call_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.match(ZCodeParser.LP)
                self.state = 413
                self.expr()
                self.state = 414
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
        self.enterRule(localctx, 94, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZCodeParser.ID)
            self.state = 419
            self.match(ZCodeParser.LP)
            self.state = 420
            self.expr_list()
            self.state = 421
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
        self.enterRule(localctx, 96, self.RULE_arr_elem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(ZCodeParser.ID)
            self.state = 424
            self.match(ZCodeParser.LSB)
            self.state = 425
            self.idx_op()
            self.state = 426
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
        self.enterRule(localctx, 98, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
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
        self.enterRule(localctx, 100, self.RULE_idx_op)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.expr()
                self.state = 431
                self.match(ZCodeParser.CM)
                self.state = 432
                self.idx_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
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
        self.enterRule(localctx, 102, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(ZCodeParser.LSB)
            self.state = 438
            self.expr_prime()
            self.state = 439
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
        self.enterRule(localctx, 104, self.RULE_dim_list)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(ZCodeParser.NUM_LIT)
                self.state = 442
                self.match(ZCodeParser.CM)
                self.state = 443
                self.dim_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        self.enterRule(localctx, 106, self.RULE_arr_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(ZCodeParser.LSB)
            self.state = 448
            self.dim_list()
            self.state = 449
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
        self.enterRule(localctx, 108, self.RULE_literal)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(ZCodeParser.STR_LIT)
                pass
            elif token in [ZCodeParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 454
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
        self._predicates[39] = self.and_expr_sempred
        self._predicates[40] = self.add_expr_sempred
        self._predicates[41] = self.mul_expr_sempred
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
         




