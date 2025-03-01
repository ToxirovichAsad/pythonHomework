import csv
from collections import defaultdict

def read_grades(filename):
    grades = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    """Calculates the average grade for each subject."""
    subject_totals = defaultdict(list)
    
    for entry in grades:
        subject_totals[entry['Subject']].append(entry['Grade'])
    
    averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
    return averages

def write_averages(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

# Main execution
grades = read_grades('grades.csv')
print(grades)
averages = calculate_average(grades)
write_averages('average_grades.csv', averages)

print("average_grades.csv has been created successfully.")
