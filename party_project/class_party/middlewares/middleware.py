import time
class Middleware1:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        print("middleware 1: before")
        
        response = self.get_response(request)
        end = time.time()
        print(f"middleware 1: after")

        return response


class Middleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("middleware 2: before")
        
        response = self.get_response(request)

        print("middleware 2: after")

        return response