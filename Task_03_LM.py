email_address = str(input("Enter your email address:  "))

at_index = email_address.find("@")
if at_index != -1:
    user_name = email_address[0:at_index]
    print("username is", user_name)
else:
    print("invalid email address")
