import streamlit as st
import pandas as pd
import mysql.connector

st.html(
    """
    <style>
    [data-testid="stSidebarContent"] {
        color: black;
        background-color:light-gray;
    }
    </style>
    """
)
#SQL Connection
mydb = mysql.connector.connect(
        host = "localhost",
        user = st.secrets["Username"],
        password = st.secrets["Password"],
        database=st.secrets["Database"],
        autocommit = True)
mycursor = mydb.cursor()

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


def intro():
    
    st.write("# Welcome to Placement eligibility application 👋")
    st.sidebar.error("Select a service above. 🙂 ")

    st.markdown(
        """
        This application is designed to help companies efficiently filter eligible candidates 
        based on their criteria, minimizing manual effort and saving valuable time.
          With an intuitive interface and robust functionality, it ensures accurate and 
          quick selection of potential candidates, making the recruitment process smoother and more effective. 
        Let technology do the work while you focus on selecting the best talent!

        **👈 Select a service from the sidebar**
       
    """
    )



def plac_eli_form():
    st.title("Placement Eligibility 🧐")
    form = st.form(key='registration_form')
    language = form.selectbox(
    "Choose Language",
    ('--None--','Python','SQL')
    )
    problem_solved = form.number_input("Problem solved ", min_value=0, max_value=1000, step=1)
    mini_Project = form.number_input("Mini Project ", min_value=0, max_value=10, step=1)
    avg_softskill = form.number_input("Average Soft Skills score", min_value=0, max_value=100, step=1)
    intership_comp= form.number_input("Intership completed", min_value=0, max_value=10, step=1)

    
    submit_button = form.form_submit_button(label='Generate List')
    
    if submit_button and language!='--None--' :
            select_query = """
                
              select s.* from Students s 
              join Programming p on s.student_id=p.student_id and p.language=%s and p.problems_solved>=%s and p.mini_projects >= %s
              join soft_skills ss on p.student_id = ss.student_id and ss.average_softskill>=%s
              join placements pp on ss.student_id=pp.student_id  and pp.placement_status='Ready' and pp.internships_completed >=%s

             """
            data = (language, problem_solved, mini_Project, avg_softskill, intership_comp)
            mycursor.execute(select_query,data)
            data = mycursor.fetchall()
            df = pd.DataFrame(data)
            column_config=(
                   "student_id",
                   "name",
                   "age",
                   "gender",
                   "email",
                   "phone",
                   "enrollment year",
                   "course batch",
                   "city",
                   'graduation year'
            )
            df = pd.DataFrame(data,columns=column_config)
            st.dataframe(df, 
               hide_index=True,
            )
                  
            #st.dataframe(df)
    else:
         st.error("Please enter fill all the field ")
          

