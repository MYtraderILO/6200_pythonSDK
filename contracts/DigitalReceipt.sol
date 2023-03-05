//SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;

// import "./OperatorFactory.sol";
//import "./Operator.sol";
contract DigitalReceipt{

//  enum Receipt_STATE {
//         NORMAL,
//         EXPIRED,
//         PLEDGING,
//         LENDING,
//         TRANSIT,
//         TOBETEST,
//         DEPOT,
//         SPLIT
//     }

//     Receipt_STATE public _receipt_state;

    struct ReceiptTrace{
    
        address operatorAddress; // Operator address

        // ownerInfo
        uint64 receiptID;
        address ownerAddress;

        // Commodity information 
        uint64 commodityId;
        uint64 commodityWeight;
        uint64 commodityAmount;
        //int16 commodityGrade;
        //int16 commodityQuality;
        //int16 commodityPackage;
        uint64 settelId;
        //uint64 cargoSpace;

        // time info
        //uint256 payDay;
        uint256 qualityDate;
        uint256 listDate;

        // other info
        string otherInfo;
        uint64 receipt_state;
    }

        address _operatorAddress; // Operator address

        // ownerInfo
        uint64 _receiptID;
        address _ownerAddress;

        // Commodity information 
        uint64 _commodityId;
        uint64 _commodityWeight;
        uint64 public _commodityAmount;
        // int16 _commodityGrade;
        // int16 _commodityQuality;
        // int16 _commodityPackage;
        uint64 _settelId;
        // uint64 _cargoSpace;

        // time info
        //uint256 _payDay;
        uint256 _qualityDate;
        uint256 _listDate;
        uint64 _receipt_state;
        // other info
        string _otherInfo;

    ReceiptTrace[] public _receiptTrace;

    constructor(uint64 receiptID, address ownerAddress, uint64 commodityId, uint64 commodityWeight, uint64 commodityAmount, uint64 settelId, uint256 qualityDate, string memory otherInfo) public{
        _operatorAddress = msg.sender;
        _receiptID = receiptID;
        _ownerAddress = ownerAddress;
        _commodityId = commodityId;
        _commodityWeight = commodityWeight;
        _commodityAmount = commodityAmount;
        _settelId = settelId;
        //_payDay = payDay;
        _qualityDate = qualityDate;
        _listDate = block.timestamp;
        _otherInfo = otherInfo;
        _receipt_state = 1;
        _receiptTrace.push(ReceiptTrace({operatorAddress:_operatorAddress, receiptID:_receiptID, ownerAddress:_ownerAddress, settelId:_settelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:_commodityAmount, qualityDate:_qualityDate,
        listDate:_listDate, receipt_state:_receipt_state, otherInfo: _otherInfo}));
    }

    // 修改数据的functions
    function changeReceiptSTATE(uint64 recepiState, string memory newInfo) public {
        _receipt_state = recepiState;
        _receiptTrace.push(ReceiptTrace({operatorAddress:_operatorAddress, receiptID:_receiptID, ownerAddress:_ownerAddress, settelId:_settelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:_commodityAmount, qualityDate:_qualityDate,
        listDate:_listDate, receipt_state:recepiState, otherInfo:newInfo}));
    }

    function changeoperatorAddress(address newAddress) public{
        _operatorAddress = newAddress;
        _receiptTrace.push(ReceiptTrace({operatorAddress:newAddress, receiptID:_receiptID, ownerAddress:_ownerAddress, settelId:_settelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:_commodityAmount, qualityDate:_qualityDate,
        listDate:_listDate, receipt_state:_receipt_state, otherInfo:"Change operatorAddress"}));
    }

    function changequalityDate(uint256 newqualityDate) public{
        _qualityDate = newqualityDate;
        _receiptTrace.push(ReceiptTrace({operatorAddress:_operatorAddress, receiptID:_receiptID, ownerAddress:_ownerAddress, settelId:_settelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:_commodityAmount, qualityDate:newqualityDate,
        listDate:_listDate, receipt_state:_receipt_state, otherInfo:"Change qualityDate"}));
    }

    function changesettelId(uint64 newsettelId) public{
        _settelId = newsettelId;
        _receiptTrace.push(ReceiptTrace({operatorAddress:_operatorAddress, receiptID:_receiptID, ownerAddress:_ownerAddress, settelId:newsettelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:_commodityAmount, qualityDate:_qualityDate,
        listDate:_listDate, receipt_state:_receipt_state, otherInfo:"Change settelId"}));
    }

    function changeownerAddress(address newownerAddress) public{
        _ownerAddress = newownerAddress;
        _receiptTrace.push(ReceiptTrace({operatorAddress:_operatorAddress, receiptID:_receiptID, ownerAddress:newownerAddress, settelId:_settelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:_commodityAmount, qualityDate:_qualityDate,
        listDate:_listDate, receipt_state:_receipt_state, otherInfo:"Change ownerAddress"}));
    }

    function changeamount(uint64 newcommodityAmount, string memory newInfo) public{
        _commodityAmount = newcommodityAmount;
        _receiptTrace.push(ReceiptTrace({operatorAddress:_operatorAddress, receiptID:_receiptID, ownerAddress:_ownerAddress, settelId:_settelId,
        commodityId:_commodityId, commodityWeight:_commodityWeight, commodityAmount:newcommodityAmount, qualityDate:_qualityDate,
        listDate:_listDate, receipt_state:_receipt_state, otherInfo: newInfo}));
    }

    //  返回Trace info情况
    function getTracce() public view returns(ReceiptTrace[] memory _data) {
        return _receiptTrace;
    }
    
}
