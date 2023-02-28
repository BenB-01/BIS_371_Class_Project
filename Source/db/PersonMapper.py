from db.DatabaseConnector import DatabaseConnector


class PeopleMapper(DatabaseConnector):

    def __init__(self):
        super().__init__()

    def insert(self, person):

        cursor = self._connection.cursor()

        """
        Insert command to add a person from the excel sheet to the database
        """
        command = "INSERT INTO people (people_id, l_name, f_name) " \
                  "VALUES (%s,%s,%s)"
        data = (person.get_id(),
                person.get_last_edit(),
                person.get_firstname(),
                person.get_lastname(),
                person.get_username(),
                person.get_mailaddress(),
                person.get_firebase_id(),
                person.get_deleted())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

        return person
