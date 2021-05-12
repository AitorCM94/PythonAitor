import json
import requests
from pprint import pprint

#BORRADO
url = 'http://school.labs.com.es/api/students/'
idAlumno = input("ID Alumno: ")


conf = input("Borrar Alumno: ")
if(conf == "si"):
    response = requests.delete(url + idAlumno) #BORRADO
    print('Registro eliminado: ', response.reason)
    
    #PARA USAR PPRINT EN EL MENSAJE (BODY) DE RESPUESTA:
    prettyJSON = json.loads(response.text) 
    pprint(f"Registro: {json.dumps(prettyJSON, indent=3)}")
else:
    print("No se ha borrado el registro.")