from suds.client import Client, log as client_log
from suds.wsdl import log as wsdl_log
from suds.transport.http import log as transport_http_log
from suds.xsd.schema import log as xsd_schema_log
from suds.transport.http import HttpAuthenticated
from settings import url, username, password
from suds.xsd.doctor import ImportDoctor, Import
import logging

"""
magento soup caller
"""

class Urls:
    pass

class Magentouch:
    modules = ['client', 'transport_http', 'xsd.schema', 'wsdl']
    def __init__(self, **kwargs):
        if 'url' not in kwargs.keys():
            self.complain(self.parameter_error, 'url')
        self.__dict__.update(kwargs)

        if self.__dict__.get('log'):
            self.switch_logging()
        
        imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
        imp.filter.add('urn:Magento')

        d = ImportDoctor(imp)
        self.client = Client(self.url, doctor=d)
        self.service = self.client.service

    def print_service(self):
        print self.client

    def login(self, username, password):
        self.session = self.client.service.login(username, password)
        return self.session
    
    def switch_logging(self, on=True):

        if on:
            level = logging.DEBUG
        else:
            level = logging.INFO

        logging.basicConfig(level=logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        for m in self.modules:
            logger = eval('{}_log'.format(m.replace('.', '_')))
            logger.setLevel(logging.DEBUG)
            logger.addHandler(ch)

    def complain(self, func, reason):
        func(reason)
        
    def parameter_error(self, par):
        print 'missing or incorrect parameter {} provided.'
        print 'available paramters to initialize the class'
        print 'are: url, [username], [password]'
        raise ValueError()

    def get_client(self):
        return self.client

    def get_service(self):
        return self.service

    def call(self, resource_name, *args):
        return self.client.service.call(self.session, resource_name, *args)

if __name__ == '__main__':
    urls = Urls()
    urls.magento = 'http://shop.digirocks.com.au/api/?wsdl'  # soap 1.0

    mgt = Magentouch(url=urls.magento)
    client = mgt.get_client()

    mgt.login(username, password)
    print mgt.call('magento.info')
    print mgt.call('catalog_category.tree')
