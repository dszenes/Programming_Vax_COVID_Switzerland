# initialize parameters number of rounds, overall swiss population, and doses receivd
per_round_change = 0.05460539532403539

T = 13

swiss_pop = 8644780

nat_rates = [2.18, 1.65, 0.62, 4.43, 5.65, 1.83, 1.83, 2.65, 5.09, 7.17, 1.36, 10.12, 13.19 ]

nat_doses = []

for dose in nat_rates:
    nat_doses.append(round((swiss_pop*dose)/100))

Cantons = [] # create empty list that we will fill with cantons

class Canton:
    def __init__(self,name, pop, init_base_usage, init_vstock, init_used_doses, stdev):
        self.name = name
        self.pop = pop
        self.stdev =stdev
        self.base_usage = init_base_usage # we will make this basic variable evolve positively by rounds
        self.init_vstock = init_vstock
        self.vstock = init_vstock # initial received doses
        self.used_doses = init_used_doses # initial administered doses


    def receive(self, doses):
        self.vstock += round(doses)

    def use(self, doses):
        self.base_usage = self.base_usage+(1-self.base_usage)*per_round_change
        self.used_doses += round(self.base_usage*doses)

    def __str__(self):
        s = '%s \n Population: %s \n base usage: %s\n received doses: %s\n used doses: %s' % (self.name, self.pop, self.base_usage, self.vstock, self.used_doses)
        return s


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



print(nat_doses)







