from Requests.request_builders.User import User
from test_data.test_data import *
from Requests.process_request import request_processor
from resources.uri_s import *
import json


class request_user(request_processor):

    @staticmethod
    def generate_body_for_create_user_with_array(is_single_user=True):
        def get_user_details(user_data):
            user = User(*user_data)
            return user.__dict__

        user = list()
        request_body = None
        if is_single_user:
            user.append(get_user_details(single_user))
            request_body = json.dumps(user)
        else:
            for usr in multiple_user:
                user.append(get_user_details(usr))
            request_body = json.dumps(user)

        return request_body

    def create_user(self, base_url, is_single_user=True):
        request_body = self.generate_body_for_create_user_with_array(is_single_user)
        response = self.process_reqeust(base_url=base_url, uri=create_user_with_array, request_type='POST',
                                        request_body=request_body)
        self.create_user_response = response # soring response in
        return response


    def get_user(self,base_url,user_id):
        uri = get_or_put_user_uri.format(user_name=user_id)
        response = self.process_reqeust(base_url=base_url,request_type='GET',uri=uri)
        self.get_user_repsonse = response # storing this response for easy accessbility
        return response

    def update_user(self,base_url,user_id):
        uri = get_or_put_user_uri.format(user_name=user_id)
        body = json.dumps(User(*single_user_update).__dict__)
        response = self.process_reqeust(base_url=base_url, uri=uri,request_type='PUT',request_body=body)
        return response
