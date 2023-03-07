from datetime import *

from application.salary import *
from application.db.people import *

current_datetime = datetime.now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(current_datetime)