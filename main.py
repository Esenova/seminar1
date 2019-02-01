from myclass import Uzbek_Plov

p_type = input("Please, enter the plove type: ")

plov = Uzbek_Plov(p_type)

print(plov.plov_type + ' ' + plov.name)
print('Рис: ', plov.rice)
print('Мясо: ', plov.meat)
plov.get_portion()
plov.add_carrot()
