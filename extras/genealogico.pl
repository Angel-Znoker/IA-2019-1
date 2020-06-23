% Autores
%	Hernández García Luis Angel
%	Vázquez Sanchez Ilse Abril
% genealogico.pl
% Hechos (conocimiento)
hombre(nil).
hombre(carl).
hombre(adam).
hombre(dave).
hombre(fred).
hombre(gustav).

mujer(nil).
mujer(bettina).
mujer(eva).

progenitor(nil,carl).
progenitor(nil,bettina).
progenitor(nil,fred).
progenitor(carl, adam).
progenitor(carl, dave).
progenitor(carl, eva).
progenitor(bettina, adam).
progenitor(bettina, dave).
progenitor(bettina, eva).
progenitor(eva, gustav).
progenitor(fred, gustav).

color(green).
color(yellow).
color(black).
color(blue).
color(pink).
color(brown).

color_ojos(carl, green).
color_ojos(bettina, green).
color_ojos(adam,yellow).
color_ojos(dave, black).
color_ojos(eva, blue).
color_ojos(fred, pink).
color_ojos(gustav, brown).

anio(1926).
anio(1950).
anio(1955).
anio(1965).
anio(1966).
anio(1988).

nacimiento(carl, 1926).
nacimiento(bettina, 1926).
nacimiento(adam, 1950).
nacimiento(dave, 1955).
nacimiento(eva, 1965).
nacimiento(fred, 1966).
nacimiento(gustav, 1988).

% reglas

% operaciones aritméticas utilizadas
suma(X,Y,Z) :- Z is X + Y.
resta(X,Y,Z) :- Z is X - Y.
division(X,Y,Z) :- Z is X / Y.

padre(X, Y) :- hombre(X), progenitor(X, Y).
madre(X, Y) :- mujer(X), progenitor(X, Y).

% ancestro_ojo_azul
% recibe: un nombre de un nodo del arbol
% genera: true si él o alguno de sus progenitores tienen los ojos azules, false en caso contrario
ancestro_ojo_azul(X) :- (color_ojos(X, Y), Y = blue) ; (progenitor(A,X), ancestro_ojo_azul(A)).

% verdadero_ancestro_ojo_azul
% recibe: un nombre de un nodo del arbol
% genera: true sólo si alguno de sus progenitores tiene los ojos azules, false en caso contrario
verdadero_ancestro_ojo_azul(X) :- progenitor(A,X), ancestro_ojo_azul(A).

% contar_personas
% recibe: un nodo, un numero (deseable que sea cero)
% genera: el numero de personas encontradas a partir de dicho nodo
contar_personas(nil,A,A).
contar_personas(X,Y,Z) :- suma(Y,1,A),padre(B,X),contar_personas(B,A,C),madre(D,X),contar_personas(D,C,Z).

% suma_edades
% recibe: un nodo, un numero (deseable cero)
% genera: la suma de las edades a partir del nodo dado
suma_edades(nil,A,A).
suma_edades(X,Y,Z) :- nacimiento(X,A),resta(2018,A,B),suma(Y,B,C),padre(D,X),suma_edades(D,C,E),madre(F,X),suma_edades(F,E,Z).

% edad_promedio
% recibe: un nodo
% genera: el promedio de edades a partir del nodo dado
edad_promedio(nil,0).
edad_promedio(X,Y) :- suma_edades(X,0,A), contar_personas(X,0,B), division(A,B,Y).

% color_ojos
% recibe: un nodo, una lista (preferible vacía)
% genera: una lista con los colores de ojos a partir del nodo de entrada
color_ojos(nil,Y,Y).
color_ojos(X,Y,Z) :- color_ojos(X,A),append(Y,[A],B),padre(C,X),color_ojos(C,B,D),madre(E,X),color_ojos(E,D,Z).