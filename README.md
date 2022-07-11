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
- mini tip de python: en una cadena poniendo  varios {}  y despues usando **.format(var1,var2,etc)** carga esas variables
- podes hacer pasaje de parametros de: [int,string,float]
- respetar flotantes como 1.0, no toma 1
- valores por defecto: solo tenemos que poner mas de un decorador, con la misma ruta pero pasando otros parametros
o bien sin pasar OJO: SIEMPRE DEFINIENDO VALOR AL PARAMETRO 

### rutas de pildoras
 - **nunca** debo reescribir el mismo metodo (cada decorador tendra su propia y unica funcion)
 - una ruta puede recibir **parametros** de distintas formas:
	 - /params? --> en ocasiones se trabaja con estos parametros; empleando desde la libreria flask **request** , y esto se logra:
		 - param = request.args.get('llave del valor del parametro a pasar', 'valor por defecto en caso de que no se pase parametro')
		 - asi cuando se accede a esa direccion retorne alguna de las dos opciones
		 - la llave sigue el mismo principio que *los diccionarios de python* 
		 - http://127.0.0.1:8000/params?parametro=pablo --> retornara pablo
		 - http://127.0.0.1:8000/params --> retornara valor por defecto
	 - parametros sin signo de interrogacion: 
		 - params/name siendo name un parametro que se define en la url; a su vez puedo añadir un decorador sin parametro en caso de que no envie un valor (**eso si, los parametros de la funcion deben tener un valor por default**)
		 - por default los parametros de la url son **string**
		 - <int: parametro> --> es entero
		 - 

## archivos estaticos
- css,js, imgs --> carpetas
- ahi irian las respectivas cosas
- para scripts imagenes o estilo, en el href pongo "{{   url_for('nombreDeCarpeta',filename="nombreDelArchivo(ruta relativa)")  }}"



## plantilla
- favicon --> va en el head
-  para pasar variables al html al hacer el render template debemos definir  var1=var2 siendo:
	- var1: como nos refererimos a la var2 en el html
	- var2: trabajo sobre python
- la var1 para ser leida gracias jinja2 es por medio de:
	- {{var1}}
		- { % accion o condicion % } { % endPalabraReservadaUsada(for,if,etc) % } --> se emplea para condiciones o ciclos
- "url_for('directorioAlqueApunto', filename='ruta del archivo')" --> sirve para que nos perdamos con los directorios  **tambien sirve para apuntar funciones**
- podemos declarar bloques (plantilla base)

### plantillas pildoras
- vamos a necesitar renderizar alguna plantilla
- flask trabaja con jinja2 es un motor de manejo de plantillas.
- si trabajara con otra carpeta que no tenga el nombre template de beria poner:
	- `app = Flask(__name__,template_folder="templates")`
- para hacer ciclos o if usamos los conocidos como **tags** por ejemplo seria:
```
<!-- ciclo -->
{% for item in lista %}

<h1>{{item}}</h1>

{% endfor %}
<!-- condicional -->

{% if name=="pablo" %}

<h2>holis</h2>

{% else %}

<h2>mi nombre es {{name}}</h2>

{% endif %}
```

## herencia
- nos permite tener control a la hora de escribir mensajes
- con esto podemos hacer uso de bloques a nuestro antojo
- **los bloques no necesariamente se llamaran content, puedes ponerle el nombre que quieras**
- para no copiar lo que se repite siempre, definimos un base.html
````
lo que va en base html:
{% block content%}

{% endblock %}
````
````
las plantillas que hereden seguiran la siguiente estructura:


{% extends "base.html"&} --> con esto nos devuelve lo que tenemos en base.html
{% block content%}

<h1>holis</h1> --> devuelve holis en la pantalla principal

{%endblock%}
````
 
## macro
- crear funciones que se llamen y que traigan un html
- se sugiere _macro.html
```
{%macro funcion()%}
<!-- lo que se me cante -->
{%endmacro%}


<!-- en la plantilla que quiero que use la funcion -->

{% from "_macro.html" import mostrar %}

{{ mostrar(lista) }}

```
## Formularios
- decorador recibe los metodos get y post
- permite trabajar con objetos de python usando wtforms
	- permite que cada objeto trabajado en python sea un elemento del formulario
		- atributo de la clase --> campo del formulario
	- creando un archivo para los formularios, solo resta ir creando clases en funcion del formulario que necesites, esos los traes a la funcion del decorador que quieras, y en la plantilla que traes tienes que usar una funcion en macro
```
{%macro render_field(campo)%}

<td>{{campo.label}}</td>

<dd>{{ campo(**kwargs)|safe }}</dd>

{%endmacro%}

{%from "_macro.html" import render_field%}



<form action="">

{{render_field(form.username)}} --> tambien se le puede pasar clases

</form>

```
- se usa request el cual sirve:
	- para saber si es metodo post (con un `if request.method =="Post")
	- o metodo get