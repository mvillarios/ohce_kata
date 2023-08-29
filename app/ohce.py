from datetime import datetime

def Ohce(nombre):
    hora = datetime.now().hour
    if hora >= 6 and hora < 12 :
        return "¡Buenos días " + nombre + "!"
    elif hora >= 12 and hora < 20:
        return "¡Buenas tardes " + nombre + "!"
    else:
        return "¡Buenas noches " + nombre + "!"