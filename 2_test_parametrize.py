import pytest

## To run same test case repeatedly with set of inputs
@pytest.mark.parametrize("a, b", [(11,12),('sriram','Balu')])
def test_add(a, b):
    print(' \n A and B values ', a, b)