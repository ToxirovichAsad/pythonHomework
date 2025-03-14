import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Scraping job data
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

jobs = []
for job in soup.find_all('div', class_='card-content'):
    title = job.find('h2', class_='title').text.strip()
    company = job.find('h3', class_='company').text.strip()
    location = job.find('p', class_='location').text.strip()
    links = job.find_all('a', class_='card-footer-item')

    apply_link = links[0]['href']
    learn_link = links[1]['href']

    jobs.append((title, company, location, apply_link, learn_link))

# Storing into SQLite database
with sqlite3.connect('jobs.db') as conn:
    cursor = conn.cursor()

    # Create table without description
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            title TEXT,
            company TEXT,
            location TEXT,
            apply_link TEXT,
            learn_link TEXT,
            PRIMARY KEY (title, company, location)
        )
    """)

    # Insert or update jobs if changed (Fixed: Removed description)
    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, apply_link, learn_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, company, location) 
            DO UPDATE SET 
                apply_link = excluded.apply_link,
                learn_link = excluded.learn_link
        """, job)

    conn.commit()


# Function to filter jobs
def filter_jobs(column, value):
    with sqlite3.connect('jobs.db') as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM jobs WHERE {column} = ?"
        cursor.execute(query, (value,))
        results = cursor.fetchall()
    
    return results


# Function to export jobs to CSV
def export_jobs_to_csv(column, value, filename="filtered_jobs.csv"):
    jobs = filter_jobs(column, value)
    
    if jobs:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Location", "Apply Link", "Learn Link"])  
            writer.writerows(jobs)
        
        print(f"Filtered jobs saved to {filename}")
    else:
        print("No jobs found for the given filter.")
