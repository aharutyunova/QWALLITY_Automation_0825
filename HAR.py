from datetime import datetime


birth_date_str = input("Enter your birth date (dd/mm/yyyy): ")

birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")

today = datetime.today()

age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

print(age)