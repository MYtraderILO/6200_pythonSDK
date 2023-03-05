//SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;
import "./ReceiptCreation.sol";

contract Satellite is ReceiptCreation{
    
    function createReceipt(uint64 receiptID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo) public{
        require(!receiptDatas[receiptID].valid, "is really exists");
        DigitalReceipt newReceipt = new DigitalReceipt(receiptID , ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
        receiptDatas[receiptID].valid = true;
        receiptDatas[receiptID].digitalreceipt = newReceipt;
    }

    function changeoperatorAddress(uint64 receiptID, address newAddress) public{
        require(receiptDatas[receiptID].valid, "is not exists");
        receiptDatas[receiptID].digitalreceipt.changeoperatorAddress(newAddress);
    }

    function changeReceiptSTATE(uint64 receiptID, uint64 recepiState, string memory otherInfo) public{
        require(receiptDatas[receiptID].valid, "is not exists");
        receiptDatas[receiptID].digitalreceipt.changeReceiptSTATE(recepiState, otherInfo);
    }

    function changequalityDate(uint64 receiptID, uint256 newqualityDate) public{
        require(receiptDatas[receiptID].valid, "is not exists");
        receiptDatas[receiptID].digitalreceipt.changequalityDate(newqualityDate);
    }

    function changesettelId(uint64 receiptID, uint64 newsettelId) public {
        require(receiptDatas[receiptID].valid, "is not exists");
        receiptDatas[receiptID].digitalreceipt.changesettelId(newsettelId);
    }

    function getTraceInfo(uint64 receiptID) public view returns(DigitalReceipt.ReceiptTrace[] memory){
        require(receiptDatas[receiptID].valid, "is not exists");
        return receiptDatas[receiptID].digitalreceipt.getTracce();
    }

    function spiltReceipt(uint64 oldreceiptID, uint64 oldAmount, bool out, uint64 newreceipID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo) public {
        require(receiptDatas[oldreceiptID].valid, "old receiptID is not exists");
        require(!receiptDatas[newreceipID].valid, "New receipID is not exists");
        // create new receipt id
        DigitalReceipt newReceipt = new DigitalReceipt(newreceipID , ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
        receiptDatas[newreceipID].valid = true;
        receiptDatas[newreceipID].digitalreceipt = newReceipt;
        // change old receipt id
        receiptDatas[oldreceiptID].digitalreceipt.changeamount(oldAmount, otherInfo);
        receiptDatas[oldreceiptID].valid = out;
    }
}
