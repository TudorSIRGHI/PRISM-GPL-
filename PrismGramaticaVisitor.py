# Generated from C:/Users/tudor/Downloads/University/ELSD\PrismGramatica.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrismGramaticaParser import PrismGramaticaParser
else:
    from PrismGramaticaParser import PrismGramaticaParser

# This class defines a complete generic visitor for a parse tree produced by PrismGramaticaParser.

class PrismGramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrismGramaticaParser#program.
    def visitProgram(self, ctx:PrismGramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#statement.
    def visitStatement(self, ctx:PrismGramaticaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#expression.
    def visitExpression(self, ctx:PrismGramaticaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:PrismGramaticaParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#ternaryExpression.
    def visitTernaryExpression(self, ctx:PrismGramaticaParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:PrismGramaticaParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:PrismGramaticaParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#bitwiseOrExpression.
    def visitBitwiseOrExpression(self, ctx:PrismGramaticaParser.BitwiseOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#bitwiseXorExpression.
    def visitBitwiseXorExpression(self, ctx:PrismGramaticaParser.BitwiseXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#bitwiseAndExpression.
    def visitBitwiseAndExpression(self, ctx:PrismGramaticaParser.BitwiseAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#equalityExpression.
    def visitEqualityExpression(self, ctx:PrismGramaticaParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#relationalExpression.
    def visitRelationalExpression(self, ctx:PrismGramaticaParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#shiftExpression.
    def visitShiftExpression(self, ctx:PrismGramaticaParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:PrismGramaticaParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:PrismGramaticaParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#arrayExpression.
    def visitArrayExpression(self, ctx:PrismGramaticaParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#expressionList.
    def visitExpressionList(self, ctx:PrismGramaticaParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#unaryExpression.
    def visitUnaryExpression(self, ctx:PrismGramaticaParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:PrismGramaticaParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#literal.
    def visitLiteral(self, ctx:PrismGramaticaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#numericLiteral.
    def visitNumericLiteral(self, ctx:PrismGramaticaParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#stringLiteral.
    def visitStringLiteral(self, ctx:PrismGramaticaParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:PrismGramaticaParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#identifier.
    def visitIdentifier(self, ctx:PrismGramaticaParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:PrismGramaticaParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#functionExpression.
    def visitFunctionExpression(self, ctx:PrismGramaticaParser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:PrismGramaticaParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#ifStatement.
    def visitIfStatement(self, ctx:PrismGramaticaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#whileStatement.
    def visitWhileStatement(self, ctx:PrismGramaticaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#forStatement.
    def visitForStatement(self, ctx:PrismGramaticaParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#returnStatement.
    def visitReturnStatement(self, ctx:PrismGramaticaParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismGramaticaParser#blockStatement.
    def visitBlockStatement(self, ctx:PrismGramaticaParser.BlockStatementContext):
        return self.visitChildren(ctx)



del PrismGramaticaParser