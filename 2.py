import pandas as pd
# Подключаем файл и переименовываем столбцы
data = pd.read_csv('kinopoisk.csv')
columns_mappimg = {'film-item-rating-position__position' : 'Место в рейтинге',
'selection-film-item-poster__rating' : 'Рейтинг 1',
'selection-film-item-meta__name' : "Название",
'selection-film-item-meta__meta-additional-item' : "Страна",
'selection-film-item-meta__meta-additional-item 2' : "Жанр",
'rating__value' : "Рейтинг 2",
'rating__count' : "Счет рейтинга"}
data = data.rename(columns = columns_mappimg)
from scipy.stats import mannwhitneyu
Так как мы имеем дело с порядковыми данными и проводим анализ по 2 критериям, то,
согласно таблице со второй лекции, выбираем анализ с помощью критерия МаннаУитни. Выдвигамем нулевую гипотезу: рейтинги не имеют отличий и проверяем её с
помощью p-value
0.15364369832961478
# Нулевая гипотеза - рейтинги не отличаются
result = mannwhitneyu(data['Рейтинг 1'], data['Рейтинг 2'])
result.pvalue
P-value больше 0.05, следовательно, мы можем сделать вывод: данные отличны друг от
друга.
