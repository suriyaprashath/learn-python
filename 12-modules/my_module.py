# my_module.py - Custom module demonstrating code organization
# This shows how to organize related functions into modules

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def calculate_average(scores):
    """Calculate average of a list of numbers"""
    if not scores:  # Handle empty list
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """Convert numeric average to letter grade"""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b

def process_student_data(students_dict):
    """Process a dictionary of student data"""
    results = {}
    for student_name, scores in students_dict.items():
        avg = calculate_average(scores)
        grade = get_letter_grade(avg)
        results[student_name] = {
            'average': avg,
            'letter_grade': grade,
            'scores': scores
        }
    return results

# Module-level variables (constants)
DEFAULT_PASSING_GRADE = 60
MODULE_VERSION = "1.0.0"
