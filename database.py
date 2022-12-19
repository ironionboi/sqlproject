import psycopg2 as pg

db = pg.connect(
    database='movies',
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)


def create_topfilm(db):
    db.autocommit = True
    with db.cursor() as cursor:
        sql_commands = ["DROP TABLE IF EXISTS topfilm;",
                        "DROP TABLE IF EXISTS oscars;",
                        "DROP TABLE IF EXISTS authors;",
                        """CREATE TABLE  topfilm(
                             ranking    INT       NOT NULL,
                             name    VARCHAR(300)       NOT NULL,
                             year    INT         NOT NULL,
                             director    VARCHAR(300)        NOT NULL,
                             genre    VARCHAR(300)       NOT NULL,
                             rating    FLOAT       NOT NULL,
                             country VARCHAR(300) NOT NULL
                    );""",
                        """CREATE TABLE oscars
        (
            year	INT,
            film 	VARCHAR(300)
        );""",
            """CREATE TABLE authors
        (
            id INT,
            name	VARCHAR(300),
            director 	VARCHAR(300)
        );"""]
        for sql_command in sql_commands:
            cursor.execute(sql_command)

def fill_topfilm(db):
    db.autocommit = True
    with db.cursor() as cursor:
        sql_commands = ["INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('1', 'Побег из Шоушенка', '1994', 'Фрэнк Дарабонт', 'драма', '9.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('2', 'Крёстный отец', '1972', 'Фрэнсис Форд Коппола', 'детектив', '9.2', 'США ')",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('3', 'Тёмный рыцарь', '2008', 'Кристофер Нолан', 'боевик', '9', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('4', 'Крёстный отец 2', '1974', 'Фрэнсис Форд Коппола', 'детектив', '9', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('5', '12 разгневанных мужчин', '1957', 'Сидни Люмет', 'драма', '9', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('6', 'Список Шиндлера', '1993', 'Стивен Спилберг', 'драма', '8.9', 'Новая Зеландия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('7', 'Властелин колец: Возвращение короля', '2003', 'Питер Джексон', 'фэнтези', '8.9', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('8', 'Криминальное чтиво', '1994', 'Квентин Тарантино', 'чёрная комедия', '8.8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('9', 'Властелин колец: Братство Кольца', '2001', 'Питер Джексон', 'фэнтези', '8.8', 'Новая Зеландия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('10', 'Хороший, плохой, злой', '1966', 'Серджо Леоне', 'приключение', '8.8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('11', 'Форрест Гамп', '1994', 'Роберт Земекис', 'драма', '8.8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('12', 'Бойцовский клуб', '1999', 'Дэвид Финчер', 'драма', '8.7', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('13', 'Начало', '2010', 'Кристофер Нолан', 'боевик', '8.7', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('14', 'Властелин колец: Две крепости', '2002', 'Питер Джексон', 'фэнтези', '8.7', 'Новая Зеландия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('15', 'Звёздные войны. Эпизод V: Империя наносит ответный удар', '1980', 'Ирвин Кершнер', 'научная фантастика', '8.7', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('16', 'Матрица', '1999', 'Энди и Ларри Вачовски', 'научная фантастика', '8.7', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('17', 'Славные парни', '1990', 'Мартин Скорсезе', 'детектив', '8.7', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('18', 'Пролетая над гнездом кукушки', '1975', 'Милош Форман', 'драма', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('19', 'Семь', '1995', 'Дэвид Финчер', 'детектив', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('20', 'Семь самураев', '1954', 'Акира Куросава', 'приключение', '8.6', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('21', 'Эта прекрасная жизнь', '1946', 'Фрэнк Капра', 'драма', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('22', 'Молчание ягнят', '1991', 'Джонатан Демми', 'детектив', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('23', 'Город Бога', '2002', 'Фернанду Мейреллиш', 'детектив', '8.6', 'Бразилия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('24', 'Спасти рядового Райана', '1998', 'Стивен Спилберг', 'боевик', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('25', 'Жизнь прекрасна', '1997', 'Роберто Бениньи', 'драма', '8.6', 'Италия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('26', 'Зелёная миля', '1999', 'Фрэнк Дарабонт', 'детектив', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('27', 'Интерстеллар', '2014', 'Кристофер Нолан', 'приключение', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('28', 'Звёздные войны. Эпизод IV: Новая надежда', '1977', 'Джордж Лукас', 'научная фантастика', '8.6', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('29', 'Терминатор 2: Судный день', '1991', 'Джеймс Кэмерон', 'боевик', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('30', 'Назад в будущее', '1985', 'Роберт Земекис', 'научная фантастика', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('31', 'Унесённые призраками', '2001', 'Хаяо Миядзаки', 'аниме', '8.5', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('32', 'Психо', '1960', 'Альфред Хичкок', 'фильм ужасов', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('33', 'Пианист', '2002', 'Роман Полански', 'биография', '8.5', 'Франция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('34', 'Леон', '1994', 'Люк Бессон', 'детектив', '8.5', 'Франция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('35', 'Паразиты', '2019', 'Пон Чжун Хо', 'комедия', '8.5', 'Южная Корея ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('36', 'Король Лев', '1994', 'Роджер Аллерс', 'мультфильм', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('37', 'Гладиатор', '2000', 'Ридли Скотт', 'боевик', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('38', 'Американская история Икс', '1998', 'Тони Кэй', 'драма', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('39', 'Отступники', '2006', 'Мартин Скорсезе', 'детектив', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('40', 'Подозрительные лица', '1995', 'Брайан Сингер', 'детектив', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('41', 'Престиж', '2006', 'Кристофер Нолан', 'фэнтези', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('42', 'Касабланка', '1942', 'Майкл Кёртиц', 'мелодрама', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('43', 'Одержимость', '2014', 'Дамьен Шазель', 'драма', '8.5', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('44', '1+1', '2011', 'Оливье Накаш, Эрик Толедано', 'трагикомедия', '8.5', 'Франция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('45', 'Могила светлячков', '1988', 'Исао Такахата', 'мультфильм', '8.5', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('46', 'Харакири', '1962', 'Масаки Кобаяси', 'боевик', '8.5', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('47', 'Новые времена', '1936', 'Чарли Чаплин', 'комедия', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('48', 'Однажды на Диком Западе', '1968', 'Серджо Леоне', 'вестерн', '8.4', 'Италия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('49', 'Окно во двор', '1954', 'Альфред Хичкок', 'детектив', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('50', 'Чужой', '1979', 'Ридли Скотт', 'фильм ужасов', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('51', 'Огни большого города', '1931', 'Чарли Чаплин', 'комедия', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('52', 'Новый кинотеатр «Парадизо»', '1988', 'Джузеппе Торнаторе', 'комедия', '8.4', 'Италия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('53', 'Апокалипсис сегодня', '1979', 'Фрэнсис Форд Коппола', 'драма', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('54', 'Помни', '2000', 'Кристофер Нолан', 'детектив', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('55', 'Индиана Джонс: В поисках утраченного ковчега', '1981', 'Стивен Спилберг', 'приключение', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('56', 'Джанго освобождённый', '2012', 'Квентин Тарантино', 'приключение', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('57', 'ВАЛЛ-И', '2008', 'Эндрю Стэнтон', 'мультфильм', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('58', 'Жизнь других', '2006', 'Флориан Хенкель фон Доннерсмарк', 'драма', '8.4', 'Германия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('59', 'Бульвар Сансет', '1950', 'Билли Уайлдер', 'драма', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('60', 'Тропы славы', '1957', 'Стэнли Кубрик', 'драма', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('61', 'Сияние', '1980', 'Стэнли Кубрик', 'фильм ужасов', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('62', 'Великий диктатор', '1940', 'Чарли Чаплин', 'комедия', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('63', 'Мстители: Война бесконечности', '2018', 'Братья Руссо', 'боевик', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('64', 'Свидетель обвинения', '1957', 'Билли Уайлдер', 'детектив', '8.4', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('65', 'Чужие', '1986', 'Джеймс Кэмерон', 'фильм ужасов', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('66', 'Красота по-американски', '1999', 'Сэм Мендес', 'драма', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('67', 'Человек-паук: Через вселенные', '2018', 'Боб Персичетти', 'мультфильм', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('68', 'Доктор Стрейнджлав, или Как я перестал бояться и полюбил бомбу', '1964', 'Стэнли Кубрик', 'комедия', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('69', 'Топ Ган: Мэверик', '2022', 'Джозеф Косински', 'боевик', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('70', 'Тёмный рыцарь: Возрождение легенды', '2012', 'Кристофер Нолан', 'боевик', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('71', 'Олдбой', '2003', 'Пак Чхан Ук', 'драма', '8.3', 'Южная Корея ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('72', 'Джокер', '2019', 'Тодд Филлипс', 'детектив', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('73', 'Амадей', '1984', 'Милош Форман', 'биография', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('74', 'Храброе сердце', '1995', 'Мел Гибсон', 'боевик', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('75', 'История игрушек', '1995', 'Джон Лассетер', 'мультфильм', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('76', 'Тайна Коко', '2017', 'Ли Анкрич', 'мультфильм', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('77', 'Бесславные ублюдки', '2009', 'Квентин Тарантино', 'военный фильм', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('78', 'Подводная лодка', '1981', 'Вольфганг Петерсен', 'боевик', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('79', 'Мстители: Финал', '2019', 'Братья Руссо', 'боевик', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('80', 'Принцесса Мононоке', '1997', 'Хаяо Миядзаки', 'мультфильм', '8.3', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('81', 'Однажды в Америке', '1984', 'Серджио Леоне', 'гангстерский фильм', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('82', 'Умница Уилл Хантинг', '1997', 'Гас Ван Сент', 'драма', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('83', 'Твоё имя', '2016', 'Макото Синкай', 'мультфильм', '8.3', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('84', 'Реквием по мечте', '2000', 'Даррен Аронофски', 'драма', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('85', 'История игрушек: Большой побег', '2010', 'Ли Анкрич', 'мультфильм', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('86', 'Поющие под дождём', '1952', 'Стэнли Донен', 'комедия', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('87', '3 идиота', '2009', 'Раджкумар Хирани', 'комедия', '8.3', 'Индия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('88', 'Рай и ад', '1963', 'Акира Куросава', 'детектив', '8.3', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('89', 'Звёздные войны. Эпизод VI: Возвращение джедая', '1983', 'Ричард Маркуанд', 'научная фантастика', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('90', 'Космическая одиссея 2001 года', '1968', 'Стэнли Кубрик', 'Кинофантастика', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('91', 'Вечное сияние чистого разума', '2004', 'Мишель Гондри', 'драма', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('92', 'Бешеные псы', '1992', 'Квентин Тарантино', 'детектив', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('93', 'Капернаум', '2018', 'Надин Лабаки', 'драма', '8.3', 'Ливан ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('94', 'Охота', '2012', 'Томас Винтерберг', 'драма', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('95', 'Лоуренс Аравийский', '1962', 'Дэвид Лин', 'приключение', '8.3', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('96', 'Гражданин Кейн', '1941', 'Орсон Уэллс', 'драма', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('97', 'М', '1931', 'Фриц Ланг', 'триллер', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('98', 'К северу через северо-запад', '1959', 'Альфред Хичкок', 'приключение', '8.3', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('99', 'Иди и смотри', '1985', 'Элем Климов', 'драма', '8.2', 'СССР ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('100', 'Головокружение', '1958', 'Альфред Хичкок', 'детектив', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('101', 'Амели', '2001', 'Жан-Пьер Жене', 'комедия', '8.2', 'Франция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('102', 'Заводной апельсин', '1971', 'Стэнли Кубрик', 'научная фантастика', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('103', 'Двойная страховка', '1944', 'Билли Уайлдер', 'детектив', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('104', 'Квартира', '1960', 'Билли Уайлдер', 'мелодрама', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('105', 'Цельнометаллическая оболочка', '1987', 'Стэнли Кубрик', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('106', 'Жить', '1952', 'Акира Куросава', 'драма', '8.2', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('107', 'Лицо со шрамом', '1983', 'Брайан де Пальма', 'детектив', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('108', 'Убить пересмешника', '1962', 'Роберт Маллиган', 'детектив', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('109', 'Афера', '1973', 'Джордж Рой Хилл', 'комедия', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('110', 'Гамильтон', '2020', 'Томас Кейл', 'биография', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('111', 'Схватка', '1995', 'Майкл Манн', 'детектив', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('112', 'Таксист', '1976', 'Мартин Скорсезе', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('113', 'Вверх', '2009', 'Пит Доктер', 'мультфильм', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('114', 'Пожары', '2010', 'Дени Вильнёв', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('115', 'Секреты Лос-Анджелеса', '1997', 'Кёртис Хэнсон', 'триллер', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('116', 'Развод Надера и Симин', '2011', 'Асгар Фархади', 'драма', '8.2', 'Иран ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('117', 'Метрополис', '1927', 'Фриц Ланг', 'научная фантастика', '8.2', 'Германия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('118', 'Крепкий орешек', '1988', 'Джон Мактирнан', 'боевик', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('119', 'Большой куш', '2000', 'Гай Ричи', 'детектив', '8.2', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('120', 'Похитители велосипедов', '1948', 'Витторио де Сика', 'детектив', '8.2', 'Италия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('121', 'Индиана Джонс и последний крестовый поход', '1989', 'Стивен Спилберг', 'приключение', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('122', '1917', '2019', 'Сэм Мендес', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('123', 'Звёздочки на земле', '2007', 'Аамир Хан', 'драма', '8.2', 'Индия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('124', 'Бункер', '2004', 'Оливер Хиршбигель', 'биография', '8.2', 'Испания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('125', 'На несколько долларов больше', '1965', 'Серджо Леоне', 'вестерн', '8.2', 'Италия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('126', 'Бэтмен: Начало', '2005', 'Кристофер Нолан', 'боевик', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('127', 'Дангал', '2016', 'Нитеш Тивари', 'боевик', '8.2', 'Индия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('128', 'Малыш', '1921', 'Чарли Чаплин', 'комедия', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('129', 'В джазе только девушки', '1959', 'Билли Уайлдер', 'комедия', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('130', 'Всё о Еве', '1950', 'Джозеф Лео Манкевич', 'детектив', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('131', 'Отец', '2020', 'Флориан Зеллер', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('132', 'Зелёная книга', '2018', 'Питер Фаррелли', 'биография', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('133', 'Волк с Уолл-стрит', '2013', 'Мартин Скорсезе', 'биография', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('134', 'Нюрнбергский процесс', '1961', 'Стэнли Крамер', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('135', 'Ран', '1985', 'Акира Куросава', 'боевик', '8.2', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('136', 'Казино', '1995', 'Мартин Скорсезе', 'биография', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('137', 'Непрощённый', '1992', 'Клинт Иствуд', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('138', 'Лабиринт фавна', '2006', 'Гильермо дель Торо', 'фэнтези', '8.2', 'Мексика ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('139', 'Человек-паук: Нет пути домой', '2021', 'Джон Уоттс', 'научная фантастика', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('140', 'Нефть', '2007', 'Пол Томас Андерсон', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('141', 'Шоу Трумана', '1998', 'Питер Уир', 'комедия', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('142', 'Шестое чувство', '1999', 'М. Найт Шьямалан', 'драма', '8.2', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('143', 'Игры разума', '2001', 'Рон Ховард', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('144', 'Монти Пайтон и Священный Грааль', '1975', 'Терри Гиллиам, Терри Джонс', 'приключение', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('145', 'Телохранитель', '1961', 'Акира Куросава', 'боевик', '8.1', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('146', 'Сокровища Сьерра-Мадре', '1948', 'Джон Хьюстон', 'приключение', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('147', 'Остров проклятых', '2010', 'Мартин Скорсезе', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('148', 'Парк юрского периода', '1993', 'Стивен Спилберг', 'приключение', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('149', 'Расёмон', '1950', 'Акира Куросава', 'драма', '8.1', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('150', 'Большой побег', '1963', 'Джон Стёрджес', 'приключение', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('151', 'Убить Билла. Фильм 1', '2003', 'Квентин Тарантино', 'боевик', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('152', 'Старикам тут не место', '2007', 'Братья Коэн', 'детектив', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('153', 'В поисках Немо', '2003', 'Эндрю Стэнтон', 'мультфильм', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('154', 'Человек-слон', '1980', 'Дэвид Линч', 'биография', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('155', 'Китайский квартал', '1974', 'Роман Полански', 'детектив', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('156', 'Бешеный бык', '1980', 'Мартин Скорсезе', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('157', 'Нечто', '1982', 'Джон Карпентер', 'научная фантастика', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('158', 'Унесённые ветром', '1939', 'Виктор Флеминг', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('159', 'V — значит вендетта', '2006', 'Джеймс Мактиг', 'боевик', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('160', 'Головоломка', '2015', 'Пит Доктер', 'мультфильм', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('161', 'Карты, деньги, два ствола', '1998', 'Гай Ричи', 'детектив', '8.1', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('162', 'В случае убийства набирайте «М»', '1954', 'Альфред Хичкок', 'детектив', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('163', 'Тайна в его глазах', '2009', 'Хуан Хосе Кампанелья', 'драма', '8.1', 'Аргенитина ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('164', 'Ходячий замок', '2004', 'Хаяо Миядзаки', 'аниме', '8.1', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('165', 'Мост через реку Квай', '1957', 'Дэвид Лин', 'приключение', '8.1', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('166', 'Три билборда на границе Эббинга, Миссури', '2017', 'Мартин Макдонах', 'комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('167', 'На игле', '1996', 'Дэнни Бойл', 'детектив', '8.1', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('168', 'Воин', '2011', 'Гэвин О’Коннор', 'боевик', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('169', 'Гран Торино', '2008', 'Клинт Иствуд', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('170', 'Фарго', '1996', 'Братья Коэн', 'детектив', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('171', 'Пленницы', '2013', 'Дени Вильнёв', 'детектив', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('172', 'Мой сосед Тоторо', '1988', 'Хаяо Миядзаки', 'мультфильм', '8.1', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('173', 'Малышка на миллион', '2004', 'Клинт Иствуд', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('174', 'Поймай меня, если сможешь', '2002', 'Стивен Спилберг', 'биография', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('175', 'Золотая лихорадка', '1925', 'Чарли Чаплин', 'комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('176', 'Бегущий по лезвию', '1982', 'Ридли Скотт', 'научная фантастика', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('177', 'Дети небес', '1997', 'Маджид Маджиди', 'драма', '8.1', 'Иран ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('178', 'В порту', '1954', 'Элиа Казан', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('179', 'Третий человек', '1949', 'Кэрол Рид', 'нуар', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('180', 'Перед рассветом', '1995', 'Ричард Линклейтер', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('181', '12 лет рабства', '2013', 'Стив Маккуин', 'биография', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('182', 'Бен-Гур', '1959', 'Уильям Уайлер', 'боевик', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('183', 'Земляничная поляна', '1957', 'Ингмар Бергман', 'драма', '8.1', 'Швеция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('184', 'Гарри Поттер и Дары Смерти. Часть 2', '2011', 'Дэвид Йейтс', 'фэнтези', '8.1', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('185', 'Исчезнувшая', '2014', 'Дэвид Финчер', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('186', 'Генерал', '1927', 'Клайд Брукман', 'комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('187', 'Охотник на оленей', '1978', 'Майкл Чимино', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('188', 'Во имя отца', '1993', 'Джим Шеридан', 'биография', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('189', 'Отель «Гранд Будапешт»', '2014', 'Уэс Андерсон', 'комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('190', 'Барри Линдон', '1975', 'Стэнли Кубрик', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('191', 'Плата за страх', '1953', 'Анри-Жорж Клузо', 'приключение', '8.1', 'Франция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('192', 'Мистер Смит едет в Вашингтон', '1939', 'Фрэнк Капра', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('193', 'По соображениям совести', '2016', 'Мел Гибсон', 'биография', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('194', 'Шерлок-младший', '1924', 'Бастер Китон', 'боевик', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('195', 'Воспоминания об убийстве', '2003', 'Пон Чжун Хо', 'драма', '8.1', 'Южная Корея ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('196', 'Клаус', '2019', 'Серхио Паблос', 'мультфильм', '8.1', 'Испания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('197', 'Дикие истории', '2014', 'Дамиан Шифрон', 'комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('198', 'Седьмая печать', '1957', 'Ингмар Бергман', 'драма', '8.1', 'Швеция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('199', 'Комната', '2015', 'Ленни Абрахамсон', 'драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('200', 'Безумный Макс: Дорога ярости', '2015', 'Джордж Миллер', 'боевик', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('201', 'Как приручить дракона', '2010', 'Крис Сандерс', 'мультфильм', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('202', 'Мэри и Макс', '2009', 'Адам Эллиот', 'приключение', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('203', 'Большой Лебовски', '1998', 'Братья Коэн', 'комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('204', 'Челюсти (фильм)', '1975', 'Стивен Спилберг', 'фильм ужасов', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('205', 'Корпорация монстров', '2001', 'Пит Доктер, Дэвид Силверман', 'мультфильм', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('206', 'Токийская повесть', '1953', 'Ясудзиро Одзу', 'драма', '8.1', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('207', 'Всё везде и сразу', '2022', 'Дэн Кван', 'чёрная комедия', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('208', 'Общество мёртвых поэтов', '1989', 'Питер Уир', 'Комедийная драма', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('209', 'Страсти Жанны д’Арк', '1928', 'Карл Теодор Дрейер', 'биография', '8.1', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('210', 'Отель Руанда', '2004', 'Терри Джордж', 'биография', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('211', 'Ford против Ferrari', '2019', 'Джеймс Мэнголд', 'фильм о спорте', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('212', 'Рокки', '1976', 'Джон Эвилдсен', 'фильм о спорте', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('213', 'Взвод', '1986', 'Оливер Стоун', 'боевик', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('214', 'Песнь дороги', '1955', 'Сатьяджит Рай', 'драма', '8', 'Индия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('215', 'Терминатор', '1984', 'Джеймс Кэмерон', 'фэнтези', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('216', 'Останься со мной', '1986', 'Роб Райнер', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('217', 'В центре внимания', '2015', 'Томас Маккарти', 'биография', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('218', 'Гонка', '2013', 'Рон Ховард', 'фильм-биография', '8', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('219', 'Логан', '2017', 'Джеймс Мэнголд', 'боевик', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('220', 'Рататуй ', '2007', 'Брэд Бёрд', 'мультфильм', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('221', 'Телесеть', '1975', 'Сидни Люмет', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('222', 'В диких условиях', '2007', 'Шон Пенн', 'приключение', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('223', 'Волшебник страны Оз ', '1939', 'Виктор Флеминг', 'приключения', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('224', 'День сурка', '1993', 'Гарольд Рамис', 'комедия', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('225', 'Перед закатом', '2004', 'Ричард Линклейтер', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('226', 'Да прольётся свет', '2021', 'TJ Gnanavel', 'драма', '8', 'Индия ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('227', 'Изгоняющий дьявола', '1973', 'Уильям Фридкин', 'фильм ужасов', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('228', 'Лучшие годы нашей жизни', '1946', 'Уильям Уайлер', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('229', 'Суперсемейка', '2004', 'Брэд Бёрд', 'приключения', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('230', 'Быть или не быть', '1942', 'Эрнст Любич', 'комедия', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('231', 'Битва за Алжир', '1966', 'Джилло Понтекорво', 'драма', '8', 'Алжир ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('232', 'Гроздья гнева', '1940', 'Джон Форд', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('233', 'Ребекка', '1940', 'Альфред Хичкок', 'мистический фильм', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('234', 'Хатико: Самый верный друг', '2009', 'Лассе Халльстрём', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('235', 'Пираты Карибского моря: Проклятие Чёрной жемчужины', '2003', 'Гор Вербински', 'экшн', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('236', 'Хладнокровный Люк', '1967', 'Стюарт Розенберг', 'детектив', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('237', 'Сука любовь', '2000', 'Алехандро Гонсалес Иньярриту', 'драма', '8', 'Мексика ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('238', 'Ненависть', '1995', 'Матьё Кассовиц', 'драма', '8', 'Фрацния ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('239', 'Мой отец и мой сын', '2005', 'Чаган Ырмак', 'драма', '8', 'Турция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('240', 'Четыреста ударов', '1959', 'Франсуа Трюффо', 'драма', '8', 'Фрацния ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('241', 'Персона', '1966', 'Ингмар Бергман', 'драма', '8', 'Швеция ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('242', 'Это случилось однажды ночью', '1934', 'Фрэнк Капра', 'комедия', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('243', 'Звуки музыки', '1965', 'Роберт Уайз', 'мюзикл', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('244', 'Житие Брайана по Монти Пайтону', '1979', 'Терри Джонс', 'комедия', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('245', 'Служанка', '2016', 'Пак Чхан Ук', 'драма', '8', 'Южная Корея ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('246', 'Дерсу Узала', '1975', 'Акира Куросава', 'драма', '8', 'Япония ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('247', 'Аладдин', '1992', 'Джон Маскер', 'мюзикл', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('248', 'Ганди', '1982', 'Ричард Аттенборо', 'драма', '8', 'Великобритания ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('249', 'Прислуга', '2011', 'Тейт Тейлор', 'драма', '8', 'США ');",
"INSERT INTO topfilm (ranking, name, year, director, genre, rating, country ) VALUES ('250', 'Стальной гигант', '1999', 'Брэд Бёрд', 'фантастика', '8', 'США ');"]
        for sql_command in sql_commands:
            cursor.execute(sql_command)





def fill_oscars(db):
    db.autocommit = True
    with db.cursor() as cursor:
        sql_commands = ["INSERT INTO oscars (year, film ) VALUES ('1929', 'Крылья ');",
"INSERT INTO oscars (year, film ) VALUES ('1930', 'Бродвейская мелодия ');",
"INSERT INTO oscars (year, film ) VALUES ('1931', 'На западном фронте без перемен ');",
"INSERT INTO oscars (year, film ) VALUES ('1932', 'Симаррон ');",
"INSERT INTO oscars (year, film ) VALUES ('1933', 'Гранд-отель ');",
"INSERT INTO oscars (year, film ) VALUES ('1934', 'Кавалькада ');",
"INSERT INTO oscars (year, film ) VALUES ('1935', 'Это случилось однажды ночью ');",
"INSERT INTO oscars (year, film ) VALUES ('1936', 'Мятеж на „Баунти“ ');",
"INSERT INTO oscars (year, film ) VALUES ('1937', 'Великий Зигфелд ');",
"INSERT INTO oscars (year, film ) VALUES ('1938', 'Жизнь Эмиля Золя ');",
"INSERT INTO oscars (year, film ) VALUES ('1939', 'С собой не унесёшь ');",
"INSERT INTO oscars (year, film ) VALUES ('1940', 'Унесённые ветром ');",
"INSERT INTO oscars (year, film ) VALUES ('1941', 'Ребекка ');",
"INSERT INTO oscars (year, film ) VALUES ('1942', 'Как зелена была моя долина ');",
"INSERT INTO oscars (year, film ) VALUES ('1943', 'Миссис Минивер ');",
"INSERT INTO oscars (year, film ) VALUES ('1944', 'Касабланка ');",
"INSERT INTO oscars (year, film ) VALUES ('1945', 'Идти своим путём');",
"INSERT INTO oscars (year, film ) VALUES ('1946', 'Потерянный уикэнд ');",
"INSERT INTO oscars (year, film ) VALUES ('1947', 'Лучшие годы нашей жизни ');",
"INSERT INTO oscars (year, film ) VALUES ('1948', 'Джентльменское соглашение ');",
"INSERT INTO oscars (year, film ) VALUES ('1949', 'Гамлет ');",
"INSERT INTO oscars (year, film ) VALUES ('1950', 'Вся королевская рать ');",
"INSERT INTO oscars (year, film ) VALUES ('1951', 'Всё о Еве ');",
"INSERT INTO oscars (year, film ) VALUES ('1952', 'Американец в Париже ');",
"INSERT INTO oscars (year, film ) VALUES ('1953', 'Величайшее шоу мира ');",
"INSERT INTO oscars (year, film ) VALUES ('1954', 'Отныне и во веки веков ');",
"INSERT INTO oscars (year, film ) VALUES ('1955', 'В порту ');",
"INSERT INTO oscars (year, film ) VALUES ('1956', 'Марти ');",
"INSERT INTO oscars (year, film ) VALUES ('1957', 'Вокруг света за 80 дней ');",
"INSERT INTO oscars (year, film ) VALUES ('1958', 'Мост через реку Квай ');",
"INSERT INTO oscars (year, film ) VALUES ('1959', 'Жижи ');",
"INSERT INTO oscars (year, film ) VALUES ('1960', 'Бен-Гур ');",
"INSERT INTO oscars (year, film ) VALUES ('1961', 'Квартира ');",
"INSERT INTO oscars (year, film ) VALUES ('1962', 'Вестсайдская история ');",
"INSERT INTO oscars (year, film ) VALUES ('1963', 'Лоуренс Аравийский ');",
"INSERT INTO oscars (year, film ) VALUES ('1964', 'Том Джонс ');",
"INSERT INTO oscars (year, film ) VALUES ('1965', 'Моя прекрасная леди ');",
"INSERT INTO oscars (year, film ) VALUES ('1966', 'Звуки музыки ');",
"INSERT INTO oscars (year, film ) VALUES ('1967', 'Человек на все времена ');",
"INSERT INTO oscars (year, film ) VALUES ('1968', 'Душной южной ночью ');",
"INSERT INTO oscars (year, film ) VALUES ('1969', 'Оливер! ');",
"INSERT INTO oscars (year, film ) VALUES ('1970', 'Полуночный ковбой ');",
"INSERT INTO oscars (year, film ) VALUES ('1971', 'Паттон ');",
"INSERT INTO oscars (year, film ) VALUES ('1972', 'Французский связной ');",
"INSERT INTO oscars (year, film ) VALUES ('1973', 'Крёстный отец ');",
"INSERT INTO oscars (year, film ) VALUES ('1974', 'Афера ');",
"INSERT INTO oscars (year, film ) VALUES ('1975', 'Крёстный отец 2 ');",
"INSERT INTO oscars (year, film ) VALUES ('1976', 'Пролетая над гнездом кукушки ');",
"INSERT INTO oscars (year, film ) VALUES ('1977', 'Рокки ');",
"INSERT INTO oscars (year, film ) VALUES ('1978', 'Энни Холл ');",
"INSERT INTO oscars (year, film ) VALUES ('1979', 'Охотник на оленей ');",
"INSERT INTO oscars (year, film ) VALUES ('1980', 'Крамер против Крамера ');",
"INSERT INTO oscars (year, film ) VALUES ('1981', 'Обыкновенные люди ');",
"INSERT INTO oscars (year, film ) VALUES ('1982', 'Огненные колесницы ');",
"INSERT INTO oscars (year, film ) VALUES ('1983', 'Ганди');",
"INSERT INTO oscars (year, film ) VALUES ('1984', 'Язык нежности ');",
"INSERT INTO oscars (year, film ) VALUES ('1985', 'Амадей ');",
"INSERT INTO oscars (year, film ) VALUES ('1986', 'Из Африки ');",
"INSERT INTO oscars (year, film ) VALUES ('1987', 'Взвод ');",
"INSERT INTO oscars (year, film ) VALUES ('1988', 'Последний император ');",
"INSERT INTO oscars (year, film ) VALUES ('1989', 'Человек дождя ');",
"INSERT INTO oscars (year, film ) VALUES ('1990', 'Шофёр мисс Дэйзи ');",
"INSERT INTO oscars (year, film ) VALUES ('1991', 'Танцующий с волками ');",
"INSERT INTO oscars (year, film ) VALUES ('1992', 'Молчание ягнят ');",
"INSERT INTO oscars (year, film ) VALUES ('1993', 'Непрощённый ');",
"INSERT INTO oscars (year, film ) VALUES ('1994', 'Список Шиндлера ');",
"INSERT INTO oscars (year, film ) VALUES ('1995', 'Форрест Гамп ');",
"INSERT INTO oscars (year, film ) VALUES ('1996', 'Храброе сердце ');",
"INSERT INTO oscars (year, film ) VALUES ('1997', 'Английский пациент ');",
"INSERT INTO oscars (year, film ) VALUES ('1998', 'Титаник ');",
"INSERT INTO oscars (year, film ) VALUES ('1999', 'Влюблённый Шекспир ');",
"INSERT INTO oscars (year, film ) VALUES ('2000', 'Красота по-американски ');",
"INSERT INTO oscars (year, film ) VALUES ('2001', 'Гладиатор ');",
"INSERT INTO oscars (year, film ) VALUES ('2002', 'Игры разума ');",
"INSERT INTO oscars (year, film ) VALUES ('2003', 'Чикаго ');",
"INSERT INTO oscars (year, film ) VALUES ('2004', 'Властелин колец: Возвращение короля ');",
"INSERT INTO oscars (year, film ) VALUES ('2005', 'Малышка на миллион ');",
"INSERT INTO oscars (year, film ) VALUES ('2006', 'Столкновение ');",
"INSERT INTO oscars (year, film ) VALUES ('2007', 'Отступники ');",
"INSERT INTO oscars (year, film ) VALUES ('2008', 'Старикам тут не место ');",
"INSERT INTO oscars (year, film ) VALUES ('2009', 'Миллионер из трущоб ');",
"INSERT INTO oscars (year, film ) VALUES ('2010', 'Повелитель бури ');",
"INSERT INTO oscars (year, film ) VALUES ('2011', 'Король говорит! ');",
"INSERT INTO oscars (year, film ) VALUES ('2012', 'Артист ');",
"INSERT INTO oscars (year, film ) VALUES ('2013', 'Операция „Арго“ ');",
"INSERT INTO oscars (year, film ) VALUES ('2014', '12 лет рабства ');",
"INSERT INTO oscars (year, film ) VALUES ('2015', 'Бёрдмэн ');",
"INSERT INTO oscars (year, film ) VALUES ('2016', 'В центре внимания ');",
"INSERT INTO oscars (year, film ) VALUES ('2017', 'Лунный свет ');",
"INSERT INTO oscars (year, film ) VALUES ('2018', 'Форма воды ');",
"INSERT INTO oscars (year, film ) VALUES ('2019', 'Зелёная книга ');",
"INSERT INTO oscars (year, film ) VALUES ('2020', 'Паразиты ');",
"INSERT INTO oscars (year, film ) VALUES ('2021', 'Земля кочевников ');",
"INSERT INTO oscars (year, film ) VALUES ('2022', 'CODA: Ребёнок глухих родителей');"]
        for sql_command in sql_commands:
            cursor.execute(sql_command)

def fill_authors(db):
    db.autocommit = True
    with db.cursor() as cursor:
        sql_commands = ["INSERT INTO authors (id, name, director ) VALUES ('1', 'Побег из Шоушенка', 'Фрэнк Дарабонт ');",
"INSERT INTO authors (id, name, director ) VALUES ('2', 'Крёстный отец', 'Фрэнсис Форд Коппола ');",
"INSERT INTO authors (id, name, director ) VALUES ('3', 'Тёмный рыцарь', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('4', 'Крёстный отец 2', 'Фрэнсис Форд Коппола ');",
"INSERT INTO authors (id, name, director ) VALUES ('5', '12 разгневанных мужчин', 'Сидни Люмет ');",
"INSERT INTO authors (id, name, director ) VALUES ('6', 'Список Шиндлера', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('7', 'Властелин колец: Возвращение короля', 'Питер Джексон ');",
"INSERT INTO authors (id, name, director ) VALUES ('8', 'Криминальное чтиво', 'Квентин Тарантино ');",
"INSERT INTO authors (id, name, director ) VALUES ('9', 'Властелин колец: Братство Кольца', 'Питер Джексон ');",
"INSERT INTO authors (id, name, director ) VALUES ('10', 'Хороший, плохой, злой', 'Серджо Леоне ');",
"INSERT INTO authors (id, name, director ) VALUES ('11', 'Форрест Гамп', 'Роберт Земекис ');",
"INSERT INTO authors (id, name, director ) VALUES ('12', 'Бойцовский клуб', 'Дэвид Финчер ');",
"INSERT INTO authors (id, name, director ) VALUES ('13', 'Начало', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('14', 'Властелин колец: Две крепости', 'Питер Джексон ');",
"INSERT INTO authors (id, name, director ) VALUES ('15', 'Звёздные войны. Эпизод V: Империя наносит ответный удар', 'Ирвин Кершнер ');",
"INSERT INTO authors (id, name, director ) VALUES ('16', 'Матрица', 'Энди и Ларри Вачовски ');",
"INSERT INTO authors (id, name, director ) VALUES ('17', 'Славные парни', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('18', 'Пролетая над гнездом кукушки', 'Милош Форман ');",
"INSERT INTO authors (id, name, director ) VALUES ('19', 'Семь', 'Дэвид Финчер ');",
"INSERT INTO authors (id, name, director ) VALUES ('20', 'Семь самураев', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('21', 'Эта прекрасная жизнь', 'Фрэнк Капра ');",
"INSERT INTO authors (id, name, director ) VALUES ('22', 'Молчание ягнят', 'Джонатан Демми ');",
"INSERT INTO authors (id, name, director ) VALUES ('23', 'Город Бога', 'Фернанду Мейреллиш ');",
"INSERT INTO authors (id, name, director ) VALUES ('24', 'Спасти рядового Райана', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('25', 'Жизнь прекрасна', 'Роберто Бениньи ');",
"INSERT INTO authors (id, name, director ) VALUES ('26', 'Зелёная миля', 'Фрэнк Дарабонт ');",
"INSERT INTO authors (id, name, director ) VALUES ('27', 'Интерстеллар', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('28', 'Звёздные войны. Эпизод IV: Новая надежда', 'Джордж Лукас ');",
"INSERT INTO authors (id, name, director ) VALUES ('29', 'Терминатор 2: Судный день', 'Джеймс Кэмерон ');",
"INSERT INTO authors (id, name, director ) VALUES ('30', 'Назад в будущее', 'Роберт Земекис ');",
"INSERT INTO authors (id, name, director ) VALUES ('31', 'Унесённые призраками', 'Хаяо Миядзаки ');",
"INSERT INTO authors (id, name, director ) VALUES ('32', 'Психо', 'Альфред Хичкок ');",
"INSERT INTO authors (id, name, director ) VALUES ('33', 'Пианист', 'Роман Полански ');",
"INSERT INTO authors (id, name, director ) VALUES ('34', 'Леон', 'Люк Бессон ');",
"INSERT INTO authors (id, name, director ) VALUES ('35', 'Паразиты', 'Пон Чжун Хо ');",
"INSERT INTO authors (id, name, director ) VALUES ('36', 'Король Лев', 'Роджер Аллерс ');",
"INSERT INTO authors (id, name, director ) VALUES ('37', 'Гладиатор', 'Ридли Скотт ');",
"INSERT INTO authors (id, name, director ) VALUES ('38', 'Американская история Икс', 'Тони Кэй ');",
"INSERT INTO authors (id, name, director ) VALUES ('39', 'Отступники', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('40', 'Подозрительные лица', 'Брайан Сингер ');",
"INSERT INTO authors (id, name, director ) VALUES ('41', 'Престиж', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('42', 'Касабланка', 'Майкл Кёртиц ');",
"INSERT INTO authors (id, name, director ) VALUES ('43', 'Одержимость', 'Дамьен Шазель ');",
"INSERT INTO authors (id, name, director ) VALUES ('44', '1+1', 'Оливье Накаш, Эрик Толедано ');",
"INSERT INTO authors (id, name, director ) VALUES ('45', 'Могила светлячков', 'Исао Такахата ');",
"INSERT INTO authors (id, name, director ) VALUES ('46', 'Харакири', 'Масаки Кобаяси ');",
"INSERT INTO authors (id, name, director ) VALUES ('47', 'Новые времена', 'Чарли Чаплин ');",
"INSERT INTO authors (id, name, director ) VALUES ('48', 'Однажды на Диком Западе', 'Серджо Леоне ');",
"INSERT INTO authors (id, name, director ) VALUES ('49', 'Окно во двор', 'Альфред Хичкок ');",
"INSERT INTO authors (id, name, director ) VALUES ('50', 'Чужой', 'Ридли Скотт ');",
"INSERT INTO authors (id, name, director ) VALUES ('51', 'Огни большого города', 'Чарли Чаплин ');",
"INSERT INTO authors (id, name, director ) VALUES ('52', 'Новый кинотеатр «Парадизо»', 'Джузеппе Торнаторе ');",
"INSERT INTO authors (id, name, director ) VALUES ('53', 'Апокалипсис сегодня', 'Фрэнсис Форд Коппола ');",
"INSERT INTO authors (id, name, director ) VALUES ('54', 'Помни', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('55', 'Индиана Джонс: В поисках утраченного ковчега', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('56', 'Джанго освобождённый', 'Квентин Тарантино ');",
"INSERT INTO authors (id, name, director ) VALUES ('57', 'ВАЛЛ-И', 'Эндрю Стэнтон ');",
"INSERT INTO authors (id, name, director ) VALUES ('58', 'Жизнь других', 'Флориан Хенкель фон Доннерсмарк ');",
"INSERT INTO authors (id, name, director ) VALUES ('59', 'Бульвар Сансет', 'Билли Уайлдер ');",
"INSERT INTO authors (id, name, director ) VALUES ('60', 'Тропы славы', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('61', 'Сияние', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('62', 'Великий диктатор', 'Чарли Чаплин ');",
"INSERT INTO authors (id, name, director ) VALUES ('63', 'Мстители: Война бесконечности', 'Братья Руссо ');",
"INSERT INTO authors (id, name, director ) VALUES ('64', 'Свидетель обвинения', 'Билли Уайлдер ');",
"INSERT INTO authors (id, name, director ) VALUES ('65', 'Чужие', 'Джеймс Кэмерон ');",
"INSERT INTO authors (id, name, director ) VALUES ('66', 'Красота по-американски', 'Сэм Мендес ');",
"INSERT INTO authors (id, name, director ) VALUES ('67', 'Человек-паук: Через вселенные', 'Боб Персичетти ');",
"INSERT INTO authors (id, name, director ) VALUES ('68', 'Доктор Стрейнджлав, или Как я перестал бояться и полюбил бомбу', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('69', 'Топ Ган: Мэверик', 'Джозеф Косински ');",
"INSERT INTO authors (id, name, director ) VALUES ('70', 'Тёмный рыцарь: Возрождение легенды', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('71', 'Олдбой', 'Пак Чхан Ук ');",
"INSERT INTO authors (id, name, director ) VALUES ('72', 'Джокер', 'Тодд Филлипс ');",
"INSERT INTO authors (id, name, director ) VALUES ('73', 'Амадей', 'Милош Форман ');",
"INSERT INTO authors (id, name, director ) VALUES ('74', 'Храброе сердце', 'Мел Гибсон ');",
"INSERT INTO authors (id, name, director ) VALUES ('75', 'История игрушек', 'Джон Лассетер ');",
"INSERT INTO authors (id, name, director ) VALUES ('76', 'Тайна Коко', 'Ли Анкрич ');",
"INSERT INTO authors (id, name, director ) VALUES ('77', 'Бесславные ублюдки', 'Квентин Тарантино ');",
"INSERT INTO authors (id, name, director ) VALUES ('78', 'Подводная лодка', 'Вольфганг Петерсен ');",
"INSERT INTO authors (id, name, director ) VALUES ('79', 'Мстители: Финал', 'Братья Руссо ');",
"INSERT INTO authors (id, name, director ) VALUES ('80', 'Принцесса Мононоке', 'Хаяо Миядзаки ');",
"INSERT INTO authors (id, name, director ) VALUES ('81', 'Однажды в Америке', 'Серджио Леоне ');",
"INSERT INTO authors (id, name, director ) VALUES ('82', 'Умница Уилл Хантинг', 'Гас Ван Сент ');",
"INSERT INTO authors (id, name, director ) VALUES ('83', 'Твоё имя', 'Макото Синкай ');",
"INSERT INTO authors (id, name, director ) VALUES ('84', 'Реквием по мечте', 'Даррен Аронофски ');",
"INSERT INTO authors (id, name, director ) VALUES ('85', 'История игрушек: Большой побег', 'Ли Анкрич ');",
"INSERT INTO authors (id, name, director ) VALUES ('86', 'Поющие под дождём', 'Стэнли Донен ');",
"INSERT INTO authors (id, name, director ) VALUES ('87', '3 идиота', 'Раджкумар Хирани ');",
"INSERT INTO authors (id, name, director ) VALUES ('88', 'Рай и ад', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('89', 'Звёздные войны. Эпизод VI: Возвращение джедая', 'Ричард Маркуанд ');",
"INSERT INTO authors (id, name, director ) VALUES ('90', 'Космическая одиссея 2001 года', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('91', 'Вечное сияние чистого разума', 'Мишель Гондри ');",
"INSERT INTO authors (id, name, director ) VALUES ('92', 'Бешеные псы', 'Квентин Тарантино ');",
"INSERT INTO authors (id, name, director ) VALUES ('93', 'Капернаум', 'Надин Лабаки ');",
"INSERT INTO authors (id, name, director ) VALUES ('94', 'Охота', 'Томас Винтерберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('95', 'Лоуренс Аравийский', 'Дэвид Лин ');",
"INSERT INTO authors (id, name, director ) VALUES ('96', 'Гражданин Кейн', 'Орсон Уэллс ');",
"INSERT INTO authors (id, name, director ) VALUES ('97', 'М', 'Фриц Ланг ');",
"INSERT INTO authors (id, name, director ) VALUES ('98', 'К северу через северо-запад', 'Альфред Хичкок ');",
"INSERT INTO authors (id, name, director ) VALUES ('99', 'Иди и смотри', 'Элем Климов ');",
"INSERT INTO authors (id, name, director ) VALUES ('100', 'Головокружение', 'Альфред Хичкок ');",
"INSERT INTO authors (id, name, director ) VALUES ('101', 'Амели', 'Жан-Пьер Жене ');",
"INSERT INTO authors (id, name, director ) VALUES ('102', 'Заводной апельсин', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('103', 'Двойная страховка', 'Билли Уайлдер ');",
"INSERT INTO authors (id, name, director ) VALUES ('104', 'Квартира', 'Билли Уайлдер ');",
"INSERT INTO authors (id, name, director ) VALUES ('105', 'Цельнометаллическая оболочка', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('106', 'Жить', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('107', 'Лицо со шрамом', 'Брайан де Пальма ');",
"INSERT INTO authors (id, name, director ) VALUES ('108', 'Убить пересмешника', 'Роберт Маллиган ');",
"INSERT INTO authors (id, name, director ) VALUES ('109', 'Афера', 'Джордж Рой Хилл ');",
"INSERT INTO authors (id, name, director ) VALUES ('110', 'Гамильтон', 'Томас Кейл ');",
"INSERT INTO authors (id, name, director ) VALUES ('111', 'Схватка', 'Майкл Манн ');",
"INSERT INTO authors (id, name, director ) VALUES ('112', 'Таксист', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('113', 'Вверх', 'Пит Доктер ');",
"INSERT INTO authors (id, name, director ) VALUES ('114', 'Пожары', 'Дени Вильнёв ');",
"INSERT INTO authors (id, name, director ) VALUES ('115', 'Секреты Лос-Анджелеса', 'Кёртис Хэнсон ');",
"INSERT INTO authors (id, name, director ) VALUES ('116', 'Развод Надера и Симин', 'Асгар Фархади ');",
"INSERT INTO authors (id, name, director ) VALUES ('117', 'Метрополис', 'Фриц Ланг ');",
"INSERT INTO authors (id, name, director ) VALUES ('118', 'Крепкий орешек', 'Джон Мактирнан ');",
"INSERT INTO authors (id, name, director ) VALUES ('119', 'Большой куш', 'Гай Ричи ');",
"INSERT INTO authors (id, name, director ) VALUES ('120', 'Похитители велосипедов', 'Витторио де Сика ');",
"INSERT INTO authors (id, name, director ) VALUES ('121', 'Индиана Джонс и последний крестовый поход', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('122', '1917', 'Сэм Мендес ');",
"INSERT INTO authors (id, name, director ) VALUES ('123', 'Звёздочки на земле', 'Аамир Хан ');",
"INSERT INTO authors (id, name, director ) VALUES ('124', 'Бункер', 'Оливер Хиршбигель ');",
"INSERT INTO authors (id, name, director ) VALUES ('125', 'На несколько долларов больше', 'Серджо Леоне ');",
"INSERT INTO authors (id, name, director ) VALUES ('126', 'Бэтмен: Начало', 'Кристофер Нолан ');",
"INSERT INTO authors (id, name, director ) VALUES ('127', 'Дангал', 'Нитеш Тивари ');",
"INSERT INTO authors (id, name, director ) VALUES ('128', 'Малыш', 'Чарли Чаплин ');",
"INSERT INTO authors (id, name, director ) VALUES ('129', 'В джазе только девушки', 'Билли Уайлдер ');",
"INSERT INTO authors (id, name, director ) VALUES ('130', 'Всё о Еве', 'Джозеф Лео Манкевич ');",
"INSERT INTO authors (id, name, director ) VALUES ('131', 'Отец', 'Флориан Зеллер ');",
"INSERT INTO authors (id, name, director ) VALUES ('132', 'Зелёная книга', 'Питер Фаррелли ');",
"INSERT INTO authors (id, name, director ) VALUES ('133', 'Волк с Уолл-стрит', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('134', 'Нюрнбергский процесс', 'Стэнли Крамер ');",
"INSERT INTO authors (id, name, director ) VALUES ('135', 'Ран', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('136', 'Казино', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('137', 'Непрощённый', 'Клинт Иствуд ');",
"INSERT INTO authors (id, name, director ) VALUES ('138', 'Лабиринт фавна', 'Гильермо дель Торо ');",
"INSERT INTO authors (id, name, director ) VALUES ('139', 'Человек-паук: Нет пути домой', 'Джон Уоттс ');",
"INSERT INTO authors (id, name, director ) VALUES ('140', 'Нефть', 'Пол Томас Андерсон ');",
"INSERT INTO authors (id, name, director ) VALUES ('141', 'Шоу Трумана', 'Питер Уир ');",
"INSERT INTO authors (id, name, director ) VALUES ('142', 'Шестое чувство', 'М. Найт Шьямалан ');",
"INSERT INTO authors (id, name, director ) VALUES ('143', 'Игры разума', 'Рон Ховард ');",
"INSERT INTO authors (id, name, director ) VALUES ('144', 'Монти Пайтон и Священный Грааль', 'Терри Гиллиам ');",
"INSERT INTO authors (id, name, director ) VALUES ('145', 'Телохранитель', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('146', 'Сокровища Сьерра-Мадре', 'Джон Хьюстон ');",
"INSERT INTO authors (id, name, director ) VALUES ('147', 'Остров проклятых', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('148', 'Парк юрского периода', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('149', 'Расёмон', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('150', 'Большой побег', 'Джон Стёрджес ');",
"INSERT INTO authors (id, name, director ) VALUES ('151', 'Убить Билла. Фильм 1', 'Квентин Тарантино ');",
"INSERT INTO authors (id, name, director ) VALUES ('152', 'Старикам тут не место', 'Братья Коэн ');",
"INSERT INTO authors (id, name, director ) VALUES ('153', 'В поисках Немо', 'Эндрю Стэнтон ');",
"INSERT INTO authors (id, name, director ) VALUES ('154', 'Человек-слон', 'Дэвид Линч ');",
"INSERT INTO authors (id, name, director ) VALUES ('155', 'Китайский квартал', 'Роман Полански ');",
"INSERT INTO authors (id, name, director ) VALUES ('156', 'Бешеный бык', 'Мартин Скорсезе ');",
"INSERT INTO authors (id, name, director ) VALUES ('157', 'Нечто', 'Джон Карпентер ');",
"INSERT INTO authors (id, name, director ) VALUES ('158', 'Унесённые ветром', 'Виктор Флеминг ');",
"INSERT INTO authors (id, name, director ) VALUES ('159', 'V — значит вендетта', 'Джеймс Мактиг ');",
"INSERT INTO authors (id, name, director ) VALUES ('160', 'Головоломка', 'Пит Доктер ');",
"INSERT INTO authors (id, name, director ) VALUES ('161', 'Карты, деньги, два ствола', 'Гай Ричи ');",
"INSERT INTO authors (id, name, director ) VALUES ('162', 'В случае убийства набирайте «М»', 'Альфред Хичкок ');",
"INSERT INTO authors (id, name, director ) VALUES ('163', 'Тайна в его глазах', 'Хуан Хосе Кампанелья ');",
"INSERT INTO authors (id, name, director ) VALUES ('164', 'Ходячий замок', 'Хаяо Миядзаки ');",
"INSERT INTO authors (id, name, director ) VALUES ('165', 'Мост через реку Квай', 'Дэвид Лин ');",
"INSERT INTO authors (id, name, director ) VALUES ('166', 'Три билборда на границе Эббинга, Миссури', 'Мартин Макдонах ');",
"INSERT INTO authors (id, name, director ) VALUES ('167', 'На игле', 'Дэнни Бойл ');",
"INSERT INTO authors (id, name, director ) VALUES ('168', 'Воин', 'Гэвин О’Коннор ');",
"INSERT INTO authors (id, name, director ) VALUES ('169', 'Гран Торино', 'Клинт Иствуд ');",
"INSERT INTO authors (id, name, director ) VALUES ('170', 'Фарго', 'Братья Коэн ');",
"INSERT INTO authors (id, name, director ) VALUES ('171', 'Пленницы', 'Дени Вильнёв ');",
"INSERT INTO authors (id, name, director ) VALUES ('172', 'Мой сосед Тоторо', 'Хаяо Миядзаки ');",
"INSERT INTO authors (id, name, director ) VALUES ('173', 'Малышка на миллион', 'Клинт Иствуд ');",
"INSERT INTO authors (id, name, director ) VALUES ('174', 'Поймай меня, если сможешь', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('175', 'Золотая лихорадка', 'Чарли Чаплин ');",
"INSERT INTO authors (id, name, director ) VALUES ('176', 'Бегущий по лезвию', 'Ридли Скотт ');",
"INSERT INTO authors (id, name, director ) VALUES ('177', 'Дети небес', 'Маджид Маджиди ');",
"INSERT INTO authors (id, name, director ) VALUES ('178', 'В порту', 'Элиа Казан ');",
"INSERT INTO authors (id, name, director ) VALUES ('179', 'Третий человек', 'Кэрол Рид ');",
"INSERT INTO authors (id, name, director ) VALUES ('180', 'Перед рассветом', 'Ричард Линклейтер ');",
"INSERT INTO authors (id, name, director ) VALUES ('181', '12 лет рабства', 'Стив Маккуин ');",
"INSERT INTO authors (id, name, director ) VALUES ('182', 'Бен-Гур', 'Уильям Уайлер ');",
"INSERT INTO authors (id, name, director ) VALUES ('183', 'Земляничная поляна', 'Ингмар Бергман ');",
"INSERT INTO authors (id, name, director ) VALUES ('184', 'Гарри Поттер и Дары Смерти. Часть 2', 'Дэвид Йейтс ');",
"INSERT INTO authors (id, name, director ) VALUES ('185', 'Исчезнувшая', 'Дэвид Финчер ');",
"INSERT INTO authors (id, name, director ) VALUES ('186', 'Генерал', 'Клайд Брукман ');",
"INSERT INTO authors (id, name, director ) VALUES ('187', 'Охотник на оленей', 'Майкл Чимино ');",
"INSERT INTO authors (id, name, director ) VALUES ('188', 'Во имя отца', 'Джим Шеридан ');",
"INSERT INTO authors (id, name, director ) VALUES ('189', 'Отель «Гранд Будапешт»', 'Уэс Андерсон ');",
"INSERT INTO authors (id, name, director ) VALUES ('190', 'Барри Линдон', 'Стэнли Кубрик ');",
"INSERT INTO authors (id, name, director ) VALUES ('191', 'Плата за страх', 'Анри-Жорж Клузо ');",
"INSERT INTO authors (id, name, director ) VALUES ('192', 'Мистер Смит едет в Вашингтон', 'Фрэнк Капра ');",
"INSERT INTO authors (id, name, director ) VALUES ('193', 'По соображениям совести', 'Мел Гибсон ');",
"INSERT INTO authors (id, name, director ) VALUES ('194', 'Шерлок-младший', 'Бастер Китон ');",
"INSERT INTO authors (id, name, director ) VALUES ('195', 'Воспоминания об убийстве', 'Пон Чжун Хо ');",
"INSERT INTO authors (id, name, director ) VALUES ('196', 'Клаус', 'Серхио Паблос ');",
"INSERT INTO authors (id, name, director ) VALUES ('197', 'Дикие истории', 'Дамиан Шифрон ');",
"INSERT INTO authors (id, name, director ) VALUES ('198', 'Седьмая печать', 'Ингмар Бергман ');",
"INSERT INTO authors (id, name, director ) VALUES ('199', 'Комната', 'Ленни Абрахамсон ');",
"INSERT INTO authors (id, name, director ) VALUES ('200', 'Безумный Макс: Дорога ярости', 'Джордж Миллер ');",
"INSERT INTO authors (id, name, director ) VALUES ('201', 'Как приручить дракона', 'Крис Сандерс ');",
"INSERT INTO authors (id, name, director ) VALUES ('202', 'Мэри и Макс', 'Адам Эллиот ');",
"INSERT INTO authors (id, name, director ) VALUES ('203', 'Большой Лебовски', 'Братья Коэн ');",
"INSERT INTO authors (id, name, director ) VALUES ('204', 'Челюсти (фильм)', 'Стивен Спилберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('205', 'Корпорация монстров', 'Пит Доктер, Дэвид Силверман ');",
"INSERT INTO authors (id, name, director ) VALUES ('206', 'Токийская повесть', 'Ясудзиро Одзу ');",
"INSERT INTO authors (id, name, director ) VALUES ('207', 'Всё везде и сразу', 'Дэн Кван ');",
"INSERT INTO authors (id, name, director ) VALUES ('208', 'Общество мёртвых поэтов', 'Питер Уир ');",
"INSERT INTO authors (id, name, director ) VALUES ('209', 'Страсти Жанны д’Арк', 'Карл Теодор Дрейер ');",
"INSERT INTO authors (id, name, director ) VALUES ('210', 'Отель Руанда', 'Терри Джордж ');",
"INSERT INTO authors (id, name, director ) VALUES ('211', 'Ford против Ferrari', 'Джеймс Мэнголд ');",
"INSERT INTO authors (id, name, director ) VALUES ('212', 'Рокки', 'Джон Эвилдсен ');",
"INSERT INTO authors (id, name, director ) VALUES ('213', 'Взвод', 'Оливер Стоун ');",
"INSERT INTO authors (id, name, director ) VALUES ('214', 'Песнь дороги', 'Сатьяджит Рай ');",
"INSERT INTO authors (id, name, director ) VALUES ('215', 'Терминатор', 'Джеймс Кэмерон ');",
"INSERT INTO authors (id, name, director ) VALUES ('216', 'Останься со мной', 'Роб Райнер ');",
"INSERT INTO authors (id, name, director ) VALUES ('217', 'В центре внимания', 'Томас Маккарти ');",
"INSERT INTO authors (id, name, director ) VALUES ('218', 'Гонка', 'Рон Ховард ');",
"INSERT INTO authors (id, name, director ) VALUES ('219', 'Логан', 'Джеймс Мэнголд ');",
"INSERT INTO authors (id, name, director ) VALUES ('220', 'Рататуй ', 'Брэд Бёрд ');",
"INSERT INTO authors (id, name, director ) VALUES ('221', 'Телесеть', 'Сидни Люмет ');",
"INSERT INTO authors (id, name, director ) VALUES ('222', 'В диких условиях', 'Шон Пенн ');",
"INSERT INTO authors (id, name, director ) VALUES ('223', 'Волшебник страны Оз ', 'Виктор Флеминг ');",
"INSERT INTO authors (id, name, director ) VALUES ('224', 'День сурка', 'Гарольд Рамис ');",
"INSERT INTO authors (id, name, director ) VALUES ('225', 'Перед закатом', 'Ричард Линклейтер ');",
"INSERT INTO authors (id, name, director ) VALUES ('226', 'Да прольётся свет', 'TJ Gnanavel ');",
"INSERT INTO authors (id, name, director ) VALUES ('227', 'Изгоняющий дьявола', 'Уильям Фридкин ');",
"INSERT INTO authors (id, name, director ) VALUES ('228', 'Лучшие годы нашей жизни', 'Уильям Уайлер ');",
"INSERT INTO authors (id, name, director ) VALUES ('229', 'Суперсемейка', 'Брэд Бёрд ');",
"INSERT INTO authors (id, name, director ) VALUES ('230', 'Быть или не быть', 'Эрнст Любич ');",
"INSERT INTO authors (id, name, director ) VALUES ('231', 'Битва за Алжир', 'Джилло Понтекорво ');",
"INSERT INTO authors (id, name, director ) VALUES ('232', 'Гроздья гнева', 'Джон Форд ');",
"INSERT INTO authors (id, name, director ) VALUES ('233', 'Ребекка', 'Альфред Хичкок ');",
"INSERT INTO authors (id, name, director ) VALUES ('234', 'Хатико: Самый верный друг', 'Лассе Халльстрём ');",
"INSERT INTO authors (id, name, director ) VALUES ('235', 'Пираты Карибского моря: Проклятие Чёрной жемчужины', 'Гор Вербински ');",
"INSERT INTO authors (id, name, director ) VALUES ('236', 'Хладнокровный Люк', 'Стюарт Розенберг ');",
"INSERT INTO authors (id, name, director ) VALUES ('237', 'Сука любовь', 'Алехандро Гонсалес Иньярриту ');",
"INSERT INTO authors (id, name, director ) VALUES ('238', 'Ненависть', 'Матьё Кассовиц ');",
"INSERT INTO authors (id, name, director ) VALUES ('239', 'Мой отец и мой сын', 'Чаган Ырмак ');",
"INSERT INTO authors (id, name, director ) VALUES ('240', 'Четыреста ударов', 'Франсуа Трюффо ');",
"INSERT INTO authors (id, name, director ) VALUES ('241', 'Персона', 'Ингмар Бергман ');",
"INSERT INTO authors (id, name, director ) VALUES ('242', 'Это случилось однажды ночью', 'Фрэнк Капра ');",
"INSERT INTO authors (id, name, director ) VALUES ('243', 'Звуки музыки', 'Роберт Уайз ');",
"INSERT INTO authors (id, name, director ) VALUES ('244', 'Житие Брайана по Монти Пайтону', 'Терри Джонс ');",
"INSERT INTO authors (id, name, director ) VALUES ('245', 'Служанка', 'Пак Чхан Ук ');",
"INSERT INTO authors (id, name, director ) VALUES ('246', 'Дерсу Узала', 'Акира Куросава ');",
"INSERT INTO authors (id, name, director ) VALUES ('247', 'Аладдин', 'Джон Маскер ');",
"INSERT INTO authors (id, name, director ) VALUES ('248', 'Ганди', 'Ричард Аттенборо ');",
"INSERT INTO authors (id, name, director ) VALUES ('249', 'Прислуга', 'Тейт Тейлор ');",
"INSERT INTO authors (id, name, director ) VALUES ('250', 'Стальной гигант', 'Брэд Бёрд ');"]
        for sql_command in sql_commands:
            cursor.execute(sql_command)








create_topfilm(db)
fill_topfilm(db)
fill_oscars(db)
fill_authors(db)

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
            print(result[0])


    except:
        print('0')
    finally:
        if (db):
            cursor.close()
            db.close()


#Узнаем, какие страны, кроме США, есть в списке
execute(["SELECT (COUNT(DISTINCT country) - 1) FROM topfilm"])
execute(["SELECT DISTINCT country FROM topfilm GROUP BY country HAVING country != 'США '"])


"""19
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
Фрацния 
СССР 
Мексика 
Италия 
Германия""" 



#Оскароносные фильмы, находящиеся в топе-250 по сей день 

execute(["SELECT film FROM oscars INTERSECT SELECT name FROM topfilm"])
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
