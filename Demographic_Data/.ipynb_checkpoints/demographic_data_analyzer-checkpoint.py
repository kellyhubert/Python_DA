import pandas as pd

def demographic_data_analyzer():
    # read the data
     df = pd.read_csv('adult.data.csv', header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ])
     
     #1.race count

     race_count = df['race'].value_counts()

     #average_age_men
     average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)
     #3 percentage with a Bachelor's degree
     percentage_bachelors= round((df['education'].value_counts()['Bachelors']/len(df))*100,1)
     #4 percentage with advanced education making >50k
     advanced_education = df['education'].isin(['Bachelors','Masters','Doctorate'])
     higher_education_rich = round(
          (df[advanced_education & (df['salaru']=='>50k')].shape[0]/
           df[advanced_education].shape[0]) * 100,1)
    # 5percantage without advanced education>50k 
     lower_education = ~advanced_education
     lower_education_rich = round(
          (df[lower_education & (df['salary']== '>50k')].shape[0]/
           df[lower_education].shape[0]) * 100,1)
#
      