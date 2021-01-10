import pytest


def teardown_function():
    print(' \n Teardown Section ')

def setup_function():
    print(' \n Setup Section ')


def test_sub():
    print(' \n Test SUB')

def test_add():
    print(' \n Test ADD')
