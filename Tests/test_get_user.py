'''
    Test cases for getUser by user_name
'''
from Tests.base_test import Test_base
from test_data.test_data import *
from resources.helpers import *

class Test_get_user(Test_base):

    def test_get_valid_user(self):
        # create user before getting user
        before_action_response = self.common_request_caller(self.user.create_user , self.base_url, True)
        if before_action_response.status_code == 200:
            get_user_response = self.user.get_user(self.base_url,single_user[1])
            self.validate_success_response(get_user_response , single_user)

    def test_get_valid_user_multiple(self):
        # create multiple user before executing test case
        before_action_response = self.common_request_caller(self.user.create_user, self.base_url, False)
        if before_action_response.status_code == 200:
            for single_user in multiple_user:
                get_user_response = self.user.get_user(self.base_url, single_user[1])
                self.validate_success_response(get_user_response , single_user)

    def test_get_invalid_user(self):
        # get invalid user
        get_user_response = self.user.get_user(self.base_url, get_random_string(5))
        self.validate_error_rsponse(get_user_response)

    def validate_success_response(self, response , single_user):
        # validate success response
        validate = validation()
        validate.validate_status_code(response,200)
        validate.validate_get_user_response(response,single_user)

    def validate_error_rsponse(self,response):
        # validate error response
        validate = validation()
        validate.validate_status_code(response,404)
        validate.validate_error_response_keys(response)


class validation():

    def validate_status_code(self , response , code):
        assert response.status_code == code

    def validate_error_response_keys(self, response):
        response = response.json()
        for key in response.keys():
            assert key in error_response_keys

    def validate_error_response(self,response):
        response = response.json()
        assert response['message'] == error_message
        assert response['type'] == type


    def validate_get_user_response(self , response , single_user):
        response = response.json()
        for expected , actual in zip(single_user , response.values()):
            assert str(expected) == str(actual)




