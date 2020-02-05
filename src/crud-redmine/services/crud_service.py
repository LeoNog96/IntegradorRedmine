import types

class Crud(object):

    def __init__(self, func):

        self.request = types.MethodType(func, self)
    
    def request(self, msg):
        pass