import pytest
from app.ohce import Ohce
from datetime import datetime
from app.ohce import es_palindromo
from unittest.mock import patch

def test_saludo_hora_inicio(capsys):
    hora = datetime.now().hour
    if hora >= 6 and hora < 12 :
        expected_output = "¡Buenos días Pedro!"
    elif hora >= 12 and hora < 20:
        expected_output = "¡Buenas tardes Pedro!"
    else:
        expected_output = "¡Buenas noches Pedro!"
    
    with patch("builtins.input", return_value="ohce Pedro"):
        Ohce()
    
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output

def test_echo(capsys):
    with patch("builtins.input", return_value="hola"):
        Ohce()
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "aloh"

def test_palindromo(capsys):
    assert es_palindromo("oto") == True

def test_bonita_palabra(capsys):
    palabra = "oto"
    with patch("builtins.input", return_value=palabra):
        Ohce()
    
    expected_output = f"{palabra}\n¡Bonita palabra!"
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output

def test_adios(capsys):
    with patch("builtins.input", side_effect=["Stop!"]):
        Ohce()
    
    captured = capsys.readouterr()
    expected_output = "Adios"
    assert captured.out.strip() == expected_output
