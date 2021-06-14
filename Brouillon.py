from Canton_Class import nat_doses, swiss_pop, equi_distr
from Canton_data import cantons

i = 0
total = 0

for i in range(len(nat_doses)):
    mode = input('Please, enter a  mode = ')
    if mode == 'manual':
        for canton in cantons:
            print(canton)
            number = float(input('Please, enter a rate = '))
            doses = number * nat_doses[i] * (canton.pop/swiss_pop)
            canton.receive(doses)
            canton.use(doses)
            print(canton)

    elif mode == 'equity':
        equi_distr(cantons, i)
        for canton in cantons:
            print(canton)




