#variables
#user inputs email
email = input("Please remove formatting like enter inputs and tabs. Input your email here: ")
#Functions
def detect(e, flag): #reads the email and detects if any words match the list of red flags
    return [key for key in flag if key.lower() in e.lower()]

def add_score(): #calls the detect funtion and adds the score assigned to each word to the score
    found_keys = detect(email, flags)
    flags_found = sum(flags[key] for key in found_keys)
    return flags_found


#database
 #red flags with assigned score to notate their weight as a likely scam
flags = {'#1': 7,
    '100%': 8,
    'best price': 12,
    'big bucks': 6,
    'free': 8,
    'access': 2,
    'consultation': 5,
    'gift': 14,
    'hosting': 2,
    'info': 2,
    'investment': 6,
    'membership': 1,
    'money': 7,
    'additional income': 17,
    'be your own boss': 17,
    'billion': 6,
    'cash bonus': 10,
    'cents on the dollar': 10,
    'consolidate debt': 20,
    'double your cash': 25,
    'double your income': 25,
    'earn extra cash': 8,
    'earn money': 25,
    'eliminate bad credit': 9,
    'extra cash': 9,
    'extra income': 9,
    'expect to earn': 7,
    'fast cash': 20,
    'financial freedom': 15,
    'limited time offer': 15,
    'guaranteed returns': 30,
    'act now': 6
}

#main
sp_score = add_score()

print("Spam score is: " + str(sp_score) + ".") #prints the result of the spam filter
if sp_score > 40:
    print("Likely malicious scam, please delete ASAP.")
elif sp_score > 20:
    print("Spam likely, place in spam folder.")
elif sp_score > 10:
    print("Spam unlikely, but proceed with caution. Add to inbox.")
else:
    print("Email seems clean. Send to inbox.")





