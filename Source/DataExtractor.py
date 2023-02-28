from openpyxl import load_workbook


class DataExtractor:

    def __init__(self, file_path):
        self._file_path = file_path

    def get_paper_data(self, row):
        wb = load_workbook(self._file_path)
        ws = wb.worksheets[0]
        paper_data = {
            "paper_title": ws["A" + str(row)].value,
            "paper_type": ws["B" + str(row)].value,
            "target": ws["C" + str(row)].value,
            "tier": ws["D" + str(row)].value,
            "co_author_1": ws["E" + str(row)].value,
            "co_author_2": ws["F" + str(row)].value,
            "co_author_3": ws["G" + str(row)].value,
            "co_author_4": ws["H" + str(row)].value,
            "role": ws["J" + str(row)].value,
            # activity still missing
        }
        return paper_data

    def get_faculty_department_data(self):
        """Retrieving the data for the department the faculty member is in"""
        wb = load_workbook(self._file_path)
        ws = wb.worksheets[0]
        names = ws["A3"].value.split(' ')
        faculty_department_data = {
            "f_name": names[0],
            "l_name": names[1],
            "department": ws["B3"].value
        }
        return faculty_department_data
