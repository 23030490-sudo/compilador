grammar Expr16;

//Número de control: 22031091

root
    : sentencia* EOF
    ;

sentencia
    : declaracion
    | impresion
    ;

declaracion
    : LET ID IGUAL valor PUNTO_COMA
    ;

impresion
    : CONSOLE PUNTO LOG PARENTESIS_ABRE valor PARENTESIS_CIERRA PUNTO_COMA
    ;

valor
    : ID
    | NUMERO
    | IDENTIFICADOR_INVALIDO
    ;

LET
    : 'let'
    ;

CONSOLE
    : 'console'
    ;

LOG
    : 'log'
    ;

IGUAL
    : '='
    ;

PUNTO
    : '.'
    ;

PUNTO_COMA
    : ';'
    ;

PARENTESIS_ABRE
    : '('
    ;

PARENTESIS_CIERRA
    : ')'
    ;

//Detecta identificadores incorrectos como: 2numero
IDENTIFICADOR_INVALIDO
    : [0-9]+ [a-zA-Z_]+ [a-zA-Z0-9_]*
    ;

ID
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

NUMERO
    : [0-9]+
    ;

COMENTARIO_LINEA
    : '//' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;