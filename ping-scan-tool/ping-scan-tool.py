import openpyxl, re, subprocess
from datetime import date
from openpyxl.styles import PatternFill
import os
from time import sleep
os.system("")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

hoy = date.today()

doc = openpyxl.Workbook()
hoja = doc['Sheet']
hoja.title = 'ips'
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

hoja['a1'].value ='Fecha Escaneo'
hoja['b1'].value ='IP'
hoja['c1'].value ='Nombre dominio'
hoja['d1'].value ='Información Adicional'


regexUsr = r'(?:Haciendo ping a |Pinging )(?P<dns>(?:.+)(?!\d{1,3}(?:\.\d{1,3}){3}))?(?: \[)?(?P<ip>\d{1,3}(?:\.\d{1,3}){3})(?:\])?'
regexIP = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
regexTimeout=r'(?:tiempo de espera agotado|request timed out)'
regexUnreach=r'(?:desintation host unreachable|host de destino inaccesible)'

ip_inicio = input("Desde que dirección IP comenzamos: ")
while not re.match(regexIP, ip_inicio):
    ip_inicio = input("Introduce una IP válida para iniciar: ")

octetos_inicio = [int(dato) for dato in ip_inicio.split('.')]

ip_fin = input("IP donde terminar de escanear (Por Defecto es 255.255.255.255): ")
if ip_fin == "" or ip_fin is None:
    ip_fin="255.255.255.255"
else:
    while not re.match(regexIP, ip_inicio):
        ip_fin = input("Introduce una IP válida: ")
        if ip_fin == "" or ip_fin is None:
            break

octetos_fin = [int(dato) for dato in ip_fin.split('.')]

doclog=f'LogEscaneo {ip_inicio}_{ip_fin}_{str(hoy)}.log'

fila = 2
for oct1 in range(octetos_inicio[0], octetos_fin[0]+1):
    for oct2 in range(octetos_inicio[1], octetos_fin[1]+1):
        for oct3 in range(octetos_inicio[2], octetos_fin[2]+1):
            for oct4 in range(octetos_inicio[3], octetos_fin[3]+1):
                log = open(doclog,'a')
                ip = f"{oct1}.{oct2}.{oct3}.{oct4}"
                proc = subprocess.Popen(f'ping -n 2 -w 3 -a {ip}', stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                hostname="No encontrado"
                if err == None:
                    texto = str(out)[2:].split('\\r\\n')
                    for linea in texto:
                        if re.match(regexUsr, linea):
                            matches = re.search(regexUsr, linea)
                            hostname = matches.group('dns') if matches.group('dns') is not None else 'No encontrado'
                            break
                    hoja[f'a{fila}'].value = hoy
                    hoja[f'b{fila}'].value = ip
                    hoja[f'c{fila}'].value = hostname
                    if (re.match(regexTimeout, texto[2].lower()) and re.match(regexTimeout, texto[3].lower())) and hostname == 'No encontrado':
                        print(f'{bcolors.FAIL}{ip} no esta en Uso{bcolors.ENDC}')
                        log.writelines(f'\n{str(hoy)},{ip},{hostname},No está en uso')
                        print(LINE_UP, end=LINE_CLEAR)
                        hoja[f'd{fila}'].value = "No está en uso"
                        fila+=1
                    elif re.match(regexTimeout, texto[2].lower()) and re.match(regexTimeout, texto[3].lower()):
                        print(f'{bcolors.WARNING}IP: {ip}, usuario: {hostname} No respondió{bcolors.ENDC}')
                        log.writelines(f'\n{str(hoy)},{ip},{hostname},No respondió pero tiene asignado un hostname en Dominio')
                        print(LINE_UP, end=LINE_CLEAR)
                        hoja[f'd{fila}'].value = "Asignada pero no respondió"
                        fila+=1
                    elif re.match(regexUnreach, texto[2].lower()) and re.match(regexUnreach, texto[3].lower()):
                        print(f'{bcolors.WARNING}IP: {ip}, usuario: {hostname} Host inaccesible{bcolors.ENDC}')
                        log.writelines(f'\n{str(hoy)},{ip},{hostname},No respondió pero tiene asignado un hostname en Dominio')
                        print(LINE_UP, end=LINE_CLEAR)
                        hoja[f'd{fila}'].value = "Destino del host Inaccesible"
                        fila+=1
                    else:
                        print(f'{bcolors.OKBLUE}IP: {ip}, usuario: {hostname} OK{bcolors.ENDC}')
                        log.writelines(f'\n{str(hoy)},{ip},{hostname},OK')
                        print(LINE_UP, end=LINE_CLEAR)
                        hoja[f'd{fila}'].value = "OK"
                        fila+=1
                else:
                    print(f'{bcolors.FAIL}{bcolors.UNDERLINE}IP: {ip}, dió Error {err}{bcolors.ENDC}')
                    hoja[f'a{fila}'].value = hoy
                    hoja[f'a{fila}'].fill = PatternFill("solid", fgColor="FF0000")
                    hoja[f'b{fila}'].value = ip
                    hoja[f'b{fila}'].fill = PatternFill("solid", fgColor="FF0000")
                    hoja[f'c{fila}'].value = hostname
                    hoja[f'c{fila}'].fill = PatternFill("solid", fgColor="FF0000")
                    hoja[f'd{fila}'].value = err
                    hoja[f'd{fila}'].fill = PatternFill("solid", fgColor="FF0000")
                    fila+=1
                log.close()

sleep(2)
nombredoc=f"Escaneo {ip_inicio}_{ip_fin}_{str(hoy)}.xlsx"
log = open(doclog,'a')
try:
    doc.save(nombredoc)
    print(f'Documento guardado como: {bcolors.OKCYAN}{bcolors.UNDERLINE}{nombredoc}{bcolors.ENDC}en la carpeta {bcolors.OKCYAN}{bcolors.UNDERLINE}{os.getcwd()}{bcolors.ENDC}')
except Exception as e:
    print(f'{bcolors.FAIL}{bcolors.UNDERLINE}No se pudo guardar el documento Error {e}{bcolors.ENDC}')
    log.writelines(f'{str(hoy)},No se pudo guardar el documento,Error {e},{str(e)}')
    
log.close()
print(f'Archivos de logs guardado como {doclog} en {os.getcwd()}')
os.startfile(os.getcwd())
