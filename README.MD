# Sistema de Gestión de Eventos 📅

Proyecto desarrollado en **Python y Django** para la gestión, registro y búsqueda de eventos, personas y ubicaciones.

## 🚀 Funcionalidades
* **Panel de Administración:** Gestión total de la base de datos desde `/admin`.
* **Registro de Personas:** Formulario para dar de alta nuevas personas.
* **Registro de Ubicaciones:** Formulario para registrar ubicaciones con capacidad.
* **Creación de Eventos:** Formulario para crear eventos vinculados a una ubicación y asistentes.
* **Buscador:** Filtro de eventos por nombre.
* **Modelos:** Relaciones entre Eventos, Personas y Ubicaciones (incluyendo ManyToMany para asistentes).

## 🛠️ Tecnologías utilizadas
* Python 3.x
* Django 4.x o superior
* SQLite (Base de Datos)

## 📦 Instalación y Uso
1. Clonar el repositorio:
```bash
   git clone https://github.com/javieralbano2020-source/Preentrega.git
```
2. Instalar dependencias:
```bash
   pip install -r requirements.txt
```
3. Ejecutar migraciones:
```bash
   python manage.py migrate
```
4. Iniciar el servidor:
```bash
   python manage.py runserver
```

## ✒️ Autor
Javier Albano da Rosa