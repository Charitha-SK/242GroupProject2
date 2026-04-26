"""
Each request record includes core information such as a request ID, the name of the person
or organization making the request, the location involved, the urgency level, the estimated
cost, and the current status of the request. In addition, some records contain details that
only make sense for certain situations. For example, a maintenance-related record may include
the type of issue and how long it has been open. An event-support record may include the
expected number of attendees and the date of the event. An emergency-related record may include
a hazard level and an expected or recorded response time.

The office wants a program that can work with this CSV data in a practical way.
Staff members must be able to enter new request information when additional service needs arise.
They must also be able to search the stored records using specific criteria so that they can
quickly find relevant cases. Beyond simply storing and displaying data, the office also wants
the system to examine the request information and produce a meaningful result that helps staff
make decisions. For example, the program might determine a recommendation, classify a request,
assign a priority level, or identify what kind of follow-up action may be needed.
"""

from data.file_handler import FileHandler
from models.emergency import emergency
from models.support import support
from models.maintenance import maintenance

class Manager:
    def __init__(self, filename):
        self.handler = FileHandler(filename)
        self.request_obj = []
        self.file_vers = self.handler.requests_file
        for i in self.file_vers:
            try:
                if i[1] == "Maintenance":
                    self.request_obj.append(maintenance(i[0], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                elif i[1] == "EventSupport":
                    self.request_obj.append(support(i[0], i[2], i[3], i[4], i[5], i[6], i[9], i[10]))
                elif i[1] == "Emergency":
                    self.request_obj.append(emergency(i[0], i[2], i[3], i[4], i[5], i[6], i[11], i[12]))
            except TypeError:
                print()


    def display_all(self):
        for i in self.request_obj:
            print(self.request_obj[i].to_str())

    def write(self):
        self.handler.write_back()

    def update_status(self):
        # Updates the status of a selected request
        request_id = input("\nEnter Request ID: ")

        for i in range(len(self.request_obj)):
            if self.request_obj[i].sr_id == request_id:
                new_status = input("New Status: ")
                self.file_vers[i][6] = new_status
                self.request_obj[i].status = new_status
                print("Status updated.\n")
                return


        print("Request not found.\n")

    def add_request(self):
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
            self.request_obj.append(maintenance(request_id, requester_name, location, urgency, cost, status, issue_type, days_open))

        elif request_type == "support":
            attendees = input("Attendees: ")
            event_date = input("Event Date: ")
            self.request_obj.append(support(request_id, requester_name, location, urgency, cost, status, attendees, event_date))

        elif request_type == "emergency":
            hazard_level = input("Hazard Level: ")
            response_time = input("Response Time Minutes: ")
            self.request_obj.append(emergency(request_id, requester_name, location, urgency, cost, status, hazard_level, response_time))
        else:
            print("Invalid request type. Request not added.\n")
            return

        new_row = [
            request_id, request_type, requester_name, location,
            urgency, cost, status,
            issue_type, days_open, attendees, event_date,
            hazard_level, response_time
        ]

        self.file_vers.append(new_row)
        print("Request added.\n")
