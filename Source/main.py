from DatabaseInteractor import DatabaseInteractor
from DataExtractor import DataExtractor
import os


class ETLPipeline:

    def __init__(self, directory):
        self._directory = directory

    def get_all_paper_data(self):
        all_data = []
        for foldername in os.listdir(self._directory):
            folder_path = os.path.join(self._directory, foldername)
            if os.path.isdir(folder_path):
                excel_path = os.path.join(folder_path, foldername + '.xlsx')
                extractor = DataExtractor(excel_path)
                paper_data = extractor.get_paper_data(7)
                all_data.extend(paper_data)
        return all_data


etl = ETLPipeline('/Users/BenBurkert/Library/CloudStorage/OneDrive-bwedu/Studium/OSU/Winter_Term/BIS 371/research_productivity')
test = etl.get_all_paper_data()
print(test)
