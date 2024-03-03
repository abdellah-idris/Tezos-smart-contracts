# Exo4: String concatenation + counter

import smartpy as sp


@sp.module
def main():
    class MyContract(sp.Contract):
        def __init__(self):
            self.data.text = ""
            self.data.counter = 0

        @sp.entry_point
        def concatenate(self, input):
            self.data.text += input + ","
            self.data.counter += 1


if "main" in __name__:
    @sp.add_test()
    def test():
        scenario = sp.test_scenario("concatenate", main)
        c = main.MyContract()

        scenario.h1("StringConcatenator")
        scenario += c
        c.concatenate("hola")
        c.concatenate("dola")
        scenario.verify(c.data.text == 'hola,dola,')
        scenario.verify(c.data.counter == 2)