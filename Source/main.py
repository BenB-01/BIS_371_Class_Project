from DatabaseInteractor import DatabaseInteractor
from DataExtractor import DataExtractor
import os


class ETLPipeline:

    def __init__(self, directory):
        self._directory = directory

    def collect_and_store_data(self):
        """Method that executes all the necessary steps after each other to retrieve all the data from the Excel files
        and saves it to the different tables in the database."""

        # create connection to the database
        db_interactor = DatabaseInteractor()
        connection = db_interactor.connect()

        # load data from nontransaction tables to know what id each value has
        department_dict = db_interactor.get_allowed_values('Department')
        people_dict = db_interactor.get_allowed_values('People')
        paper_type_dict = db_interactor.get_allowed_values('Paper_Type')
        activity_type_dict = db_interactor.get_allowed_values('Activity_Type')
        role_dict = db_interactor.get_allowed_values('Role')

        # loop through folders
        for foldername in os.listdir(self._directory):
            folder_path = os.path.join(self._directory, foldername)
            if os.path.isdir(folder_path):
                # get the file path for each Excel file to be able to extract the data
                excel_path = os.path.join(folder_path, foldername + '.xlsx')

                # get the worksheet in the Excel file in which the data is saved
                extractor = DataExtractor(excel_path)
                worksheet = extractor.get_worksheet()

                # get data defining in which department a person works in
                faculty_department_data = extractor.get_faculty_department_data(worksheet)
                # get ids for department and person
                department_id = department_dict[faculty_department_data['department']]
                person_id = people_dict[faculty_department_data['f_name']]
                # insert people_department data to database
                query = "INSERT INTO People_Department (People_ID, Department_ID) " \
                        "VALUES ({}, {})".format(person_id, department_id)
                db_interactor.insert_data(query)

                # loop through the rows in the sheet
                for row in range(7, worksheet.max_row):
                    # check if the row contains data related to a paper and not only related to activities
                    if worksheet["A" + str(row)].value is not None:
                        # get data related to a paper
                        raw_paper_data = extractor.get_paper_data(worksheet, row)

                        # check if target is already in database, if yes get the id
                        target = raw_paper_data['target']
                        existing_value = db_interactor.search_by_name(target, 'Target')
                        if existing_value is not None:
                            target_id = existing_value[0][0]
                        # if not: insert target into the database, get the id (last inserted)
                        else:
                            query = "INSERT INTO Target (Target_Name) VALUES ({})".format(target)
                            db_interactor.insert_data(query)
                            target_id = db_interactor.get_max_id('Target')

                        # get id for paper_type

                        # check if paper is already in database, if yes get the id

                        # if not: insert paper into the database, get the id (last inserted)

                        # insert paper_person

                        # while loop for actvities of paper
                        # get id for activity type
                        # insert actvity

        # disconect from database
        db_interactor.disconnect()



etl = ETLPipeline('/Users/BenBurkert/Library/CloudStorage/OneDrive-bwedu/Studium/OSU/Winter_Term/BIS 371/research_productivity')
etl.collect_and_store_data()
