import openpyxl, re, subprocess
from datetime import date


log = open('LogIPs.log','a')
doc = openpyxl.Workbook()
hoja = doc.create_sheet('ips')
hoja.title = 'ips'
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

hoja['a1'].value ='ip'
hoja['b1'].value ='Nombre dominio'

regexUsr = r"\b.*\s(.*)\.cerrey\.com\.mx"

fila = 2
for h in range(1):
    for i in range(255):
        ip = f'172.16.{h}.{i}'
        proc = subprocess.Popen(f'ping -n 2 -w 3 -a {ip}', stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if err == None:
            salida = str(out)[2:].split('\\r\\n')
            userout = re.findall(regexUsr, salida[1])
            userout = "" if userout == [] else userout[0]
            if 'tiempo de espera agotado' in salida[2].lower() and userout == '':
                #print(f'IP: {ip}, {salida[2].lower()} NO SE GUARDARÁ')
                print(f'{ip} No está en uso')
                log.writelines(f'\n{ip} No está en uso')
                print(LINE_UP, end=LINE_CLEAR)
                #hoja[f'J{fila}'].value = userout
            else:
                print(f'IP: {ip}, usuario: {userout}')
                log.writelines(f'IP: {ip}, usuario: {userout}')
                print(LINE_UP, end=LINE_CLEAR)
                hoja[f'a{fila}'].value = ip
                hoja[f'b{fila}'].value = userout
                fila+=1
        else:
            print(f'IP: {ip}, dió {err}')
            hoja[f'a{fila}'].value = ip
            hoja[f'b{fila}'].value = err
            fila+=1

log.close()
doc.save(f'Escaneo Segmento 0 {str(date.today())}.xlsx')
print("Documento guardado")
