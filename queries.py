import psycopg2

def execute(queries):
    try:
        db = pg.connect(
            database='movies',
            user='postgres',
            password='password',
            host='localhost',
            port='5432'
        )
        db.autocommit = True
        cursor = db.cursor()
        for query in queries:
            cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)


    except:
        print('0')
    finally:
        if (db):
            cursor.close()
            db.close()


#Узнаем, какие страны, кроме США, есть в списке
execute(["SELECT COUNT(DISTINCT country) from trivia WHERE country != 'США'"])
execute(["SELECT DISTINCT country from trivia WHERE country != 'США'"])


"""18
Аргенитина 
Великобритания 
Бразилия 
Япония 
Франция 
Турция 
Ливан 
Иран 
Швеция 
Южная Корея 
Индия 
Испания 
Алжир 
Новая Зеландия 
СССР 
Мексика 
Италия 
Германия""" 



#Оскароносные фильмы, находящиеся в топе-250 по сей день 

execute(["SELECT film FROM oscars o INNER JOIN topfilm t ON o.film = t.name"])
"""Бен-Гур
Молчание ягнят
Малышка на миллион
Крёстный отец 2
Властелин колец: Возвращение короля
Это случилось однажды ночью
Квартира
Ребекка
Амадей
Непрощённый
Старикам тут не место
Лоуренс Аравийский
В центре внимания
Охотник на оленей
Крёстный отец
Унесённые ветром
Звуки музыки
Всё о Еве
Игры разума
Красота по-американски
Список Шиндлера
Пролетая над гнездом кукушки
Лучшие годы нашей жизни
Касабланка
Паразиты
Отступники
Афера
Взвод
Рокки
В порту
12 лет рабства
Мост через реку Квай
Храброе сердце
Гладиатор
Ганди
Зелёная книга
Форрест Гамп"""


execute(["SELECT COUNT(film) FROM oscars"])
"""94"""

"""ответ: 28/94"""

#Хронологическая популярность
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1920 and year < 1930"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1930 and year < 1940"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1940 and year < 1950"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1950 and year < 1960"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1960 and year < 1970"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1970 and year < 1980"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1980 and year < 1990"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 1990 and year < 2000"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 2000 and year < 2010"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 2010 and year < 2020"])
execute(["SELECT COUNT(id) FROM trivia WHERE year >= 2020"])

"""6
7
12
23
18
19
27
41
48
43
6"""

#Самый популярный режиссер
execute(["SELECT director, COUNT(director) AS t1 FROM authors GROUP BY director ORDER BY  t1 DESC LIMIT 1;"])
"""Мартин Скорсезе"""

#Список актеров, игравших в комедиях и в детективах
execute(["""SELECT actor FROM actors JOIN trivia ON actors.id = trivia.id WHERE trivia.genre = 'детектив' 
INTERSECT SELECT actor FROM actors JOIN trivia ON actors.id = trivia.id WHERE trivia.genre = 'комедия'"""])
"""Мэттью Макконахи
Том Хэнкс
Сергей Бондарчук
Леонардо ДиКаприо
Георгий Юматов
Майкл Дж. Фокс"""

#Список оскароносных фильмов в топе-250 по популярности 
execute(["SELECT film FROM oscars o INNER JOIN topfilm t ON o.film = t.name"])
"""Крёстный отец
Крёстный отец 2
Список Шиндлера
Властелин колец: Возвращение короля
Форрест Гамп
Пролетая над гнездом кукушки
Молчание ягнят
Паразиты
Гладиатор
Отступники
Касабланка
Красота по-американски
Амадей
Храброе сердце
Лоуренс Аравийский
Квартира
Афера
Всё о Еве
Зелёная книга
Непрощённый
Игры разума
Старикам тут не место
Унесённые ветром
Мост через реку Квай
Малышка на миллион
В порту
12 лет рабства
Бен-Гур
Охотник на оленей
Рокки
Взвод
В центре внимания
Лучшие годы нашей жизни
Ребекка
Это случилось однажды ночью
Звуки музыки
Ганди"""

#Автор самого популярного оскароносного фильма
execute(["SELECT director FROM authors WHERE id = (SELECT MIN(id) FROM topfilm t INNER JOIN oscars o ON o.film = t.name)"])

#Найдем лучший год в истории кино (с наибольшим количеством фильмов)
execute(["""SELECT year,COUNT(*) 
  FROM trivia
  GROUP BY year
  ORDER BY 2 DESC LIMIT 1"""])

"""(1995, 8)"""





