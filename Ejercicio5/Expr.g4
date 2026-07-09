grammar Expr;

root : sentencia+ EOF ;

sentencia : asignacion
          | impresion
          ;

asignacion : ID IGUAL CADENA PC ;

impresion : PRINT ID PC ;

PRINT : 'print' ;
ID : [a-zA-Z]+ ;
CADENA : '"' .*? '"' ;
IGUAL : '=' ;
PC : ';' ;

WS : [ \t\r\n]+ -> skip ;