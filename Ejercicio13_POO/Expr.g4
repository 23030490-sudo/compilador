grammar Expr;
root : expr EOF;
expr : EOF;
CREATE  : 'CREATE';
TABLE   : 'TABLE';
SERIAL  : 'SERIAL';
PRIMARY : 'PRIMARY';
KEY     : 'KEY';
VARCHAR : 'VARCHAR';
NOT     : 'NOT';
NULL    : 'NULL';
INTEGER : 'INTEGER';
DATE    : 'DATE';

INSERT  : 'INSERT';
INTO    : 'INTO';
VALUES  : 'VALUES';

SELECT  : 'SELECT';
FROM    : 'FROM';
INNER   : 'INNER';
JOIN    : 'JOIN';
ON      : 'ON';
WHERE   : 'WHERE';

IGUAL      : '=';
PUNTO_COMA : ';';
PAR_A      : '(';
PAR_C      : ')';
COMA       : ',';
PUNTO      : '.';

ID   : [a-zA-Z_][a-zA-Z0-9_]*;
NUM  : [0-9]+;
STRING_LIT : '\'' (~['\r\n])* '\'';

WS   : [ \t\r\n]+ -> skip;