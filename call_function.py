import os
import sys
os.chdir(r'C:\Users\32179\Desktop\CityU\6200\project\solidity\python_sdk')
sys.path.append(r'C:\Users\32179\Desktop\CityU\6200\project\solidity\python_sdk')

from client.bcosclient import BcosClient
from client.stattool import StatTool
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
from client_config import client_config
from client.bcoserror import BcosException, BcosError
import traceback
import json

# 从文件加载abi定义
demo_config = client_config
abi_file = "contracts/Storage.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
# print(data_parser.contract_abi)


try:
    client = BcosClient()
    print(client.getinfo())
    # 部署合约
    user_address = '0xa1bec288a3757996b2b84fcd04c0747a527196ab'
    contract_address = '0x33c11a01daf7e21fc34814c91f4c9000e227c6c8'
    result = client.sendRawTransaction(contract_address, data_parser.contract_abi, 'store', ["45"])
    print(result)
    client.finish()

except:
    pass
