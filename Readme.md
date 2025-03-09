# Proyecto DeltaData

Examen Práctico: Desarrollo de una Herramienta de Registro de Créditos
Objetivo: Desarrollar una herramienta web en Python-Flask que permita registrar
créditos, almacenar la información en una base de datos SQLite y mostrar una gráfica del
total de créditos otorgados.

## Requisitos

- [Python](https://www.python.org/) 3.10 o superior.
- Librerías necesarias (instaladas a partir de `requirements.txt`).
  
## Instalación

1. **Clona el repositorio:**

   Si aún no tienes el proyecto, clónalo usando Git:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio

## Correr el programa

### dado que la base de datos esta en la raiz no se necesitara mayor configuracion.
### correr el app.py que esta en la raiz de proyecto con 

python app.py 

## consumir Apis 

### Rutas de la API, Todas las apis estan configuradas con las urls para consumirlas via local host, si tu puerto es diferente unicamente se tiene que cambiar en la url

### **1. Crear un crédito** (POST)
- **Ruta**: `http://127.0.0.1:5000/apiCreate/api/crear`
- **Método**: `POST`
- **Descripción**: Este endpoint permite crear un nuevo crédito. No es necesario proporcionar el `id`, ya que es generado automáticamente de forma incremental.

- **Cuerpo de la solicitud (JSON)**:
  ```json
  {
    "cliente": "hector leal",
    "tasa_interes": 4.4,
    "plazo": 36,
    "fecha_otorgamiento": "2023-03-10",
    "monto": 15000
  }

### **2. Read** (GET)
- **Ruta**: `    http://127.0.0.1:5000/apiGet/api/creditos  `
- **Método**: `GET`
- **Descripción**: Este endpoint permite leer los todos los registros

### **3.Update ** (PUT)
- **Ruta**: ` http://127.0.0.1:5000/apiUpdate/api/update/20`
- **Método**: `PUT`
- **Descripción**: Este endpoint permite hacer un update, se requiere poner el id a actualizar junto con la estructura JSON  de los valores nuevos a actualizar

- **Cuerpo de la solicitud (JSON)**:
  ```json
    {
    "tasa_interes": 4.4,
    "plazo": 36,
    "fecha_otorgamiento": "2023-03-10",
    "monto": 15000
    } 

### **4. Delete** (DEL)
- **Ruta**: `    http://127.0.0.1:5000/apiDelete/api/creditos/20`
- **Método**: `DEL`
- **Descripción**:  para delete se requiere poner el id unicamente del registro a eliminar




  

    

   





