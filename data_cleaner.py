# This application will take user input, clean it and save it

def main():
    print("Data Cleaner Lite")

    #NAME
    full_name = input("What is your full name?")
   
    cleaned_name = full_name.strip().lower()
    
    name_parts = cleaned_name.split()
    
    capitalized_parts = []

    for part in name_parts:
        capitalized_parts.append(part.title())
    
    cleaned_name = " ".join(capitalized_parts)

    # EMAIL
    email = input("Enter your email: ")

    cleaned_email = email.strip().lower()

    if cleaned_email.count("@") != 1:
        print("Invalid email")
    else: 
        email_parts = cleaned_email.split("@")
        domain_part = email_parts[1]

        if "." not in domain_part:
            print("Invalid email")
        else:
            print("Email format accepted")
   
    # PHONE NUMBER
    phone_number = input("What is your phone number?")
    
    cleaned_phone = ""
    
    for char in phone_number:
        if char.isdigit():
            cleaned_phone += char

    print()
    print("CLEANED DATA:")
    print("Name:", cleaned_name)
    print("Email:", cleaned_email)
    print("Phone:", cleaned_phone)

if __name__ == "__main__":
    main()
