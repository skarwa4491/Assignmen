import requests


class request_processor():
    '''
        parent of all request classes
        this will process the request and return the repsonses
    '''
    def __init__(self):
        self.create_user_response = None

    def process_reqeust(self, base_url, uri, request_type, request_body=None,
                        headers={'Content-Type': 'application/json'}):

        response = None
        url = base_url + uri
        if request_type == 'GET':
            response = requests.get(
                url=url,
                headers=headers
            )
        elif request_type == 'POST':
            response = requests.post(
                url=url,
                headers=headers,
                data=request_body
            )
        elif request_type == 'PUT':
            response = requests.put(
                url=url,
                headers=headers,
                data=request_body
            )
        print()
        print(request_type ,'-->', url)
        print('request_body' , '-->' , request_body)
        print('response_body' , '-->' , response.json())
        print('response_code' , '-->' , response.status_code)
        return response
