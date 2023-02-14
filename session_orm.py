# Создание сессии

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models_orm import create_tables, Course, Homework


DSN = 'postgresql://postgres:6814@localhost:5432/ORM_db' 
engine = sqlalchemy.create_engine(DSN)

create_tables(engine) #Создание таблиц

Session = sessionmaker(bind=engine)

session = Session()

course1 = Course(name="Python")  # Заполнение таблиц


session.add(course1)
session.commit()


hw1 = Homework(number=1, description='простая задача', course=course1)  # Заполнение таблиц
hw2 = Homework(number=2, description='сложная задача', course=course1)  # Заполнение таблиц
session.add_all([hw1, hw2])
session.commit()
print(course1)


# for c in session.query(Homework).all():    # Создание запроса
#     print(c)

# for q in session.query(Homework).filter(Homework.number > 1).all():    # Создание запроса с наложением фильтра
#     # print(q)    

query_filter = session.query(Homework).filter(Homework.description.like('%прос%')).all()   # Создание запроса с наложением фильтра  и паттерна
for w in query_filter:
    print(w) 


query_join = session.query(Course).join(Homework).filter(Homework.description.like('%прос%')).all()
for i in query_join:
    print(i)
   
course2 = Course(name="Java")
session.add(course2)
session.commit()

subq = session.query(Homework).filter(Homework.description.like('%слож%')).subquery()   #Создание подзапросов
subq_ = session.query(Course).join(subq, Course.id == subq.c.course_id).all()
for i in subq_:
    print(i)

session.query(Course).filter(Course.name =='Java').update({'name' : 'JavaScript'})    #Обновление таблицы
session.commit()
print('-'*90)
for c in session.query(Course).all():    # Создание запроса
    print(c)

session.query(Course).filter(Course.name =='JavaScript').delete()    #Удаление таблицы
session.commit()

print('-'*90)
for c in session.query(Course).all():    # Создание запроса
    print(c)

session.close()