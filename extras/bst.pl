% Autores:
%	Hernández García Luis Angel
%	Vázquez Sanchez Ilse Abril

% creararbol: crea un arbol con numeros dados en una lista
% recibe una lista con numeros y un árbol que puede ser vacío (nil)
% genera el arbol con los datos de la lista
creararbol([], A, A).
creararbol([N|R], A, Y) :- insertar(N, A, B), creararbol(R, B, Y).


% insertar
% recibe un numero, un arbol, que puede ser vacío nil
% genera el arbol con el nuevo dato agregado
% tres casos:
% 1: insertar(nuevo valor, vacio, arbol con el nuevo valor como raiz)
insertar(N, nil, a(N, nil, nil)).
% 2: nuevo valor igual a raiz, se queda igual
insertar(N, a(N, I, D), a(N, I, D)).
% 3: nuevo valor diferente a raiz
% 		insertar(nuevo valor, arbol con datos, arbol con el nuevo dato) :- comparación, llamada recursiva, asignación
insertar(N, a(X, I, D), a(A, B, C)) :- N < X, insertar(N, I, Y), (B, A, C) = (Y, X, D).
insertar(N, a(X, I, D), a(A, B, C)) :- N > X, insertar(N, D, Y), (B, A, C) = (I, X, Y).


% buscar
% recibe un numero y un arbol con datos
% devuelve true o false, dependiendo de la existencia del numero en el arbol
% 1: el valor buscado está en la raiz, se encontró
buscar(X, a(X, _, _)).
% 2: el valor es menor a la raiz, se busca por la izquierda
buscar(X, a(Y, I, _)) :- X < Y, buscar(X, I).
% 3: el valor es mayor a la raiz, se busca por la derecha
buscar(X, a(Y, _, D)) :- X > Y, buscar(X, D).


% eliminar
% recibe un numero y un arbol
% devuelve el arbol sin el numero indicado
% 1: si el numero no esta en la raiz y ya no hay más hojas
eliminar(N,a(X,nil,nil),a(X,nil,nil)) :- N \= X.
% 2: si el numero esta en la raiz y solo tiene un hijo
eliminar(N,a(N,nil,D),D).
eliminar(N,a(N,I,nil),I).
% 3: Si el numero es mayor o menor a la raiz
eliminar(N,a(X,I,D),a(X,I,ND)) :- N > X, eliminar(N,D,ND).
eliminar(N,a(X,I,D),a(X,NI,D)) :- N < X, eliminar(N,I,NI).
% si el numero esta en la raiz y tiene ambos hijos, se busca el numero más a la izquierda (numero consecutivo
% en orden ascendente) del que se va a eliminar para reemplazarlo
eliminar(N,a(N,I,D),a(X,I,ND)) :- obtenerMasIzq(D,X), eliminar(X,D,ND).


% obtiene el nodo más a la izquierda de un arbol
% recibe un arbol
% devuelve el valor del nodo más a la izquierda
obtenerMasIzq(a(N,nil,_),N).
obtenerMasIzq(a(_,I,_),X) :- obtenerMasIzq(I,X).

%recorridos
% recibe un arbol (que puede ser vacío), una lista ([] o con datos)
% devuelve la lista con los numeros ordenados 
preorden(nil,A,A).
preorden(a(X,I,D),A,Y) :- append(A,[X],B), preorden(I,B,C), preorden(D,C,Y).

% recibe un arbol (que puede ser vacío), una lista ([] o con datos)
% devuelve la lista con los numeros ordenados 
inorden(nil,A,A).
inorden(a(X,I,D),A,Y) :- inorden(I,A,B), append(B,[X],C), inorden(D,C,Y).

% recibe un arbol (que puede ser vacío), una lista ([] o con datos)
% devuelve la lista con los numeros ordenados 
postorden(nil,A,A).
postorden(a(X,I,D),A,Y) :- postorden(I,A,B), postorden(D,B,C), append(C,[X],Y).


% ejemplos:
% ?- creararbol([7,5,9,2,6,8,12,3,10],nil,Y).
% Y = a(7, a(5, a(2, nil, a(3, nil, nil)), a(6, nil, nil)), a(9, a(8, nil, nil), a(12, a(10, nil, nil), nil)))

% ?- insertar(13, a(7,a(5,a(2,nil,a(3,nil,nil)),a(6,nil,nil)),a(9,a(8,nil,nil),a(12,a(10,nil,nil),nil))), Y).
% Y = a(7, a(5, a(2, nil, a(3, nil, nil)), a(6, nil, nil)), a(9, a(8, nil, nil), a(12, a(10, nil, nil), a(13, nil, nil))))

% ?- eliminar(9, a(7,a(5,a(2,nil,a(3,nil,nil)),a(6,nil,nil)),a(9,a(8,nil,nil),a(12,a(10,nil,nil),nil))), Y).
% Y = a(7, a(5, a(2, nil, a(3, nil, nil)), a(6, nil, nil)), a(10, a(8, nil, nil), a(12, nil, nil)))

% ?- preorden(a(7,a(5,a(2,nil,a(3,nil,nil)),a(6,nil,nil)),a(9,a(8,nil,nil),a(12,a(10,nil,nil),nil))), [], Y).
% Y = [7, 5, 2, 3, 6, 9, 8, 12, 10].

% ?- inorden(a(7,a(5,a(2,nil,a(3,nil,nil)),a(6,nil,nil)),a(9,a(8,nil,nil),a(12,a(10,nil,nil),nil))), [], Y).
% Y = [2, 3, 5, 6, 7, 8, 9, 10, 12].

% ?- postorden(a(7,a(5,a(2,nil,a(3,nil,nil)),a(6,nil,nil)),a(9,a(8,nil,nil),a(12,a(10,nil,nil),nil))), [], Y).
% Y = [3, 2, 6, 5, 8, 10, 12, 9, 7].