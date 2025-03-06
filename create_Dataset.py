from faker import Faker
from datetime import datetime
import pandas as pd
import mysql.connector
fake = Faker(locale='en_IN')

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor = connection.cursor()
query ="create database if not exists guvi_projects "
cursor.execute(query)

query = "use guvi_projects"
cursor.execute(query)

def generate_age():
     birth_date = fake.date_of_birth(minimum_age=18, maximum_age=50)  
     today = datetime.today()    
     age = today.year - birth_date.year
     return age

def create_students(num_students):
   
    for i in range(1,num_students+1):
        gender=fake.random_element(elements=('Female','Male','Other'))
        name=fake.first_name_male() if gender =="Male" else fake.first_name_female()
        age=generate_age() #doubt
        email= fake.email()
        phone= fake.phone_number()
        enrollment_year= fake.random_element(elements=(2023,2024,2025))
        course_batch=fake.random_element(elements=('AI','ML','Data Science'))
        city= fake.city()
        graduation_year=enrollment_year  

        d = insertdataset.save_students_table(name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
     

def create_pragramming(num_students):
   
    for i in range(1,num_students+1):
       student_id=i
       language=fake.random_element(elements=('Python','SQL'))
       problems_solved= fake.random_int(min=0,max=1000)
       assessments_completed= fake.random_int(min=0,max=10)
       mini_projects= fake.random_int(min=0,max=5)
       certifications_earned= fake.random_int(min=0,max=10)
       latest_project_score=fake.random_int(min=10,max=100)
         
       d = insertdataset.save_programming_table(student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)

 
def create_softskill(num_students):
    for i in range(1,num_students+1):
         student_id=i
         communication=fake.random_int(min=0,max=100)
         teamwork= fake.random_int(min=0,max=100)
         presentation= fake.random_int(min=0,max=100)
         leadership= fake.random_int(min=0,max=100)
         critical_thinking= fake.random_int(min=0,max=100)
         interpersonal_skills=fake.random_int(min=0,max=100)
         average_softskill=(communication+teamwork+presentation+leadership+critical_thinking+interpersonal_skills)/6
         d = insertdataset.save_softskill_table(student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills,average_softskill)

def create_placement(num_students):
    for i in range(1,num_students+1):
         student_id=i
         mock_interview_score=fake.random_int(min=0,max=100)
         internships_completed= fake.random_int(min=0,max=5)
         placement_status= fake.random_element(elements=('Ready', 'Not Ready', 'Placed'))
         
         if placement_status=='Placed' :
              companyname= fake.company()
              salary=fake.random_int(min=150000,max=850000,step=1000)
              placement_dt=fake.date_between(start_date="-1y", end_date="+1w")
         else:
               companyname= None
               salary=None
               placement_dt=None
              
         interview_rounds_cleared=fake.random_int(min=0,max=5)
         insertdataset.save_placement_table(student_id, mock_interview_score, internships_completed, placement_status, companyname, salary,interview_rounds_cleared, placement_dt)
         

#class  for table createion

class createdataset:
   
    def create_students_table(cls):
        query = """create table if not exists Students(
                                student_id int primary key AUTO_INCREMENT,
                                name varchar(100) not null,
                                age int,
                                gender varchar(50),
                                email varchar(100) ,
                                phone varchar(20),
                                enrollment_year int,
                                course_batch varchar(50),
                                city varchar(100),
                                graduation_year int
                                )
                                """
        cursor.execute(query)
        connection.commit()
    
    def create_Programming_table(cls):
        query = """create table if not exists Programming(
                                programming_id int primary key AUTO_INCREMENT,
                                student_id int ,
                                language varchar(100),
                                problems_solved int,
                                assessments_completed int,
                                mini_projects int,
                                certifications_earned int,
                                latest_project_score int,
                                FOREIGN KEY (student_id) REFERENCES Students(student_id)
                                )
                                """
        cursor.execute(query)
        connection.commit()
    
    def create_Softskills_table(cls):
        query = """create table if not exists Soft_skills(
                                soft_skill_id int primary key AUTO_INCREMENT,
                                student_id int ,
                                communication int,
                                teamwork int,
                                presentation int,
                                leadership int,
                                critical_thinking int,
                                interpersonal_skills int,
                                average_softskill float,
                                FOREIGN KEY (student_id) REFERENCES Students(student_id)
                                )
                                """
        cursor.execute(query)
        connection.commit()

    def create_Placements_table(cls):
        query =  """create table if not exists Placements(
                                placement_id int primary key AUTO_INCREMENT,
                                student_id int ,
                                mock_interview_score int,
                                internships_completed int,
                                placement_status varchar(50),
                                company_name varchar(100),
                                placement_package int(4),
                                interview_rounds_cleared int,
                                placement_date date,
                                FOREIGN KEY (student_id) REFERENCES Students(student_id)
                                )
                                """
        cursor.execute(query)
        connection.commit()
        
    
    def drop_students_table(cls):
        sql = """   
            DROP TABLE IF EXISTS Students;
        """
        cursor.execute(sql)
        connection.commit() 

    def drop_Programming_table(cls):
        sql = """   
            DROP TABLE IF EXISTS Programming;
        """
        cursor.execute(sql)
        connection.commit()

    def drop_Soft_skills_table(cls):
        sql = """   
            DROP TABLE IF EXISTS Soft_skills;
        """
        cursor.execute(sql)
        connection.commit()

    def drop_Placements_table(cls):
        sql = """   
            DROP TABLE IF EXISTS Placements;
        """
        cursor.execute(sql)
        connection.commit()

#class for inserting data

class insertdataset:
   
    def save_students_table(name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year):
        
        query = """
            INSERT INTO Students (name,age,gender, email,phone,enrollment_year,course_batch,city,graduation_year)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query,(name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))
        connection.commit()

    def save_programming_table(student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score):
        
        query =  """
            INSERT INTO Programming (student_id,language,problems_solved, assessments_completed,mini_projects,certifications_earned,latest_project_score)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query,(student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score))
        connection.commit()

        
    def save_softskill_table(student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills,average_softskill):
        
        query = """
            INSERT INTO Soft_skills (student_id,communication,teamwork, presentation,leadership,critical_thinking,interpersonal_skills,average_softskill)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query,(student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills,average_softskill))
        connection.commit()

    def save_placement_table(student_id, mock_interview_score, internships_completed, placement_status, companyname, salary,interview_rounds_cleared, placement_dt):
        
        query = """
            INSERT INTO Placements (student_id,mock_interview_score,internships_completed, placement_status,company_name,placement_package,interview_rounds_cleared,placement_date)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query,(student_id, mock_interview_score, internships_completed, placement_status, companyname, salary,interview_rounds_cleared, placement_dt))
        connection.commit()    

s= createdataset()

# s.create_students_table()
# s.create_Programming_table()
#s.create_Softskills_table()
# s.create_Placements_table()

# s.drop_Programming_table()
#s.drop_Soft_skills_table()
# s.drop_Placements_table()
# s.drop_students_table()

# create_students(500)
# create_pragramming(500) 
#create_softskill(500) 
# create_placement(500)