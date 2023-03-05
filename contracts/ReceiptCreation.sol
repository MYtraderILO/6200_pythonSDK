//SPDX-License-Identifier: MIT
pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;

import "./DigitalReceipt.sol";
// import "./create.sol";
//import "./Operator.sol";
contract ReceiptCreation{

    struct ReceiptDatas{
        DigitalReceipt digitalreceipt;
        bool valid;
    }

    mapping(uint64=>ReceiptDatas) public receiptDatas;
}
