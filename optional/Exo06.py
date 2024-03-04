# EXO6: option

import smartpy as sp


@sp.module
def main():
    class Account(sp.Contract):

        def __init__(self):
            self.data.total = 0
            self.data.lastUser = None

        @sp.entry_point
        def add(self, value):

            if self.data.lastUser.is_some():
                if sp.sender == self.data.lastUser.unwrap_some(error="Not an adress!"):
                    raise "Not Allowed"

                else:
                    self.data.lastUser = sp.Some(sp.sender)
                    self.data.total += value

            else:
                self.data.lastUser = sp.Some(sp.sender)
                self.data.total += value

        @sp.entry_point
        def sub(self, value):

            if self.data.lastUser.is_some():
                if sp.sender == self.data.lastUser.unwrap_some(error="Not a some!"):
                    raise "Not Allowed"


                else:
                    self.data.lastUser = sp.Some(sp.sender)
                    self.data.total -= value

            else:
                self.data.lastUser = sp.Some(sp.sender)
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