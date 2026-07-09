grammar Expr;

//Nombre: Carmen Arreguin
//Número de control: 22031091
//Ejercicio 7: int total = 100

root : expr EOF ;

expr : INT IDT ASIG NUM ;

INT  : 'int' ;
IDT  : [a-zA-Z]+ ;
ASIG : '=' ;
NUM  : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;