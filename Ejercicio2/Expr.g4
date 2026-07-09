grammar Expr;

root : expr EOF;
expr: expr MENOS expr | NUM;
//expr: EOF;
MENOS: '-';
NUM: [0-9]+;
WS : [ \t\r\n]+ -> skip ;