
class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    pass
    # Escribe tu código aquí.


class FileEmpty(StudentsDataException):
    pass
    # Escribe tu código aquí.


try:
    file = input("Que archivo desea ordenar? ")
    
    fileOpen = open(file, 'rt')
    
    for line in fileOpen:
        name = [True, ""]
        last = [False, ""]
        note = [False, ""]
        
        for ch in line:
            if name[0]:
                name[1] += ch
                
                if ch == " " or ch == "\t":
                    name[0] = False
            
            if last[0]:
                last[1] += ch
                
                if ch == " " or ch == "\t":
                    last[0] = False
                
            if note[0]:
                note[1] += ch
                
                if ch == "\n":
                    note[0] = False
                    
            
    
except WrongLine as wl:
    print("Error en los datos.")
except FileEmpty as fe:
    print("Archivo vacio.")
except StudentsDataException as sdr:
    print("Datos inexistentes.")
except:    
    print("Error")
