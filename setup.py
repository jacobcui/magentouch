#from distutils.core import setup
from setuptools import setup
setup(name='magentouch',
      version='1.0.0',
      description='Magento Soup v2 suds client',
      author='Jacob CUI',
      author_email='jacobcui123@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['magentouch'],
      install_requires=['suds'],
      license='GPL',
     )
