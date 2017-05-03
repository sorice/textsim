#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
String Similarity Distances
==================================

Based on term/token similarity calculations.

"""

__author__ = 'Pablo'

import nltk
import math
import stringdists

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as ws

def tfidf(t, d, D):
    tf = float(d.count(t)) / sum(d.count(w) for w in set(d))
    idf =math.log10(float(len(D)) /(1+(len([doc for doc in D if t in doc]))))
    return tf * idf

#Obtiene un peso para un termino a traves de la frecuencia en el documento
def tf(t,d):
    return float(d.count(t)) / float(sum(d.count(w) for w in set(d)))

#metodo auxiliar para calcular la longitud de un texto
def len_texto(direccion_doc,idioma):
    if direccion_doc is None:
        return 0
    else:
        input_file=open(direccion_doc,'r')
        v1=input_file.read()
        d1=set(self.stop_words(word_tokenize(v1),idioma))
        return len(d1)
    
#metodo para eliminar palabras vacias de un texto
def stop_words(texto_arreglo,idioma = 'english'):
    palabra_vacia = set(stopwords.words(idioma))
    return [word for word in texto_arreglo if word not in palabra_vacia]

def preprocesamiento(s1,s2,idioma='english'):
    c1=s1.lower()
    c2=s2.lower()
    d1=set(self.stop_words(word_tokenize(c1),idioma))#filtrado del texto
    d2=set(self.stop_words(word_tokenize(c2),idioma))#filtrado del texto
    return d1,d2
 
def leer(doc1,doc2):
    input_file=open(doc1,'r')
    input_file1=open(doc2,'r')
    s1=input_file.read()
    s2=input_file1.read()
    return s1,s2 

#***************************************************************************

#****************************************************************************
#similitudes basadas en terminos

def matching_coefficient(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    Medida de similitud basada en vectores. Similar a la distancia de Hamming pero
    esta debe ser entre vectores de igual longitud. Esta distancia va a devolver un
    valor entre [0-x] donde cuanto menor sea la distancia entre los vectores mas
    semejanza existira por lo que su valor tendera a 0.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor 
    similitud.
    Esta operacion se realizo dividiendo entre la longitud de la cadena mas larga y restando el resultado 
    con 1 para invertir el orden a que esta tendiendo
    
                   (|x|-|x∩y|)
    M(x,y) = 1 -  -----------------
                   max_longitud(x,y)
    
    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> matching_coefficient(x, y, "", "",idioma) ==  0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    #Condicion necesaria para el algoritmo los vectores deben ser de la misma longitud, utiliza un metodo auxiliar
    if doc1 and doc2:#entrada de doc
        s1,s2=self.leer(doc1, doc2)
    d1,d2=self.preprocesamiento(s1, s2, idioma)
    if len(d1)==len(d2):#condicion para ver si los doc tienen la misma longitud
        interseccion=d1.intersection(d2)
        return float(1-((float(len(d1))-float(len(interseccion))))/len(d1))
    else:
        msg= "La distancia entre los dos vectores debe ser la misma"
        return msg
    
def jaccard(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    La medida de Jaccard es una medida de similitud que va a tender a 1 mientras mas
    semejanza exista entre dos vectores y el rango de su resultado va estar entre [0-1]
    
                    |X ∩ Y|
    jaccard(X,Y) = -----------
                    |X ∪ Y|
    
    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> jaccard(x, y, "", "",idioma) == 0.6
    True
    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    if doc1 and doc2:#entrada de doc
        s1,s2=self.leer(doc1, doc2)
    d1,d2=self.preprocesamiento(s1, s2, idioma)
    c1 = d1 & d2
    c2 = d1 | d2
    if len(c2) == 0:
        result = 'inf'
    else:
        result = float(len(c1))/float(len(c2))
    return result

def dice_coefficient(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    La medida de Dice_coefficient (similar a Jaccard) es una medida de similitud que va
    a tender a 2 mientras mas semejanza exista entre dos vectores y el rango de su
    resultado va estar entre [0-2]

                    2|X ∩ Y|
    dice(X,Y) = -----------
                     |X|+|Y|

    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> dice_coefficient(x, y, "", "",idioma) == 1.2
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    if doc1 and doc2:#entrada de doc
        s1,s2=self.leer(doc1,doc2)
    d1,d2=self.preprocesamiento(s1,s2)
    c1 = d1 & d2
    c2 = d1 | d2
    return 2*(float(len(c1)))/(float(len(c2))+float(len(c2)))

def overlap(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    Overlap es una medida que tiende a 1 mientras mayor sea la semejanza entre los
    dos vectores y su resultado esta entre [0-1]. Este machea completamente si el vector1
    es un subconjunto del vector2 o viceversa

                |X ∩ Y|
    OC(x,y)= ---------------
              min(|x|,|y|)
              
    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> overlap(x, y, "", "", idioma) == 0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    if doc1 and doc2:#entrada de doc
        s1,s2=self.leer(doc1, doc2)
    d1,d2=self.preprocesamiento(s1, s2, idioma)
    if float(min(len(d1),len(d2))) == 0:
        result = 'inf'
    else:
        result = float(len(d1.intersection(d2)))/float(min(len(d1),len(d2)))
    
    return result

def euclidean(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    Euclidean es una medida de distancia geometrica entre dos vectores que tiende a 0 mientras mas
    semejantes son los vectores. Esta medida utiliza el metodo tf para asignarle un peso a las palabras
    de acuerdo a la frecuencia.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor 
    similitud.
    Esta operacion se realizo  restando el resultado con 1 para invertir el orden a que esta tendiendo

                               ₂
    euclidean(x,y)= ⎷∑ |x - y | 
                      i  i   i
    
    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> euclidean(x, y, "", "", idioma) == 1.0
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    try:#entrada de doc
        s1,s2=self.leer(doc1, doc2)
        s1=sw.lower()
        s2=s2.lower()
        d1=set(self.stop_words(word_tokenize(s1),idioma))#filtrado del texto
        d2=set(self.stop_words(word_tokenize(s2),idioma))#filtrado del texto
        suma=0
        if len(s1)<len(s2):#Para ver hasta donde recorrer que no se vaya de rango las iteraciones
            for i in range(len(d1)):
                suma+=pow(self.tf(d1[i],d1) - self.tf(d2[i],d2),2)#tf es una funcion que un peso a la variable de acuerdo a su frecuencia en el doc
            return float(1-float(pow(suma,0.5)))
        else:
            for i in range(len(d2)):
                suma+=pow(self.tf(d1[i],d1) - self.tf(d2[i],d2),2)#tf es una funcion que un peso a la variable de acuerdo a su frecuencia en el doc
            return float(1-float(pow(suma,0.5)))
    finally:#entrada de cadenas
        s1=s1.lower()
        s2=s2.lower()
        s1=self.stop_words(word_tokenize(s1),idioma)
        s2=self.stop_words(word_tokenize(s2),idioma)
        suma=0
        if len(s1)<len(s2):
            for i in range(len(s1)):
                suma+=pow(self.tf(s1[i],s1) - self.tf(s2[i],s2),2)
            return float(1-float(pow(suma,0.5)))
        else:
            for i in range(len(s2)):
                suma+=pow(self.tf(s1[i],s1) - self.tf(s2[i],s2),2)
            return float(1-float(pow(suma,0.5)))

def manhattan(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    La distancia de Manhattan es una distancia que tiende a 0 mientras mas
    semejantes son los vectores. Esta medida utiliza el metodo tf para asignarle
    un peso a las palabras de acuerdo a la frecuencia.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor 
    similitud.
    Esta operacion se realizo restando el resultado con 1 para invertir el orden a que esta tendiendo
    
                               ₂
    manhattan(x,y)=  ∑ |x - y | 
                      i  i   i
    
    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> manhattan(x, y, "", "", idioma) == 1.0
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    try:#entrada de doc
        s1,s2=self.leer(doc1, doc2)
        s1=s1.lower()
        s2=s2.lower()
        d1=set(self.stop_words(word_tokenize(s1),idioma))#filtrado del texto
        d2=set(self.stop_words(word_tokenize(s2),idioma))#filtrado del texto
        suma=0.0
        if len(s1)<len(s2):#para ver hasta donde llegan las iteraciones
            for i in range(len(s1)):
                suma+=float(pow(self.tf(d1[i],d1)-self.tf(d2[i],d2),2))
            return float(1-suma)
        else:
            for i in range(len(v2)):
                suma+=float(pow(self.tf(d1[i],d1)-self.tf(d2[i],d2),2))
            return float(1-suma)
    finally:#entrada de cadenas
        s1=self.stop_words(word_tokenize(s1),idioma)
        s2=self.stop_words(word_tokenize(s2),idioma)
        suma=0.0
        if len(s1)<len(s2):
            for i in range(len(s1)):
                suma+=float(pow(self.tf(s1[i],s1)-self.tf(s2[i],s2),2))
            return float(1-suma)
        else:
            for i in range(len(s2)):
                suma+=float(pow(self.tf(s1[i],s1)-self.tf(s2[i],s2),2))
            return float(1-suma)

def num(s1,s2,idioma):#metodo auxiliar que calcula la parte del numerador del metodo coseno
    s1=s1.lower()
    s2=s2.lower()
    d1=set(self.stop_words(word_tokenize(s1),idioma))
    d2=set(self.stop_words(word_tokenize(s2),idioma))
    s1=self.stop_words(word_tokenize(s1),idioma)
    s2=self.stop_words(word_tokenize(s2),idioma)
    suma=0
    for i in range(len(d1.intersection(d2))):
        suma+=self.tf(s1[i],s1) * self.tf(s2[i],s2)
    return suma
def norma(s,idioma):#metodo para normalizar
    s=s.lower()
    d1=set(self.stop_words(word_tokenize(s),idioma))
    s=self.stop_words(word_tokenize(s),idioma)
    resultado=0
    for i in range(len(d1)):
        resultado+=pow(self.tf(s[i],s),2)
    return resultado
def cos(s1=None,s2=None,doc1=None,doc2=None,idioma='english'):
    """
    La distancia de Coseno es una distancia que tiende a 1 mientras mas
    semejantes son los vectores y su valor se encuentra entre [0-1].
    Esta medida utiliza el metodo tf para asignarle un peso a las palabras
    de acuerdo a la frecuencia.

    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> cos(x, y, "", "",idioma) == 0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    if doc1 and doc2:#entrada de doc
        s1,s2=self.leer(doc1, doc2)
    
    if pow(self.norma(s1,idioma)*self.norma(s2,idioma),0.5) == 0:
        result = 'inf'
    else:
        result = self.num(s1,s2,idioma)/pow(self.norma(s1,idioma)*self.norma(s2,idioma),0.5)
    
    return result
    
