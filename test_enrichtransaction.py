

import unittest
import requests
import logging
import uuid
import json
import random
import time

from utils.configloader     import ConfigUtil
from utils.mssqlutil        import MSSQLUtil


class TestEnrichTransactionServiceComponent(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    __envConfiguration = None  # Environment configuration object laoded from ConfigUtil
    _POST_TIMEOUT = 30000
    _GET_TIMEOUT = 30000
    _NUMBER_OF_USERS = 3 # Total number of users required to be created for paging test-case
    _PAGING_COUNT = f'1to{_NUMBER_OF_USERS}'

    @classmethod
    def setUpClass(self):
        instance = ConfigUtil.getInstance()
        self.__envConfiguration = instance.configJSON
        self.log.info('Testing enrichtransaction.mssql.sca service component')
        self.log.info('Special Config Params')
        self.log.info(f'POST Timeout {self._POST_TIMEOUT} GET Timeout {self._GET_TIMEOUT}')

    @classmethod
    def tearDownClass(self):        
        pass

    def setUp(self):
        """ Get's environment variables from the configuration """
        pass
   
    def test_PostAccount(self):
        """ [TEST-ENRICHTRANSACTION-CASE-01] Post Account Enrich Transaction. """
        
        headers = {
            'Content-Type': 'application/json'
        }
       
        # authToken = response3.json()["token"]
        authToken = 'a4652bb494314731aacf7991f2826a20'

        headers["Authorization"] = f"Bearer {authToken}"
        headers["X-Channel-ID"] = f""
        
        # Step5: Post Account  
        
        userID = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
        customerID = str(uuid.uuid4().int).replace('-', '')[:7]
        transactionCode = str(uuid.uuid4().int).replace('-', '')[:7]
        productCode = str(uuid.uuid4().int).replace('-', '')[:7]
        transRef = str(uuid.uuid4()).replace('-', '').upper()[:12]
        transAmount = round(random.uniform(0.00, 10.00), 2)

        time.sleep(2)
        # select product type
        productTypeGetQuery = f"SELECT TOP 1 ProductTypeCode from ING_ProductType WHERE BaseType = 'Accounts'" 
        record = MSSQLUtil.getInstance().executeQuery(productTypeGetQuery)
        if len(record) == 0:
            self.assertEqual(len(record), 0,
                    msg=f"Product with BaseType = 'Accounts' not found")
            

        productTypeCode = record[0][0] 

        time.sleep(2)
        # select product type
        transCodeGetQuery = f"SELECT TOP 1 SourceTransCode from ING_Trans_Category WHERE RangeOfCode = '10000'" 
        record = MSSQLUtil.getInstance().executeQuery(transCodeGetQuery)
        if len(record) == 0:
            self.assertEqual(len(record), 0,
                    msg=f"SourceTransCode of type account is not found in DB")
        
        # print(record, 'transactionCode')
        transactionCode = record[0][0] 
        # self.assertEqual(record, 200,
        #             msg=f'Error response received from the server: {response5.status_code} and {response5.text}') 

        time.sleep(2)
        enrichUrlPost = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageEnrichTransactionSCAURL'] == '' else self.__envConfiguration['ingageEnrichTransactionSCAURL']}{self.__envConfiguration['ingageEnrichTransactionCTXRoot']}/account"
        self.log.info(f"POST to: {enrichUrlPost}")
        print(f"POST to: {enrichUrlPost}")
        payload5 =     {
    "customerID": customerID,
    "productCode": "1212121212122501",
    "productTypeCode": productTypeCode,
    "ccyCode": "BHD",
    "transAmount": "15.97",
    "description": "ATM Withdrawal AJMAN BANK",
    "transRef": transRef,
    "transDate": "2023-02-14 01:39:55.807",
    "transType": "D",
    "transactionCode": "withdrawal_D"
}

        print(payload5, "payload5")

        try:
            response5 = requests.request("POST", enrichUrlPost, headers=headers, timeout=self._POST_TIMEOUT, data=json.dumps(payload5))
            self.assertEqual(response5.status_code, 200,
                                msg=f'Error response received from the server: {response5.status_code} and {response5.text}') 

            # adding delay so that processor can store the transaction in DB 
            time.sleep(2)
            transGetQuery = f"SELECT TOP 1 * from ING_Transaction WHERE TransReference = '{transRef}'" 
            print(transGetQuery, "transGetQuery")
            record = MSSQLUtil.getInstance().executeQuery(transGetQuery)
            print(record, "record")
            
            if len(record) == 0:
                self.assertEqual(len(record), 0,
                    msg=f"Account transaction not uploaded")
            
            self.assertEqual(len(record), 1,
                    msg=f"Account transaction uploaded successfully")

             
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
 
 
    def test_PostCard(self):
        """ [TEST-ENRICHTRANSACTION-CASE-02] Post Card Enrich Transaction. """
        # Step1: Create a user
        userUrl = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageUserMgmtSCAURL'] == '' else self.__envConfiguration['ingageUserMgmtSCAURL']}{self.__envConfiguration['ingageUserMgmtCTXRoot']}/"
        loginUrl = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageLoginSCAURL'] == '' else self.__envConfiguration['ingageLoginSCAURL']}{self.__envConfiguration['ingageLoginCTXRoot']}/"
        self.log.info(f"POST to: {loginUrl}")
        userID = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))
        customerID = str(uuid.uuid4().int).replace('-', '')[:7]
        transactionCode = str(uuid.uuid4().int).replace('-', '')[:7]
        productCode = str(uuid.uuid4().int).replace('-', '')[:16]

        transRef = str(uuid.uuid4()).replace('-', '').upper()[:12]
        transAmount = round(random.uniform(0.00, 10.00), 2)
        mcc = ''

        # select product type
        productTypeGetQuery = f"SELECT TOP 1 ProductTypeCode from ING_ProductType WHERE BaseType like '%Card%'" 
        record = MSSQLUtil.getInstance().executeQuery(productTypeGetQuery)
        if len(record) == 0:
            self.assertEqual(len(record), 0,
                    msg=f"Product with BaseType = 'Accounts' not found")

        productTypeCode = record[0][0] 

        time.sleep(1)
        # select MCC
        MCCGetQuery = f"SELECT TOP 1 MCC from ING_Trans_Category WHERE SourceTransCode = '0000'" 
        record = MSSQLUtil.getInstance().executeQuery(MCCGetQuery)
        if len(record) == 0:
            self.assertEqual(len(record), 0,
                    msg=f"MCC for card not found")
        mcc = record[0][0]

        headers = {
            'Content-Type': 'application/json'
        }
        try:
            
            # authToken = response3.json()["token"]
            authToken = 'a4652bb494314731aacf7991f2826a20'

            headers["Authorization"] = f"Bearer {authToken}"
            headers["X-Channel-ID"] = f""
           

            # Step5: Post Card  

            enrichUrlPost = f"{self.__envConfiguration['inagaeBaseURL'] if self.__envConfiguration['ingageEnrichTransactionSCAURL'] == '' else self.__envConfiguration['ingageEnrichTransactionSCAURL']}{self.__envConfiguration['ingageEnrichTransactionCTXRoot']}/card"
            self.log.info(f"POST to: {enrichUrlPost}")
            payload5 =     {
                "customerID": customerID,
                "productCode": productCode,
                "productTypeCode": productTypeCode,
                "ccyCode": "BHD",
                "transAmount": transAmount,
                "description": "AZURA THE COFFEE COMPA BAUSHER",
                "transRef": transRef,
                "transDate": "2023-06-01 17:39:55.807",
                "transType": "D",
                "mcc": mcc,
                "merchantDetails": "AZURA THE COFFEE COMPA BAUSHER"
            }
            response5 = requests.request("POST", enrichUrlPost, headers=headers, timeout=self._POST_TIMEOUT, data=json.dumps(payload5))
            self.assertEqual(response5.status_code, 200,
                             msg=f'Error response received from the server: {response5.status_code} and {response5.text}') 
            
            # adding delay so that processor can store the transaction in DB 
            time.sleep(5)
            transGetQuery = f"SELECT TOP 1 * from ING_Transaction WHERE TransReference = '{transRef}'" 
            print(transGetQuery, "transGetQuery")
            record = MSSQLUtil.getInstance().executeQuery(transGetQuery)
            
            if len(record) == 0:
                self.assertEqual(len(record), 0,
                    msg=f"Card transaction not uploaded")
            
            self.assertEqual(len(record), 1,
                    msg=f"Card transaction uploaded successfully")
            
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