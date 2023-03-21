# Generated from C:/Users/tudor/Downloads/University/ELSD\PrismGramatica.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,306,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,5,0,66,8,0,
        10,0,12,0,69,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        82,8,1,1,2,1,2,1,3,1,3,1,3,5,3,89,8,3,10,3,12,3,92,9,3,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,100,8,4,1,5,1,5,1,5,5,5,105,8,5,10,5,12,5,108,
        9,5,1,6,1,6,1,6,5,6,113,8,6,10,6,12,6,116,9,6,1,7,1,7,1,7,5,7,121,
        8,7,10,7,12,7,124,9,7,1,8,1,8,1,8,5,8,129,8,8,10,8,12,8,132,9,8,
        1,9,1,9,1,9,5,9,137,8,9,10,9,12,9,140,9,9,1,10,1,10,1,10,5,10,145,
        8,10,10,10,12,10,148,9,10,1,11,1,11,1,11,5,11,153,8,11,10,11,12,
        11,156,9,11,1,12,1,12,1,12,5,12,161,8,12,10,12,12,12,164,9,12,1,
        13,1,13,1,13,5,13,169,8,13,10,13,12,13,172,9,13,1,14,1,14,1,14,5,
        14,177,8,14,10,14,12,14,180,9,14,1,15,1,15,3,15,184,8,15,1,15,1,
        15,1,16,1,16,1,16,5,16,191,8,16,10,16,12,16,194,9,16,1,17,1,17,1,
        17,3,17,199,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,209,
        8,18,1,19,1,19,1,19,3,19,214,8,19,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,230,8,24,10,24,12,24,
        233,9,24,3,24,235,8,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,5,
        25,245,8,25,10,25,12,25,248,9,25,3,25,250,8,25,1,25,1,25,1,25,1,
        26,1,26,1,26,1,26,3,26,259,8,26,1,26,1,26,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,3,27,270,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,
        29,1,29,1,29,3,29,282,8,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        30,1,30,3,30,293,8,30,1,30,1,30,1,31,1,31,5,31,299,8,31,10,31,12,
        31,302,9,31,1,31,1,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,8,
        1,0,10,11,1,0,12,15,1,0,16,17,1,0,18,19,1,0,20,22,2,0,18,19,26,27,
        1,0,42,43,1,0,30,31,311,0,67,1,0,0,0,2,81,1,0,0,0,4,83,1,0,0,0,6,
        85,1,0,0,0,8,93,1,0,0,0,10,101,1,0,0,0,12,109,1,0,0,0,14,117,1,0,
        0,0,16,125,1,0,0,0,18,133,1,0,0,0,20,141,1,0,0,0,22,149,1,0,0,0,
        24,157,1,0,0,0,26,165,1,0,0,0,28,173,1,0,0,0,30,181,1,0,0,0,32,187,
        1,0,0,0,34,198,1,0,0,0,36,208,1,0,0,0,38,213,1,0,0,0,40,215,1,0,
        0,0,42,217,1,0,0,0,44,219,1,0,0,0,46,221,1,0,0,0,48,223,1,0,0,0,
        50,239,1,0,0,0,52,254,1,0,0,0,54,262,1,0,0,0,56,271,1,0,0,0,58,277,
        1,0,0,0,60,290,1,0,0,0,62,296,1,0,0,0,64,66,3,2,1,0,65,64,1,0,0,
        0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,
        1,0,0,0,70,71,5,0,0,1,71,1,1,0,0,0,72,73,3,4,2,0,73,74,5,1,0,0,74,
        82,1,0,0,0,75,82,3,52,26,0,76,82,3,54,27,0,77,82,3,56,28,0,78,82,
        3,58,29,0,79,82,3,48,24,0,80,82,3,60,30,0,81,72,1,0,0,0,81,75,1,
        0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,81,78,1,0,0,0,81,79,1,0,0,0,81,
        80,1,0,0,0,82,3,1,0,0,0,83,84,3,6,3,0,84,5,1,0,0,0,85,90,3,8,4,0,
        86,87,5,2,0,0,87,89,3,8,4,0,88,86,1,0,0,0,89,92,1,0,0,0,90,88,1,
        0,0,0,90,91,1,0,0,0,91,7,1,0,0,0,92,90,1,0,0,0,93,99,3,10,5,0,94,
        95,5,3,0,0,95,96,3,4,2,0,96,97,5,4,0,0,97,98,3,4,2,0,98,100,1,0,
        0,0,99,94,1,0,0,0,99,100,1,0,0,0,100,9,1,0,0,0,101,106,3,12,6,0,
        102,103,5,5,0,0,103,105,3,12,6,0,104,102,1,0,0,0,105,108,1,0,0,0,
        106,104,1,0,0,0,106,107,1,0,0,0,107,11,1,0,0,0,108,106,1,0,0,0,109,
        114,3,14,7,0,110,111,5,6,0,0,111,113,3,14,7,0,112,110,1,0,0,0,113,
        116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,13,1,0,0,0,116,114,
        1,0,0,0,117,122,3,16,8,0,118,119,5,7,0,0,119,121,3,16,8,0,120,118,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,15,1,
        0,0,0,124,122,1,0,0,0,125,130,3,18,9,0,126,127,5,8,0,0,127,129,3,
        18,9,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,
        0,0,0,131,17,1,0,0,0,132,130,1,0,0,0,133,138,3,20,10,0,134,135,5,
        9,0,0,135,137,3,20,10,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,19,1,0,0,0,140,138,1,0,0,0,141,146,3,
        22,11,0,142,143,7,0,0,0,143,145,3,22,11,0,144,142,1,0,0,0,145,148,
        1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,21,1,0,0,0,148,146,1,
        0,0,0,149,154,3,24,12,0,150,151,7,1,0,0,151,153,3,24,12,0,152,150,
        1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,23,1,
        0,0,0,156,154,1,0,0,0,157,162,3,26,13,0,158,159,7,2,0,0,159,161,
        3,26,13,0,160,158,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,
        1,0,0,0,163,25,1,0,0,0,164,162,1,0,0,0,165,170,3,28,14,0,166,167,
        7,3,0,0,167,169,3,28,14,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,
        1,0,0,0,170,171,1,0,0,0,171,27,1,0,0,0,172,170,1,0,0,0,173,178,3,
        34,17,0,174,175,7,4,0,0,175,177,3,34,17,0,176,174,1,0,0,0,177,180,
        1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,29,1,0,0,0,180,178,1,
        0,0,0,181,183,5,23,0,0,182,184,3,32,16,0,183,182,1,0,0,0,183,184,
        1,0,0,0,184,185,1,0,0,0,185,186,5,24,0,0,186,31,1,0,0,0,187,192,
        3,4,2,0,188,189,5,25,0,0,189,191,3,4,2,0,190,188,1,0,0,0,191,194,
        1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,33,1,0,0,0,194,192,1,
        0,0,0,195,196,7,5,0,0,196,199,3,34,17,0,197,199,3,36,18,0,198,195,
        1,0,0,0,198,197,1,0,0,0,199,35,1,0,0,0,200,209,3,38,19,0,201,209,
        3,46,23,0,202,203,5,28,0,0,203,204,3,4,2,0,204,205,5,29,0,0,205,
        209,1,0,0,0,206,209,3,30,15,0,207,209,3,50,25,0,208,200,1,0,0,0,
        208,201,1,0,0,0,208,202,1,0,0,0,208,206,1,0,0,0,208,207,1,0,0,0,
        209,37,1,0,0,0,210,214,3,40,20,0,211,214,3,42,21,0,212,214,3,44,
        22,0,213,210,1,0,0,0,213,211,1,0,0,0,213,212,1,0,0,0,214,39,1,0,
        0,0,215,216,7,6,0,0,216,41,1,0,0,0,217,218,5,44,0,0,218,43,1,0,0,
        0,219,220,7,7,0,0,220,45,1,0,0,0,221,222,5,41,0,0,222,47,1,0,0,0,
        223,224,5,32,0,0,224,225,3,46,23,0,225,234,5,28,0,0,226,231,3,46,
        23,0,227,228,5,25,0,0,228,230,3,46,23,0,229,227,1,0,0,0,230,233,
        1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,235,1,0,0,0,233,231,
        1,0,0,0,234,226,1,0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,236,237,
        5,29,0,0,237,238,3,62,31,0,238,49,1,0,0,0,239,240,5,32,0,0,240,249,
        5,28,0,0,241,246,3,46,23,0,242,243,5,25,0,0,243,245,3,46,23,0,244,
        242,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,
        250,1,0,0,0,248,246,1,0,0,0,249,241,1,0,0,0,249,250,1,0,0,0,250,
        251,1,0,0,0,251,252,5,29,0,0,252,253,3,62,31,0,253,51,1,0,0,0,254,
        255,5,33,0,0,255,258,3,46,23,0,256,257,5,2,0,0,257,259,3,4,2,0,258,
        256,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,0,260,261,5,1,0,0,261,
        53,1,0,0,0,262,263,5,34,0,0,263,264,5,28,0,0,264,265,3,4,2,0,265,
        266,5,29,0,0,266,269,3,62,31,0,267,268,5,35,0,0,268,270,3,62,31,
        0,269,267,1,0,0,0,269,270,1,0,0,0,270,55,1,0,0,0,271,272,5,36,0,
        0,272,273,5,28,0,0,273,274,3,4,2,0,274,275,5,29,0,0,275,276,3,62,
        31,0,276,57,1,0,0,0,277,278,5,37,0,0,278,281,5,28,0,0,279,282,3,
        52,26,0,280,282,3,4,2,0,281,279,1,0,0,0,281,280,1,0,0,0,281,282,
        1,0,0,0,282,283,1,0,0,0,283,284,5,1,0,0,284,285,3,4,2,0,285,286,
        5,1,0,0,286,287,3,4,2,0,287,288,5,29,0,0,288,289,3,62,31,0,289,59,
        1,0,0,0,290,292,5,38,0,0,291,293,3,4,2,0,292,291,1,0,0,0,292,293,
        1,0,0,0,293,294,1,0,0,0,294,295,5,1,0,0,295,61,1,0,0,0,296,300,5,
        39,0,0,297,299,3,2,1,0,298,297,1,0,0,0,299,302,1,0,0,0,300,298,1,
        0,0,0,300,301,1,0,0,0,301,303,1,0,0,0,302,300,1,0,0,0,303,304,5,
        40,0,0,304,63,1,0,0,0,28,67,81,90,99,106,114,122,130,138,146,154,
        162,170,178,183,192,198,208,213,231,234,246,249,258,269,281,292,
        300
    ]