def _edit_dist_init(len1, len2):
    lev = []
    for i in range(len1):
        lev.append([0] * len2)  # initialize 2D array to zero
    for i in range(len1):
        lev[i][0] = i           # column 0: 0,1,2,3,4,...
    for j in range(len2):
        lev[0][j] = j           # row 0: 0,1,2,3,4,...
    return lev


def _edit_dist_step(lev, i, j, s1, s2, transpositions=False):
    c1 = s1[i - 1]
    c2 = s2[j - 1]

    # skipping a character in s1
    a = lev[i - 1][j] + 1
    # skipping a character in s2
    b = lev[i][j - 1] + 1
    # substitution
    c = lev[i - 1][j - 1] + (c1 != c2)

    # transposition
    d = c + 1  # never picked by default
    if transpositions and i > 1 and j > 1:
        if s1[i - 2] == c2 and s2[j - 2] == c1:
            d = lev[i - 2][j - 2] + 1

    # pick the cheapest
    lev[i][j] = min(a, b, c, d)


def edit_distance(s1, s2, transpositions=False):
    """
    Calculate the Levenshtein edit-distance between two strings.
    The edit distance is the number of characters that need to be
    substituted, inserted, or deleted, to transform s1 into s2.  For
    example, transforming "rain" to "shine" requires three steps,
    consisting of two substitutions and one insertion:
    "rain" -> "sain" -> "shin" -> "shine".  These operations could have
    been done in other orders, but at least three steps are needed.

    This also optionally allows transposition edits (e.g., "ab" -> "ba"),
    though this is disabled by default.

    @param s1, s2: The strings to be analysed
    @param transpositions: Whether to allow transposition edits
    @type s1: str
    @type s2: str
    @type transpositions: bool
    @rtype: int
    """
    # set up a 2-D array
    len1 = len(s1)
    len2 = len(s2)
    lev = self._edit_dist_init(len1 + 1, len2 + 1)

    # iterate over the array
    for i in range(len1):
        for j in range(len2):
            self._edit_dist_step(lev, i + 1, j + 1, s1, s2, transpositions=transpositions)
    return lev[len1][len2]

