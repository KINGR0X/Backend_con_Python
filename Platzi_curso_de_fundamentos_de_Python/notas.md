## Clase 4- Comentarios largos

- Para los comentarios largos usamos:

  ```python
  """
  Comentario largo
  de
  varias
  lineas
  """
  ```

---

## clase 6- Variables

- Para concatenar palabras y variables en python lo podemos ahcer de la siguiente manera:

```python
print("aqui cambio el nombre a:", my_name)
```

## Clase 23- indexing

- Indexing devuelve la posición que se le pasa, para que devuelve el caracter de esa posición. Ej:

```python
text= "Ella sabe Python"
print(text[0])
print(text[1])
```

Salida:

```terminal
E
l
```

- Para acceder a la ultima posisión de por ejemplo la función index, e imprimir el caracter de esa posicion usariamos len(texto)-1, pero existe una forma más facil en python:

```python
print(text[-1])
```

salida:

```terminal
n
```

## Clase 26- Metodos de listas

- append(): Añade un ítem al final de la lista.
- clear(): Vacía todos los ítems de una lista.
- extend(): Une una lista a otra.
- count(): Cuenta el número de veces que aparece un ítem.
- index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
- insert(): Agrega un ítem a la lista en un índice específico.
- pop(): Extrae un ítem de la lista y lo borra.
- remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
- reverse(): Le da la vuelta a la lista actual.
- sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

ejemplo eindex:

```python
lista= ["hola","mundo"]
index= lista.index("hola")
print("index =>",index)
```

salida:

```Terminal
index => 1
```

## Clase 27 - Tuplas

La diferencia con las tuplas con las listas es que no se pueden agregar nuevos elementos, eliminar, o editar al final, porque son no modificables

Las tuplas son utiles cuando no se necesitan modificar elementos, porque no se necesitan más datos o opciones, como por ejemplo en un juego de piedra, papel, o tijera, donde siempre tendra 3 opciones.

## Clase 29 - Diccionarios

Un diccionarios tienen una llave y un valor, ambas pueden ser de diferentes tipos, no es extrictamente necesario que la llave del diccionario sea un valor numerioc ej:

```python
my_dic={
  "avion": "bla bla bla",
  "name" : "Nicolas",
  "las_name" : "Molina",
  "age" : 87
}

```

- al momento de buscar un valor se hace usando la llave.
- Dentro de los diccionarios pueden haber listas
