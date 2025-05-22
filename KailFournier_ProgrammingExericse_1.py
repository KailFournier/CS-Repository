
#Asks user how many tickets they want
def ticket_booth():
    ticket_request = int(input("How many tickets would you like to order? "))
    return ticket_request

#the main function of the program. calculates the tickets bought by the customer, and how many bought total
def ticket_sale(ticket_req):
    global total_tickets
    if ticket_req <= 4:
        if total_tickets ++ ticket_req <= 20:
            if ticket_req == 1:
                print("Thank you for your purchase. Here is your ticket.")
                total_tickets += int(ticket_req)
            else:
                print("Thank you for your purchase. Here are your " + str(ticket_req) + " tickets.")
                total_tickets += int(ticket_req)
        else:
            rem_tickets = remaining_tickets()
            print("I'm sorry, but we only have " + str(rem_tickets) + " presale tickets remaining." )

    else:
        print("I'm sorry, but presales are limited to 4 tickets per party.")

#calculates the remaining presale tickets
def remaining_tickets():
    global total_tickets
    r_tickets = 20 - total_tickets
    return r_tickets


# Main program
total_tickets = 0
while total_tickets < 20:  # The standalone line
    ticket_sale (ticket_booth())
    print("Current tickets sold:", total_tickets)
print("Sorry folks, we're all sold out! Hope to see you again tomorrow!")