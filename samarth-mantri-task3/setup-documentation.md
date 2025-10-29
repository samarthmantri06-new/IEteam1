(1) -
List Of Dependencies installed from package.json:-
 devDependency  `@nomicfoundation/hardhat-ignition`              `^3.0.3`                             
 devDependency  `@nomicfoundation/hardhat-toolbox-mocha-ethers`  `^3.0.0`                             
 devDependency  `@types/chai`                                    `^4.3.20`                            
 devDependency  `@types/chai-as-promised`                        `^8.0.2`                             
 devDependency  `@types/mocha`                                   `^10.0.1`                            
 devDependency  `@types/node`                                    `^22.13.8`                           
 devDependency  `chai`                                           `^5.3.3`                             
 devDependency  `ethers`                                         `^6.15.0`                            
 devDependency  `forge-std`                                      `github:foundry-rs/forge-std#v1.9.4` 
 devDependency  `hardhat`                                        `^3.0.9`                             
 devDependency  `mocha`                                          `^11.7.4`                            
 devDependency  `typescript`                                     `~5.8.0`                             


Hardhat :- Hardhat is a development environment and framework for Ethereum smart contracts. It helps developers write, compile, test, and deploy Solidity code efficiently — all in one place.
Reason to use it :- automatically complies your solidity contracts, also creates a local Ethereum network on our computer, integrates with mocha and chai so you can write automated tests for your contracts, provides easy scripts and plugins to deploy contracts to local / testnets network, also gives detailed stack traces and error messages, which make debugging solidity much easier. 

(2) - 
contracts , ignition , node_modules, scripts , test , hardhat.config.ts, package.json, README.md , etc.

reasons :-
i- contracts/ :- This folder contains all Solidity smart contracts that you create.
ii- scripts/ :- This folder stores deployment and interaction scripts written in JavaScript or TypeScript. You use these scripts to deploy your contracts to a blockchain network (like local Hardhat, Sepolia, or Mainnet).
iii - tests/ :- This folder holds testing scripts for verifying your smart contracts’ behavior. You can write tests using Mocha and Chai frameworks to ensure your contract works as expected before deploying it.

hardhat.config.ts :- 
This is the main configuration file for your Hardhat project. It defines important project settings such as:
Solidity compiler version, Plugin imports, Network configurations and Custom paths for contracts, scripts, and tests

