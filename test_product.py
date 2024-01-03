

import unittest
import requests
import logging
import uuid
import json
import random

from utils.configloader     import ConfigUtil
from utils.mssqlutil        import MSSQLUtil


class TestProductServiceComponent(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    __envConfiguration = None  # Environment configuration object laoded from ConfigUtil
    _POST_TIMEOUT = 5
    _GET_TIMEOUT = 3
    _NUMBER_OF_USERS = 3 # Total number of users required to be created for paging test-case
    _PAGING_COUNT = f'1to{_NUMBER_OF_USERS}'

    @classmethod
    def setUpClass(self):
        instance = ConfigUtil.getInstance()
        self.__envConfiguration = instance.configJSON
        self.log.info('Testing product.mssql.sca service component')
        self.log.info('Special Config Params')
        self.log.info(f'POST Timeout {self._POST_TIMEOUT} GET Timeout {self._GET_TIMEOUT}')

    @classmethod
    def tearDownClass(self):        
        pass

    def setUp(self):
        """ Get's environment variables from the configuration """
        pass
   
    def test_CreateProduct(self):
        """ 
            [TEST-PRODUCT-CASE-01]: 
            This test-case creates a product. Simulates POST /product/type endpoint
        """

        headers = {
            'Content-Type': 'application/json',
            'X-Channel-ID': ''
        }
        try:
            
            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'
            
            headers["Authorization"] = "Bearer "+authToken
           
            # Step4.1: post product
            productUrlPost = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageProductSCAURL'] == '' else self.__envConfiguration['ingageProductSCAURL']}{self.__envConfiguration['ingageProductCTXRoot']}/type"
            self.log.info(f"POST to: {productUrlPost}")
            productName = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(16))
            productCode = str(uuid.uuid4().int).replace('-', '')[:7]

        
            payload4 = {
                "code": productCode,
                "name": productName,
                "base_type": "Accounts"
            }

            response4 = requests.request("POST", productUrlPost, headers=headers, data=json.dumps(
                payload4), timeout=self._POST_TIMEOUT)
            self.assertEqual(response4.status_code, 200,
                             msg=f'Error response received from the server: {response4.status_code} and {response4.text}') 

            # Delete product
            productDeleteQuery = f"DELETE ING_ProductType WHERE ProductTypeCode = ?" 
            MSSQLUtil.getInstance().executeDMLQuery(productDeleteQuery, productCode)

           
        except requests.exceptions.HTTPError as ex:
            self.fail(
                f"Error Received error response code form the backend system:{ex}")
        except requests.exceptions.ConnectionError as ex:
            self.fail(f"Error Connecting: {ex}")
        except requests.exceptions.Timeout as ex:
            self.log.error(ex)
            self.fail(f"Timeout Error: {ex}")
        except requests.exceptions.RequestException as ex:
            self.log.error(ex)
            self.fail(f"Request Exception: {ex}")
        except Exception as ex:
            self.log.error(ex)
            self.fail(f"Generic Exception: {ex}")

   

if __name__ == '__main__':
    unittest.main()