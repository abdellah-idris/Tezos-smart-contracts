# EXO 07: Transaction

import smartpy as sp


@sp.module
def main():
    class DonationContract(sp.Contract):
        def __init__(self, owner):
            self.data.owner = owner
            self.data.balance = sp.tez(20)

        @sp.entry_point
        def donate(self):
            assert sp.amount > sp.mutez(0), "Cannot donate amount < 0 tez"
            self.data.balance += sp.amount

        @sp.entry_point
        def withdraw(self, amount):
            assert sp.sender == self.data.owner, "Only the owner can withdraw"
            assert self.data.balance >= amount, "Insufficient balance"
            sp.send(self.data.owner, amount)
            self.data.balance -= amount


if "main" in __name__:
    @sp.add_test()
    def test():
        scenario = sp.test_scenario("DonationContract", main)
        owner = sp.test_account("admin")
        donator = sp.test_account("donator")

        contract = main.DonationContract(owner.address)
        scenario += contract

        contract.donate(_sender=donator, _amount=sp.tez(40))
        contract.withdraw(sp.tez(1), _sender=owner)

        # Attempt to withdraw more than the balance
        contract.withdraw(sp.tez(100), _sender=owner)  # "Insufficient balance"

        # Attempt to withdraw more than the balance! Not executed, Insufficient balance before
        contract.withdraw(sp.tez(100), _sender=donator)  # "Only the owner can withdraw"