class PrismGramaticaParser ( Parser ):

    grammarFileName = "PrismGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'?'", "':'", "'||'", "'&&'", 
                     "'|'", "'^'", "'&'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'<<'", "'>>'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'['", "']'", "','", "'!'", "'~'", "'('", 
                     "')'", "'true'", "'false'", "'function'", "'var'", 
                     "'if'", "'else'", "'while'", "'for'", "'return'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INT", "FLOAT", "STRING", 
                      "ESC", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_assignmentExpression = 3
    RULE_ternaryExpression = 4
    RULE_logicalOrExpression = 5
    RULE_logicalAndExpression = 6
    RULE_bitwiseOrExpression = 7
    RULE_bitwiseXorExpression = 8
    RULE_bitwiseAndExpression = 9
    RULE_equalityExpression = 10
    RULE_relationalExpression = 11
    RULE_shiftExpression = 12
    RULE_additiveExpression = 13
    RULE_multiplicativeExpression = 14
    RULE_arrayExpression = 15
    RULE_expressionList = 16
    RULE_unaryExpression = 17
    RULE_primaryExpression = 18
    RULE_literal = 19
    RULE_numericLiteral = 20
    RULE_stringLiteral = 21
    RULE_booleanLiteral = 22
    RULE_identifier = 23
    RULE_functionDeclaration = 24
    RULE_functionExpression = 25
    RULE_variableDeclaration = 26
    RULE_ifStatement = 27
    RULE_whileStatement = 28
    RULE_forStatement = 29
    RULE_returnStatement = 30
    RULE_blockStatement = 31

    ruleNames =  [ "program", "statement", "expression", "assignmentExpression", 
                   "ternaryExpression", "logicalOrExpression", "logicalAndExpression", 
                   "bitwiseOrExpression", "bitwiseXorExpression", "bitwiseAndExpression", 
                   "equalityExpression", "relationalExpression", "shiftExpression", 
                   "additiveExpression", "multiplicativeExpression", "arrayExpression", 
                   "expressionList", "unaryExpression", "primaryExpression", 
                   "literal", "numericLiteral", "stringLiteral", "booleanLiteral", 
                   "identifier", "functionDeclaration", "functionExpression", 
                   "variableDeclaration", "ifStatement", "whileStatement", 
                   "forStatement", "returnStatement", "blockStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    IDENTIFIER=41
    INT=42
    FLOAT=43
    STRING=44
    ESC=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PrismGramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PrismGramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33500150104064) != 0:
                self.state = 64
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(PrismGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(PrismGramaticaParser.VariableDeclarationContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ForStatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(PrismGramaticaParser.FunctionDeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PrismGramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.expression()
                self.state = 73
                self.match(PrismGramaticaParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.variableDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.functionDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.returnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PrismGramaticaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ternaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.TernaryExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.TernaryExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = PrismGramaticaParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.ternaryExpression()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.match(PrismGramaticaParser.T__1)
                    self.state = 87
                    self.ternaryExpression() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.LogicalOrExpressionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_ternaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpression" ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpression" ):
                listener.exitTernaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpression" ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def ternaryExpression(self):

        localctx = PrismGramaticaParser.TernaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ternaryExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.logicalOrExpression()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 94
                self.match(PrismGramaticaParser.T__2)
                self.state = 95
                self.expression()
                self.state = 96
                self.match(PrismGramaticaParser.T__3)
                self.state = 97
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.LogicalAndExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = PrismGramaticaParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.logicalAndExpression()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 102
                self.match(PrismGramaticaParser.T__4)
                self.state = 103
                self.logicalAndExpression()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseOrExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.BitwiseOrExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.BitwiseOrExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = PrismGramaticaParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.bitwiseOrExpression()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 110
                self.match(PrismGramaticaParser.T__5)
                self.state = 111
                self.bitwiseOrExpression()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseXorExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.BitwiseXorExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.BitwiseXorExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_bitwiseOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseOrExpression" ):
                listener.enterBitwiseOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseOrExpression" ):
                listener.exitBitwiseOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseOrExpression" ):
                return visitor.visitBitwiseOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseOrExpression(self):

        localctx = PrismGramaticaParser.BitwiseOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bitwiseOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.bitwiseXorExpression()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 118
                self.match(PrismGramaticaParser.T__6)
                self.state = 119
                self.bitwiseXorExpression()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseXorExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.BitwiseAndExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.BitwiseAndExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_bitwiseXorExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseXorExpression" ):
                listener.enterBitwiseXorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseXorExpression" ):
                listener.exitBitwiseXorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseXorExpression" ):
                return visitor.visitBitwiseXorExpression(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseXorExpression(self):

        localctx = PrismGramaticaParser.BitwiseXorExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bitwiseXorExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.bitwiseAndExpression()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 126
                self.match(PrismGramaticaParser.T__7)
                self.state = 127
                self.bitwiseAndExpression()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.EqualityExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_bitwiseAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseAndExpression" ):
                listener.enterBitwiseAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseAndExpression" ):
                listener.exitBitwiseAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseAndExpression" ):
                return visitor.visitBitwiseAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseAndExpression(self):

        localctx = PrismGramaticaParser.BitwiseAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bitwiseAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.equalityExpression()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 134
                self.match(PrismGramaticaParser.T__8)
                self.state = 135
                self.equalityExpression()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.RelationalExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = PrismGramaticaParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.relationalExpression()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.relationalExpression()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.ShiftExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.ShiftExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = PrismGramaticaParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.shiftExpression()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0:
                self.state = 150
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.shiftExpression()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.AdditiveExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_shiftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpression" ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpression" ):
                listener.exitShiftExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftExpression" ):
                return visitor.visitShiftExpression(self)
            else:
                return visitor.visitChildren(self)




    def shiftExpression(self):

        localctx = PrismGramaticaParser.ShiftExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_shiftExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.additiveExpression()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.additiveExpression()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.MultiplicativeExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = PrismGramaticaParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.multiplicativeExpression()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 166
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 167
                self.multiplicativeExpression()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.UnaryExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = PrismGramaticaParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.unaryExpression()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0:
                self.state = 174
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self.unaryExpression()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_arrayExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpression" ):
                listener.enterArrayExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpression" ):
                listener.exitArrayExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpression" ):
                return visitor.visitArrayExpression(self)
            else:
                return visitor.visitChildren(self)




    def arrayExpression(self):

        localctx = PrismGramaticaParser.ArrayExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(PrismGramaticaParser.T__22)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 32993343963136) != 0:
                self.state = 182
                self.expressionList()


            self.state = 185
            self.match(PrismGramaticaParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = PrismGramaticaParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expression()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 188
                self.match(PrismGramaticaParser.T__24)
                self.state = 189
                self.expression()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.UnaryExpressionContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = PrismGramaticaParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 202113024) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.unaryExpression()
                pass
            elif token in [23, 28, 30, 31, 32, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.primaryExpression()
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


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(PrismGramaticaParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(PrismGramaticaParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,0)


        def arrayExpression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ArrayExpressionContext,0)


        def functionExpression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.FunctionExpressionContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = PrismGramaticaParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primaryExpression)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 31, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.literal()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.identifier()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.match(PrismGramaticaParser.T__27)
                self.state = 203
                self.expression()
                self.state = 204
                self.match(PrismGramaticaParser.T__28)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.arrayExpression()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.functionExpression()
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(PrismGramaticaParser.NumericLiteralContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(PrismGramaticaParser.StringLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(PrismGramaticaParser.BooleanLiteralContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = PrismGramaticaParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.numericLiteral()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.stringLiteral()
                pass
            elif token in [30, 31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.booleanLiteral()
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


    class NumericLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PrismGramaticaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PrismGramaticaParser.FLOAT, 0)

        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteral" ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = PrismGramaticaParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
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


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PrismGramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteral(self):

        localctx = PrismGramaticaParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(PrismGramaticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLiteral" ):
                return visitor.visitBooleanLiteral(self)
            else:
                return visitor.visitChildren(self)




    def booleanLiteral(self):

        localctx = PrismGramaticaParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PrismGramaticaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = PrismGramaticaParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(PrismGramaticaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.IdentifierContext,i)


        def blockStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = PrismGramaticaParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(PrismGramaticaParser.T__31)
            self.state = 224
            self.identifier()
            self.state = 225
            self.match(PrismGramaticaParser.T__27)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 226
                self.identifier()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 227
                    self.match(PrismGramaticaParser.T__24)
                    self.state = 228
                    self.identifier()
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 236
            self.match(PrismGramaticaParser.T__28)
            self.state = 237
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.BlockStatementContext,0)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.IdentifierContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_functionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpression" ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpression" ):
                listener.exitFunctionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpression" ):
                return visitor.visitFunctionExpression(self)
            else:
                return visitor.visitChildren(self)




    def functionExpression(self):

        localctx = PrismGramaticaParser.FunctionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(PrismGramaticaParser.T__31)
            self.state = 240
            self.match(PrismGramaticaParser.T__27)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 241
                self.identifier()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 242
                    self.match(PrismGramaticaParser.T__24)
                    self.state = 243
                    self.identifier()
                    self.state = 248
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 251
            self.match(PrismGramaticaParser.T__28)
            self.state = 252
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(PrismGramaticaParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = PrismGramaticaParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(PrismGramaticaParser.T__32)
            self.state = 255
            self.identifier()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 256
                self.match(PrismGramaticaParser.T__1)
                self.state = 257
                self.expression()


            self.state = 260
            self.match(PrismGramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,0)


        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.BlockStatementContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = PrismGramaticaParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(PrismGramaticaParser.T__33)
            self.state = 263
            self.match(PrismGramaticaParser.T__27)
            self.state = 264
            self.expression()
            self.state = 265
            self.match(PrismGramaticaParser.T__28)
            self.state = 266
            self.blockStatement()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 267
                self.match(PrismGramaticaParser.T__34)
                self.state = 268
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = PrismGramaticaParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(PrismGramaticaParser.T__35)
            self.state = 272
            self.match(PrismGramaticaParser.T__27)
            self.state = 273
            self.expression()
            self.state = 274
            self.match(PrismGramaticaParser.T__28)
            self.state = 275
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,i)


        def blockStatement(self):
            return self.getTypedRuleContext(PrismGramaticaParser.BlockStatementContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(PrismGramaticaParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = PrismGramaticaParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(PrismGramaticaParser.T__36)
            self.state = 278
            self.match(PrismGramaticaParser.T__27)
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 279
                self.variableDeclaration()
                pass
            elif token in [18, 19, 23, 26, 27, 28, 30, 31, 32, 41, 42, 43, 44]:
                self.state = 280
                self.expression()
                pass
            elif token in [1]:
                pass
            else:
                pass
            self.state = 283
            self.match(PrismGramaticaParser.T__0)
            self.state = 284
            self.expression()
            self.state = 285
            self.match(PrismGramaticaParser.T__0)
            self.state = 286
            self.expression()
            self.state = 287
            self.match(PrismGramaticaParser.T__28)
            self.state = 288
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrismGramaticaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = PrismGramaticaParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(PrismGramaticaParser.T__37)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 32993343963136) != 0:
                self.state = 291
                self.expression()


            self.state = 294
            self.match(PrismGramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrismGramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(PrismGramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return PrismGramaticaParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = PrismGramaticaParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(PrismGramaticaParser.T__38)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 33500150104064) != 0:
                self.state = 297
                self.statement()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
            self.match(PrismGramaticaParser.T__39)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





