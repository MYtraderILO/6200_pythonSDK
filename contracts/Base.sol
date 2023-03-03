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

    event createreceipt(uint256 time1, uint64 ownerId1, address ownerAddress1, uint64 commodityId1, string remark1);

    function createReceipt(uint64 ownerId, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo) public{
        _proxy.createReceipt(ownerId, ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
        emit createreceipt(block.timestamp, ownerId, ownerAddress, commodityId, otherInfo);
    }

    function changeoperatorAddress(uint64 ownerId, address newAddress) public{
        _proxy.changeoperatorAddress(ownerId, newAddress);
    }

    function changeReceiptSTATE(uint64 ownerId, uint64 recepiState) public{
        _proxy.changeReceiptSTATE(ownerId, recepiState);
    }

    function changequalityDate(uint64 ownerId, uint256 newqualityDate) public{
        _proxy.changequalityDate(ownerId, newqualityDate);
    }

    function changesettelId(uint64 ownerId, uint64 newsettelId) public {
        _proxy.changesettelId(ownerId, newsettelId);
    }

    function getTraceInfo(uint64 ownerId) public view returns(DigitalReceipt.ReceiptTrace[] memory){
        return _proxy.getTraceInfo(ownerId);
    }





}
