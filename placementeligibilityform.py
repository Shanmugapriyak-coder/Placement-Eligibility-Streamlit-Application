import streamlit as st
import pandas as pd
import mysql.connector

#SQL Connection
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database='guvi_projects',
        autocommit = True)
mycursor = mydb.cursor()


def plac_eli_form():
    st.title("Placement Eligibility")
    # Create the form
    form = st.form(key='registration_form')
    # Input fields
    language = form.selectbox(
    "Choose Language",
    ('--None--','Python','SQL')
    )
    problem_solved = form.number_input("Problem solved ", min_value=0, max_value=1000, step=1)
    mini_Project = form.number_input("Mini Project ", min_value=0, max_value=10, step=1)
    avg_softskill = form.number_input("Average Soft Skills score", min_value=0, max_value=100, step=1)
    intership_comp= form.number_input("Intership completed", min_value=0, max_value=10, step=1)
    
    # Form submit button
    submit_button = form.form_submit_button(label='Generate List')
    
    if submit_button:
            # Create a dictionary with the form data
            # form_data = {
            #     'language': language,
            #     'problem_solved': problem_solved,
            #     'mini_Project': mini_Project,
            #     'avg_softskill': avg_softskill,
            #     'intership_comp': intership_comp
            # }
            
            # Convert the dictionary to a DataFrame
            # df = pd.DataFrame([form_data])
            
            # Display a success message
            # st.success("Registration Successful!")
            
            # Display the form data as a table
            # st.write("Here are your details:")
           # st.write(df)
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
            st.dataframe(
                df,
                 column_config={
                   1: "student_id",
                   2: "name",
                   3:"age",
                   4:"gender",
                   5:"email",
                   6:"phone",
                   7:"enrollment year",
                   8:"course batch",
                   9:"city",
                   10:'graduation year'
                 },
                 hide_index=True,
            )
            #st.dataframe(df)

page_names_to_funcs = {
    "Placement Eligibility Form":plac_eli_form
    #"insight": insight_form 
    # "Mapping Demo": mapping_demo,
    # "DataFrame Demo": data_frame_demo
}
demo_name = st.sidebar.selectbox("Choose a service", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
