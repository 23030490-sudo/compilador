grammar Expr15;

//Número de control: 22031091

root
    : linea* EOF
    ;

linea
    : comando
    ;

comando
    : SUDO? NMAP opcion* valor*
    | SS opcion*
    | SUDO? TCPDUMP opcion* valor*
    | CURL opcion* valor*
    | DIG valor*
    | JOURNALCTL opcion* valor*
    | GREP CADENA valor*
    | SUDO? UFW valor*
    ;

SUDO : 'sudo';
NMAP : 'nmap';
SS : 'ss';
TCPDUMP : 'tcpdump';
CURL : 'curl';
DIG : 'dig';
JOURNALCTL : 'journalctl';
GREP : 'grep';
UFW : 'ufw';

OPCION_CORTA
    : '-' [a-zA-Z]+
    ;

OPCION_LARGA
    : '--' [a-zA-Z]+
    ;

RANGO_IP
    : NUMERO '.' NUMERO '.' NUMERO '.' NUMERO '/' NUMERO
    ;

IP
    : NUMERO '.' NUMERO '.' NUMERO '.' NUMERO
    ;

RUTA
    : '/' [a-zA-Z0-9_./-]+
    ;

DOMINIO
    : [a-zA-Z0-9_-]+ '.' [a-zA-Z]+
    ;

CADENA
    : '"' .*? '"'
    ;

PALABRA
    : [a-zA-Z0-9_:-]+
    ;

NUMERO
    : [0-9]+
    ;

opcion
    : OPCION_CORTA
    | OPCION_LARGA
    ;

valor
    : RANGO_IP
    | IP
    | RUTA
    | DOMINIO
    | CADENA
    | PALABRA
    | NUMERO
    ;

COMENTARIO_LINEA
    : '#' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;