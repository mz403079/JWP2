from sqlalchemy import create_engine, Column, Integer, Float, String, text, inspect, select, MetaData, Table, func
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)

#1.1
query = select(census.c.state).distinct()
output = connection.execute(query)
results = output.fetchall()
print(results)

#1.2 Alaska 2000
query = select(
    func.sum(census.c.pop2000)
).where(census.c.state == 'Alaska')
results = connection.execute(query).fetchall()
print(results)

#1.2 Alaska 2008
query = select(
    func.sum(census.c.pop2008)
).where(census.c.state == 'Alaska')
results = connection.execute(query).fetchall()
print(results)

#1.2 New York 2000
query = select(
    func.sum(census.c.pop2000)
).where(census.c.state == 'New York')
results = connection.execute(query).fetchall()
print(results)

#1.2 New York 2008
query = select(
    func.sum(census.c.pop2008)
).where(census.c.state == 'New York')
populationNY2008 = connection.execute(query).fetchall()
print('Populacja Nowy York 2008:',populationNY2008[0][0])

#1.2 New York kobiety 2008
query = select(
    func.sum(census.c.pop2008)
).where(census.c.state == 'New York').where(census.c.sex =='F')
femaleNY2008 = connection.execute(query).fetchall()
print('Kobiety York 2008:',femaleNY2008[0][0])

#1.2 New York mezczyzni 2008
query = select(
    func.sum(census.c.pop2008)
).where(census.c.state == 'New York').where(census.c.sex =='M')
maleNY2008 = connection.execute(query).fetchall()
print('Mezczyzni Nowy York 2008:',maleNY2008[0][0])
sum = maleNY2008[0][0] + femaleNY2008[0][0]
print('Suma:',sum)
print(sum == populationNY2008[0][0])


#2
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students '
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)

# Tworzenie wszystkich tabel
Base.metadata.create_all(engine)

# Utworzenie sesji
with Session(engine) as session:
    new_student = Student(name="Kamil Kowalski", age=30,grade=4.5)
    session.add(new_student)
    session.commit()

# oeczyt danych z sesji
with Session(engine) as session:
    students = session.query(Student).all()
    for student in students:
        print(f'{student.name}, {student.age}, {student.grade}')

# aktualizacja istniejącego rekordu
with Session(engine) as session:
    student_to_update = session.get(Student, 1) # Zalóżmy, że rekord z ID 1 istnieje
    if student_to_update:
        student_to_update.name = "Jan Nowak"
        session.commit()

# Usuwanie rekordy z bazy
with Session(engine) as session:
    student_to_delete = session.get(Student, 1)
    if student_to_delete:
        session.delete(student_to_delete)
        session.commit()