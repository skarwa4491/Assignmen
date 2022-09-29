from Tests.base_test import Test_base
from test_data.test_data import *


class Test_create_user(Test_base):

    def test_create_single_user(self):
        response = self.user.create_user(self.base_url)
        self.validate_response(response)

    def test_create_multiple_user(self):
        response = self.user.create_user(self.base_url , is_single_user=False)
        self.validate_response(response)

    def validate_response(self, response):
        validate = validation()
        validate.validate_status_code(response)
        validate.validate_response_keys(response)
        validate.validate_response_data(response)

class validation():

    def validate_status_code(self,response):
        assert response.status_code == 200

    def validate_response_keys(self,response):
        response = response.json()
        for key in response.keys():
            assert key in create_user_response_valid_keys

    def validate_response_data(self,response):
        response = response.json()
        assert response['code'] == 200
        assert response['type'] == "unknown"
        assert response['message'] == "ok"