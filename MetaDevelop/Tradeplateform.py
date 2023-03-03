import os
import sys
import sys, os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
# PROJ_DIR = r'C:\Users\32179\Desktop\CityU\6200\project\solidity\python_sdk\MetaDevelop'
# sys.path.append(os.path.join(PROJ_DIR, 'python_sdk'))

from python_sdk.client.bcosclient import BcosClient
from python_sdk.client.stattool import StatTool
from python_sdk.client.datatype_parser import DatatypeParser
from python_sdk.client.common.compiler import Compiler
from python_sdk.client_config import client_config
from python_sdk.client.bcoserror import BcosException, BcosError
import traceback
import json

demo_config = client_config
abi_file = "contracts/Base.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
# print(data_parser.contract_abi)


try:
    client = BcosClient()
    print(client.getinfo())
    # 部署合约
    # user_address = '0xa1bec288a3757996b2b84fcd04c0747a527196ab'
    contract_address = '0x6a56ad8e43f5743c4c7f1be3c353f33281a546bb'
    result = client.sendRawTransaction(contract_address, data_parser.contract_abi, 'getTraceInfo', 11)
    # result = client.sendRawTransaction(contract_address, data_parser.contract_abi, 'store', ["45"])
    print(result)
    client.finish()

except:
    pass
