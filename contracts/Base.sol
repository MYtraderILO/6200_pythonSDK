//SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;
import "./SatelliteProxy.sol";
import "./ReceiptCreation.sol";


contract Base {

    ReceiptCreation public _receiptCreation;
    SatelliteProxy private _proxy;

    constructor(address contractAddress) public{
        _proxy = SatelliteProxy(contractAddress);
    }

    event createreceipt(uint256 time1, uint64 receiptID1, address ownerAddress1, uint64 commodityId1, string remark1);

    function createReceipt(uint64 receiptID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo) public{
        _proxy.createReceipt(receiptID, ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
        emit createreceipt(block.timestamp, receiptID, ownerAddress, commodityId, otherInfo);
    }

    function changeoperatorAddress(uint64 receiptID, address newAddress) public{
        _proxy.changeoperatorAddress(receiptID, newAddress);
    }

    function changeReceiptSTATE(uint64 receiptID, uint64 recepiState, string memory otherInfo) public{
        _proxy.changeReceiptSTATE(receiptID, recepiState, otherInfo);
    }

    function changequalityDate(uint64 receiptID, uint256 newqualityDate) public{
        _proxy.changequalityDate(receiptID, newqualityDate);
    }

    function changesettelId(uint64 receiptID, uint64 newsettelId) public {
        _proxy.changesettelId(receiptID, newsettelId);
    }

    function spiltReceipt(uint64 oldreceiptID, uint64 oldAmount, bool out, uint64 newreceipID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo ) public{
        _proxy.spiltReceipt(oldreceiptID, oldAmount, out, newreceipID, ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
    }

    function getTraceInfo(uint64 receiptID) public view returns(DigitalReceipt.ReceiptTrace[] memory){
        return _proxy.getTraceInfo(receiptID);
    }
}
