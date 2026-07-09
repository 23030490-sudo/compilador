grammar Expr;

root : expr EOF;

expr : IF P1 ID MAYORQUE NUM P2;

IF : 'if';
ID : [a-zA-Z]+;
MAYORQUE : '>';
NUM : [0-9]+;
P1 : '(';
P2 : ')';

WS : [ \t\r\n]+ -> skip;