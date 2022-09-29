import pytest
from Requests.user_request import request_user

@pytest.mark.usefixtures("set_up_base_uri")

class Test_base:
    user = request_user()

    def common_request_caller(self , action , *params):
        return action(*params)





