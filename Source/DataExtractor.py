from openpyxl import load_workbook


class DataExtractor:

    def __init__(self, file_path):
        self._file_path = file_path

    def get_worksheet(self):
        """Returns the worksheet in the Excel file in which the data is contained."""
        wb = load_workbook(self._file_path)
        ws = wb.worksheets[0]
        return ws

    def get_paper_data(self, worksheet, row):
        """Retrieving all the data related to one paper in one Excel file. Relates to one row in the file."""
        paper_data = {
            "paper_title": worksheet["A" + str(row)].value,
            "paper_type": worksheet["B" + str(row)].value,
            "target": worksheet["C" + str(row)].value,
            "tier": worksheet["D" + str(row)].value,
            "co_author_1": worksheet["E" + str(row)].value,
            "co_author_2": worksheet["F" + str(row)].value,
            "co_author_3": worksheet["G" + str(row)].value,
            "co_author_4": worksheet["H" + str(row)].value,
            "role": worksheet["J" + str(row)].value,
        }
        return paper_data

    def get_activity_data(self):
        pass

    def get_faculty_department_data(self, worksheet):
        """Retrieving the data for the department the faculty member is in."""
        names = worksheet["A3"].value.split(' ')
        faculty_department_data = {
            "f_name": names[0],
            "l_name": names[1],
            "department": worksheet["B3"].value
        }
        return faculty_department_data
