import pandas as pd
import sqlite3




#task1

#sqlite3

with sqlite3.connect('data/chinook.db') as connection:
    df_employee = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    
    )
print(df_employee.head(10))

#json

df_iris = pd.read_json('data/iris.json')
print(df_iris.shape)
print(df_iris.columns)

#excell

df_titanic = pd.read_excel('data/titanic.xlsx', sheet_name='Sheet1')
print(df_titanic.head(5))

#parquet

df_flights = pd.read_parquet('data/flights')

print(df_flights.info())

#csv

movie_csv = pd.read_csv('data/movie.csv')
print(movie_csv.head(10))

#task2

#iris json 

df_iris = df_iris.rename(columns=lambda x: x.lower())
print(df_iris.columns)

selected_df = df_iris[['sepallength', 'sepalwidth']]
print(selected_df.head(10))

#titanic excel
filtered_df = df_titanic[df_titanic['Age'] > 30]
print(filtered_df)

gender_count = df_titanic['Sex'].value_counts()
print(gender_count)

#movie csv

filtered_movie_csv = movie_csv[movie_csv['duration'] > 120]
print(filtered_movie_csv)

#task3
#iris json
numeric_columns = ['sepallength', 'sepalwidth','petallength','petalwidth']
mean_values = df_iris[numeric_columns].mean()
median_values = df_iris[numeric_columns].median()
std_values = df_iris[numeric_columns].std()
print(mean_values)
print(median_values)    
print(std_values)

#titanic excel
df_titanic_age_mean = df_titanic['Age'].mean()
print("Titanic age mean: ",df_titanic_age_mean)
df_titanic_age_median = df_titanic['Age'].median()
print("Titanic age median: ",df_titanic_age_median)
df_titanic_age_std = df_titanic['Age'].std()
print("Titanic age std: ",df_titanic_age_std)

#movie csv

director_likes = movie_csv.nlargest(1, 'director_facebook_likes')
print(director_likes['director_name'], director_likes['director_facebook_likes'])


longest_movies_top5 = movie_csv.nlargest(5, 'duration')
print(longest_movies_top5['movie_title'], longest_movies_top5['duration'],longest_movies_top5['director_name'])

# parquet


print("Missing values in each column before filling:\n", df_flights.isnull().sum())


df_flights = df_flights.dropna(axis=1, how='all')

numerical_cols = df_flights.select_dtypes(include=["number"]).columns
df_flights[numerical_cols] = df_flights[numerical_cols].fillna(df_flights[numerical_cols].mean())


categorical_cols = df_flights.select_dtypes(include=['object']).columns
df_flights[categorical_cols] = df_flights[categorical_cols].fillna("Unknown")

print("\nMissing values after filling:\n", df_flights.isnull().sum())
#got this from internet

