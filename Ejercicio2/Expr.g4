grammar Expr;
root : expr EOF;
expr : (NUM | RESTA)+ ;
NUM : [0-9]+ ;
RESTA: '-' ;
WS : [ \t\r\n]+ -> skip ;