def insight_form():
    st.title("Insight form 📊📉")
    form = st.form(key='insight_form')
    insight = form.selectbox(
    "Choose insight",
    ('--None--',
     'overall average softskill score each year','Distribution of soft skill scores',
     'Top performing students in programming','exceptionally high or low average soft skill scores using 1.5 stddev',
     'Average for each soft skill','Top 5 Companies Hiring the Most Students','students ready for placement',
     'Enrollment per year and batch','Impact of internships,Mock Interview Scores on Placement'
     ,'Top programming students')
    )
  
    submit_button = form.form_submit_button(label='Generate List')
    
    if submit_button:
            if (insight=='Enrollment per year and batch'):
               query = """
                 select count(*) as no_of_student,enrollment_year,course_batch from students group by enrollment_year,course_batch order by enrollment_year
               """
               column_config=(
                   "Number of students",
                   "enrollment year",
                   "course batch",
                )
            elif insight=='students ready for placement':
                  query = """
                 select s.student_id,s.name,s.phone,s.email,s.course_batch,s.graduation_year,ss.communication,
                ss.teamwork,ss.presentation,ss.leadership,ss.critical_thinking,ss.interpersonal_skills,
                ss.average_softskill from students s join placements p on s.student_id=p.student_id and placement_status='Not Ready' 
                join soft_skills ss on ss.student_id=p.student_id and ss.average_softskill>60 
                join programming pp on ss.student_id=pp.student_id and pp.problems_solved>=350 order by ss.average_softskill desc ;
               """
                  column_config=(
                    "student id",
                    "name",
                   "phone",
                   "email",
                   "course_batch",
                   "enrollment year",
                   "Communcication",
                   "team work",
                   "presentation",
                   "leadership",
                   "critical thinking",
                   "interpersonal skills",
                   "average_softskill"
                  )
            elif insight=='overall average softskill score each year':
                 
                query = """
                select count(*),avg(ss.average_softskill),s.course_batch,s.graduation_year from Students s  
                join soft_skills ss on s.student_id=ss.student_id group by s.graduation_year,s.course_batch 
                order by s.graduation_year;
                 """
                column_config=(
                    "Number of students",
                    "overall Average soft skill",
                   "course_batch",
                   "graduation year"
                )
            elif insight=='Distribution of soft skill scores':
                query="""select s.student_id,s.name,s.phone,s.email,s.course_batch,s.graduation_year,ss.communication,
                ss.teamwork,ss.presentation,ss.leadership,ss.critical_thinking,ss.interpersonal_skills,
                ss.average_softskill from Students s  join soft_skills ss on s.student_id=ss.student_id 
                order by s.course_batch,s.graduation_year """
                column_config=(
                    "student id",
                    "name",
                    "phone",
                    "email",
                    "course_batch",
                    "enrollment year",
                    "Communcication",
                    "team work",
                    "presentation",
                    "leadership",
                    "critical thinking",
                    "interpersonal skills",
                    "average_softskill"
                )
            elif insight=='Top performing students in programming' :
                 query=""" 
                 SELECT s.student_id,s.name,s.course_batch,s.phone,s.email, language, problems_solved, assessments_completed, 
                  mini_projects, certifications_earned, latest_project_score,
                 (problems_solved * 0.3 + assessments_completed * 0.2 + 
                  mini_projects * 0.2 + certifications_earned * 0.2 + 
                  latest_project_score * 0.1) AS performance_score
                  FROM programming p inner join students s on p.student_id=s.student_id
                  ORDER BY performance_score DESC
                  LIMIT 10;
                  """
                 column_config=(
                    "student id",
                    "Name", 
                    "Course batch", 
                    "phone", 
                    "email",
                    "language", 
                    "problems solved", 
                    "assessments completed",
                    "mini projects", 
                    "certifications earned", 
                    "latest project score", 
                    "performance score"
                 )
            elif insight=='exceptionally high or low average soft skill scores using 1.5 stddev' :
                 query=""" 
                SELECT s.student_id,s.name,s.course_batch,s.phone,s.email, ss .average_softskill
                FROM soft_skills ss inner join students s on ss.student_id=s.student_id
                WHERE average_softskill > (SELECT AVG(average_softskill) + 1.5 * STDDEV(average_softskill) FROM soft_skills)
                OR average_softskill < (SELECT AVG(average_softskill) - 1.5 * STDDEV(average_softskill) FROM soft_skills)
                ORDER BY average_softskill DESC;
                  """
                 column_config=(
                    "student id",
                    "Name", 
                    "Course batch", 
                    "phone", 
                    "email", 
                    "Average soft skill"
                 )
            elif insight=='Average for each soft skill':
                 query="""
                  SELECT 'Communication' AS skill, AVG(communication) AS avg_score FROM soft_skills
                  UNION ALL
                  SELECT 'Teamwork', AVG(teamwork) FROM soft_skills
                  UNION ALL
                  SELECT 'Presentation', AVG(presentation) FROM soft_skills
                  UNION ALL
                  SELECT 'Leadership', AVG(leadership) FROM soft_skills
                  UNION ALL
                  SELECT 'Critical Thinking', AVG(critical_thinking) FROM soft_skills
                  UNION ALL
                  SELECT 'Interpersonal Skills', AVG(interpersonal_skills) FROM soft_skills
                  ORDER BY avg_score DESC;
                  """
                 column_config=(
                    "skill",
                    "average score"
                 )   
            elif insight=='Top 5 Companies Hiring the Most Students':
                 query="""
                  SELECT company_name, COUNT(*) AS students_placed FROM placements
                  WHERE placement_status = 'Placed'
                  GROUP BY company_name
                  ORDER BY students_placed DESC
                  LIMIT 5;
                  """
                 column_config=(
                    "company name",
                    "No. of student placed"
                 )   

            elif insight=='Impact of internships,Mock Interview Scores on Placement':
                 query=    """SELECT internships_completed, 
                              ROUND(AVG(mock_interview_score), 2) AS avg_mock_score,
                              COUNT(*) AS total_students,
                              SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) AS placed_students,
                              (SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS placement_rate
                              FROM placements
                              GROUP BY internships_completed
                              ORDER BY internships_completed DESC;
                           """   
                 column_config=(
                    "No. of internships completed",
                    "Average mock interview score",
                    "No. of students",
                    "No. of placed students",
                    "Placement rate",
                 ) 
           
            elif insight=='Top programming students':
                 query=    """SELECT s.student_id,s.name,s.course_batch,s.phone,s.email,p. problems_solved
                              FROM programming p inner join students s on s.student_id=p.student_id
                              WHERE problems_solved > (SELECT AVG(problems_solved) + STDDEV(problems_solved) FROM programming)
                              ORDER BY problems_solved DESC;
                           """   
                 column_config=(
                    "student id",
                    "Name", 
                    "Course batch", 
                    "phone", 
                    "email",
                    "problems solved"
                 ) 
            if insight!="--None--" :
                  mycursor.execute(query)
                  data = mycursor.fetchall()
                  df = pd.DataFrame(data,columns=column_config)
                  st.dataframe(df, 
                  hide_index=True,
                  )
                  csv = convert_df(df)
                  st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="data.csv",
                    mime="text/csv",
                    icon=":material/download:"
                  )
            else:
                 st.error("select insight above")
          
            

page_names_to_funcs = {
     "--None--":intro,
    "Placement Eligibility Form":plac_eli_form,
    "Insight": insight_form 
}
demo_name = st.sidebar.selectbox("Choose a service", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
