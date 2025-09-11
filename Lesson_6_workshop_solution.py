# Write a Python program that takes a Qwallity course name and start month as input
# and calculates the end month based on the course duration.

# Course information:
# Title                    Duration
# Manual Testing              3
# Automated Testing           4
# API Testing                 3 
# DB Testing                  1.5


# If the entered course is not available, show an appropriate message and stop the program.

course_info = {"manual_testing": 3, "automated_testing": 4, "API_testing": 3,
               "DB_Testing": 1.5}
course_titles = list(course_info.keys())

course_title = input(f"Input Course Title: {course_titles} ")
if course_title in course_titles:
    start_month = int(input("Input Start Month: "))
    if start_month > 0 and start_month < 13:
        duration = course_info.get(course_title)
        end_date = start_month + duration
        if end_date > 12:
            end_date = end_date - 12
        print(end_date)
    else:
        print("Month number is not valid")
else:
    print("Select course from available list")
