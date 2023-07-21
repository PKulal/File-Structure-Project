import os
import random
import platform

# Constants
BUS_FILE = 'bus.txt'
TICKET_FILE = 'ticket.txt'

#index files
BUS_INDEX_FILE = 'busindex.txt'
TICKET_INDEX_FILE = 'ticketindex.txt'

# Admin login credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

# Function to clear the screen
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Function to display a menu and get user choice
def get_choice(is_admin):
    if is_admin:
        print("\n====================================================================================")
        print("\n**************---------------------- Admin Menu----------------------************** ")
        print("\n====================================================================================")
        print("\n")
        print(" ||                                        1. Add Bus                               ||")
        print(" ||                                        2. Delete Bus                            ||")
        print(" ||                                        3. View Buses                            ||")
        print(" ||                                        4. Edit Bus                              ||")
        print(" ||                                        5. View Booked Tickets                   ||")
        print(" ||                                        6. Book Ticket                           ||")
        print(" ||                                        7. Cancel Ticket                         ||")
        print(" ||                                        8. Logout                                ||")
        print("\n====================================================================================")
        print("\n")
        choice = input("                             Enter your choice: ")
    else:
        print("\n====================================================================================")
        print("\n**************---------------------- User Menu----------------------************** ")
        print("\n====================================================================================")
        print("\n")
        print(" ||                                        1. Book Ticket                           ||")
        print(" ||                                        2. Cancel Ticket                         ||")
        print(" ||                                        3. View Buses                            ||")
        print(" ||                                        4. View Booked Tickets                   ||")
        print(" ||                                        5. Logout                                ||")
        print("\n====================================================================================")
        print("\n")
        choice = input("                             Enter your choice: ")                              
    return choice

# Function to perform admin login
def admin_login():
    print("\n====================================================================================")
    print("\n**************----------------------Admin login----------------------************** ")
    print("\n====================================================================================")
    username = input("                              Enter admin username: ")
    print("\n")
    password = input("                              Enter admin password: ")
    print("\n====================================================================================")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    else:
        print("                             Invalid username or password.")
        return False

# Function to add a new bus
def add_bus():
    print("\n====================================================================================")
    bus_number = input("                                Enter your 4 digit bus number: ")
    if(len(bus_number)!=4):
        print("                             Enter valid 4 digit bus number")                                
        return
    
    bus_name = input("                              Enter bus name: ")
    source = input("                                Enter source: ")
    destination = input("                               Enter destination: ")
    seats = input("                             Enter total number of seats: ")
    fare = input("                              Enter fare: ")
    print("\n====================================================================================")

    with open(BUS_FILE, 'a') as file:
        file.write(f"{bus_number}|{bus_name}|{source}|{destination}|{seats}|{fare}\n")
    print("                             Bus added successfully.")

    update_bus_index()  # Update the bus index file

