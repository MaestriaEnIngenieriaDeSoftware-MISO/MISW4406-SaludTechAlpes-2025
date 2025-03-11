# MISW4406-SaludTechAlpes-2025

## 🎯 Propósito del Proyecto

Este proyecto tiene como objetivo probar la arquitectura de nuestra aplicación mediante la implementación de distintos servicios. Se han seleccionado estos microservicios como prueba para evaluar los atributos de calidad de escalabilidad, disponibilidad y seguridad. Todos los servicios están desarrollados en Python, utilizando FastAPI para el BFF y Flask para los otros componentes.

## 🛡️ Escenarios de Calidad Cubiertos

### 🔐 Seguridad: Cifrado de datos en tránsito

Descripción: Se ha implementado cifrado de extremo a extremo para proteger los datos médicos durante su transferencia entre servicios, asegurando confidencialidad e integridad.

Medidas implementadas:

- Uso de TLS 1.3 para cifrar todas las conexiones de red.

- 100% del tráfico de datos médicos cifrado en tránsito.

- Latencia de cifrado/desencriptado menor a 5 ms por solicitud.

### ⚡ Escalabilidad: Procesamiento de solicitudes de exportación de imágenes médicas

Descripción: Para manejar la creciente demanda de exportación de imágenes médicas, se usa una arquitectura basada en eventos con colas de comandos y tópicos de consultas, evitando la sobrecarga del sistema.

Medidas implementadas:

- Manejo de hasta 1,515 solicitudes en un periodo corto.

- Desacoplamiento del procesamiento y almacenamiento de solicitudes para evitar bloqueos.

### 🏗️ Disponibilidad: Continuidad del servicio ante fallos

Descripción: Se adoptó una arquitectura de microservicios junto con balanceo de carga y comunicación basada en eventos para garantizar la continuidad del servicio en caso de fallas.

Medidas implementadas:

- 99.99% de disponibilidad garantizada.

- Capacidad de redirigir tráfico a instancias saludables.


