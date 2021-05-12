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
    
    prettyJSON = json.loads(response.text) #PARA PINTAR BONITO EL MENSAJE (BODY) DE RESPUESTA.
    pprint(f"Registro: {json.dumps(prettyJSON, indent=3)}")
else:
    print("No se ha borrado el registro.")