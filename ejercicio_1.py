import csv
def create_email(nombre, apellido):
    '''Crea un correo electrónico a partir de nombre y apellido, con el dominio
"@educacion.navarra.es".
Parametros:
- nombre: str con el nombre de la persona
- apellido: str con el apellido de la persona
Return:
- str con el correo electrónico generado'''
    if len(apellido) >= 5:
        return nombre[0].lower() + apellido[0:5].lower() + '@educacion.navarra.es'
    else:
        return nombre[0].lower() + apellido[0:len(apellido)].lower() + '@educacion.navarra.es'

def calculate_grade(practica01, practica02, practica03, examen, recuperacion, actitud):
    '''Esta funcion calcula la nota media de un alumno
Parametros:
- Práctica 01: float
- Práctica 02: float
- Práctica 03: float
- Examen: float
- Recuperación: float
- Actitud: float
Return:
- Nota final: float con la nota final del alumno
- Aprobado: booleano. Si ha aprobado true, si ha suspendido false'''

    nota_final = ((practica01 + practica02 + practica03) / 3 * 0.3
              + max(examen, recuperacion) * 0.6 + actitud * 0.1)
    aprobado = nota_final >= 5
    return nota_final, aprobado

def process_class(ruta):
    '''Lee los datos del fichero CSV, calcula el email y la nota final para cada alumno, y guarda los
datos en un nuevo fichero CSV.
:param ruta: un str con la ruta del fichero (.csv) a abrir.
:return: None'''

    alumnado = []
    
    with open(ruta, newline=", encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            nombre = fila[Nombre]
            apellido = fila[Apellido]
            practica01 = float(fila['Practica01'].replace(',' , '.'))
            practica02 = float(fila['Practica02'].replace(',' , '.'))
            practica03 = float(fila['Practica03'].replace(',' , '.'))
            examen = float(fila['Examen'].replace(',' , '.'))
            recuperacion = float(fila['Recuperacion'].replace(',' , '.'))
            actitud = float(fila['Actitud'].replace(',' , '.'))
            email = create_email(nombre, apellido)
            
            nota_final, aprobado = calculate_grade(practica01, practica02, practica03, examen,
recuperacion, actitud)

alumno = {
'Nombre': nombre,
'Apellido': apellido,
'Email': email,
'Nota final':f"{nota_final:.2f}".replace('.' , ','),
'Aprobado/suspendido': aprobado}

alumnado.append(alumno)

with open('grades.csv', 'w', newline=", encoding='utf-8') as csvfile:
    fieldnames = ['Nombre', 'Apellido', 'Email', 'Nota final', 'Aprobado/suspendido']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in alumnado:
        writer.writerow(i)

process_class("class.csv")