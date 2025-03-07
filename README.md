# Placement-Eligibility-Streamlit-Application
Placement Eligibility Streamlit Application  where users can input eligibility criteria for placement. Based on these criteria, the application shows the dataset of student details of eligible candidates .

# create_dataset.py
This file contains the two class for the database.
#### -> createdataset 
this class contains the creating tables namely and droping the table .
#### ->insertdatadset
This class used to insert the data using faker python library in the table .

# requirements.txt
This file contains the required library to install.

# placementeligibilityform.py
This file contains the main code for streamlit application . the first page of application show a sidebar with selectbox ** choose the service ** dropdown two option "placement eligibility form" and "insight form "
#### Placement Eligibility Form 
this navigate to a form with five fields for filtering the data according to the input criteria given by the user after submiting the form by clicking "generate list" button to see the results.Result are shown in tabular format .
#### insight form 
this form has one selectbox which has ten option as insight query for students development.

