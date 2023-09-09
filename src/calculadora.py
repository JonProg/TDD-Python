def soma(x,y):
    assert isinstance(x, (int, float)), 'x tem que ser um valor int ou float'
    assert isinstance(y, (int, float)), 'y tem que ser um valor int ou float'
    return x+y


#Doctest ------------------------------------------------------

"""
>>> soma(10,20) -- teste que tem que ser feito dentro da função
30
"""

"""
if _name_ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
"""

#--------------------------------------------------------------