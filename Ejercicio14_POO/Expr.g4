grammar Expr;
root : expr EOF;
expr : EOF;
UPDATE  : 'UPDATE';
SET     : 'SET';
WHERE   : 'WHERE';
IGUAL      : '=';
COMA       : ',';
PUNTO_COMA : ';';
ID   : [a-zA-Z_][a-zA-Z0-9_]*;
NUM  : [0-9]+;
STRING_LIT : '\'' (~['’\r\n])* ('\'' | '’') ;

WS   : [ \t\r\n]+ -> skip ;