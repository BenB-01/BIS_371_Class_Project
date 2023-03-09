ALTER TABLE Activity DROP CONSTRAINT fk1_Activity;
ALTER TABLE Activity DROP CONSTRAINT fk2_Activity;
-- ALTER TABLE Activity DROP CONSTRAINT PK_Activity;
DROP TABLE Activity; 

ALTER TABLE Paper_Person DROP CONSTRAINT fk1_Paper_Person;
ALTER TABLE Paper_Person DROP CONSTRAINT fk2_Paper_Person;
ALTER TABLE Paper_Person DROP CONSTRAINT fk3_Paper_Person;
-- ALTER TABLE Paper_Person DROP CONSTRAINT PK_Paper_Person;
DROP TABLE Paper_Person;

ALTER TABLE Co_Author DROP CONSTRAINT fk1_Co_Author;
DROP TABLE Co_Author; 

ALTER TABLE Paper DROP CONSTRAINT fk1_Paper;
ALTER TABLE Paper DROP CONSTRAINT fk2_Paper;
-- ALTER TABLE Paper DROP CONSTRAINT PK_Paper;
DROP TABLE Paper; 

ALTER TABLE People_Department DROP CONSTRAINT fk1_People_Department;
ALTER TABLE People_Department DROP CONSTRAINT fk2_People_Department;
-- ALTER TABLE People_Department DROP CONSTRAINT PK_People_Department;
DROP TABLE People_Department; 

-- ALTER TABLE Activity_Type DROP CONSTRAINT PK_Activity_Type;
DROP TABLE Activity_Type; 

-- ALTER TABLE Target DROP CONSTRAINT PK_Target;
DROP TABLE Target; 

-- ALTER TABLE Target_Type DROP CONSTRAINT PK_Target_Type;
DROP TABLE Target_Type; 

-- ALTER TABLE Role DROP CONSTRAINT PK_Role;
DROP TABLE Role; 

-- ALTER TABLE Department DROP CONSTRAINT PK_Department;
DROP TABLE Department; 

-- ALTER TABLE People DROP CONSTRAINT PK_People;
DROP TABLE People;