# Function to delete a bus
def delete_bus():
    print("***************************************************************************************")
    bus_number = input("                                Enter bus number to delete: ")
    print("***************************************************************************************")

    # Update bus.txt file
    with open(BUS_FILE, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.startswith(bus_number):
                file.write('*' + line[1:])
            else:
                file.write(line)
        file.truncate()

    # Update ticket.txt file
    with open(TICKET_FILE, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.split('|')[1] == bus_number:
                file.write('*' + line[1:])
            else:
                file.write(line)
        file.truncate()

    print("                             Bus deleted successfully.")

    
    update_bus_index()  # Update the bus index file
    update_ticket_index()  # Update the ticket index file


#updating index files
def update_bus_index():
     bus_index = []
     with open(BUS_FILE, 'r') as bus_file:
            for i, line in enumerate(bus_file, start=1):
                bus_number = line.split('|')[0]
                bus_index.append((bus_number, i))

     bus_index.sort(key=lambda x: x[0])

     with open(BUS_INDEX_FILE, 'w') as index_file:
            for key, address in bus_index:
                index_file.write(f"{key}|{address}\n")

def update_ticket_index():
    ticket_index = []
    
    with open(TICKET_FILE, 'r') as ticket_file:
        for i, line in enumerate(ticket_file, start=1):
            ticket_id = line.split('|')[0]
            ticket_index.append((ticket_id, i))

    ticket_index.sort(key=lambda x: x[0])

    with open(TICKET_INDEX_FILE, 'w') as index_file:
        for key, address in ticket_index:
            index_file.write(f"{key}|{address}\n")


# Function to view all buses
def view_buses():
    print("\n====================================================================================")
    print("\n**************----------------------Bus lists------------------------************** ")
    print("\n====================================================================================")
    bus_data = []

    with open(BUS_FILE, 'r') as file:
        for line in file:
            if not line.startswith('*'):
                bus_data.append(line.split('|'))

    if len(bus_data) > 0:
        sorted_bus_data = sorted(bus_data, key=lambda x: x[0])
        for data in sorted_bus_data:
            print(f"                                Bus Number: {data[0]}")
            print(f"                                Bus Name: {data[1]}")
            print(f"                                Source: {data[2]}")
            print(f"                                Destination: {data[3]}")
            print(f"                                Total Seats: {data[4]}")
            print(f"                                Fare: {data[5]}")
            print("\n")
            print("\n====================================================================================")
    else:
        print("                             No buses available.")

# Function to edit a bus
def edit_bus():
    bus_number = input("                                Enter bus number to edit: ")
    if(len(bus_number)!=4):
        print("                             Enter valid 4 digit bus number");
        return

    # Check if bus exists
    bus_found = False
    bus_data_lines = []
    with open(BUS_FILE, 'r') as file:
        for line in file:
            if line.startswith(bus_number):
                bus_found = True
                bus_data = line.strip().split('|')
                print("\n====================================================================================")
                print("\n**************---------------------- Bus Details----------------------************** ")
                print("\n====================================================================================")
                print(f"                                Bus Number: {bus_data[0]}")
                print(f"                                Bus Name: {bus_data[1]}")
                print(f"                                Source: {bus_data[2]}")
                print(f"                                Destination: {bus_data[3]}")
                print(f"                                Total Seats: {bus_data[4]}")
                print(f"                                Fare: {bus_data[5]}")
                print("=====================================================================================")
                print("\n**************---------------------- Edit bus----------------------************** ")
                print("=====================================================================================")

                new_bus_name = input("                         Enter new bus name (leave blank to keep current): ")
                new_source = input("                           Enter new source (leave blank to keep current): ")
                new_destination = input("                          Enter new destination (leave blank to keep current): ")
                new_seats = input("                        Enter new total number of seats (leave blank to keep current): ")
                new_fare = input("                         Enter new fare (leave blank to keep current): ")
                print("=====================================================================================")

                bus_data[1] = new_bus_name if new_bus_name else bus_data[1]
                bus_data[2] = new_source if new_source else bus_data[2]
                bus_data[3] = new_destination if new_destination else bus_data[3]
                bus_data[4] = new_seats if new_seats else bus_data[4]
                bus_data[5] = new_fare if new_fare else bus_data[5]

                bus_data_lines.append('|'.join(bus_data) + '\n')
            else:
                bus_data_lines.append(line)

    if not bus_found:
        print("                             Bus not found.")
        return

    with open(BUS_FILE, 'w') as file:
        file.writelines(bus_data_lines)

    print("                             Bus details updated successfully.")

# Function to book a ticket
def book_ticket():
    print("=====================================================================================")
    print("\n**************---------------------- Book Ticket----------------------************** ")
    print("=====================================================================================")
    bus_number = input("                                Enter bus number: ")

    # Check if bus exists
    bus_found = False
    available_seats = 0
    fare = 0
    bus_data_lines = []
    with open(BUS_FILE, 'r') as file:
        for line in file:
            if line.startswith(bus_number):
                bus_found = True
                bus_data = line.strip().split('|')
                available_seats = int(bus_data[4])
                fare = float(bus_data[5])
                if available_seats == 0:
                    print("                             No seats available for this bus.")
                    return
                else:
                    bus_data[4] = str(available_seats - 1)
                bus_data_lines.append('|'.join(bus_data) + '\n')
            else:
                bus_data_lines.append(line)

    if not bus_found:
        print("                             Bus not found.")
        return

    passenger_name = input("                                Enter passenger name: ")
    if not passenger_name:
        print("                             Passenger name is required.")
        return

    contact_number = input("                                Enter contact number: ")
    if not contact_number or len(contact_number) != 10:
        print("                             Invalid contact number. Contact number should be 10 digits.")
        return

    seat_number = input("                               Enter seat number: ")
    print("=====================================================================================")
    if not seat_number:
        print("                             Seat number is required.")
        return

    # Check if seat is available
    if int(seat_number) > available_seats:
        print("                             Seats not available.")
        return
    
    with open(TICKET_FILE, 'r')as file:
        for line in file:
            ticket_data=line.strip().split('|')
            if ticket_data[1]==bus_number and ticket_data[4]==seat_number:
                print("                             Seat is already booked try other......")
                return
    
    with open(BUS_FILE, 'w') as file:
        file.writelines(bus_data_lines)

    with open(TICKET_FILE, 'a') as file:
        # Generate a unique ticket ID
        ticket_id = str(random.randint(1000, 9999))

        file.write(f"{ticket_id}|{bus_number}|{passenger_name}|{contact_number}|{seat_number}|{fare}\n")

    print("                             Ticket booked successfully.")
    print("                             Ticket details are sent to your contact number")
    update_ticket_index()  # Update the ticket index file


# Function to cancel a ticket
def cancel_ticket():
    print("=====================================================================================")
    print("\n**************---------------------- Cancel Ticket----------------------************** ")
    print("=====================================================================================")

    ticket_id = input("                             Enter ticket ID to cancel: ")
    print("=====================================================================================")
    if(len(ticket_id)!=4):
        print("                             Enter valid 4 digit ticket number");
        return

    # Check if ticket exists
    ticket_found = False
    ticket_data_lines = []
    with open(TICKET_FILE, 'r') as file:
        for line in file:
            if line.startswith(ticket_id):
                ticket_found = True
                ticket_data = line.strip().split('|')
                print("\n**************---------------------- Ticket Details----------------------************** ")
                print(f"                                Ticket ID: {ticket_data[0]}")
                print(f"                                Bus Number: {ticket_data[1]}")
                print(f"                                Passenger Name: {ticket_data[2]}")
                print(f"                                Contact Number: {ticket_data[3]}")
                print(f"                                Seat Number: {ticket_data[4]}")
                print(f"                                Fare: {ticket_data[5]}")
                ticket_data_lines.append('*' + line[1:])
            else:
                ticket_data_lines.append(line)

    if not ticket_found:
        print("                             Ticket not found.")
        return

    with open(TICKET_FILE, 'w') as file:
        file.writelines(ticket_data_lines)

    # Update available seats in bus.txt file
    with open(BUS_FILE, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.startswith(ticket_data[1]):
                bus_data = line.strip().split('|')
                bus_data[4] = str(int(bus_data[4]) + 1)
                file.write('|'.join(bus_data) + '\n')
            else:
                file.write(line)
        file.truncate()

    print("                             Ticket cancelled successfully.")


#index search
def get_bus_details(bus_number):
    with open(BUS_INDEX_FILE, 'r') as index_file:
        for line in index_file:
            key, address = line.strip().split('|')
            if key == bus_number:
                with open(BUS_FILE, 'r') as bus_file:
                    for i, bus_line in enumerate(bus_file, start=1):
                        if i == int(address):
                            return bus_line.strip().split('|')
                break
    return None

def get_ticket_details(ticket_id):
    with open(TICKET_INDEX_FILE, 'r') as index_file:
        for line in index_file:
            key, address = line.strip().split('|')
            if key == ticket_id:
                with open(TICKET_FILE, 'r') as ticket_file:
                    for i, ticket_line in enumerate(ticket_file, start=1):
                        if i == int(address):
                            return ticket_line.strip().split('|')
                break
    return None


# Function to view booked tickets
def view_booked_tickets():
    print("\n**************---------------------- Booked Tickets----------------------************** ")
    ticket_data = []

    with open(TICKET_FILE, 'r') as file:
        for line in file:
            if not line.startswith('*'):
                ticket_data.append(line.strip().split('|'))

    if len(ticket_data) > 0:
        for data in ticket_data:
            print(f"                                Ticket ID: {data[0]}")
            print(f"                                Bus Number: {data[1]}")
            print(f"                                Passenger Name: {data[2]}")
            print(f"                                Contact Number: {data[3]}")
            print(f"                                Seat Number: {data[4]}")
            print(f"                                Fare: {data[5]}")
            print("=====================================================================================")
    else:
        print("                             No booked tickets.")

is_admin = False
is_logged_in = False
while True:
    if not is_logged_in:
        clear_screen()
        print("=====================================================================================")
        print("\n **************************---- Bus Ticket Booking System ----**********************")
        print("=====================================================================================")
        print("\n")
        print("=====================================================================================")
        print("||                           1. Admin Login                                        ||")
        print("||                           2. User Login                                         ||")
        print("||                           3. Exit                                               ||")
        print("=====================================================================================")

        choice = input("                                Enter your choice: ")

        if choice == '1':
            is_admin = admin_login()
            if is_admin:
                is_logged_in = True
        elif choice == '2':
            is_admin = False
            is_logged_in = True
        elif choice == '3':
            break
        else:
            print("                             Invalid choice. Please try again.")

    else:
        choice = get_choice(is_admin)

        if is_admin:
            clear_screen()
            if choice == '1':
                add_bus()
            elif choice == '2':
                delete_bus()
            elif choice == '3':
                view_buses()
            elif choice == '4':
                edit_bus()
            elif choice == '5':
                view_booked_tickets()
            elif choice == '6':
                book_ticket()
            elif choice == '7':
                cancel_ticket()
            elif choice == '8':
                is_logged_in = False
                print("                             Logged out successfully.")
            else:
                print("                             Invalid choice. Please try again.")
                input("                             Press any key to continue...")

        else:
            clear_screen()
            if choice == '1':
                book_ticket()
            elif choice == '2':
                cancel_ticket()
            elif choice == '3':
                view_buses()
            elif choice == '4':
                view_booked_tickets()
            elif choice == '5':
                is_logged_in = False
                print("                             Logged out successfully.")
            else:
                print("                             Invalid choice. Please try again.")
                input("                             Press any key to continue...")