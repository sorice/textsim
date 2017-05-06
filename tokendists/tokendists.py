#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Token Similarity Distances
==================================

Based on term/token similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

from ..decorators import string2tokenset, string2vec

try:
    from nltk.metrics import jaccard_distance as jaccard_distance_nltk
except:
    pass

try:
    from sklearn.metrics.pairwise import manhattan_distances as manhattan_sklearn
except:
    pass

@string2tokenset
def jaccard_distance(s1,s2):
    return jaccard_distance_nltk(s1,s2)

@string2vec
def manhattan_distance(s1,s2):
    "Manhattan distance also known as City Block, L2, and "
    return manhattan_sklearn(s1,s2)

@string2tokenset
def matching_coefficient(s1,s2):
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
    maxlen = float(max(len(s1),len(s2)))
    return 1-(maxlen -len(s1.intersection(s2)))/maxlen

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
        s1,s2=leer(doc1, doc2)
    d1,d2=preprocesamiento(s1, s2, idioma)
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
        s1,s2=leer(doc1,doc2)
    d1,d2=preprocesamiento(s1,s2)
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
        s1,s2=leer(doc1, doc2)
    d1,d2=preprocesamiento(s1, s2, idioma)
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
        s1,s2=leer(doc1, doc2)
        s1=sw.lower()
        s2=s2.lower()
        d1=set(stop_words(word_tokenize(s1),idioma))#filtrado del texto
        d2=set(stop_words(word_tokenize(s2),idioma))#filtrado del texto
        suma=0
        if len(s1)<len(s2):#Para ver hasta donde recorrer que no se vaya de rango las iteraciones
            for i in range(len(d1)):
                suma+=pow(tf(d1[i],d1) - tf(d2[i],d2),2)#tf es una funcion que un peso a la variable de acuerdo a su frecuencia en el doc
            return float(1-float(pow(suma,0.5)))
        else:
            for i in range(len(d2)):
                suma+=pow(tf(d1[i],d1) - tf(d2[i],d2),2)#tf es una funcion que un peso a la variable de acuerdo a su frecuencia en el doc
            return float(1-float(pow(suma,0.5)))
    finally:#entrada de cadenas
        s1=s1.lower()
        s2=s2.lower()
        s1=stop_words(word_tokenize(s1),idioma)
        s2=stop_words(word_tokenize(s2),idioma)
        suma=0
        if len(s1)<len(s2):
            for i in range(len(s1)):
                suma+=pow(tf(s1[i],s1) - tf(s2[i],s2),2)
            return float(1-float(pow(suma,0.5)))
        else:
            for i in range(len(s2)):
                suma+=pow(tf(s1[i],s1) - tf(s2[i],s2),2)
            return float(1-float(pow(suma,0.5)))

def manhattan(s1,s2,doc1=None,doc2=None,idioma='english'):
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

    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError('Data values must be string type.')

    s1=stop_words(word_tokenize(s1),idioma)
    s2=stop_words(word_tokenize(s2),idioma)
    suma=0.0
    if len(s1)<len(s2):
        for i in range(len(s1)):
            suma+=float(pow(tf(s1[i],s1)-tf(s2[i],s2),2))
        return float(1-suma)
    else:
        for i in range(len(s2)):
            suma+=float(pow(tf(s1[i],s1)-tf(s2[i],s2),2))
        return float(1-suma)

def num(s1,s2,idioma):#metodo auxiliar que calcula la parte del numerador del metodo coseno
    s1=s1.lower()
    s2=s2.lower()
    d1=set(stop_words(word_tokenize(s1),idioma))
    d2=set(stop_words(word_tokenize(s2),idioma))
    s1=stop_words(word_tokenize(s1),idioma)
    s2=stop_words(word_tokenize(s2),idioma)
    suma=0
    for i in range(len(d1.intersection(d2))):
        suma+=tf(s1[i],s1) * tf(s2[i],s2)
    return suma

def norma(s,idioma):#metodo para normalizar
    s=s.lower()
    d1=set(stop_words(word_tokenize(s),idioma))
    s=stop_words(word_tokenize(s),idioma)
    resultado=0
    for i in range(len(d1)):
        resultado+=pow(tf(s[i],s),2)
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
        s1,s2=leer(doc1, doc2)

    if pow(norma(s1,idioma)*norma(s2,idioma),0.5) == 0:
        result = 'inf'
    else:
        result = num(s1,s2,idioma)/pow(norma(s1,idioma)*norma(s2,idioma),0.5)

    return result

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
        s1,s2=leer(doc1, doc2)
    d1,d2=preprocesamiento(s1, s2, idioma)
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
        s1,s2=leer(doc1, doc2)
    d1,d2=preprocesamiento(s1, s2, idioma)
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

    d1=set(stop_words(word_tokenize(v1),idioma))#filtrado del texto
    d2=set(stop_words(word_tokenize(v2),idioma))#filtrado del texto
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