def binary_distance(s1=None, s2=None, doc1=None,doc2=None,idioma='english'):
    """Simple equality test.

    0.0 if the labels are identical, 1.0 if they are different.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor 
    similitud.
    Esta operacion se realizo restando el resultado con 1 para invertir el orden a que esta tendiendo

    >>> from nltk.metrics import binary_distance

    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> binary_distance(x, y, "", "",idioma) == 0.0
    True
    """

    if doc1 and doc2:#entrada por doc
        s1,s2=self.leer(doc1, doc2)
    d1,d2=self.preprocesamiento(s1, s2, idioma)
    if d1==d2:
        return 1.0
    else:
        return 0.0
    
def masi_distance(s1=None, s2=None, doc1=None,doc2=None,idioma='english'):
    """Distance metric that takes into account partial agreement when multiple
    labels are assigned.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor 
    similitud.
    Esta operacion se realizo restando el resultado con 1 para invertir el orden a que esta tendiendo

    @param x, y: Cadenas a analizar
    @param doc1, doc2: Direccion de los archivos a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> masi_distance(x, y, "", "",idioma) == 0.802
    True

    Passonneau 2006, Measuring Agreement on Set-Valued Items (MASI) for Semantic and Pragmatic Annotation.
    """
    if doc1 and doc2:#entrada por doc
        s1,s2=self.leer(doc1, doc2)
    d1,d2=self.preprocesamiento(s1, s2, idioma)
    len_intersection = len(d1.intersection(d2))
    len_union = len(d1.union(d2))
    len_s1 = len(d1)
    len_s2 = len(d2)
    if len_s1 == len_s2 and len_s1 == len_intersection:
        m = 1
    elif len_intersection == min(len_s1, len_s2):
        m = 0.67
    elif len_intersection > 0:
        m = 0.33
    else:
        m = 0
    
    if float(len_union)*m == 0:
        result = 'inf'
    else:
        result = 1-(float(len_intersection)/float(len_union))*m
        
    return result

