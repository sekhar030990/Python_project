'''
Test case function should start with tests_
test cases
'''

def sub(a,b):
    return a = b

    
def test_verify_sub():
    r = sub(10,5)
    assert r == 5 , ' \n Sub fun is not working as expected'
    r = sub(10.5,5.3)
    assert r == 5.2 , ' \n Sub fun is not working as expected'
    r = sub(-10,-5)
    assert r == -5 ,' \n Sub fun is not working as expected'
    print(' \n\n sub fun Ran successfully')

test_verify_sub()



