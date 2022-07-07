#!/usr/bin/f python
# -*- coding: utf-8 -*-
#crashbit

from sys import argv
import itertools
from os import remove
from random import choice


def hace_lista(archivo):
    '''
    Funcion que convierte un archivo en una lista
    Recibe un archivo y regresa una lista. cuyo elementos son cada line a del archivo
    '''
    lista=[]
    with open(archivo, 'r') as convierte:
        for linea in convierte:
            lista.append(linea.replace('\n',''))
    return lista

def permuta(lista):
    '''
    Funcion que obtiene las permutaciones de los elementos de una lista
    Recibe una lista y obtiene la permutación de dos elementos de ésta guardando la permutación en un archivo temporal
    '''
    f1=open('temp.txt','w')
    #for i in range(1,len(lista)+1):
    #for i in range(1,4):
    for i in range(1,4):
        aux=list(itertools.permutations(lista,i))
        for j in aux:
            aux2=' '.join(j)
            f1.write(aux2+ '\n')
    f1.close()


def permuta_mayus_minus():
    '''
    Funcion que obtiene todas las combinaciones de una cadena, entre sus minusculas y sus mayusculas
    No recibe argumentos, pero lee el contenido del archivo temporal creado por la funcion permuta para hacer el producto cartesiano de cada palabra econtrada ahí, el producto se hace entre la palabra en minusculas contra la palabra en mayusculas.
    El resultado del producto lo almacena en otro archivo temporal llamado: 'temp2.txt'
    '''
    with open('temp.txt', 'r') as f1_temp:
        with open('temp2.txt','w') as f2_temp2:
            for linea in f1_temp.readlines():
                cadena=linea.replace('\n','')
                lista=map(''.join, itertools.product(*((x.upper(), x.lower()) for x in cadena)))
                lista2=list(set(lista))
                for elemento in lista2:
                    f2_temp2.write(''.join(elemento)+'\n')

def cambia_numeros():
    '''
    Funcion que reemplaza las vocales por numeros
    Lee el contenido del archivo temporal 'temp.txt' y cambia las vocales por numeros y el resultado lo agrega al archivo temporal 'temp2.txt'
    '''
    cads_numeros=[]
    with open('temp.txt','r') as f_temp:
        for linea in f_temp.readlines():
            linea2=linea.replace('\n','').replace('a','4').replace('e','3').replace('i','1').replace('o','0')
            cads_numeros.append(linea2)
            cads_numeros=list(set(cads_numeros))
    #print cads_numeros
    for cadena in cads_numeros: 
        lista2=map(''.join, itertools.product(*((x.upper(), x.lower()) for x in cadena)))
        lista2=list(set(lista2))
        with open('temp2.txt','a') as f_temp2:
            for cadena in lista2:
                f_temp2.write(cadena+'\n')
    remove('temp.txt')


def cambia_espacios():
    '''
    Funcion que reemplaza espacios por caracteres aleatoriamente
    Lee el archivo 'temp2.txt' y escribe todo su contenido en un archivo nuevo
    llamado 'diccionario.txt' y vuelve a tomar ese contenido y escribe pero cambiando los espacios aleatoriamente
    '''
    chars=['@','#','$','.',',','%','&']
    cadena=''
    with open('temp2.txt','r') as f_temp2:
        with open('diccionario.txt','w') as f_diccionario:
            for linea in f_temp2.readlines():
                f_diccionario.write(linea)
    with open('temp2.txt','r') as f_temp2:
        with open('diccionario.txt','a') as f_diccionario:
            for linea in f_temp2.readlines():
                for char in linea:
                    if char==' ':
                        cadena+=choice(chars)
                    else:
                        cadena+=char
                f_diccionario.write(cadena)
                cadena=''
    remove('temp2.txt')





lista2=hace_lista(argv[1])
permuta(lista2)
permuta_mayus_minus()
cambia_numeros()
cambia_espacios()
