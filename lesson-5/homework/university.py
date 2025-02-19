universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions


def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)  
    n = len(sorted_numbers)
    middle = n // 2  
    if n % 2 == 1:  
        return sorted_numbers[middle]  
    else:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle])


enrollments, tuitions = enrollment_stats(universities)

print("******************************")
print(f"Total students: {sum(enrollments):,}")  
print(f"Total tuition: $ {sum(tuitions):,}")
print("\n")
print(f"Student mean: {mean(enrollments):,.2f}")
print(f"Student median: {median(enrollments):,.0f}")
print("\n")
print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,.0f}")
print("******************************")
