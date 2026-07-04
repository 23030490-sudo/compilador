grammar Expr;

//Nombre: Carmen Arreguin
//Número de control: 22031091
//Ejercicio 6: 15 + 3 * 2

root : expr EOF ;

expr : NUM SUM NUM MULT NUM ;

NUM  : [0-9]+ ;
SUM  : '+' ;
MULT : '*' ;

WS : [ \t\r\n]+ -> skip ;