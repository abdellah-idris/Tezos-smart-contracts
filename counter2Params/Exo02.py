import smartpy as sp

@sp.module
def main():
    class Counter2(sp.Contract):
        def __init__(self):
            self.data.v = 0

        @sp.entrypoint
        def inc(self):
            self.data.v += 1

        @sp.entrypoint
        def dec(self):
            self.data.v -= 1


if "main" in __name__:
    @sp.add_test()
    def test():
        scenario = sp.test_scenario("counter2", main)
        c1 = main.Counter2()

        scenario.h1("Counter2Entry")

        scenario += c1
        c1.inc()
        c1.dec()