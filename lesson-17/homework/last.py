#chinook
import pandas as pd
import sqlite3

with sqlite3.connect('data/chinook.db') as connection:
    df_customer = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    )
with sqlite3.connect('data/chinook.db') as connection:
    df_invoice = pd.read_sql(
        "SELECT * FROM invoices",
        con=connection
    )

inner_join = pd.merge(df_customer, df_invoice, on='CustomerId', how='inner')
invoice_counts = inner_join.groupby(['CustomerId', 'FirstName', 'LastName']).size().reset_index(name='TotalInvoices')

print(invoice_counts.head(10))

#outer join 

movies_csv = pd.read_csv('data/movie.csv')

first_dataframe = movies_csv[['director_name','color']]
second_dataframe = movies_csv[['director_name','num_critic_for_reviews']]

left_join = pd.merge(first_dataframe, second_dataframe, on='director_name', how='left')
outer_join = pd.merge(first_dataframe, second_dataframe, on='director_name', how='outer')

print("How many rows resulting on left join :", len(left_join))
print("How many rows resultingon outer join :",len(outer_join))

#grouping and aggregating 

titanic = pd.read_excel('data/titanic.xlsx', sheet_name='Sheet1')

print(titanic.columns)

grouped_titanic = titanic.groupby('Pclass').agg(
    Avg_Age=('Age', 'mean'),
    Total_Fare=('Fare', 'sum'),
    Passenger_Count=('PassengerId', 'count')
).reset_index()

print(grouped_titanic)

#second multilevel grouping

grouped_movie = movies_csv.groupby('director_name').agg(
    num_critic_for_reviews = ('num_critic_for_reviews', 'sum'),
    average_duration  = ('duration', 'mean')
).reset_index()
print(grouped_movie)

#nested grouping flights 

flight = pd.read_parquet('data/flights')

flight['ArrDelay'] = pd.to_numeric(flight['ArrDelay'], errors='coerce')
flight['DepDelay'] = pd.to_numeric(flight['DepDelay'], errors='coerce')


group_by_flights = flight.groupby(['Year', 'Month']).agg(
    total_number_of_flights = ('FlightDate', 'count'),
    average_arrival_delay = ('ArrDelay', 'mean'),
    maximum_departure_delay  = ('DepDelay','max')


).reset_index()
print(group_by_flights)


#applying functions

def classify_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

titanic["Age_Group"] = titanic["Age"].apply(classify_age)

print(titanic[["Age", "Age_Group"]].head(10))

#another task

employee_df = pd.read_csv("data/employee.csv")

def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())

employee_df["Normalized_Salary"] = employee_df.groupby("DEPARTMENT")["BASE_SALARY"].transform(min_max_normalize)

print(employee_df[["DEPARTMENT", "BASE_SALARY", "Normalized_Salary"]].head(10))

#movies duration 

def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif duration < 120:
        return 'Medium'
    else:
        return 'Long'

movies_csv["Duration_Category"] = movies_csv["duration"].apply(classify_duration)
print(movies_csv[["movie_title", "duration", "Duration_Category"]].head(10))


#using pipe


def filter_survivors(df):
    """Filter passengers who survived (Survived == 1)."""
    return df[df["Survived"] == 1].copy()  

def fill_missing_age(df):
    """Fill missing Age values with the mean age."""
    df = df.copy()  
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

def create_fare_per_age(df):
    """Create a new column Fare_Per_Age by dividing Fare by Age."""
    df = df.copy()  
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

processed_df = (
    titanic
    .pipe(filter_survivors)
    .pipe(fill_missing_age)
    .pipe(create_fare_per_age)
)

print(processed_df.head())


#pipe with flights 


flight['ArrDelay'] = pd.to_numeric(flight['ArrDelay'], errors='coerce')
flight['DepDelay'] = pd.to_numeric(flight['DepDelay'], errors='coerce')
flight['CRSElapsedTime'] = pd.to_numeric(flight['CRSElapsedTime'], errors='coerce')  



def filter_delayed_flights(df):
    """Filter flights with a departure delay greater than 30 minutes."""
    return df[df["DepDelay"] > 30]

def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["CRSElapsedTime"]
    return df

processed_flights = (
    flight
    .pipe(filter_delayed_flights)
    .pipe(add_delay_per_hour)
)

print(processed_flights.head())
