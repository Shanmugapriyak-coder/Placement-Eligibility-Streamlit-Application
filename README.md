# Placement-Eligibility-Streamlit-Application
Placement Eligibility Streamlit Application  where users can input eligibility criteria for placement. Based on these criteria, the application shows the dataset of student details of eligible candidates .

# create_dataset.py
The create_dataset.py  contains the two class for creating/dropping the table and insertion of dataset in database.The four function outside the class to create dataset using faker library.
#### -> createdataset 
this class contains the creating tables and droping the table using the OOP concept to create and rop the table .
#### ->insertdatadset
This class used to insert the data using faker python library in the table .

# requirements.txt
This file contains the required library to install.

# insights_query.sql
this file consists of insight queries used in insight form .

# placementeligibilityform.py
This file contains the main code for streamlit application . the first page of application show a sidebar with selectbox ** choose the service ** dropdown contains two option "placement eligibility form" and "insight form "
#### Placement Eligibility Form 
this navigate to a form with five fields for filtering the data according to the input criteria given by the user after submiting the form by clicking "generate list" button to see the results.Result are shown in tabular format and also can be download as csv file .If the selectbox option choosed to be "None" it throws a error to the user to"please fill all the fields".
#### insight form 
this form has one selectbox which has ten option as insights query for students development.
##### 1.overall average softskill score each year.
##### 2.Distribution of soft skill scores .
##### 3.Top performing students in programming .
##### 4.exceptionally high or low average soft skill scores using 1.5 stddev'
##### 5.Average for each soft skill.
##### 6.Top 5 Companies Hiring the Most Students.
##### 7.students ready for placement.
##### 8.Enrollment per year and batch.
##### 9.Impact of internships ,Mock Interview Scores on Placement
##### 10.Top programming students.

