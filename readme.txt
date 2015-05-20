Following python code shows you how to
inititialize the Magentouch instance
and then call an Magento SOUPv2 api

Further api reference can be found here
http://www.magentocommerce.com/api/soap/introduction.html


from magentouch import Magentouch
from magentouch.utils import recursive_asdict

url=''
username=''
password=''

mgt = Magentouch(url=url, username=username, password=password)
suds_ret = mgt.service.catalogCategoryTree(mgt.session)
categories = recursive_asdict(suds_ret)['children']
for c in categories:
    print c
