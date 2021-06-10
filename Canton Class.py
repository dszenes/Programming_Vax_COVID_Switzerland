

T = 13

swiss_pop = 8644169

Cantons = []

nat_rates = [2.18, 1.65, 0.62, 4.43, 5.65, 1.83, 1.83, 2.65, 5.09, 7.17, 1.36, 10.12, 13.19 ]

for dose in nat_rates:
    nat_doses = []
    nat_doses.append(round((swiss_pop*dose)/100))

class Canton:
    def __init__(self,name, pop, usage, init_vstock, init_used_doses):
        self.name = name
        self.pop = pop
        self.usage = usage
        self.vstock = init_vstock
        self.used_doses = init_used_doses


    def receive(self, doses):
        self.vstock += doses

    def use(self):
        self.vstock -= self.usage*self.vstock
        self.used_doses += self.usage*self.vstock


def equi_distr(cantons, round):
    for canton in cantons:
        cdoses = nat_doses[round]*(canton.pop/swiss_pop)
        canton.receive(cdoses)
        canton.use(cdoses)

def opti_distr(cantons, round, min_rate, max_rate):
    rem_doses = nat_doses[round] - min_rate
    ranked_cantons = sorted(cantons, key=lambda canton: canton.usage, reverse=True)
    for canton in cantons:
        base_dose = nat_doses[round]*(swiss_pop/canton.pop)*min_rate
        canton.receive(base_dose)
        canton.use(base_dose)

    for canton in ranked_cantons:
        extra_dose = rem_doses*(canton.pop/swiss_pop)*max_rate
        while rem_doses > extra_dose:
            canton.receive(extra_dose)
            canton.use(extra_dose)
            rem_doses -= extra_dose
        else:
            canton.receive(rem_doses)
            canton.use(rem_doses)











