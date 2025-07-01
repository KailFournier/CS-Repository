import re #imports regular expressions


def check_phone(phone): #Checks phone input to see if it is a valid phone number
    pattern = r'^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$' #indicates the RE pattern to be matched
    return bool(re.match(pattern, phone))


def check_ssn(ssn): #checks if provided SSN is a valid SSN
    pattern = r'^\d{3}-\d{2}-\d{4}$' #indicates the RE pattern to be matched
    return bool(re.match(pattern, ssn))


def check_zip(zip_code): #CHecks if provided ZIP code is valid
    pattern = r'^\d{5}(-\d{4})?$' #indicates the RE pattern to be matched
    return bool(re.match(pattern, zip_code))


def main():
    retry = 'yes'
    while retry == 'yes': #loops the function to test more options of the user wishes
        phone = input("Enter a phone number: ").strip() #input phone number
        ssn = input("Enter a social security number: ").strip() #input SSN
        zip_code = input("Enter a zip code: ").strip() #input ZIP code
        #prints the results of the regular expression processing
        print(f"The phone number you entered is {'valid' if check_phone(phone) else 'invalid'}.")
        print(f"The social security number you entered is {'valid' if check_ssn(ssn) else 'invalid'}.")
        print(f"The zip code you entered is {'valid' if check_zip(zip_code) else 'invalid'}.")
        retry = input("Do you want to process another set? (yes/no) ") #allows the user to indicate if they want to process another data set
main()