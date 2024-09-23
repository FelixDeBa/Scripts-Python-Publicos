# Herramienta para escaneo de Direcciones IP
Esta herramienta se hizo con el fin de escanear un rango de direcciones IP a través de un subproceso de windows y vaciar el resultante a un archivo excel que se generará en la misma carpeta donde sejecutó el script

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

3. Una vez cumplidos estos requerimientos puedes ejecutar el script desde una terminal como normalmente se hace, o bien, puedes dar doble clic al archivo y este se ejecutará en una nuva ventana de cmd o powershell.
```
  python ping-scan-tool.py
```


4. Te solicitará una dirección IP de inicio y una dirección IP de fin para generar el rango a escanear y comenzará el escaneo mostrando un output corto por cada IP escaneanda

> [!NOTE]
> El escaneo hace uso del "ping" haciendo dos intentos por cada dirección IP encontrada en el rango con un tiempo de 3 segundos para cada respuesta, por lo que cada ip demorará 6~7 segundos en revisarse aproximadamente, considera los tiempos y la cantidad de Direcciones IP en el rango introducido para asegurar que el equipo que ejecutará el script se mantenga encendido y con conexión a intenet todo el tiempo 

5. Una vez terminado el escaneo generará un archivo excel en la misma carpeta donde se ejecutó el script con el nombre "Escaneo <ip_inicio>_<ip_fin>_<fecha>.xlsx" así como un archivo log con el nombre "LogEscaneo <ip_inicio>_<ip_fin>_<fecha>.log" y abrirá el explorador de windows en la carpeta en la que se guardó el archivo

## LIMITANTES
+ Actualmente esta librería no funciona para Sistemas operativos distitos a Windows, solo ha sido testeado en Windows 10 y Windows 11
+ No existe un botón de Pausa, para ese caso se genera el archivo ".log" el cual almacena la ultima dirección IP que se escaneó en caso de un error inesperado
+ Si no introduces un rango válido de direcciones IP no escaneará nada e igual generar un documento excel y un documento de log, ambos en blanco.
+ En caso de no introducir una dirección IP válida, podría ciclarse pidiendo de nuevo otra dirección IP, por favor, revisar la entrada que se está dando para evitar ciclos infinitos
+ El soporte para inglés/español está hecho de manera rudimentaria, sin embargo, en un inicio no debería causar problemas.

