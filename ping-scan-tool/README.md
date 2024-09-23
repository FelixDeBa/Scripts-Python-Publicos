# Herramienta para escaneo de Direcciones IP
Esta herramienta se hizo con el fin de escanear un rango de direcciones IP a través de un subproceso de windows y vaciar el resultante a un archivo excel que se generará en la misma carpeta donde sejecutó el script

## REQUIERIMIENTOS
- Sistema Operativo Windows
- Python >=3.11
- openpyxl>=3.1.5

## INSTRUCCIONES
Antes de ejecutar el script asegurarse que tengas instalado el lenguaje Python en su versión 3, de preferencia 3.11 o superior
```
  python --version
```

Es necesario contar ocn la librería que brinda soporte para Excel en python, en este caso se utiliza openpyxl
```
  pip install openpyxl
```

Una vez cumplidos estos requerimientos puedes ejecutar el script desde una terminal como normalmente se hace, o bien, puedes dar doble clic al archivo y este se ejecutará en una nuva ventana de cmd o powershell.
```
  python ping-scan-tool.py
```


 Te solicita una dirección IP de inicio y una dirección IP de fin para generar el rango a escanear.


## LIMITANTES
+ Actualmente esta librería no funciona para Sistemas operativos distitos a Windows, solo ha sido testeado en Windows 10 y Windows 11
+ Si no introduces un rango válido de direcciones IP no escaneará nada e igual generar un documento excel y un documento de log, ambos en blanco.
+ En caso de no introducir una dirección IP válida, podría ciclarse pidiendo de nuevo otra dirección IP, por favor, revisar la entrada que se está dando para evitar ciclos infinitos
+ El soporte para inglés/español está hecho de manera rudimentaria, sin embargo, en un inicio no debería causar problemas.
