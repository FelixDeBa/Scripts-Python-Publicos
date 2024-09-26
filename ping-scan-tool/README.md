# Herramienta para escaneo de Direcciones IP
Esta herramienta se hizo con el fin de escanear un rango de direcciones IP a través de un subproceso de windows y vaciar el resultante de las direcciones IP que respondieron y las que tenían un DNS asignado pero no respondieron a un archivo excel que se generará en la misma carpeta donde sejecutó el script.

## REQUIERIMIENTOS
- Sistema Operativo Windows
- Python >=3.11
- openpyxl>=3.1.5

## INSTRUCCIONES
1. Antes de ejecutar el script asegurarse que tengas instalado el lenguaje Python en su versión 3, de preferencia 3.11 o superior
```
  python --version
```

2. Para instalar la librería que brinda soporte para Excel en python (en este caso openpyxl) se ejecuta el siguiente comando:
```
  pip install openpyxl
```
o
```
  python -m pip install openpyxl
```

3. Una vez cumplidos estos requerimientos puedes ejecutar el script desde una terminal como normalmente se hace, o bien, puedes dar doble clic al archivo y este se ejecutará en una nuva ventana de cmd o powershell.
```
  python ping-scan-tool.py
```


4. Te solicitará una dirección IP de inicio y una dirección IP de fin para generar el rango a escanear y comenzará el escaneo mostrando un output corto por cada IP escaneanda

> [!NOTE]
> El escaneo hace uso del "ping" haciendo dos intentos por cada dirección IP encontrada en el rango con un tiempo de 3 segundos para cada respuesta, por lo que cada ip demorará 6~7 segundos en revisarse aproximadamente, considera los tiempos y la cantidad de Direcciones IP en el rango introducido para asegurar que el equipo que ejecutará el script se mantenga encendido y con conexión a intenet todo el tiempo

5. Una vez introducidas las direcciones IP preguntará si deseas crear un nuevo archivo para el escaneo o si quieres usar une excel ya existente
- En caso de elegir un archivo existente abrirá un cuadro de diálogo pidiendo el archivo Excel sobre el que vas a escribir, este arcivo excel deberá tener los títulos de columna originales ('Fecha Escaneo','IPs','Nombre Dominio','Informacion Adicional') que utiliza este script para generar archivos, en caso de no ser así, creará una nueva hoja agregando un contador al final del nombre e.g. IPs4. El archivo será guardado con su mismo nombre y ubicación reemplazando al anterior, sin embargo, no se eliminará ninguna celda, solo comenzará a escribir a partir de la ultima fila escrita
> [!CAUTION]
> Si el archivo que seleccionas está en uso por otro programa el script generará un error una vez terminado de hacer el escaneo,
> ASEGURATE DE CERRAR EL ARCHIVO QUE SELECCIONASTE ANTES DE CONTINUAR
-En caso de elegir crear un archivo nuevo, creará un documento excel llamado Escaneo_<Rango_Semanal>.xlsx, donde Rango Semanal sigue el formato "dia de mes-dia de mes" e.g. "23 de sep-29 de sep" y lo guardará en la misma ruta de ejecución del script

5. Una vez terminado el escaneo generará archivo log de nombre "LogEscaneo <rango_semanal>.log" y abrirá el explorador de windows en la carpeta en la que se guardó el archivo

## LIMITANTES/ADVERTENCIAS
+ Actualmente esta librería no funciona para Sistemas operativos distitos a Windows, solo ha sido testeado en Windows 10 y Windows 11
+ No existe un botón de Pausa, para ese caso se genera el archivo ".log" el cual almacena la ultima dirección IP que se escaneó en caso de un error inesperado
+ En caso que elijas la opción de Trabajar sobre un archvo excel ya existente y éste se encuentre abierto, el programa dará un error al finalizar, puesto que no puede escribir un archivo que está en uso por otro programa.
+ Si no introduces un rango válido de direcciones IP no escaneará nada e igual generar un documento excel y un documento de log, ambos en blanco.
+ En caso de no introducir una dirección IP válida, podría ciclarse pidiendo de nuevo otra dirección IP, por favor, revisar la entrada que se está dando para evitar ciclos infinitos
+ El soporte para inglés/español está hecho de manera rudimentaria, sin embargo, en un inicio no debería causar problemas.

