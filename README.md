Proyecto semestral python
================================================
Este proyecto consta de un pequeño sistema web para administrar pacientes e inventario de vacunas
para el vacunatorio de la localidad de Coelemu, Región del Ñuble, Chile.

Pre-requisitos
--------------
Se requiere tener instalado lo siguiente:
* ```MYSQL``` 
* ```PYTHON 3.6 en adelante``` 
* ```PIP``` 
* ```GIT``` 
* ```Cmder (para windows) ``` 

Descarga del repositorio e importar base de datos
-----------
Una vez instalado git en windows o linux, escribir en su consola el siguiente comando:
* ```git clone https://github.com/AlainMoragaVargas/proyecto_python.git```  para descargar el repositorio en su máquina local.

Acceda a la carpeta documentos dentro del repositorio e importe la base de datos a mysql:

* ```mysql -u root -p vacunatorio < vacunatorio.sql``` Para linux: donde vacunatorio, es una base de datos vacía creada previamente.
* ```En el caso de windows, dependerá de su gestor de mysql.```

Entre al repositorio clonado y en la raíz ejecute en cmder(windows) o en una terminal (linux) el siguiente comando:
* ```pip install -r requirements.txt``` En windows.
* ```pip3 install -r requirements.txt``` En linux.

Instala los requerimientos necesarios para ejecutar el proyecto.

Verificación de credenciales
-----------
Dentro del repositorio en el archivo * ```vacunatorio.py``` en la línea 13, 14 y 15 están las credenciales de acceso a la base de datos.
Si su base de datos no posee contraseña, elimine la línea 15 * ```app.config["MYSQL_DATABASE_PASSWORD"]  = "1234"```, de lo contrario cambiela por su contraseña de acceso. Realice lo mismo en la línea 13 * ```app.config["MYSQL_DATABASE_USER"] = "root"``` en caso de tener otro nombre de usuario.

Ejecutar el proyecto
-----------
Dentro del repositorio en la raíz del proyecto, ejecute el siguiente comando:
* ```python vacunatorio.py``` En windows.
* ```python3 vacunatorio.py``` En linux.

Esto deplegará el proyecto en su localhost.

Entrar el proyecto
-----------
Dentro de su navegador web, escriba en la url:
* ```http://127.0.0.1:5000/listado_pacientes``` para acceder al listado de pacientes.






