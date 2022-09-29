import pytest


@pytest.fixture(scope='function')
def set_up_base_uri(request):
    # set up base_url for execution
    base = 'https://petstore.swagger.io'
    request.cls.base_url = base
