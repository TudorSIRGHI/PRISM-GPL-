grammar PrismGramatica;

// Lexer rules
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]* '.' [0-9]+;
STRING : '"' (ESC | ~["\\])* '"' ;
ESC : '\\' ["\\/bfnrt] ;
WS: [ \t\n\r]+ -> skip;

// Rules
program : statement* EOF ;
statement : expression ';'
          | variableDeclaration
          | ifStatement
          | whileStatement
          | forStatement
          | functionDeclaration
          | returnStatement
          ;
expression : assignmentExpression ;
assignmentExpression : ternaryExpression ('=' ternaryExpression)* ;
ternaryExpression : logicalOrExpression ('?' expression ':' expression)? ;
logicalOrExpression : logicalAndExpression ('||' logicalAndExpression)* ;
logicalAndExpression : bitwiseOrExpression ('&&' bitwiseOrExpression)* ;
bitwiseOrExpression : bitwiseXorExpression ('|' bitwiseXorExpression)* ;
bitwiseXorExpression : bitwiseAndExpression ('^' bitwiseAndExpression)* ;
bitwiseAndExpression : equalityExpression ('&' equalityExpression)* ;
equalityExpression : relationalExpression (('==' | '!=') relationalExpression)* ;
relationalExpression : shiftExpression (('<' | '<=' | '>' | '>=') shiftExpression)* ;
shiftExpression : additiveExpression (('<<' | '>>') additiveExpression)* ;
additiveExpression : multiplicativeExpression (('+' | '-') multiplicativeExpression)* ;
multiplicativeExpression : unaryExpression (('*' | '/' | '%') unaryExpression)* ;
arrayExpression: '[' expressionList? ']';

expressionList: expression (',' expression)*;
unaryExpression : ('+' | '-' | '!' | '~') unaryExpression
                 | primaryExpression ;
primaryExpression : literal
                   | identifier
                   | '(' expression ')'
                   | arrayExpression
                   | functionExpression
                   ;
literal : numericLiteral
        | stringLiteral
        | booleanLiteral
        ;
numericLiteral : INT | FLOAT ;
stringLiteral : STRING ;
booleanLiteral : 'true' | 'false' ;
identifier : IDENTIFIER ;


functionDeclaration : 'function' identifier '(' (identifier (',' identifier)*)? ')' blockStatement ;
functionExpression : 'function' '(' (identifier (',' identifier)*)? ')' blockStatement ;
variableDeclaration : 'var' identifier ('=' expression)? ';' ;
ifStatement : 'if' '(' expression ')' blockStatement ('else' blockStatement)? ;
whileStatement : 'while' '(' expression ')' blockStatement ;
forStatement : 'for' '(' (variableDeclaration | expression)? ';' expression ';' expression ')' blockStatement ;
returnStatement : 'return' expression? ';' ;
blockStatement : '{' statement* '}' ;



