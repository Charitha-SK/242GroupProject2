class FileHandler:
    def __init__(self, filename):
        self.file_name = filename
        self.events_file = []
        try:
            infile = open(filename, "r")
            for line in infile:
                line = line.strip()
                temp = line.split(",")
                self.events_file.append(temp)
            infile.close()
            self.events_file.pop(0)
        except FileNotFoundError:
            print("File does not exist.")

    def write_back(self):
        outfile = open(self.file_name, "w")
        outfile.write("request_id,request_type,requester_name,location,urgency_level,estimated_cost,status,issue_type,days_open,attendees,event_date,hazard_level,response_time_minutes")
        for i in self.events_file:
            outfile.write(str(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]},{i[10]},{i[11]},{i[12]}\n"))
        outfile.close()