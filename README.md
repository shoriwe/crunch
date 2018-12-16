# Crunch
## Descripcion:
 Es una script que se utiliza para generar diccionarios especificamente para
 fuerza bruta, no es 100% versatil pero si sele puede alterar los caracteres
 que utilizara, el tamano minimo de las palabras, el tamano maximo de las
 palabras, se puede decidir si almacenar todas las palabras en un diccionario
 y por ultimo si se quiere realizar cierta funcion la palabra que salga

# Pre-requisitos
 Deberia funcionar en cualquier version desde python 3.4 en adelante,
 para python 2 se deberian revisar el codigo para cambiar alguna parte que le
 cause problema; no requiere de ninguna libreria externa

# Instalacion
 Copiar la carpeta crunch en su directorio de 'site-packages'

# Quickstart

```python
from crunch import Crunch
tamano_minimo = 2 #Se generaran palabras que tengan al menos 2 caracteres
tamano_maximo = 3 #Maximo tamano de las palabras generadas
almacenar = False #Se determina si se quiere que la funcion generar retorne un
#diccionario
def f(palabra):
  '''La funcion generar puede utilizar una funciona que tenga como entrada la
     palabra generada y que con ella se realize x actividad. (por defecto la
     funcion es print, si no se quiere hacer nada cambiar la variable funcion
     de generar a False)
  '''
  print(len(palabra))
c = Crunch() #Crunch(letras=assci_letters+digits...,remover='')

c.generar(tamano_minimo,tamano_maximo,f,almacenar)
'''Esto crearia palabras con un minimo tamano de 2 y un maximo de 3, imprimiendo
la longitud de cada palabra generada y no retornaria todas las palabras
en una lista'''
```
