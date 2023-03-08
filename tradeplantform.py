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

import time

# print(data_parser.contract_abi)

demo_config = client_config
abi_file = "contracts/Base.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)


def decode_call_getTraceInfo(data, print_out=False):
    dic = {}
    index = 0
    for info in data[0]:
        if len(info) == 11:
            index += 1
            operator_address, owner_id, owner_address, settel_Id, commodityId, commodityWeight, commodityAmount, quality_date, list_date, receipt_state, sting_info = info
            list_date_new = time.localtime(list_date // 1000)  # 转为本地时间
            time_style = time.strftime("%Y-%m-%d %H:%M:%S", list_date_new)

            dic[index] = dict(operator_address=operator_address, owner_id=owner_id, owner_address=owner_address, settel_Id=settel_Id, commodityId=commodityId, commodityWeight=commodityWeight,
                              commodityAmount=commodityAmount, quality_date=quality_date, list_date=time_style, sting_info=sting_info, receipt_state=receipt_state)
    if print_out:
        print('共有记录{}行'.format(index))
        for each_info in dic:
            print('信息{} 操作者地址:{}  拥有者信息:{} 拥有者地址{} \n 存放仓库id{} 货品id{} 货品重量{} 货品数量{} \n 质检日期{} 上链时间{} 仓单状态:{} 其他信息{}'.format(each_info, dic[each_info]['owner_address'], dic[each_info]['owner_id'],
                                                                                                                            dic[each_info]['owner_address'], dic[each_info]['settel_Id'],
                                                                                                                            dic[each_info]['commodityId'],
                                                                                                                            dic[each_info]['commodityWeight'],
                                                                                                                            dic[each_info]['commodityAmount'],
                                                                                                                            dic[each_info]['quality_date'],
                                                                                                                            dic[each_info]['list_date'],
                                                                                                                            dic[each_info]['sting_info'],
                                                                                                                            dic[each_info]['receipt_state']))

    return index, dic


# 找到所有的 event 信息
def get_all_create_Info():
    client = BcosClient()
    hash_value = []
    decode_result = []
    out_value = []
    latest_block = client.getBlockNumber()
    for index in range(1, latest_block + 1):
        tmp_info = client.getTransactionByBlockNumberAndIndex(index, 0)
        hash_value.append(tmp_info['hash'])
    for _hash in hash_value:
        tmp_info = client.getTransactionReceipt(str(_hash))
        decode_result.append(data_parser.parse_event_logs(tmp_info['logs']))
    for decode_info in decode_result:
        if len(decode_info) > 0:
            if 'eventname' in decode_info[0]:
                out_value.append(decode_info[0]['eventdata'])
    client.finish()
    return out_value


def getReceiptTraceInfo(receipt_id, pri=False):
    try:
        demo_config = client_config
        abi_file = "contracts/Base.abi"
        data_parser = DatatypeParser()
        data_parser.load_abi_file(abi_file)
        client = BcosClient()
        print(client.getinfo())
        # 部署合约
        # user_address = '0xa1bec288a3757996b2b84fcd04c0747a527196ab'
        contract_address = '0xa1f31739948aa3a4061286498ebb1b70ce8bbf9f'
        result = client.call(contract_address, data_parser.contract_abi, 'getTraceInfo', [receipt_id])
        decode_info = decode_call_getTraceInfo(result, pri)
        # print(result)

        # result_2 = client.getTransactionByBlockNumberAndIndex(48, 0)
        # client.getTransactionByBlockHashAndIndex('0x3383cf3604d9006b42a5d3e24861be7e8a95ca8d7260d4cc9be32cef24696e5d', 0)

        # 目前只有通过交易信息来获取 event 信息
        # result_hash = client.getTransactionReceipt('0x69b787d800a671687997631066aafd248361e720e91feb48ec10a197b46114d8')
        client.finish()
        # tmp = data_parser.parse_event_logs(result_hash['logs'])

        return decode_info

    except:
        print('Fail to get the information')


def createNewReceipt(args):
    result = 'query error'
    try:
        demo_config = client_config
        abi_file = "contracts/Base.abi"
        data_parser = DatatypeParser()
        data_parser.load_abi_file(abi_file)
        client = BcosClient()
        print(client.getinfo())
        # 部署合约
        # user_address = '0xa1bec288a3757996b2b84fcd04c0747a527196ab'
        contract_address = '0xa1f31739948aa3a4061286498ebb1b70ce8bbf9f'
        # args = [3, '0x5B38Da6a701c568545dCfcB03FcB875f56beddC4' ,3 ,3 ,4 ,5 ,6 ,'8']
        result = client.sendRawTransactionGetReceipt(contract_address, data_parser.contract_abi, 'createReceipt', args)
        client.finish()

        print("Successfully create receipts")

        print(result)

        return True
    # txhash = result['transactionHash']
    # txresponse = client.getTransactionByHash(txhash)
    # inputresult = data_parser.parse_transaction_input(txresponse['input'])
    # outputresult = data_parser.parse_receipt_output(inputresult['name'], result['output'])
    except:
        print(result)
        print("Fail to create receipts")
        return False

