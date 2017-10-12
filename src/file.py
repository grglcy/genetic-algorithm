import csv


class File(object):
    def __init__(self, filename, header):
        self.file = open(filename, 'w')
        self.writer = csv.DictWriter(self.file, fieldnames=header)

    def write_header(self):
        self.writer.writeheader()

    def write_row(self, row):
        self.writer.writerow(row)

    def close(self):
        self.file.close()
