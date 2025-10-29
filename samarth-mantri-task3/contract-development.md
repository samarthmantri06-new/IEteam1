(1) :-
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloVPN {
    string private greeting;        // Stores the greeting message
    uint256 private nodeCount;      // Stores the number of VPN nodes
    address private deployer;       // Stores the address of the deployer

    constructor() {
        deployer = msg.sender;      // Runs once when deployed - saves deployer address
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;       // Sets the greeting message
    }

    function getGreeting() public view returns (string memory) {
        return greeting;            // Returns the stored greeting message
    }

    function setNodeCount(uint256 _count) public {
        nodeCount = _count;         // Sets the node count
    }

    function getNodeCount() public view returns (uint256) {
        return nodeCount;           // Returns the node count
    }

    function getDeployerAddress() public view returns (address) {
        return deployer;            // Returns the deployer's address
    }
}


(2) :- 
1. A constructor is a special function in Solidity that runs only once, when the contract is first deployed on the blockchain.
2. Explanation of the keyword used :-
	(A) :- public :- makes that particular function or method accessible to anyone.
	(B) :- private :- the variable or the function have a restricted access and can only be accessed by the same particular contract , not by the derived one or the other.
	(C) :- view :- it means that the particular function cannot modify or change it only can read it/
	(D) :- memory :- Used for temporary storage of data during a function call. Data in memory exists only while the function is executing and is not saved permanently on the blockchain.
3. msg.sender :- msg.sender is a built-in global variable in Solidity that gives the Ethereum address of the account (or contract) that called or triggered the function.
4. we do so to tell the solidity about what data we are storing, allows the complier to optimize the storage and prevent the errors and the mismatched data while computation.


(3) :- 
i - A state variable is a variable that is stored permanently on the blockchain inside the contract. Its value stays there even after the function ends, unlike temporary (local) variables.
ii - State variables are stored in the Ethereum blockchain’s storage — specifically in the contract’s storage area on the blockchain, not in computer’s memory.
iii - Nothing changes — because the data is not stored on your computer, it’s stored on the blockchain.
iv - screenshot.
