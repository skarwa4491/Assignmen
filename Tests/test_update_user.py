from Tests.base_test import Test_base
from test_data.test_data import *
from resources.helpers import *

class Test_update_user(Test_base):

    def test_update_user(self):
        before_action_response = self.common_request_caller(self.user.create_user, self.base_url, True)
        if before_action_response.status_code == 200:
            update_user_response = self.user.update_user(self.base_url, single_user[1]) # update user
            self.validate_update_user_response(update_user_response,single_user_update) #validate updated_user response
            get_user_response = self.user.get_user(self.base_url,single_user_update[1]) # get updated user
            self.validate_get_user_after_update(get_user_response, single_user_update) # validate get user after update


    def validate_get_user_after_update(self, response , single_user):
        # validate success response
        validate = validation()
        validate.validate_status_code(response,200)
        validate.validate_get_user_response(response,single_user)

    def validate_update_user_response(self,response,expected_data):
        validate = validation()
        validate.validate_status_code(response,200)
        validate.validate_response_keys(response)
        validate.validate_response_data(response,expected_data)


class validation():

    def validate_status_code(self , response , code):
        assert response.status_code == code

    def validate_response_keys(self, response):
        response = response.json()
        for key in response.keys():
            assert key in update_response_valid_keys

    def validate_response_data(self,response,expected_data):
        # verify data in response
        response = response.json()
        assert response['code'] == 200
        assert response['type'] == "unknown"
        assert response['message']==expected_data[0]

    def validate_get_user_response(self , response , single_user):
        # validate get response
        response = response.json()
        for expected , actual in zip(single_user , response.values()):
            assert str(expected) == str(actual)
