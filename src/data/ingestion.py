import pandas as pd
import sweetviz as sv
import os


df = pd.read_excel("C:\\Users\\nikhil.puri\\OneDrive - Marico Ltd\\Desktop\\customer_churn\\chustomer_churn_test\\data\\external\\capstone_project-telecom_churn.xlsx", sheet_name=0)

my_report = sv.analyze(df)
my_report.show_html(filepath='C:\\Users\\nikhil.puri\\OneDrive - Marico Ltd\\Desktop\\customer_churn\\chustomer_churn_test\\reports\\eda.html')

print('Hello')