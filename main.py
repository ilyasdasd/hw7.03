from datetime import datetime


from application.salary import calculate_salary
from application.db.people import get_employees

current_datetime = datetime.now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(current_datetime)