grammar Expr3;

root : (elemento)* EOF ;

elemento : PUBLIC | CLASS | STATIC | VOID | STRING | INT | SYSTEM | IF
         | ID
         | CADENA | NUM
         | ASIGNACION | MAYORIGUAL | MAS | PUNTO
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
IF : 'if' ;

// Identificadores (Main, main, args, edad, adulto, out, println, etc.)
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// Cadenas (permite cualquier caracter, incluidos acentos y signos ¿ ?, menos salto de línea)
CADENA : '"' ~["\r\n]* '"' ;

// Números
NUM : [0-9]+ ;

// Operadores (el de 2 caracteres SIEMPRE antes que el de 1)
MAYORIGUAL : '>=' ;
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