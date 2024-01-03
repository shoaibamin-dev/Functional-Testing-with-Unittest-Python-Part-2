


import unittest
import requests
import logging
import uuid
import json
import random
import datetime

from utils.configloader     import ConfigUtil
from utils.mssqlutil        import MSSQLUtil


class TestTransactionInsightServiceComponent(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    __envConfiguration = None  # Environment configuration object laoded from ConfigUtil
    _POST_TIMEOUT = 30
    _GET_TIMEOUT = 30
    _NUMBER_OF_USERS = 3 # Total number of users required to be created for paging test-case
    _PAGING_COUNT = f'1to{_NUMBER_OF_USERS}'

    @classmethod
    def setUpClass(self):
        instance = ConfigUtil.getInstance()
        self.__envConfiguration = instance.configJSON
        self.log.info('Testing transactioninsight.mssql.sca service component')
        self.log.info('Special Config Params')
        self.log.info(f'POST Timeout {self._POST_TIMEOUT} GET Timeout {self._GET_TIMEOUT}')

    @classmethod
    def tearDownClass(self):        
        pass

    def setUp(self):
        """ Get's environment variables from the configuration """
        pass
   
    def test_GetTransactionCategoryType(self):
        """ [TEST-TXNINSIGHT-CASE-01] Get Transaction Insight Category Type.  """
       
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            
            # authToken = response3.json()["token"]
    
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""
           
          
            # Step5: Get Transaciton Insight Category Type  

            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/category/type?typeCode=01"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200,404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 
            
            
            
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
    
    def test_GetTransactionSummary(self):
        """ [TEST-TXNINSIGHT-CASE-04] Get Transaction Insight Summary Provided User ID. """

        # customerID = str(uuid.uuid4().int).replace('-', '')[:7]

        # Query params

        customerID = '9211325'
        fromRow = 1
        toRow = 500
        fromDate = '2020-01-01'
        toDate = datetime.date.today()
        txnType = 'C'
        
        

        headers = {
            'Content-Type': 'application/json'
        }
        try:
            

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""
           
           
            # Step5: Get Transaciton Insight Category Provided User ID  
            print(f"/{customerID}/summary?from={fromRow}&toDate={toDate}&fromDate={fromDate}&txnType={txnType}&to={toRow}")
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/{customerID}/summary?from={fromRow}&toDate={toDate}&fromDate={fromDate}&txnType={txnType}&to={toRow}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200,404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

            
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
 
    def test_GetTransactionHistory(self):
        """ [TEST-TXNINSIGHT-CASE-05] Get Transaction Insight History Provided User ID. """
        
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            
            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""

            # customerID = str(uuid.uuid4().int).replace('-', '')[:7]
            customerID = '9211325'
            monthYear = '0922'
            merchantID = '773f8d4f5b964f7ea8637c8bc2039c2a'
            # Step5: Get Transaciton Insight History Provided User ID  

            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/{customerID}/history/{merchantID}?month={monthYear}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200, 404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

            
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
 
    def test_GetTransactionDetail(self):
        """ [TEST-TXNINSIGHT-CASE-06] Get Transaction Insight Details Provided User ID.  """
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""
           

            # Delete product
            txnGetQuery = f"SELECT TOP 1 CustomerID, TransID from ING_Transaction" 
            record = MSSQLUtil.getInstance().executeQuery(txnGetQuery)

            if len(record) == 0:
                response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
                self.assertIn(response2.status_code, [404],
                msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 


            customerID = record[0][0]
            txnID = record[0][1]

            # Step5: Get Transaciton Insight History Provided User ID  
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/{customerID}/{txnID}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200,404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

        
            
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
 
    def test_GetTransactionSummaryCategoryWiseTillToday(self):
        """ [TEST-TXNINSIGHT-CASE-06] Get Transaction Insight Summary Wise.  """
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
           
            fromDate= (datetime.datetime.now() - datetime.timedelta(days=10*365)).strftime('%Y-%m-%d')
            toDate=datetime.date.today()
            query= 'OD' # should get result 'Food'

            # Step5: Get Transaciton Insight History Provided User ID  
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/summary/category-wise?fromDate={fromDate}&toDate={toDate}&query={query}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200, 404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

        
            
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
 
    def test_GetTransactionSummaryMerchantWiseTillToday(self):
        """ [TEST-TXNINSIGHT-CASE-06] Get Transaction Insight Summary Wise.  """
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
           
            fromDate= (datetime.datetime.now() - datetime.timedelta(days=10*365)).strftime('%Y-%m-%d')
            toDate=datetime.date.today()
            query= 'International' # should get all merchant having 'international' in it

            # Step5: Get Transaciton Insight History Provided User ID  
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/summary/merchant-wise?fromDate={fromDate}&toDate={toDate}&query={query}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200, 404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

        
            
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
 
    def test_GetTransactionSummaryLocationWiseTillToday(self):
        """ [TEST-TXNINSIGHT-CASE-06] Get Transaction Insight Summary Wise.  """
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
           
            fromDate= (datetime.datetime.now() - datetime.timedelta(days=10*365)).strftime('%Y-%m-%d')
            toDate=datetime.date.today()
            query= 'Oman' # should get all location having either city = 'Oman' or country = 'Oman' in it

            # Step5: Get Transaciton Insight History Provided User ID  
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/summary/location-wise?fromDate={fromDate}&toDate={toDate}&query={query}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200, 404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

        
            
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
    
    def test_GetTransactionsAll(self):
        """ [TEST-TXNINSIGHT-CASE-06] Get Transaction Insight Details Provided User ID.  """
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""
           
            customerID = '9211325'

            # Step5: Get Transaciton Insight History Provided User ID  
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/{customerID}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200, 404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

        
            
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
    
    def test_GetTransactionsCategories(self):
        """ [TEST-TXNINSIGHT-CASE-06] Get Transaction Insight Details Provided User ID.  """
        
        headers = {
            'Content-Type': 'application/json'
        }
        try:

            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""
           
            customerID = '9211325'

            txnType='D'
            toDate='2024-03-01'
            fromDate='2005-03-01'

            # Step5: Get Transaciton Insight Categories Provided User ID and Params  
            txtUrlGet = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageTxnInsightSCAURL'] == '' else self.__envConfiguration['ingageTxnInsightSCAURL']}{self.__envConfiguration['ingageTxnInsightCTXRoot']}/{customerID}/categories?txnType={txnType}&toDate={toDate}&fromDate={fromDate}"

            self.log.info(f"GET to: {txtUrlGet}")
           
            response2 = requests.request("GET", txtUrlGet, headers=headers, timeout=self._POST_TIMEOUT)
            self.assertIn(response2.status_code, [200, 404],
                             msg=f'Error response received from the server: {response2.status_code} and {response2.text}') 

        
            
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
