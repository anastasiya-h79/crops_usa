import pandas
data = pandas.read_csv('crops_usa.csv')

states_unique = []
years_unique = []

# смотрим, какие штаты есть в столбце 'State'
for states in data['State']:
    if states not in states_unique:
        states_unique.append(states)

print(states_unique)
print(len(states_unique))

# смотрим, какие года есть в столбце 'Year'
for years in data['Year']:
    if years not in years_unique:
        years_unique.append(years)

print(years_unique)
print(len(years_unique))

# преобразуем Acres, Year и State в списки
acres = list(data['Acres'])
years = list(data['Year'])
states = list(data['State'])
production = list(data['Production'])

acres_2019 = []
states_2019 = []
production_2019 = []

# фильтруем значения в acres и states по значению в year (2019)
for index in range(len(years)):
    if years[index] == 2019:
        #acres_2019.append(acres[index])
        states_2019.append(states[index])
        production_2019.append(production[index])

#print(acres_2019)
#print(states_2019)

import seaborn

# смотрим урожайность по штатам за 2019г.
seaborn.barplot(x=production_2019, y=states_2019)

production = list(data['Production'])

# сумма площадей посевов по всем штатам по годам
acres_usa = []
# общий объём урожая по всем штатам для каждого года
production_usa = []

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

#print(acres_usa)
#print(production_usa)

years_unique = list(range(1980, 2020))

seaborn.barplot(x=years_unique, y=acres_usa)

# вычисляем урожайность по США по годам
yield_usa = []
for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])

#print(yield_usa)

# смотрим, как меняется урожайность в США по годам
seaborn.barplot(x=years_unique, y=yield_usa)