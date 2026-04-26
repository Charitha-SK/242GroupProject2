from data.file_handler import FileHandler
from services.request_manager import Manager

# Helper functions
def view_all_requests(requests):
    # Displays a summary of all requests
    if not requests:
        print("\nNo requests found.\n")
        return

    print("\n--- All Requests ---")
    for row in requests:
        print(row.to_str())

def search_requests(requests):
    # Searches requests using a keyword
    keyword = input("\nSearch keyword: ").lower()
    found = False

    for row in requests:
        if keyword in row.to_str().lower():
            print(row.to_str())
            found = True

    if not found:
        print("No matching requests.\n")

# Main program menu
def main():
    file = Manager("service_requests.csv")
    requests = file.request_obj

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
            file.add_request()

        elif choice == "3":
            search_requests(requests)

        elif choice == "4":
            file.update_status()

        elif choice == "5":
            file.write()
            print("Saved successfully. Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
