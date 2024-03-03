# EXO5: check sender before performing add or sub

import smartpy as sp


@sp.module
def main():
    owner = sp.address("tz1UMisusJioYPEpu8rkFq19LZguSQH4jJ94")

    class Account(sp.Contract):
        def __init__(self):
            self.data.total = 0
            self.data.lastUser = owner

        @sp.entry_point
        def add(self, value):
            if sp.sender == self.data.lastUser:
                raise "Cannot call twice, Not Autorized"


            else:
                self.data.lastUser = sp.sender
                self.data.total += value

        @sp.entry_point
        def sub(self, value):
            if sp.sender == self.data.lastUser:
                raise "Cannot call twice, Not Autorized"

            else:
                self.data.lastUser = sp.sender
                self.data.total -= value


# Tests
if "main" in __name__:
    sarah = sp.test_account("sarah")
    ziri = sp.test_account("ziri")


    @sp.add_test()
    def test():
        scenario = sp.test_scenario("Add-Sub", main)
        c = main.Account()

        scenario += c

        # pass
        c.add(1, _sender=ziri)
        c.sub(1, _sender=sarah)
        c.sub(1, _sender=ziri)

        # will fail
        c.add(1, _sender=ziri)