from app.ohce import Ohce
from datetime import datetime

# def test_nombre():
#     assert Ohce("Pedro") == "Pedro"

def test_saludo_hora():
    #Test de saludo según la hora
    hora = datetime.now().hour
    if hora >= 6 and hora < 12 :
        assert Ohce("Pedro") == "¡Buenos días Pedro!" # 6:00 - 12:00
    elif hora >= 12 and hora < 20:
        assert Ohce("Pedro") == "¡Buenas tardes Pedro!" # 12:00 - 20:00
    else:
        assert Ohce("Pedro") == "¡Buenas noches Pedro!" # 20:00 - 6:00