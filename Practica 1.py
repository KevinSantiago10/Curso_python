#Introducción al manejo de datos en Python con pandas
    #numpy: varialbes nuemricas
    #pandas: variables numéricas y categoricas

#Variable de texto
mi_variable = "La vida esta aquí y yo quiero aca"
print(mi_variable)
#Lista de número
mi_lista = [1,2,3,4,5]
print(mi_lista)

#----//Diccionario//---- dan una etiquta a un valor, ej: hombre=1, mujer=2
mi_diccionario = {"clave_1" : "valor1", "clave_2": "valor2", "clave_3": "valor3"}
print(mi_diccionario)

# NUMÉRICA
vector_enteros = [10]*5
print(vector_enteros)

vector_flotante = [3.14]*5
print(vector_flotante)

diccionario = {"entero": vector_enteros, "flotante": vector_flotante, "complejo": vector_flotante}
print(diccionario)

# CADENAS
cadena_simple = "Harvey Specter"
cadena_doble = ["Python es poderoso", "Mike Ross"]           #contiene 2 variables de texto
print(cadena_doble)



###----///Dataframe: tiene dos dimensiones de datos, puede ser flotante, int:entero
            #simpre inicia de un cero 0
            #Usamos libreria panda
            #importar libreria pandas, pd es para llamar a la liberira
import pandas as pd

#crear un Data frame con los datos de rendimiento en juegos
# Crear un DataFrame con los datos de rendimiento en juegos
datos = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Ana'],
    'Juego 1 (puntos)': [150, 180, 130, 200],
    'Juego 2 (puntos)': [120, 90, 110, 150],
    'Juego 3 (puntos)': [200, 160, 180, 190]
}

df = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df)



