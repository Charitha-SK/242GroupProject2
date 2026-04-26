from data.file_handler import FileHandler


# Helper functions

def view_all_requests(requests):
    # Displays a summary of all requests
    if not requests:
        print("\nNo requests found.\n")
        return

    print("\n--- All Requests ---")
    for row in requests:
        print(f"ID: {row[0]} | Type: {row[1]} | Location: {row[3]} | Status: {row[6]}")


def add_request(requests):
    # Collects user input and adds a new request
    print("\n--- Add New Request ---")

    request_id = input("Request ID: ")
    request_type = input("Type (maintenance/support/emergency): ").lower()
    requester_name = input("Requester Name: ")
    location = input("Location: ")
    urgency = input("Urgency Level: ")
    cost = input("Estimated Cost: ")
    status = input("Status: ")

    # Validate estimated cost input
    try:
        float(cost)
    except ValueError:
        print("Invalid cost. Request not added.\n")
        return

    issue_type = ""
    days_open = ""
    attendees = ""
    event_date = ""
    hazard_level = ""
    response_time = ""

    if request_type == "maintenance":
        issue_type = input("Issue Type: ")
        days_open = input("Days Open: ")

    elif request_type == "support":
        attendees = input("Attendees: ")
        event_date = input("Event Date: ")

    elif request_type == "emergency":
        hazard_level = input("Hazard Level: ")
        response_time = input("Response Time Minutes: ")

    else:
        print("Invalid request type. Request not added.\n")
        return

    new_row = [
        request_id, request_type, requester_name, location,
        urgency, cost, status,
        issue_type, days_open, attendees, event_date,
        hazard_level, response_time
    ]

    requests.append(new_row)
    print("Request added.\n")


def search_requests(requests):
    # Searches requests using a keyword
    keyword = input("\nSearch keyword: ").lower()
    found = False

    for row in requests:
        if keyword in str(row).lower():
            print(f"ID: {row[0]} | Type: {row[1]} | Location: {row[3]} | Status: {row[6]}")
            found = True

    if not found:
        print("No matching requests.\n")


def update_status(requests):
    # Updates the status of a selected request
    request_id = input("\nEnter Request ID: ")

    for row in requests:
        if row[0] == request_id:
            new_status = input("New Status: ")
            row[6] = new_status
            print("Status updated.\n")
            return

    print("Request not found.\n")


# Main program menu

def main():
    file = FileHandler("service_requests.csv")
    requests = file.events_file

    while True:
        print("\n========== MENU ==========")
        print("1. View Requests")
        print("2. Add Request")
        print("3. Search Requests")
        print("4. Update Status")
        print("5. Save & Exit")
        print("==========================")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_requests(requests)

        elif choice == "2":
            add_request(requests)

        elif choice == "3":
            search_requests(requests)

        elif choice == "4":
            update_status(requests)

        elif choice == "5":
            file.write_back()
            print("Saved successfully. Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()