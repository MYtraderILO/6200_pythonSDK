//SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;
import "./ReceiptCreation.sol";
import "./Satellite.sol";

contract SatelliteProxy is ReceiptCreation{

    address _current;

    constructor(address currentAddress) public {
        _current = currentAddress;
    }

    function createReceipt(uint64 receiptID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo) public{
        Satellite satellite = Satellite(_current);
        satellite.createReceipt(receiptID, ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
    }

    function changeoperatorAddress(uint64 receiptID, address newAddress) public{
        Satellite satellite = Satellite(_current);
        satellite.changeoperatorAddress(receiptID, newAddress);
    }

    function changeReceiptSTATE(uint64 receiptID, uint64 recepiState, string memory otherInfo) public{
        Satellite satellite = Satellite(_current);
        satellite.changeReceiptSTATE(receiptID, recepiState, otherInfo);
    }

    function changequalityDate(uint64 receiptID, uint256 newqualityDate) public{
         Satellite satellite = Satellite(_current);
        satellite.changequalityDate(receiptID, newqualityDate);
    }

    function changesettelId(uint64 receiptID, uint64 newsettelId) public {
         Satellite satellite = Satellite(_current);
        satellite.changesettelId(receiptID, newsettelId);
    }

    function getTraceInfo(uint64 receiptID) public view returns(DigitalReceipt.ReceiptTrace[] memory){
        Satellite satellite = Satellite(_current);
        return satellite.getTraceInfo(receiptID);
    }

    function spiltReceipt(uint64 oldreceiptID, uint64 oldAmount, bool out, uint64 newreceipID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo ) public {
        Satellite satellite = Satellite(_current);
        satellite.spiltReceipt(oldreceiptID, oldAmount, out, newreceipID, ownerAddress, commodityId, commodityWeight, commodityAmount, settelId, qualityDate, otherInfo);
    }
    //子合约升级了，就通过update函数更新地址
    function update(address newAddress) public{
        if(newAddress != _current){
            _current = newAddress;
        }
    }
}
