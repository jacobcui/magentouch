import logging
from suds.client import Client
from suds.transport.http import HttpAuthenticated

class Urls:
    pass

class Magentouch:
    def __init__(self, **kwargs):
        if 'url' not in kwargs.keys():
            self.complain(self.parameter_error, 'url')

        self.__dict__.update(kwargs)

        t = HttpAuthenticated(username=self.username, password=self.password)
        #self.client = Client(self.url, transport=t)
        self.client = Client(self.url)
        self.service = self.client.service
        self.session = self.service.login(self.username, self.password)

    def complain(self, func, reason):
        func(reason)
        
    def parameter_error(self, par):
        print 'missing or incorrect parameter {} provided.'
        print 'available paramters to initialize the class'
        print 'are: url, [username], [password]'
        raise ValueError()

    def login(self, **kwargs):
        if kwargs:
            self.__dict__.update(kwargs)
        try:
            self.service.login(self.username, self.password)
        except KeyError:
            self.complain(self.parameter_error, 'username, password')
    def get_client(self):
        return self.client
