grammar Expr;

root : expr EOF;

expr : NUM ; 

NUM: [0-9]+;
MAS: '+';
WS: [ \t\r\n]+ -> skip ;