import pytest 
from speed import CarSpeed


def test_CarSpeed():
    assert CarSpeed(-10) == "Invalid"
    assert CarSpeed(0) == "Low"
    assert CarSpeed(39) == "Low"
    assert CarSpeed(40) == "Normal"
    assert CarSpeed(119) == "Normal"
    assert CarSpeed(120) == "High"
    assert CarSpeed(199) == "High"
    assert CarSpeed(200) == "V.High"
    assert CarSpeed(220) == "V.High"
    assert CarSpeed(221) == "Invalid"

