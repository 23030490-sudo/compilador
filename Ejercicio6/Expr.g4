grammar Expr;

//Nombre: Carmen Arreguin
//Número de control: 22031091
//Ejercicio 6: 15 + 3 * 2

root : expr EOF ;

expr : expr MULT expr
     | expr SUM expr
     | NUM
     ;

NUM  : [0-9]+ ;
SUM  : '+' ;
MULT : '*' ;

WS : [ \t\r\n]+ -> skip ;