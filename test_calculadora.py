from calculadora import horaextra
from calculadora import calcularferias
from calculadora import calcularaumento
from calculadora import calculardecimo

def test_horaextra():
    assert horaextra(1100) == 5

def test_calcularaumento():
    assert calcularaumento(900, 12) == 108

def test_calcularferias():
    assert calcularferias(900, 12) == 900

def test_calculardecimo():
    assert calculardecimo(900, 12) == 1200
