grammar Expr;

root : PRINT P1 CADENA P2 EOF ;

PRINT : 'Print' ;
P1 : '(' ;
P2 : ')' ;

CADENA : '"' ~["\r\n]* '"' ;

WS : [ \t\r\n]+ -> skip ;