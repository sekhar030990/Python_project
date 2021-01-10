'''
Fixture provide a advanced setup and tear down options
# function   Run once per test
# module     Run once per module
@pytest.fixture(scope='module')
'''
import pytest

@pytest.fixture(scope='function')
def set_tear(request):
    print('\n Setup')
    yield
    print('\n Teardown')

def test_add(set_tear):
    print(' \n Add :')

def test_sub(set_tear):
    print('\n sub :')

