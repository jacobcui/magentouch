from suds.client import Client
from suds.transport.http import HttpAuthenticated
from settings import url, username, password
"""
http://www.service-repository.com
"""
class Urls:
    pass

class Magentouch:
    def __init__(self, **kwargs):
        if 'url' not in kwargs.keys():
            self.complain(self.parameter_error, 'url')

        self.__dict__.update(kwargs)

        t = HttpAuthenticated(username=self.username, password=self.password)
        self.client = Client(self.url, transport=t)
        self.service = self.client.service

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
    
urls = Urls()
urls.weather = 'http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL'
urls.magento = 'http://shop.digirocks.com.au/api/?wsdl'

mgt = Magentouch(url=urls.magento, username=username, password=password)
#mgt.username = 'admin_jacob'
#mgt.password = "Digirocks123!@#"
#print mgt.get_client().service.GetWeatherInformation()
print mgt.get_client()
