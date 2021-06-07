

T = 12


initial_usage = 0

initial_stock = 0

class Canton:
    def __init__(self, pop, prio_pop):
        self.pop = pop
        self.prio_pop = prio_pop
        self.vstock = initial_stock
        self.used_doses = initial_usage

    def receive(self, doses):
        self.vstock += doses

    def use(self, usage, doses):
        self.vstock -= usage*doses
        self.used_doses += usage*doses
