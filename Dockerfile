FROM python:3.11.11-alpine3.21
ENV PYTHONUNBUFFERED=1
# Configurar el directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY ./requirements.txt /app/requirements.txt

# Instalar dependencias
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . /app/

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
