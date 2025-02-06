# APIGraphQL-GrapheneCRUD

<div align="center"><img src="https://custom-icon-badges.demolab.com/badge/Python-white.svg?style=social&#x26;logo=python-seeklogo" alt="Python"> <img src="https://custom-icon-badges.demolab.com/badge/Django-white.svg?style=social&#x26;logo=django-seeklogo" alt="Django"> <img src="https://custom-icon-badges.demolab.com/badge/GraphQL-white.svg?style=social&#x26;logo=graphql-seeklogo" alt="GraphQL"> <img src="https://custom-icon-badges.demolab.com/badge/Graphene-white.svg?style=social&#x26;logo=graphene-seeklogo" alt="Graphene"> <img src="https://custom-icon-badges.demolab.com/badge/SQLite-white.svg?style=social&#x26;logo=sqlite-seeklogo" alt="SQLite"> <img src="https://custom-icon-badges.demolab.com/badge/Docker-white.svg?style=social&#x26;logo=docker-seeklogo" alt="Docker"></div>

<details>

<summary>Indice</summary>

[#resumen](./#resumen "mention")

[#datos](./#datos "mention")

[#uso-de-comandos](./#uso-de-comandos "mention")

[#mapa](./#mapa "mention")

</details>

## Resumen

Repositorio para desarrollo de una API con Django.\
GraphQL como lenguaje de consulta para API.\
Graphene como biblioteca de Python para construir APIs de forma sencilla y flexible usando GraphQL.



***

## Datos

Para obtener los datos dirigirse al portal del servicio de metrobus de la CDMX:

{% embed url="https://www.metrobus.cdmx.gob.mx/" %}
Portal web Metrobus CDMX
{% endembed %}

Después en sección >> Ver más >> [`Datos abiertos`](https://www.metrobus.cdmx.gob.mx/portal-ciudadano/datos-abiertos)

***

## Uso de comandos

{% stepper %}
{% step %}
Creación entorno virtual:

```python
// python -m venv venv
```

```python
// .\venv\Scripts\activate
```
{% endstep %}

{% step %}
[Instalación de librerías](#user-content-fn-1)[^1]

```sh
// pip install geopy
```

```sh
// pip install django
```

```sh
// pip install graphene-django
```
{% endstep %}

{% step %}
### Procesamiento de datos

Limpieza

```
// Some code
```


{% endstep %}

{% step %}
Creación del proyecto:

```django
// django-admin startproject core . 
```
{% endstep %}

{% step %}
Creación de la app del proyecto:

```python
// python manage.py startapp metrobus
```
{% endstep %}

{% step %}
Migración de modelos de datos:

```python
// python manage.py makemigrations
```

```python
// python manage.py showmigrations
```

```python
// python manage.py migrate  
```
{% endstep %}

{% step %}
Creación de usuario de datos:

```python
// python manage.py createsuperuser
```
{% endstep %}

{% step %}
Ejecutar servidor:

```python
// python manage.py runserver
```


{% endstep %}

{% step %}
### Docker

Login

```docker
// docker login
```

Empaquetado&#x20;

```docker
// docker build --tag ferjml97/metrobus-app:latest .
```

Subir imagen

```docker
// docker push ferjml97/metrobus-app:latest
```
{% endstep %}
{% endstepper %}

***

## Mapa

De los datos procesados, se ha creado de un mapa con la herramienta My Maps de Google Maps, con las ventajas que contiene toda metadata posible de las rutas y estaciones del metrobus de CDMX.

{% embed url="https://www.google.com/maps/d/edit?mid=1N5PSdHzyv8ooBdEfjbKjn9-CQkFLWKs&usp=sharing" %}
Mapa Metrobus CDMX
{% endembed %}



***

❤ **@ferjml97**

[^1]: &#x20;principales a utilizar
