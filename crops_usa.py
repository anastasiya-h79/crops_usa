import pandas
import seaborn
from crops_ds import *

"""
Определить, что даст более точный прогноз объёма урожая: предсказание площади посевов или урожайности
production_t = acres_t * yield_t 

"""
# 1 стратегия.  Предскажем объём урожая за определённый год. Он равен реальной площади посевов за этот год * на прошлогоднюю урожайность
# берем реальные данные по площади посевов
predict_acres = []
for index in range(1, len(acres_usa)):
    predict_acres.append(acres_usa[index] * yield_usa[index-1])
#print(predict_acres)

# берем реальные данные по урожайности
predict_yield = []

# 2 стратегия.  Предскажем объём урожая за определённый год. Он равен произведению урожайности за каждый год, кроме 1980го на прошлогоднюю площадь посевов
for index in range(1, len(yield_usa)):
    predict_yield.append(yield_usa[index] * acres_usa[index - 1])

#print(predict_yield)

years_numbers = list(range(1980, 2020))
# разница реального и предсказанного урожая за каждый год - вычисляем ошибки предсказаний cтратегии 1
error_acres = []
for index in range(1, len(acres_usa)):
    error_acres.append(production_usa[index] - acres_usa[index] * yield_usa[index - 1])
print(error_acres)
seaborn.barplot(x=years_numbers[1:], y=error_acres)

# разница реального и предсказанного урожая за каждый год - вычисляем ошибки предсказаний cтратегии 2
error_yield = []
for index in range(1, len(yield_usa)):
    error_yield.append(production_usa[index] - yield_usa[index] * acres_usa[index-1])
print(error_yield)
seaborn.barplot(x=years_numbers[1:], y=error_yield)

# модули ошибок модели по стратегии 1
error_abs_acres = []
for values in range(len(error_acres)):
    error_abs_acres.append(abs(error_acres[values]))
print(error_abs_acres)
# MAE первой модели
print(sum(error_abs_acres) / len(error_abs_acres))

# модули ошибок модели по стратегии 2
error_abs_yield = []
for value in error_yield:
    error_abs_yield.append(abs(value))
# MAE второй модели
print(sum(error_abs_yield) / len(error_abs_yield))

#Средняя ошибка во 2й стратегии почти в два раза меньше, чем в первой