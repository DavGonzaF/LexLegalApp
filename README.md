# Oficina de Abogados - Proyecto Django

Este proyecto es una aplicación web para una oficina de abogados, desarrollada con Django. Incluye funcionalidades para iniciar sesión, registrarse, ver información sobre nosotros y contactarnos.

## Requisitos previos

Asegúrate de tener instalado lo siguiente en tu sistema:
- Python 3.6+
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv abogadosvenv
    ```

    En Windows:
    ```bash
    abogadosvenv\Scripts\activate
    ```

    En macOS/Linux:
    ```bash
    source abogadosvenv/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura el archivo `settings.py`:
    Crea un archivo `.env` en el directorio raíz del proyecto y añade las siguientes variables de entorno:

    ```
    SECRET_KEY='tu_clave_secreta_aqui'
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=tu_email@gmail.com
    EMAIL_HOST_PASSWORD=tu_contraseña
    ```

5. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```

6. Carga los archivos estáticos:
    ```bash
    python manage.py collectstatic
    ```

7. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

Abre tu navegador y ve a [http://127.0.0.1:8000](http://127.0.0.1:8000) para ver la aplicación en funcionamiento.

## Estructura del Proyecto

- `core/`: Contiene la lógica principal del proyecto.
- `templates/`: Contiene las plantillas HTML.
- `static/`: Contiene los archivos estáticos como CSS y JavaScript.
- `media/`: Contiene los archivos subidos por los usuarios.

## Asegúrate de incluir un archivo requirements.txt en la raíz de tu proyecto con todas las dependencias necesarias. Puedes generar este archivo usando:

pip freeze > requirements.txt

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de nuestro formulario de contacto ([http://127.0.0.1:8000/contacto/](http://127.0.0.1:8000/contacto/)).

---

¡Gracias por usar nuestra aplicación!

