grammar Expr;
root : expr EOF;
expr: EOF;

WS : [ \t\r\n]+ -> skip ;