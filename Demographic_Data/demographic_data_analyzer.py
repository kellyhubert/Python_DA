import pandas as pd
data= {
    "age": [39,50,38,53,28],
    "workclass": ["state-gov","self-em-not-inc","private","private","private"],
    "fnlwgt":[77516,83311,215646,234721,338409],
    "education":["Bachelors","Bachelors","HS-grad","11th","Bachelors"],
    "education-num":[13,13,9,7,13],
    "martial-status":[
        "Never-married",
        "Married-civ-spouse",
        "Divorced",
        "Married-civ-spouse",
        "Married-civ-spoouse",
    ],
    "Occupation":[
    "Adm-clerical",
    "Exec-managerial",
    "Handlers-cleaners",
    "Handlers-Cleaners",
    "Prof-specialty",
    ],
   "relationship":[
       "Not-in-family",
       "Husband",
       "Not-in-family",
       "Husband",
       "wife",
   ],
  "race": ["White","White","White","Black","Black"],
  "sex":["Male", "Male", "Male","Male","Female"],
  "Capital-gain":[2174,0,0,0,0],
  "Capital-loss":[0,0,0,0,0],
  "hours-per-week":[40,13,40,40,40],
  "native-country":[
      "United-states",
      "United-states",
      "united-states",
      "united-states",
      "cuba",
  ],
  "salary":["<=50k","<=50k","<=50k","<=50k","<=50k"],
}
df = pd.DataFrame(data)
#print(df.columns)
race_counts =df["race"].value_counts()
#1 How many peole of eachrace are represented in this dataset
print("Race counts:\n",race_counts)
#what is the average of men
average_age_men=df[df["sex"]=="Male"]["age"].mean()
print("Average age of men:",average_age_men)

#what is the percentage of people who have BAchelors degree
bachelors_percentage= (df["education"]=="Bachelors").mean()*100
print("percentage woth bachelor's ddegree:", bachelors_percentage)

#what is the percentage of people with highy education 
advanced_education =df["education"].isin(["Bachelors", "Masters","Doctorate"])
percentage_advanced_edu_high_salary = ( (df[advanced_education & (df["salary"] == ">50k")].shape[0] / df[advanced_education].shape[0])*100)
print("percentage with advanced education making >50K:",percentage_advanced_edu_high_salary)

#what is the percentage of people without  advanced education make more than 50K
percentage_non_advanced_edu_high_salary = (
    (df[~advanced_education & (df["salary"] ==">50k")].shape[0] / df[~advanced_education].shape[0])*100)

#whatbis number of minimum number of hours a person works per week
min_hours_per_week= df["hours-per-week"].min()
print("Minimum hours worked per week:", min_hours_per_week)

#what is the percentage of people who work the minimum nnumber of hours per week have a salary of more than 50k
min_hours_workers =df[df["hours-per-week"] == min_hours_per_week]
percentage_min_hours_high_salary =(
    min_hours_workers[min_hours_workers["salary"] == ">50k"].shape[0] /min_hours_workers.shape[0]*100)
print("Percentage of those working minimum hours and earning >50k:", percentage_min_hours_high_salary)

# what is the percentage of people working the minimum number of hours that earn >50k and what is tha percentage
country_earning_high= df[df["salary"]==">50k"]["native-country"].value_counts()
country_total = df["native-country"].value_counts()

earning_percentage=(
    country_earning_high.reindex(country_total.index,fill_value=0)/country_total *100)

highest_earning_country =earning_percentage.dropna().idxmax()
highest_earning_country_percentage = earning_percentage.dropna().max()
print("country with the highest percentage of >50K earning:",highest_earning_country)
print("Highest percentage of >50K earners:", highest_earning_country_percentage)

#indetifiying the most popular occupation for those who earn >50k in india
popular_occupation_india = (
    df[(df["salary"] == ">50k") & (df["native_country"] == "India")]["occupation"].value_counts().idmax()
    if not df[(df["salary"] == ">50k") & (df["native-country"] =="India")].empty
    else None)
print("Most popular occupation for >50K earners in India:", popular_occupation_india)