def interval_distance(label1,label2):
    """Krippendorff's interval distance metric

    >>> from nltk.metrics import interval_distance
    >>> interval_distance(1,10)
    81

    Krippendorff 1980, Content Analysis: An Introduction to its Methodology
    """

    try:
        return pow(label1 - label2, 2)
#        return pow(list(label1)[0]-list(label2)[0],2)
    except:
        print("non-numeric labels not supported with interval distance")


def presence(label):
    """Higher-order function to test presence of a given label
    """

    return lambda x, y: 1.0 * ((label in x) == (label in y))

def jaccard_ulacia(v1=None,v2=None,doc1=None,doc2=None,idioma='english'):
    """Modificacion de la medida Jaccard utilizando wordnet para expandir la busqueda

    @param x, y: Cadenas a analizar
    @param idioma: Idioma del contenido que se le esta pasando
    @type x: str
    @type y: str
    @type doc1: str
    @type doc2: str
    @type idioma: str
    @rtype: float

    >>> import nltk
    >>> from nltk.tokenize import word_tokenize
    >>> from nltk.corpus import stopwords
    >>> from nltk.corpus import wordnet as ws
    >>> x = "my house is pretty"
    >>> y = "the house my is pretty"
    >>> idioma = 'english'
    >>> jaccard_ulacia(x, y,doc1,doc2, idioma) == 1
    True
    """
    if doc1 and doc2:#entrada por doc
        input_file=open(doc1,'r')
        input_file1=open(doc2,'r')
        v1=input_file.read()
        v2=input_file1.read()

    d1=set(self.stop_words(word_tokenize(v1),idioma))#filtrado del texto
    d2=set(self.stop_words(word_tokenize(v2),idioma))#filtrado del texto
    contador=0
    
    for i in d1:   
        for j in d2:
            try: 
                tmp1=ws.synsets(i)[0]
                tmp2=ws.synsets(j)[0]                        
                similitud=tmp1.wup_similarity(tmp2)
                similitud2=tmp1.path_similarity(tmp2)
                if similitud>=similitud2:
                    tmp=similitud
                else:
                    tmp=similitud2
                if tmp>0.75:
                    contador+=1
                    break
            except:
                if len(i)<len(j):
                    tmp=float(damerau_levenshtein_distance(i, j, doc1, doc2))
                else:
                    tmp=float(damerau_levenshtein_distance(i, j, doc1, doc2))
                if tmp<0.3:
                    contador+=1 
                    break          
                    
    if float(len(d1.union(d2))) == 0:
        result = 'inf'
    else:
        result = contador/float(len(d1.union(d2)))
    return result
                   
