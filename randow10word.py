from urllib2 import urlopen         # из модуля urllib2 импортируем функцию urlopen

u = urlopen("http://python.org")    # открываем URL на чтение
words = {}                          # связываем имя words с пустым словарём
                                    # (словарь — неупорядоченный [[ассоциативный массив]])
for line in u:                      # читаем u по строкам
    line = line.strip(" \n")        # отбрасываем начальные и конечные пробелы
    for word in line.split(" "):    # режем каждую строку на слова, ограниченные пробелами
        try:                        # блок обработки исключений
            words[word] += 1        # пытаемся увеличить words[word] на единицу
        except KeyError:            # если не получилось (раньше words[word] не было)
            words[word] = 1         # присваиваем единицу

# теперь словарь words содержит частоту встречаемости каждого слова.
# например, words может содержать {"яблоко": 5, "апельсин": 12, "груша": 8}

pairs = words.items()               # делаем из словаря список пар
                                    # pairs == [("яблоко",5), ("апельсин",12), ("груша",8)]
pairs.sort(key=lambda x: x[1], reverse=True)  # сортируем по убыванию второго элемента пары

for p in pairs[:10]:                # печатаем первые 10 элементов списка
    print(p[0], p[1])

####################################################################
# пример использования Counter из стандартной библиотеки
from urllib2 import urlopen
from collections import Counter
from re import findall

page = urlopen("http://python.org").read()
words = findall(r"\w+", page)
counter = Counter(words)

print(counter.most_common(10))
#[('a', 417), ('class', 354), ('li', 304), ('href', 211), ('span', 142), ('2', 135), ('title', 135), ('tier', 125), ('element', 122), ('role', 120)]