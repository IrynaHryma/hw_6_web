from datetime import datetime,date,timedelta
from faker import Faker
from random import randint
import sqlite3
from pprint import pprint


subjects=[
   "Advanced Mathematics",
   "Discrete Mathematics",
   "Linear Algebra",
   "Programming",
   "Mathematical Statistics",
   "Ukrainian Language",
   "English",
   "History of Ukraine"
    
]

groups =["AN 331", "NA332","AF333"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker()
connect = sqlite3.connect("Home_work6")
curs = connect.cursor()


def seed_teachers():
   teachers=[fake.name() for _ in range(NUMBER_TEACHERS)]
   sql = "INSERT INTO teachers(fullname) VALUES(?)"
   curs.executemany(sql,zip(teachers,))

def seed_subjects():
   sql = "INSERT INTO subjects(name,teacher_id) VALUES(?,?)"
   curs.executemany(sql,zip(subjects,iter(randint(1,NUMBER_TEACHERS) for _ in range(len(subjects)))))


def seed_students():
   students=[fake.name() for _ in range(NUMBER_STUDENTS)]
   sql = "INSERT INTO students(fullname,group_id) VALUES(?,?)"
   curs.executemany(sql,zip(students,(randint(1,len(groups)) for _ in range(len(students)))))

def seed_groups():
   sql = "INSERT INTO groups(name) VALUES(?)"
   curs.executemany(sql,zip(groups,))


def seed_grades():
   start_date = datetime.strptime('2022-09-01','%Y-%m-%d')
   end_date = datetime.strptime("2023-06-20", '%Y-%m-%d')
   sql = "INSERT INTO grades(subject_id, student_id,grades,date_of) VALUES(?,?,?,?)"

   
   def get_list_date(start:date,end:date):
      result=[]
      current_date = start
      while current_date<=end:
         if current_date.isoweekday()<6:
            result.append(current_date)

         current_date +=(timedelta(1))
      return result
   list_dates = get_list_date(start_date,end_date)
   grades =[]
   for day in list_dates:
      random_subject= randint(1,len(subjects))
      random_students = [randint(1,NUMBER_STUDENTS) for _ in range(5)]
      for student in random_students:
          grades.append((random_subject,student, randint(1,12),day.date()))
   
   curs.executemany(sql,grades)


if __name__=="__main__":
   try:
      seed_teachers()
      seed_subjects()
      seed_students()
      seed_grades()
      seed_groups()
      connect.commit()
   except sqlite3.Error as error:
      pprint(error)
   
   finally:
      connect.close()