def fractional_presence(label):
    return lambda x, y:\
        abs((float(1.0 / len(x)) - float(1.0 / len(y)))) * (label in x and label in y) \
        or 0.0 * (label not in x and label not in y) \
        or abs(float(1.0 / len(x))) * (label in x and label not in y) \
        or (float(1.0 / len(y))) * (label not in x and label in y)


def custom_distance(file):
    data = {}
    with open(file, 'r') as infile:
        for l in infile:
            labelA, labelB, dist = l.strip().split("\t")
            labelA = frozenset([labelA])
            labelB = frozenset([labelB])
            data[frozenset([labelA,labelB])] = float(dist)
    return lambda x,y:data[frozenset([x,y])]

if __name__ == '__main__':
        cl=Stringdists()
#         edit_distance_examples = [
#         ("rain", "shine"), ("abcdef", "acbdef"), ("language", "lnaguaeg"),
#         ("language", "lnaugage"), ("language", "lngauage")]
#         for s1, s2 in edit_distance_examples:
#             print("Edit distance between '%s' and '%s':" % (s1, s2), cl.edit_distance(s1, s2))
#         for s1, s2 in edit_distance_examples:
#             print("Edit distance with transpositions between '%s' and '%s':" % (s1, s2), cl.edit_distance(s1, s2, transpositions=True))
# 
#         s1 = set([1, 2, 3, 4])
#         s2 = set([3, 4, 5])
#         print("s1:", s1)
#         print("s2:", s2)
# 
#         doc1=raw_input("Escribe el camino del doc1")
#         doc2=raw_input("Escribe el camino del doc2")
        doc1=None
        doc2=None
        #v1=raw_input("Escribe el texto")
        #v2=raw_input("Escribe el texto")
        #v1="Amrozi accused his brother, whom he called the witness, of deliberately distorting his evidence."
        #v2="Referring to him as only the witness, Amrozi accused his brother of deliberately distorting his evidence."
        idioma='english'#raw_input("Escribe el idioma del texto")
        v1="PCCW's chief operating officer, Mike Butcher, and Alex Arena, the chief financial officer, will report directly to Mr So."
        v2="Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So."
        print("Binary distance:", cl.binary_distance("0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.5",doc1,doc2,idioma))
        print("MASI distance:", cl.masi_distance("0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.5",doc1, doc2,idioma))
        print("La respuesta de la medida Dice's coefficient es:",cl.dice_coefficient("el niño come pescado","el muchacho de María engulló el peje velozmente",doc1,doc2,'spanish'))
        print("La respuesta de la medida Matching coefficient es:",cl.matching_coefficient("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",doc1,doc2,idioma))
        print("La respuesta de la medida Jaccard es:",cl.jaccard(v1,v2,doc1,doc2,idioma))
        print("La respuesta de la medida Overlap coefficient es:",cl.overlap("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",doc1,doc2,idioma))
        print("La respuesta de la medida Coseno  es:",cl.cos("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5",doc1,doc2,idioma))
        print("La respuesta de la distancia Euclideana  es:",cl.euclidean("el niño come pescado","el muchacho de María engulló el peje velozmente",doc1,doc2,"spanish"))
        print("La respuesta de la distancia Manhattan  es:",cl.manhattan("el niño come pescado","el muchacho de María engulló el peje velozmente",doc1,doc2,"spanish"))
        print("La respuesta de la distancia jaccard_ulacia  es:",cl.jaccard_ulacia(v1,v2, doc1,doc2,idioma))
#        print (cl.binary_distance(v1, v2,doc1,doc2,idioma), cl.masi_distance(v1, v2,doc1, doc2,idioma), cl.jaccard(v1,v2,doc1,doc2,idioma), cl.overlap(v1,v2,doc1,doc2,idioma), cl.cos(v1,v2,doc1,doc2,idioma), cl.euclidean(v1,v2,doc1,doc2,idioma), cl.manhattan(v1,v2,doc1,doc2,idioma))
