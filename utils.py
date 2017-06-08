#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from time import time
from collections import defaultdict

from sklearn.feature_extraction.text import CountVectorizer

t=time()
def calcall():
    LETTER =''.join([string.letters, unicode('ñ,Ñ','utf8')])
    doc1=None
    doc2=None
    idioma='spanish'
    array=defaultdict(list)
    respuesta=defaultdict(list)
    f = open("msr_paraphrase_train.arff", "w+")#permite leer y escribir al mismo tiempo
    with open('doc/msr_paraphrase_train.txt','r') as doc:
        for i,line in enumerate(doc):
            for param in line.split('\t'):
                array[i].append(param)
            tmp=array[i][0]
            s1=array[i][3]
            s2=array[i][4]
            respuesta[i].append(medidas.funcion(s1, s2, doc1, doc2))
            cadena=str(respuesta[i][0])[1:len(str(respuesta[i][0]))-1]+", "+tmp+'\n'#borra solo los extremos parentisis
            print (i,cadena)  #imprime los arreglos uno debajo de otro
            f.write(cadena)
        return respuesta #copiar los resultados para un arreglo separados por coma

def string2vector(s1,s2):
    count_v = CountVectorizer()
    tdm = count_v.fit_transform([s1, s2])
    s1 = tdm[0].toarray()
    s2 = tdm[1].toarray()
    return s1,s2

def bigrams(s):
    return set(s[i:i+2] for i in range(len(s)-1))

if __name__ == '__main__':
    print (ts)
    print (time()-t)
