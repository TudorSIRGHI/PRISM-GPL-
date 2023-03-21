# Generated from C:/Users/tudor/Downloads/University/ELSD\PrismGramatica.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrismGramaticaParser import PrismGramaticaParser
else:
    from PrismGramaticaParser import PrismGramaticaParser

# This class defines a complete listener for a parse tree produced by PrismGramaticaParser.
class PrismGramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by PrismGramaticaParser#program.
    def enterProgram(self, ctx:PrismGramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#program.
    def exitProgram(self, ctx:PrismGramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#statement.
    def enterStatement(self, ctx:PrismGramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#statement.
    def exitStatement(self, ctx:PrismGramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#expression.
    def enterExpression(self, ctx:PrismGramaticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#expression.
    def exitExpression(self, ctx:PrismGramaticaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:PrismGramaticaParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:PrismGramaticaParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#ternaryExpression.
    def enterTernaryExpression(self, ctx:PrismGramaticaParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#ternaryExpression.
    def exitTernaryExpression(self, ctx:PrismGramaticaParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:PrismGramaticaParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:PrismGramaticaParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:PrismGramaticaParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:PrismGramaticaParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#bitwiseOrExpression.
    def enterBitwiseOrExpression(self, ctx:PrismGramaticaParser.BitwiseOrExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#bitwiseOrExpression.
    def exitBitwiseOrExpression(self, ctx:PrismGramaticaParser.BitwiseOrExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#bitwiseXorExpression.
    def enterBitwiseXorExpression(self, ctx:PrismGramaticaParser.BitwiseXorExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#bitwiseXorExpression.
    def exitBitwiseXorExpression(self, ctx:PrismGramaticaParser.BitwiseXorExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#bitwiseAndExpression.
    def enterBitwiseAndExpression(self, ctx:PrismGramaticaParser.BitwiseAndExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#bitwiseAndExpression.
    def exitBitwiseAndExpression(self, ctx:PrismGramaticaParser.BitwiseAndExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#equalityExpression.
    def enterEqualityExpression(self, ctx:PrismGramaticaParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#equalityExpression.
    def exitEqualityExpression(self, ctx:PrismGramaticaParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#relationalExpression.
    def enterRelationalExpression(self, ctx:PrismGramaticaParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#relationalExpression.
    def exitRelationalExpression(self, ctx:PrismGramaticaParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#shiftExpression.
    def enterShiftExpression(self, ctx:PrismGramaticaParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#shiftExpression.
    def exitShiftExpression(self, ctx:PrismGramaticaParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:PrismGramaticaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:PrismGramaticaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:PrismGramaticaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:PrismGramaticaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#arrayExpression.
    def enterArrayExpression(self, ctx:PrismGramaticaParser.ArrayExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#arrayExpression.
    def exitArrayExpression(self, ctx:PrismGramaticaParser.ArrayExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#expressionList.
    def enterExpressionList(self, ctx:PrismGramaticaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#expressionList.
    def exitExpressionList(self, ctx:PrismGramaticaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#unaryExpression.
    def enterUnaryExpression(self, ctx:PrismGramaticaParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#unaryExpression.
    def exitUnaryExpression(self, ctx:PrismGramaticaParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:PrismGramaticaParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:PrismGramaticaParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#literal.
    def enterLiteral(self, ctx:PrismGramaticaParser.LiteralContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#literal.
    def exitLiteral(self, ctx:PrismGramaticaParser.LiteralContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#numericLiteral.
    def enterNumericLiteral(self, ctx:PrismGramaticaParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#numericLiteral.
    def exitNumericLiteral(self, ctx:PrismGramaticaParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#stringLiteral.
    def enterStringLiteral(self, ctx:PrismGramaticaParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#stringLiteral.
    def exitStringLiteral(self, ctx:PrismGramaticaParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:PrismGramaticaParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:PrismGramaticaParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#identifier.
    def enterIdentifier(self, ctx:PrismGramaticaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#identifier.
    def exitIdentifier(self, ctx:PrismGramaticaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PrismGramaticaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PrismGramaticaParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#functionExpression.
    def enterFunctionExpression(self, ctx:PrismGramaticaParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#functionExpression.
    def exitFunctionExpression(self, ctx:PrismGramaticaParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:PrismGramaticaParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:PrismGramaticaParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#ifStatement.
    def enterIfStatement(self, ctx:PrismGramaticaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#ifStatement.
    def exitIfStatement(self, ctx:PrismGramaticaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#whileStatement.
    def enterWhileStatement(self, ctx:PrismGramaticaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#whileStatement.
    def exitWhileStatement(self, ctx:PrismGramaticaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#forStatement.
    def enterForStatement(self, ctx:PrismGramaticaParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#forStatement.
    def exitForStatement(self, ctx:PrismGramaticaParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#returnStatement.
    def enterReturnStatement(self, ctx:PrismGramaticaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#returnStatement.
    def exitReturnStatement(self, ctx:PrismGramaticaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PrismGramaticaParser#blockStatement.
    def enterBlockStatement(self, ctx:PrismGramaticaParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by PrismGramaticaParser#blockStatement.
    def exitBlockStatement(self, ctx:PrismGramaticaParser.BlockStatementContext):
        pass



del PrismGramaticaParser