Backend - Panzofi (Django REST Framework)
Este es el backend del proyecto Panzofi, desarrollado con Django y Django REST Framework (DRF).
Aquí se maneja la lógica para la creación de usuarios, la autenticación mediante tokens, la gestión de la Landing Page, el seguimiento de sesiones y el registro de interacciones de los usuarios.

🚀 Instalación y Configuración

1️⃣ Clonar el repositorio
git clone https://github.com/V4roah/panzofi-backend.git
cd panzofi-backend/backend


2️⃣ Instalar dependencias
Asegúrate de estar en la carpeta backend y luego ejecuta:
pip install -r requirements.txt


3️⃣ Crear y configurar el superusuario
Para acceder al panel de administración y gestionar los usuarios:
python manage.py createsuperuser
Sigue las instrucciones para crear un usuario administrador.


4️⃣ Crear 35 usuarios normales
Dentro de la carpeta backend se encuentra un script llamado create_users.py, que creará automáticamente los 35 usuarios normales en la base de datos.
Ejecuta el siguiente comando:
python create_users.py
Esto generará los usuarios de prueba para la aplicación.


5️⃣ Ejecutar migraciones
python manage.py migrate


6️⃣ Iniciar el servidor
python manage.py runserver
El backend estará disponible en:
➡ http://localhost:8000/

📡 Acceso a la Documentación de la API
Este proyecto incluye Swagger, que proporciona una documentación interactiva con todas las rutas y funcionalidades del backend.
Puedes acceder en:
🔗 http://localhost:8000/swagger/

Aquí encontrarás información sobre los endpoints disponibles, cómo interactuar con la API y ejemplos de solicitudes.
