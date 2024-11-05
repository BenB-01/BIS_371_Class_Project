<!--
SPDX-FileCopyrightText: 2024 Ben Burkert

SPDX-License-Identifier: MIT
-->

# Business Information Systems 371 - Class Project

A tool created for the Business Information Systems 371 class at Oregon State University during Fall Term 2023. 

- Automacically access folder with Excel files containing data regarding research papers from OSU
- Exctract data from Excel sheets
- Scripts to create MySQL database with correct schema
- Store data in one single MySQL database

## 🔨 Installation & Setup

1. Install [Python 3.11](https://www.python.org/downloads/release/python-3110/)
2. Install [poetry](https://python-poetry.org)
3. Install [dependencies](https://python-poetry.org/docs/basic-usage/#installing-with-poetrylock) using poetry
4. Select Poetry environment as Python environment for the project

## 💡 Usage

1. Create a MySQL database using the [table creation script](database/table_creation_mysql.sql)
2. Add the values of [the nontransaction tables](database/values_nontransaction_tables.sql) 
3. Run the [ETL Pipeline](src/backend/ETLPipeline.py) to extract the information from the folder with Excel files
4. When the pipeline is done, run the [Frontend](src/frontend/class_project_tkinter_GUI_query_tool.py) to view the data in the database