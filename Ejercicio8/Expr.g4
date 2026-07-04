grammar Expr;

//Nombre: Carmen Arreguin
//Número de control: 22031091
//Ejercicio 8: edad >= 18

root : expr EOF ;

expr : IDT CON NUM ;

IDT : [a-zA-Z]+ ;
CON : '>=' ;
NUM : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;