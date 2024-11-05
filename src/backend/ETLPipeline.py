# SPDX-FileCopyrightText: 2024 Ben Burkert
#
# SPDX-License-Identifier: MIT

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
        target_type_dict = db_interactor.get_allowed_values('Target_Type')
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
                people_id = people_dict[faculty_department_data['f_name']]
                # insert people_department data to database
                query = "INSERT INTO People_Department (People_ID, Department_ID) " \
                        "VALUES ({}, {})".format(people_id, department_id)
                print('- Executing People_Department -')
                print('-> ', faculty_department_data['f_name'], faculty_department_data['department'])
                db_interactor.insert_data(query)

                # loop through the rows in the sheet
                for row in range(7, worksheet.max_row):
                    # check if the row contains data related to a paper and not only related to activities
                    if worksheet["A" + str(row)].value is not None:
                        # get data related to a paper
                        raw_paper_data = extractor.get_paper_data(worksheet, row)
                        paper_title = raw_paper_data['paper_title']
                        target_type = raw_paper_data['target_type']
                        target_name = raw_paper_data['target']
                        tier = raw_paper_data['tier']
                        if tier is None:
                            tier = 'NULL'
                        role = raw_paper_data['role']

                        # search for the target name in database
                        existing_target = db_interactor.search_for_duplicate(target_name, 'Target')
                        target_type_id = target_type_dict[target_type]
                        # define query for the case that target is not yet in database
                        query = "INSERT INTO Target (Target_Name, Target_Type) " \
                                "VALUES ('{}', {})".format(target_name, target_type_id)
                        print('- Executing Target -')
                        print('-> ', target_name)
                        # check if target is already in database, if yes get the id, if not insert it and get max(id)
                        target_id = db_interactor.get_id(existing_target, 'Target', query)

                        # search for the paper title in database
                        existing_paper = db_interactor.search_for_duplicate(paper_title, 'Paper')
                        # define query for the case that the paper is not yet in the database
                        query = "INSERT INTO Paper (Paper_Title, Target, Tier)" \
                                "VALUES ('{}', {}, {})".format(paper_title, target_id, tier)
                        print('- Executing Paper -')
                        print('-> ', paper_title)
                        # check if paper is already in database, if yes get the id, if not insert it and get max(id)
                        paper_id = db_interactor.get_id(existing_paper, 'Paper', query)

                        # insert paper_person
                        role_id = role_dict[role]
                        query = "INSERT INTO Paper_Person (Paper_ID, People_ID, Role)" \
                                "VALUES ({}, {}, {})".format(paper_id, people_id, role_id)
                        print('- Executing Paper_Person -')
                        print('-> ', paper_title, faculty_department_data['f_name'])
                        db_interactor.insert_data(query)

                        # insert coauthors of paper
                        coauthors = extractor.get_coauthor_data(worksheet, row)
                        for key, value in coauthors.items():
                            # if there is a coauthor listed in the cell: insert into the database
                            if value is not None:
                                # check if the entry already exists in the database, if not: insert it
                                existing_entry = db_interactor.search_for_duplicate(value, 'Co_Author', paper_id)
                                if len(existing_entry) == 0:
                                    query = "INSERT INTO Co_Author (Co_Author_Name, Paper_ID)" \
                                            "VALUES ('{}', {})".format(value, paper_id)
                                    print('- Executing Coauthor -')
                                    print('-> ', value, paper_id)
                                    db_interactor.insert_data(query)

                        # get all the activities related to one paper
                        activities = extractor.get_activity_data(worksheet, row)
                        # loop through the activites and save them in the database
                        for key, (activity_date, activity_type) in activities.items():
                            activity_type = activity_type
                            activity_type_id = activity_type_dict[activity_type]
                            activity_date = activity_date.date()
                            paper_id = db_interactor.get_max_id('Paper')
                            query = "INSERT INTO Activity (Activity_Date, Activity_Type, Paper_ID)" \
                                    "VALUES ('{}', {}, {})".format(activity_date, activity_type_id, paper_id)
                            print('- Executing Activity -')
                            print('-> ', activity_date, activity_type)
                            db_interactor.insert_data(query)

        # disconect from database
        db_interactor.disconnect()


etl = ETLPipeline('../../excel_data')
etl.collect_and_store_data()
