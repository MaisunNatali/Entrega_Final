# Project Hogwart (With Django)

## Consigna principal
+ Desarrollar una WEB Django con patrón MVT subida a Github.

## Debera tener los siguientes fundamentos
+ Herencia de HTML.
+ Por lo menos 3 clases en models.
+ Un formulario para insertar datos a todas las clases de tu models.
+ Un formulario para buscar algo en la BD
+ Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

## Instrucciones instalar proyecto en local

+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona el proyecto
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para cargar casa, estudiante y profesor.

``
from Profesores.models import *
from Casas.models import *
from Estudiantes.models import * 
``

``
Profesor/Casa/Estudiante = ''.objects.create(nombre='')
``


## Autores
- ['Maisun Akil, Marcos Zamora, Marcos Rossi']*(https://github.com/MaisunNatali/)*
