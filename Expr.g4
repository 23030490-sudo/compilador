grammar Expr;

root : IF P1 ID MAYORQUE NUM P2 EOF ;

IF : 'if' ;
ID : [a-zA-Z]+ ;
MAYORQUE : '>' ;
NUM : [0-9]+ ;
P1 : '(' ;
P2 : ')' ;

WS : [ \t\r\n]+ -> skip ;