from class1 import main

def test_function():
    r= main.start()
    assert r == "Abu Hurairah is learning Python and FastAPIs"
def test_function2():
    r= main.start()
    assert r != "Abu Hurairah"

