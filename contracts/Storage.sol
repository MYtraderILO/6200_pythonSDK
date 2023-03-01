//SPDX-License-Identifier: MIT
pragma solidity ^0.4.24;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract Storage {

    string number;

    /**
     * @dev Store value in variable
     * @param num value to store
     */
    function store(string num) public {
        number = num;
    }

    /**
     * @dev Return value
     * @return value of 'number'
     */
    function retrieve() public view returns (string){
        return number;
    }
}
