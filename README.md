# FlaskForDumDum
I want learn how to use flask so im gonna make this guida following codigofacilito´s tutorial  link:https://www.youtube.com/watch?v=s6IF9ZVohz8&amp;list=PLagErt3C7iltAydvN6SgCVKsOH4xQQKsk

## que es flask?
- es un nos permite llevar python al navegador desde el servidor, framework con curva de aprendizaje corta.
- ES PIOLITA
- manejo de coockies
- sesiones

## se puede trabajar con entorno virtual
- esto es por sis tenes distintas versiones de python, no es obligatorio [COMO ME PEGAN YO PENSE QUE SI]

## Arquitectura cliente-servidor
- un cliente realiza peticion a servidor, el servidor maneja y responde la peticion en cualquier formato, que pasa si no tengo nada
me devuelve error

## Metodo Run
- puedo cambiar el puerto por defecto (el cual es 5000) --> la compu tiene 2 a la 16 puertos
- el mas popular es 8000
- por default, el modo debug=false, asi que los cambios no los toma a menos reiniciemos el server

## que es el __name__?
- es una variable especial de python que almacena el nombre del modulo en el que estamos (sin la extension)
- al compararla con __main__ cuando se ejecuta (encendemos el server) name pasa a llamarse main lo que confirma la ejecucion
- host es el servidor en el que se pare el programa

## RUTAS
- necesitamos rutas duraderas
- cada ruta se destaca por un decorador, y tiene una funcion con un nombre que la refiera
- podes pasar como parametro variables, <string:user> es un ejemplo de pasar cadena de caracteres
- mini tip de python: en una cadena poniendo  varios {}  y despues usando .format(var1,var2,etc) carga esas variables
- podes hacer pasaje de parametros de: [int,string,float]
- respetar flotantes como 1.0, no toma 1
- valores por defecto: solo tenemos que poner mas de un decorador, con la misma ruta pero pasando otros parametros
o bien sin pasar OJO: SIEMPRE DEFINIENDO VALOR AL PARAMETRO 


## archivos estaticos
- css,js, imgs --> carpetas
- ahi irian las respectivas cosas

## jinja 2
- 

## plantilla
- favicon --> va en el head
-  para pasar variables al html al hacer el render template debemos definir  var1=var2 siendo:
	- var1: como nos refererimos a la var2 en el html
	- var2: trabajo sobre python
- la var1 para ser leida gracias jinja2 es por medio de:
	- {{var1}}
		- { % accion o condicion % } { % endPalabraReservadaUsada(for,if,etc) % } --> se emplea para condiciones o ciclos
- "url_for('directorioAlqueApunto', filename='ruta del archivo')" --> sirve para que nos perdamos con los directorios  **tambien sirve para apuntar funciones**
- podemos declarar bloques (plantilla base) de la siguiente forma:
	- crears una clase base.html que contenga lo que repetis siempre
````
{% block content%}

{% endblock %}
````
````
{% extends "base.html"&} --> con esto nos devuelve lo que tenemos en base.html
{% block content%}

<h1>holis</h1> --> devuelve holis en la pantalla principal

{%endblock%}
````

## Formularios
- decorador recibe los metodos get y post
- se usa request el cual sirve:
	- para saber si es metodo post (con un `if request.method =="Post")
	- o metodo get