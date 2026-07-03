grammar Expr;
root : expr EOF;
expr : EOF;
PRINT : 'print';
ID : [a-zA-Z]+;
CADENA : '"' .*? '"';
IGUAL: '=';
WS : [ \t\r\n]+ -> skip ;