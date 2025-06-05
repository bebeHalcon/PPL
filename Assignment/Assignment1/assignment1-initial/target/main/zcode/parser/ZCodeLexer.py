# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0181\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\6+\u0118")
        buf.write("\n+\r+\16+\u0119\3,\3,\7,\u011e\n,\f,\16,\u0121\13,\3")
        buf.write("-\3-\5-\u0125\n-\3-\6-\u0128\n-\r-\16-\u0129\3.\3.\3.")
        buf.write("\3/\3/\3/\3/\5/\u0133\n/\3\60\3\60\5\60\u0137\n\60\3\61")
        buf.write("\3\61\5\61\u013b\n\61\3\61\5\61\u013e\n\61\3\62\3\62\5")
        buf.write("\62\u0142\n\62\3\63\3\63\7\63\u0146\n\63\f\63\16\63\u0149")
        buf.write("\13\63\3\63\3\63\3\63\3\64\3\64\7\64\u0150\n\64\f\64\16")
        buf.write("\64\u0153\13\64\3\65\3\65\3\66\6\66\u0158\n\66\r\66\16")
        buf.write("\66\u0159\3\66\3\66\3\67\3\67\3\67\3\67\7\67\u0162\n\67")
        buf.write("\f\67\16\67\u0165\13\67\3\67\3\67\38\38\78\u016b\n8\f")
        buf.write("8\168\u016e\138\38\58\u0171\n8\38\38\39\39\79\u0177\n")
        buf.write("9\f9\169\u017a\139\39\39\39\3:\3:\3:\2\2;\3\2\5\2\7\3")
        buf.write("\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16")
        buf.write("\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65")
        buf.write("\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U\2W\2")
        buf.write("Y\2[\2]\2_\2a*c+e,g-i.k/m\60o\61q\62s\63\3\2\f\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f\16\17$$^^")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\16\"\"\4\2\f\f")
        buf.write("\16\17\4\3\f\f\16\17\2\u0188\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\3u\3\2\2\2\5z\3\2\2\2\7\u0080\3\2\2\2\t\u0087")
        buf.write("\3\2\2\2\13\u008c\3\2\2\2\r\u0093\3\2\2\2\17\u009a\3\2")
        buf.write("\2\2\21\u009e\3\2\2\2\23\u00a6\3\2\2\2\25\u00ab\3\2\2")
        buf.write("\2\27\u00af\3\2\2\2\31\u00b5\3\2\2\2\33\u00b8\3\2\2\2")
        buf.write("\35\u00be\3\2\2\2\37\u00c7\3\2\2\2!\u00ca\3\2\2\2#\u00cf")
        buf.write("\3\2\2\2%\u00d4\3\2\2\2\'\u00da\3\2\2\2)\u00de\3\2\2\2")
        buf.write("+\u00e2\3\2\2\2-\u00e6\3\2\2\2/\u00e9\3\2\2\2\61\u00eb")
        buf.write("\3\2\2\2\63\u00ed\3\2\2\2\65\u00ef\3\2\2\2\67\u00f1\3")
        buf.write("\2\2\29\u00f3\3\2\2\2;\u00f5\3\2\2\2=\u00f8\3\2\2\2?\u00fb")
        buf.write("\3\2\2\2A\u00fd\3\2\2\2C\u0100\3\2\2\2E\u0102\3\2\2\2")
        buf.write("G\u0105\3\2\2\2I\u0109\3\2\2\2K\u010c\3\2\2\2M\u010e\3")
        buf.write("\2\2\2O\u0110\3\2\2\2Q\u0112\3\2\2\2S\u0114\3\2\2\2U\u0117")
        buf.write("\3\2\2\2W\u011b\3\2\2\2Y\u0122\3\2\2\2[\u012b\3\2\2\2")
        buf.write("]\u0132\3\2\2\2_\u0134\3\2\2\2a\u0138\3\2\2\2c\u0141\3")
        buf.write("\2\2\2e\u0143\3\2\2\2g\u014d\3\2\2\2i\u0154\3\2\2\2k\u0157")
        buf.write("\3\2\2\2m\u015d\3\2\2\2o\u0168\3\2\2\2q\u0174\3\2\2\2")
        buf.write("s\u017e\3\2\2\2uv\7v\2\2vw\7t\2\2wx\7w\2\2xy\7g\2\2y\4")
        buf.write("\3\2\2\2z{\7h\2\2{|\7c\2\2|}\7n\2\2}~\7u\2\2~\177\7g\2")
        buf.write("\2\177\6\3\2\2\2\u0080\u0081\7p\2\2\u0081\u0082\7w\2\2")
        buf.write("\u0082\u0083\7o\2\2\u0083\u0084\7d\2\2\u0084\u0085\7g")
        buf.write("\2\2\u0085\u0086\7t\2\2\u0086\b\3\2\2\2\u0087\u0088\7")
        buf.write("d\2\2\u0088\u0089\7q\2\2\u0089\u008a\7q\2\2\u008a\u008b")
        buf.write("\7n\2\2\u008b\n\3\2\2\2\u008c\u008d\7u\2\2\u008d\u008e")
        buf.write("\7v\2\2\u008e\u008f\7t\2\2\u008f\u0090\7k\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\u0092\7i\2\2\u0092\f\3\2\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7g\2\2\u0095\u0096\7v\2\2\u0096\u0097")
        buf.write("\7w\2\2\u0097\u0098\7t\2\2\u0098\u0099\7p\2\2\u0099\16")
        buf.write("\3\2\2\2\u009a\u009b\7x\2\2\u009b\u009c\7c\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\20\3\2\2\2\u009e\u009f\7f\2\2\u009f\u00a0")
        buf.write("\7{\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7o\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7e\2\2\u00a5\22")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\24\3\2\2\2\u00ab\u00ac")
        buf.write("\7h\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7t\2\2\u00ae\26")
        buf.write("\3\2\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7n\2\2\u00b4\30")
        buf.write("\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7{\2\2\u00b7\32")
        buf.write("\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7m\2\2\u00bd\34")
        buf.write("\3\2\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7g\2\2\u00c6\36")
        buf.write("\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7h\2\2\u00c9 ")
        buf.write("\3\2\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\"\3\2\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7h\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7i\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9&\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7f\2\2\u00dd(\3\2\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7v\2\2\u00e1*\3")
        buf.write("\2\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7f\2\2\u00e5,\3\2\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8.\3\2\2\2\u00e9\u00ea\7-\2\2\u00ea\60\3\2")
        buf.write("\2\2\u00eb\u00ec\7/\2\2\u00ec\62\3\2\2\2\u00ed\u00ee\7")
        buf.write(",\2\2\u00ee\64\3\2\2\2\u00ef\u00f0\7\61\2\2\u00f0\66\3")
        buf.write("\2\2\2\u00f1\u00f2\7\'\2\2\u00f28\3\2\2\2\u00f3\u00f4")
        buf.write("\7?\2\2\u00f4:\3\2\2\2\u00f5\u00f6\7>\2\2\u00f6\u00f7")
        buf.write("\7/\2\2\u00f7<\3\2\2\2\u00f8\u00f9\7#\2\2\u00f9\u00fa")
        buf.write("\7?\2\2\u00fa>\3\2\2\2\u00fb\u00fc\7>\2\2\u00fc@\3\2\2")
        buf.write("\2\u00fd\u00fe\7>\2\2\u00fe\u00ff\7?\2\2\u00ffB\3\2\2")
        buf.write("\2\u0100\u0101\7@\2\2\u0101D\3\2\2\2\u0102\u0103\7@\2")
        buf.write("\2\u0103\u0104\7?\2\2\u0104F\3\2\2\2\u0105\u0106\7\60")
        buf.write("\2\2\u0106\u0107\7\60\2\2\u0107\u0108\7\60\2\2\u0108H")
        buf.write("\3\2\2\2\u0109\u010a\7?\2\2\u010a\u010b\7?\2\2\u010bJ")
        buf.write("\3\2\2\2\u010c\u010d\7*\2\2\u010dL\3\2\2\2\u010e\u010f")
        buf.write("\7+\2\2\u010fN\3\2\2\2\u0110\u0111\7]\2\2\u0111P\3\2\2")
        buf.write("\2\u0112\u0113\7_\2\2\u0113R\3\2\2\2\u0114\u0115\7.\2")
        buf.write("\2\u0115T\3\2\2\2\u0116\u0118\t\2\2\2\u0117\u0116\3\2")
        buf.write("\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011aV\3\2\2\2\u011b\u011f\7\60\2\2\u011c\u011e")
        buf.write("\t\2\2\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120X\3\2\2\2\u0121")
        buf.write("\u011f\3\2\2\2\u0122\u0124\t\3\2\2\u0123\u0125\t\4\2\2")
        buf.write("\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3")
        buf.write("\2\2\2\u0126\u0128\t\2\2\2\u0127\u0126\3\2\2\2\u0128\u0129")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a")
        buf.write("Z\3\2\2\2\u012b\u012c\7^\2\2\u012c\u012d\t\5\2\2\u012d")
        buf.write("\\\3\2\2\2\u012e\u012f\7)\2\2\u012f\u0133\7$\2\2\u0130")
        buf.write("\u0133\n\6\2\2\u0131\u0133\5[.\2\u0132\u012e\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133^\3\2\2\2\u0134")
        buf.write("\u0136\7^\2\2\u0135\u0137\n\5\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137`\3\2\2\2\u0138\u013a\5U+\2")
        buf.write("\u0139\u013b\5W,\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2")
        buf.write("\2\2\u013b\u013d\3\2\2\2\u013c\u013e\5Y-\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013eb\3\2\2\2\u013f\u0142")
        buf.write("\5\3\2\2\u0140\u0142\5\5\3\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142d\3\2\2\2\u0143\u0147\7$\2\2\u0144")
        buf.write("\u0146\5]/\2\u0145\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u014a\u014b\7$\2\2\u014b\u014c\b")
        buf.write("\63\2\2\u014cf\3\2\2\2\u014d\u0151\t\7\2\2\u014e\u0150")
        buf.write("\t\b\2\2\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152h\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0155\7\f\2\2\u0155j\3\2\2\2\u0156")
        buf.write("\u0158\t\t\2\2\u0157\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\3")
        buf.write("\2\2\2\u015b\u015c\b\66\3\2\u015cl\3\2\2\2\u015d\u015e")
        buf.write("\7%\2\2\u015e\u015f\7%\2\2\u015f\u0163\3\2\2\2\u0160\u0162")
        buf.write("\n\n\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0166\u0167\b\67\3\2\u0167n\3\2\2")
        buf.write("\2\u0168\u016c\7$\2\2\u0169\u016b\5]/\2\u016a\u0169\3")
        buf.write("\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0171\t\13\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2")
        buf.write("\2\u0172\u0173\b8\4\2\u0173p\3\2\2\2\u0174\u0178\7$\2")
        buf.write("\2\u0175\u0177\5]/\2\u0176\u0175\3\2\2\2\u0177\u017a\3")
        buf.write("\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\5_\60\2\u017c")
        buf.write("\u017d\b9\5\2\u017dr\3\2\2\2\u017e\u017f\13\2\2\2\u017f")
        buf.write("\u0180\b:\6\2\u0180t\3\2\2\2\23\2\u0119\u011f\u0124\u0129")
        buf.write("\u0132\u0136\u013a\u013d\u0141\u0147\u0151\u0159\u0163")
        buf.write("\u016c\u0170\u0178\7\3\63\2\b\2\2\38\3\39\4\3:\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    BOOL = 2
    STRING = 3
    RETURN = 4
    VAR = 5
    DYNAMIC = 6
    FUNC = 7
    FOR = 8
    UNTIL = 9
    BY = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSE = 14
    ELIF = 15
    BEGIN = 16
    END = 17
    NOT = 18
    AND = 19
    OR = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQ = 26
    ASSIGN = 27
    NEQ = 28
    LESS = 29
    LEQ = 30
    GREATER = 31
    GEQ = 32
    CONCAT = 33
    STR_EQ = 34
    LP = 35
    RP = 36
    LSB = 37
    RSB = 38
    CM = 39
    NUM_LIT = 40
    BOOL_LIT = 41
    STR_LIT = 42
    ID = 43
    NEWLINE = 44
    WS = 45
    COMMENT = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    ERROR_TOKEN = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
            "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", 
            "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "EQ", "ASSIGN", "NEQ", "LESS", "LEQ", "GREATER", "GEQ", 
            "CONCAT", "STR_EQ", "LP", "RP", "LSB", "RSB", "CM", "NUM_LIT", 
            "BOOL_LIT", "STR_LIT", "ID", "NEWLINE", "WS", "COMMENT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "ASSIGN", "NEQ", "LESS", "LEQ", "GREATER", "GEQ", "CONCAT", 
                  "STR_EQ", "LP", "RP", "LSB", "RSB", "CM", "INT", "DEC", 
                  "EXP", "ESC_SEQ", "STR_CHAR", "ILL_ESC", "NUM_LIT", "BOOL_LIT", 
                  "STR_LIT", "ID", "NEWLINE", "WS", "COMMENT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.STR_LIT_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	s = str(self.text)
            	if s[-1] in ['\n', '\r', '\f']:
            		raise UncloseString(s[1:-1])
            	else:
            		raise UncloseString(s[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	s = str(self.text)
            	raise IllegalEscape(s[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


