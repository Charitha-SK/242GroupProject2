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
        except FileNotFoundError:
            print("File does not exist.")

    def write_back(self):
        outfile = open(self.file_name, "w")

        for i in self.events_file:
            outfile.write(str(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]},{i[10]},{i[11]},{i[12]}\n"))
        outfile.close()