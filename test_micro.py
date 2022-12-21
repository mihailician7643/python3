from micro import *

def test_micro1():
    assert acces('https://ionaapp.com/assignment-magic/dk/short/XV') == "{'uid': '9db500d31ee99016d30ade523c91d3b3'}"
    
def test_micro2():
    assert acces('https://ionaapp.com/assignment-magic/dk/short/1b') == "{'uid': 'a35aea60fe097c885568babb48ee7d1e'}"
    
def test_micro3():
    assert acces('https://ionaapp.com/assignment-magic/dk/short/Bz') == "{'uid': '338565467469af42c7b06f6238570053'}"
    
def test_micro4():
    assert acces('https://ionaapp.com/assignment-magic/dk/long/11D') == "{'uid': '5e652a653d1d5357a6246a22d80fe2e8'}"
    
def test_micro5():
    assert acces('https://ionaapp.com/assignment-magic/dk/long/b2c') == "{'uid': '4ea7bf2a68d7aef22cf427421aaae9e9'}"
    
def test_micro6():
    assert acces('https://ionaapp.com/assignment-magic/dk/long/rTk') == "{'uid': '82b8aa3cf88227e90f2dafbac133e3bb'}"
    
def test_micro7():
    assert acces('https://ionaapp.com/assignment-magic/dk/long/P1e') == "{'uid': '32e55357cf506c1a78260eb6746a5f65'}"
    
def test_micro8():
    assert acces('https://ionaapp.com/assignment-magic/dk/long/YHK') == "{'uid': '6e3970edced0184fc4435bbd7227cb4e'}" 
    
def test_micro9():
    assert acces('https://ionaapp.com/assignment-magic/dk/short/1q') == "{'uid': '852301e1234000e61546c131345e8b8a'}" 
    
def test_micro10():
    assert acces('https://ionaapp.com/assignment-magic/dk/short/10') == "{'uid': 'd3d9446802a44259755d38e6d163e820'}"                                  