
"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import defaultdict


NUM_OF_QUARTERS = 4


companies_profit = defaultdict(list)
num_of_comanies = int(input('Ведите количество предприятий '))
profits_sum = 0
for _ in range(num_of_comanies):
     company = input('Введите компанию ')
     for quarter in range(1, NUM_OF_QUARTERS + 1):
         profit = float(input(f'Введите прибыль компании {company} за {quarter} квартал '))
         companies_profit[company].append(profit)
         profits_sum += profit


average_profit = profits_sum / (num_of_comanies)

below_average = []
above_average = []

for company in companies_profit:
    company_profit = sum(companies_profit[company])
    if company_profit >= average_profit:
        above_average.append((company, company_profit))
    else:
        below_average.append((company, company_profit))

print('Компании с дохоходами выше или равному среднему')
for company, profit in above_average:
    print(f'компания: {company}, прибыль: {profit}')
print('Компании с дохоходами ниже среднего')
for company, profit in below_average:
    print(f'компания: {company}, прибыль: {profit}')
