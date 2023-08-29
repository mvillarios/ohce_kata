from datetime import datetime

def Ohce(string):
    if "ohce" in string:
        string = string.replace("ohce ", "")
        hora = datetime.now().hour
        if hora >= 6 and hora < 12 :
            return "¡Buenos días " + string + "!"
        elif hora >= 12 and hora < 20:
            return "¡Buenas tardes " + string + "!"
        else:
            return "¡Buenas noches " + string + "!"