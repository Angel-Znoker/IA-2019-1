% Hechos (conocimiento)

nivel(animal).
nivel(ave).
nivel(pez).
nivel(canario).
nivel(avestruz).

caracteristica(respira).
caracteristica(piel).
caracteristica(movimiento).
caracteristica(vuelo).
caracteristica(alas).
caracteristica(plumas).
caracteristica(canta).
caracteristica(amarillo).
caracteristica(alta).
caracteristica(no_vuelo).

pertenece(animal,ave).
pertenece(animal,pez).
pertenece(ave,canario).
pertenece(ave,avestruz).

tiene_es(animal,respira).
tiene_es(animal,piel).
tiene_es(animal,movimiento).
tiene_es(ave,alas).
tiene_es(ave,plumas).
tiene_es(canario,canta).
tiene_es(canario,amarillo).
tiene_es(canario,vuelo).
tiene_es(avestruz,no_vuelo).
tiene_es(avestruz,alta).

% Reglas

% caracteristicas
% Recibe: un nodo de la red semantica
% devuelve: todas las caracteristicas del nodo, particulares y generales
caracteristicas(X,Y) :- tiene_es(X,Y).
caracteristicas(X,Y) :- pertenece(A,X), caracteristicas(A,Y).