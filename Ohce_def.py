from datetime import datetime     

def Ohce():
    nombre = ""
    while True:
        string = input()
        if "ohce" in string:
            string = string.replace("ohce ", "")
            nombre = string
            hora = datetime.now().hour
            if hora >= 6 and hora < 12 :
                print("¡Buenos días " + string + "!")
            elif hora >= 12 and hora < 20:
                print("¡Buenas tardes " + string + "!")
            else:
                print("¡Buenas noches " + string + "!")
        elif string == "Stop!":
            print("Adios " + nombre)
        else:
            if es_palindromo(string):
                print(string + "\n" +"¡Bonita palabra!")
            else:
                print(string[::-1])

def es_palindromo(string):
    return string == string[::-1]

if __name__ == "__main__":
    Ohce()