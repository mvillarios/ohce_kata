from app.ohce import Ohce
from datetime import datetime

# def test_nombre():
#     assert Ohce("Pedro") == "Pedro"

def test_saludo_hora_inicio():
    # Test de saludo según la hora solo cuando se inicia el programa con ohce
    hora = datetime.now().hour
    if hora >= 6 and hora < 12 :
        assert Ohce("ohce Pedro") == "¡Buenos días Pedro!" # 6:00 - 12:00
    elif hora >= 12 and hora < 20:
        assert Ohce("ohce Pedro") == "¡Buenas tardes Pedro!" # 12:00 - 20:00
    else:
        assert Ohce("ohce Pedro") == "¡Buenas noches Pedro!" # 20:00 - 6:00