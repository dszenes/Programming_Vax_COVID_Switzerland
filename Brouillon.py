from Canton_Class import nat_doses, swiss_pop, equi_distr
from Canton_data import cantons

i = 0
total = 0

for i in range(len(nat_doses)):
    mode = input('Please, enter a  mode = ')
    if mode == 'manual':
        available_doses = nat_doses[i]
        for canton in cantons:
            print(canton)
            print('Available doses:', available_doses)
            number = float(input('Please, enter a rate = '))
            doses = number * nat_doses[i] * (canton.pop/swiss_pop)
            if doses > available_doses:
                print("All doses consumed for this round")
                canton.receive(available_doses, cantons)
                canton.use(available_doses)
                print(canton)
                break
            else:
                available_doses -= doses
                canton.receive(doses, cantons)
                canton.use(doses)
                print(canton)

    elif mode == 'equity':
        equi_distr(cantons, i)
        for canton in cantons:
            print(canton)




