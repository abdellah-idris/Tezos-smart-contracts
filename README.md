# SmartPy Exercices

This repository contains a series of exercises completed using SmartPy, a Python-based smart contract development platform for the Tezos blockchain.


## Exercice 1: Counter Increment

**Objective:** Implement a simple counter with an increment function.

**Steps:**
1. Write the contract in the SmartPy IDE and include a test scenario.
2. Test the code in the SmartPy IDE.
3. Retrieve the Michelson code and test it using octez-client.
4. Deploy the contract using octez-client.
5. Interact with the contract by sending a transaction to its `inc()` entry point.
6. Verify all operations using a block explorer.

## Exercice 2: Increment & Decrement

**Objective:** Extend the counter contract to include a decrement function.

**Steps:**
1. Test the Michelson code with octez-client.
2. Originate the contract.
3. Make multiple calls to the contract, varying the entry points.
4. Verify the results obtained using octez-client or a block explorer.

## Exercice 3: String Concatenation

**Objective:** Write a contract that concatenates string values to its storage, separating each string by a comma.

**Steps:**
1. Implement the contract in the SmartPy IDE.
2. Test the contract in the IDE.
3. Retrieve and test the Michelson code.
4. Deploy the contract using octez-client.
5. Interact with the contract using a block explorer.

## Exercice 4: Storage Modification

**Objective:** Modify a contract to include a pair or record type storage containing TString and TInt components.

**Steps:**
1. Modify the contract to include the desired storage structure.
2. Test the contract's functionality in the SmartPy IDE.
3. Retrieve the Michelson code and test it.
4. Deploy the updated contract and verify its behavior.

## Exercice 5: Multi-Entrypoint Contract

**Objective:** Write a contract with two entry points (`add` and `sub`) to modify its storage.

**Steps:**
1. Implement the contract in the SmartPy IDE.
2. Test each entry point's functionality.
3. Retrieve the Michelson code and deploy the contract.
4. Interact with the contract using different addresses and verify its behavior.

## Exercice 6: Options Usage

**Objective:** Rewrite the contract from Exercise 5 using Options.

**Steps:**
1. Modify the contract to use Options for certain values.
2. Test the modified contract in the SmartPy IDE.
3. Deploy the contract and verify its behavior.

## Exercice 7: Donation Contract

**Objective:** Write a contract allowing the owner to receive donations and withdraw funds.

**Steps:**
1. Implement the contract in the SmartPy IDE.
2. Write tests to verify its functionality.
3. Originate the contract and test its behavior.
4. Verify the contract's operation using a block explorer.

## Conclusion

By completing these exercises, we gain practical experience in writing, testing, deploying, and interacting with smart contracts on the Tezos blockchain using SmartPy.