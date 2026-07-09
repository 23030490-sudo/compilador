grammar Expr3;

root : (elemento)* EOF ;

elemento : PUBLIC | CLASS | STATIC | VOID | STRING | INT | SYSTEM | NEW | THIS | RETURN
         | ID
         | CADENA | NUM
         | ASIGNACION | MAS | PUNTO
         | PC
         | PARENTESIS1 | PARENTESIS2
         | LLAVE1 | LLAVE2
         | CORCHETE1 | CORCHETE2
         ;

// Palabras clave (van ANTES que ID para tener prioridad)
PUBLIC : 'public' ;
CLASS : 'class' ;
STATIC : 'static' ;
VOID : 'void' ;
STRING : 'String' ;
INT : 'int' ;
SYSTEM : 'System' ;
NEW : 'new' ;
THIS : 'this' ;
RETURN : 'return' ;

// Identificadores (Main, main, args, Calculadora, calc, numero1, numero2, sumar, resultado, out, println)
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// Cadenas
CADENA : '"' ~["\r\n]* '"' ;

// Números
NUM : [0-9]+ ;

// Operadores
ASIGNACION : '=' ;
MAS : '+' ;
PUNTO : '.' ;

// Símbolos
PC : ';' ;
PARENTESIS1 : '(' ;
PARENTESIS2 : ')' ;
LLAVE1 : '{' ;
LLAVE2 : '}' ;
CORCHETE1 : '[' ;
CORCHETE2 : ']' ;

// Espacios en blanco
WS : [ \t\r\n]+ -> skip ;