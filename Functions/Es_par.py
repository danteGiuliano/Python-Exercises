# Algoritmo que invoca a la función es_par() pasandole como argumento un número, luego la función verifica si es par o impar el número.
# Retorna una cadena de caracteres que es mostrada por consola.

"Zona de declaración e inicialización de variable"

def es_par(num):
    res = ""
    if num % 2 == 0:
        res = 'El numero es par'
    else:
        res = 'El numero no es par'
    return res

print(es_par(2)) # Muestra por consola el resultado de invocar a la funcion es_par con el argumento 2
print(es_par(11)) # Muestra por consola el resultado de invocar a la funcion es_par con el argumento 11