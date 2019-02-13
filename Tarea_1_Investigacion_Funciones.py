#!/usr/bin/env python
# coding: utf-8

# **Funciones**
# 
# Tambien llamadas sub-rutinas, procedimientos o metodos en otros lenguajes.
# 
# En el contexto de la programación, una función es una secuencia de sentencias que realizan una operacion y se les asigna un nombre. Al definir una función, se especifica el nombre de dicha función y se le asigna la secuencia o función a realizar conocido como argumento y esto arroja un resultado.
# 
# * Funciones en Python
# 
# En Python, la definición de funciones se realiza mediante la instrucción def más un nombre de función descriptivo.

# In[13]:


##Una función, no es ejecutada hasta tanto no sea invocada. Para invocar una función, simplemente se la llama por su nombre:

def mi_funcion():
    print("Hola Mundo")  

mi_funcion()

##Cuando una función, haga un retorno de datos, éstos, pueden ser asignados a una variable:

def funcion(): 
    return "Hola Mundo Virtual" 

frase = funcion() 
print(frase)


# * Parametros posisionales
# 
# Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, 
# generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente. Encontrar un término en el español para estos últimos resulta algo complejo, equivaldría a “argumentos de palabras clave”, así que simplemente los llamaremos por su nombre original.
# 
# 

# In[ ]:


def f(a, b, c):
    return a + b*c

f(2, 5, 3)
17


##Sin embargo, todos los argumentos pueden tener un valor por defecto en caso que no sean especificados.

def h(a, b=4, c=2):
    return a + b*c

h(1)  # a=1, b=4 y c=2
9
h(1, 5, 6)  # a=1, b=5 y c=6
31


# In[ ]:


* Parametros nombrados

##Los argumentos pueden llevar cualquier valor por defecto, incluyendo None y llamadas a otras funciones.

def a(c=None):
    return 100

def b(n=a()):
    return n + 50

b()


# In[ ]:


* Retorno de multiples valores

##Una de las principales diferencias entre los dos tipos de argumentos, como observamos anteriormente, 
##es que los convencionales son posicionales, mientras que en los keyword arguments su ubicación es indistinta.

##Al ser un lenguaje interpretado Python presenta mucha flexibilidad. Por ejemplo, para que una función tome una cantidad 
##indefinida de argumentos, se utiliza la expresión *args.

def f(*args):
    return args

f(1, 5, True, False, "Hello, world!")
(1, 5, True, False, 'Hello, world!')


# In[ ]:


* Funciones como objetos y como parametros de otras funciones

##En este caso kwargs es un diccionario que contiene el nombre de cada uno de los argumentos junto con su valor. 
##Siendo esto así, el orden de los mismos es indistinto.

##Ambos métodos pueden ser implementados en una misma función como excepción al error de sintaxis.

def f(*args, **kwargs):
    return args, kwargs

args, kwargs = f(True, False, 3.5, message="Hello, world!", year=2014)
args
(True, False, 3.5)

kwargs
{'message': 'Hello, world!', 'year': 2014}

##Los signos * y ** pueden también ser utilizados para almacenar argumentos en un objeto para ser pasados luego a una función.
##Considerando la función:

def f(a, b, c):
    return a*b**c

argumentos = (5, 10, 2)
f(*argumentos)


# In[ ]:


* Funciones anonimas o lambda

## Se trata de crear funciones de manera rápida, just in time, sobre la marcha, para prototipos ligeros que requieren 
## únicamente de una pequeña operación o comprobación. Por lo tanto, toda función lambda también puede expresarse como 
## una convencional (pero no viceversa).

f = lambda argumentos: resultado

def f(argumentos):
    return resultado

def f(x, y, z=1):
    return (x+y) * z

f(5, 6)

f(5, 6, 7)

f = lambda x, y, z=1: (x+y) * z

f(5, 6)

f(5, 6, 7)

def f():
    return
    print(f())
None

f = lambda: None
    print(f())
None

