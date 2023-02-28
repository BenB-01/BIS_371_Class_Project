import os
from openpyxl import load_workbook


class DataExtracor:

    def __init__(self, directory):
        self._directory = directory

    def get_paper_data(self, sheet_path, row):
        wb = load_workbook(sheet_path)
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

    def get_faculty_department_data(self, sheet_path):
        wb = load_workbook(sheet_path)
        ws = wb.worksheets[0]
        names = ws["A3"].value.split(' ')
        faculty_department_data = {
            "f_name": names[0],
            "l_name": names[1],
            "department": ws["B3"].value
        }
        return faculty_department_data




da = DataExtracor('/Users/BenBurkert/Library/CloudStorage/OneDrive-bwedu/Studium/OSU/Winter_Term/BIS 371/research_productivity')
data = da.get_paper_data('/Users/BenBurkert/Library/CloudStorage/OneDrive-bwedu/Studium/OSU/Winter_Term/BIS 371/research_productivity/aarav_roberts/aarav_roberts.xlsx', 7)
print(data)
data_2 = da.get_faculty_department_data('/Users/BenBurkert/Library/CloudStorage/OneDrive-bwedu/Studium/OSU/Winter_Term/BIS 371/research_productivity/aarav_roberts/aarav_roberts.xlsx')
print(data_2)