## 📁 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```plaintext
├── .github/                         # Pipelines de la aplicación
├── deployment/                      # Carpeta de despliegue de microservicios en Kubernetes
│   ├── k8s-deployment.yaml          # Despliega los microservicios
│   ├── pulsar-standalone.yaml       # Despliega el servicio de Pulsar
├── src/                             # Código fuente del proyecto
│   ├── bff_sta/                     # Backend For Frontend (BFF) del servicio STA
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── consumidores.py
│   │   ├── despachadores.py
│   │   ├── main.py
│   │   ├── utils.py
│   ├── exportacionsta/              # Servicio de exportación de imágenes
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── aplicacion/
│   │   ├── dominio/
│   │   ├── infraestructura/
│   ├── notificaciones/              # Servicio de exportación de imágenes
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── schema/
│   ├── saludtechalpes/              # Servicio principal de Salud Tech de los Alpes
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── aplicacion/
│   │   ├── dominio/
│   │   ├── infraestructura/
│   ├── ui_sta/                      # Interfaz de usuario para el servicio STA
│   │   ├── index.html
│   │   ├── consumidor.js
├── tests/                           # Pruebas unitarias del proyecto
│   ├── __init__.py
│   ├── unit/
├── .coveragerc                       # Configuración de cobertura de pruebas
├── .gitignore                        # Archivos y directorios ignorados por Git
├── .gitpod.yml                       # Configuración de Gitpod
├── bff-requirements.txt              # Dependencias del BFF
├── bff.Dockerfile                    # Dockerfile para el BFF
├── db-docker-compose.yml             # Docker Compose para la base de datos
├── docker-compose.yml                # Docker Compose para todos los servicios
├── docker-entrypoint-initdb.d/       # Scripts de inicialización para la base de datos
│   ├── init-db.sh
├── exportacionsta-requirements.txt   # Dependencias del servicio de exportación
├── exportacionsta.Dockerfile         # Dockerfile para el servicio de exportación
├── pyproject.toml                    # Configuración del proyecto
├── README.md                         # Documentación principal del proyecto
├── requirements.txt                   # Dependencias generales del proyecto
├── saludtechalpes.Dockerfile         # Dockerfile para el servicio principal
├── test.http                         # Archivo de pruebas HTTP
```

---

## 🐍 Configuración de un Ambiente Virtual con Pyenv

Para configurar un ambiente virtual de Python usando **pyenv**, sigue estos pasos:

### 📥 Instalación de Pyenv
1. Instala `pyenv` siguiendo las instrucciones oficiales: [Guía de instalación](https://github.com/pyenv/pyenv#installation).
2. Verifica que `pyenv` esté instalado correctamente:
   ```sh
   pyenv --version
   ```

### 🔧 Configuración del Ambiente Virtual
1. Instala la versión de Python requerida (por ejemplo, 3.10.6):
   ```sh
   pyenv install 3.10.6
   ```
2. Crea un entorno virtual con `pyenv virtualenv`:
   ```sh
   pyenv virtualenv 3.10.6 mi_entorno
   ```
3. Activa el entorno virtual en el proyecto:
   ```sh
   pyenv local mi_entorno
   ```
   Esto asegurará que el entorno virtual se use dentro del directorio del proyecto.

4. Verifica que el entorno virtual está activo:
   ```sh
   pyenv version
   ```

5. Instala las dependencias del proyecto:
   ```sh
   pip install -r requirements.txt
   ```

📌 *Recuerda agregar `.python-version` a tu `.gitignore` si no deseas compartir la configuración del entorno virtual.* 🚀

---

## 📦 Módulos

### 🖥️ BFF STA
El **Backend For Frontend (BFF)** es responsable de manejar las solicitudes del frontend y comunicarse con otros servicios.

### 📤 Exportación STA
El servicio de **exportación de imágenes médicas** gestiona la conversión y entrega de imágenes en diferentes formatos.

### 📤 Notificaciones
El servicio de **notificaciones** recibe un evento e imprime una notifiacacion.

### 🏥 Salud Tech de los Alpes
El **servicio principal** que maneja la lógica de negocio y la interacción con la base de datos.

### 🎨 UI STA
La **interfaz de usuario** para el servicio STA, que permite a los usuarios interactuar con el sistema.

---

## 🚀 Ejecución de Servicios

### 🐳 Ejecución con Docker Compose
Para ejecutar todos los servicios de forma local usando **Docker Compose**, sigue estos pasos:

1. Asegúrate de tener **Docker** y **Docker Compose** instalados.
2. En la raíz del proyecto, ejecuta el siguiente comando:

   ```sh
   docker-compose up --build
   ```

   Esto construirá y levantará todos los servicios definidos en `docker-compose.yml`.

---

### ⚙️ Ejecución Individual sin Docker
Si prefieres ejecutar los servicios manualmente sin usar Docker, sigue estos pasos:

#### 🔹 **BFF STA**
1. Instala las dependencias:
   ```sh
   pip install -r bff-requirements.txt
   ```
2. Ejecuta el servicio:
   ```sh
   uvicorn src.bff_sta.main:app --host 0.0.0.0 --port 5002
   ```

#### 🔹 **Exportación STA**
1. Instala las dependencias:
   ```sh
   pip install -r exportacionsta-requirements.txt
   ```
2. Ejecuta el servicio:
   ```sh
   flask --app src.exportacionsta.api run --host=0.0.0.0 --port=5001
   ```

#### 🔹 **Notificacion**
1. Instala las dependencias:
   ```sh
   pip install -r notificacion-requirements.txt
   ```
2. Ejecuta el servicio:
   ```sh
   python src/notificaciones/main.py
   ```

#### 🔹 **Salud Tech de los Alpes**
1. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
2. Ejecuta el servicio:
   ```sh
   flask --app src.saludtechalpes.api run --host=0.0.0.0 --port=5000
   ```

---

## ☸️ Despliegue en Kubernetes
Para desplegar los servicios en Kubernetes, utiliza los archivos de configuración en el directorio `deployment`.

1. Asegúrate de tener `kubectl` y `gcloud` configurados.
2. Aplica los archivos de configuracion para apache pulsar
    ```sh
   kubectl apply -f deployment/pulsar-standalone.yaml
   ```
3. Aplica los archivos de configuración de los service:
   ```sh
   kubectl apply -f deployment/k8s-deployment.yaml
   ```

---

## 🧪 Uso de la Colección de Postman

Para facilitar la interacción con el BFF STA, se ha creado una colección de Postman que contiene las consultas necesarias.

### 📥 Importar la Colección

1. Abre Postman.
2. Ve a `File -> Import`.
3. Selecciona el archivo `postman_collections/bff_sta_queries.json` ubicado en el directorio del proyecto.
4. La colección `BFF STA Queries` aparecerá en tu lista de colecciones.

### 🚀 Ejecutar Consultas

1. Asegúrate de que el servicio BFF STA esté en ejecución.
2. Selecciona la colección `BFF STA Queries`.
3. Ejecuta la consulta `Obtener Imágenes` para probar la funcionalidad del servicio.

---

## 🧪 Pruebas de GraphQL con Strawberry

Para probar las consultas GraphQL directamente en el BFF STA, puedes acceder al endpoint de Strawberry.

### 🌐 Acceder al Endpoint de GraphQL

1. Asegúrate de que el servicio BFF STA esté en ejecución.
2. Abre tu navegador web.
3. Navega a la siguiente URL:
   ```
   http://localhost:5002/v1
   ```
4. Utiliza la interfaz de Strawberry para ejecutar tus consultas GraphQL.

### 📋 Ejemplo de Consulta

Puedes probar la siguiente consulta para obtener imágenes:

```graphql
query {
  imagenes(tipoPatologia: "patologia 1", tipoImagen: "tipo imagen 1") {
    statusCode
  }
}
```

Esto te permitirá verificar que el servicio está funcionando correctamente y que puedes realizar consultas GraphQL.

---

## 🌐 Probar `index.html` con Live Server

Para probar la interfaz de usuario del servicio STA (`index.html`) utilizando la extensión de Live Server en Visual Studio Code, sigue estos pasos:

### 📥 Instalar la Extensión Live Server

1. Abre Visual Studio Code.
2. Ve a la pestaña de extensiones (`Ctrl+Shift+X`).
3. Busca `Live Server` y haz clic en `Install`.

### 🚀 Ejecutar Live Server

1. Navega al directorio `src/ui_sta` en tu proyecto.
2. Haz clic derecho en el archivo `index.html`.
3. Selecciona `Open with Live Server`.

Esto abrirá una nueva pestaña en tu navegador web con la interfaz de usuario del servicio STA. Cualquier cambio que realices en el archivo `index.html` se reflejará automáticamente en el navegador.


## Asignaciones de los integrantes del equipo
Se realizaron las siguientes asignaciones de tareas para cada integrante del equipo:
### 📋 Asignaciones Entrega 5
| Nombre                   | Asignación                                                                          |
|--------------------------|-------------------------------------------------------------------------------------|
| **Andrés Sánchez**       | Comando de eliminación de registro de imágenes exportadas                           |
| **Andrés Sánchez**       | Tópico de eventos de estado de transacción de datos anonimizados                    |
| **Juan Carlos De Jesus** | Creación de base de datos en servicio de exportación de información                 |
| **Juan Carlos De Jesus** | Integración y actualización de estado de transacción de datos anonimizados          |
| **Cristian Pinzón**      | Desarrollo de fallo aleatorio en servicio de Notificaciones                         |
| **Cristian Pinzón**      | Publicación de evento de estado del envio de Notificaciones                         |
| **Cristian Pinzón**      | Publicación de comando para la eliminación de registro creado en datos anonimizados |
| **Edgar Melara**         | Desarrollo del BFF, postman collection, SagaLog                                     |
   

