# Atsunori_Kaneshige SI508-FinalProject

This is SI508 Final project README.


### What this program does?


You will be getting data from two sites. **Zinc** and **Protein Data Bank(PDB)**.
Zinc (http://zinc15.docking.org/) is  a free database of commercially-available compounds for virtual screening. PDB stores data of biological macromolecular structures, mostly protein crystal structures.
To make the search easier in this SI508 final project, a user can simply run a py file that interacts with the user.


### Cloning from Github repository


Please clone all necessary files from NoriKaneshige's repository.
1) Please go to this link: https://github.com/NoriKaneshige/SI508-FinalProject
2) Please use the repository adress: https://github.com/NoriKaneshige/SI508-FinalProject.git
3) Please open your terminal and type the following.


**git clone https://github.com/NoriKaneshige/SI508-FinalProject.git**


4) The files that you really need is the following.


num of files | File Names
------------ | -------------
1 | PDB_ligands.csv
2 | advanced_expiry_caching.py
3 | final_project_class.py
4 | final_project_functions_for_compounds.py
5 | final_project_functions_for_proteins
6 | final_project_functions_for_sql
7 | final_project_functions_for_visual
8 | final_project_human_protein_id.json
9 | final_project_test_suites.py
10 | final_project_user_interactive.py
11 | Lecture18_Postgres_Database_setup.pdf

### Prerequisites/Installing/Database_SetUp


num | libraries/modules | url
------------ | -------------------- | --------------------------------------------------------------------------
1 | Beautiful Soup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2 | Plotly | https://plot.ly/python/getting-started/
3 | Psycopg | http://initd.org/psycopg/docs/install.html
4 | Numpy | https://docs.scipy.org/doc/numpy-1.15.0/user/install.html
5 | PostgreSQL | If necessary, please look at Lecture18_Postgres_Database_setup.pdf


The libraries/modules in the table need to be installed. Please go to the sources below if you need them.
You can go to the links below and follow the instructions to install those libraries/modules.


**Plotly**: If you don't have a Plotly account, please have **user name** and **api key** to use plotly.


**PostgreSQL**: the installation of PosgreSQL is bit complicated. If you do not have PostgreSQL installed, please take a close look at Lecture18_Postgres_Database_setup.pdf and follow the instruction step by step!


After successfully install PostgreSQL, you need to create a database to run SI508-FinalProject files. The name should be **si508_final_project**.


1) To run the server, please type **pg_ctl -D /usr/local/var/postgres start**


2) Then type **psql** and **createdb si508_final_project** as shown in the display image.
![Image of psql_createdb](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display_sql_createdb.png)

3) When you type **\l**, you should see a database table as shown.
![Image of psql_createdb_result](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display_sql_createdb_result.png)

 in your terminal, then type


 **createdb SI508-FinalProject files**


 to create a database.


### Other libraries/modules

You will be importing **requests**/**json**/**datetime**/**sys**/**csv**/**webbrowser**/**unittest** when you run the program.


### Secret information
You need to replace two things in py files with your secret information. So please have your plotly usename and plotly api_key. You will be cloning all files from Github repository.


1) Please open the file, final_project_functions_for_sql, and replace username with yours.


**e.g. user='YOUR_USER_NAME'**


2) Please open the file, final_project_functions_for_visual, and replace plotly username and plotly api_key.


**e.g. username='YOUR_PLOTLY_USER_NAME', api_key='YOUR_PLOTLY_API_KEY'**


## Instructuions about how to run the project!


After cloning all necessary files into the same directory, please run final_project_user_interactive.py


You should see the result like this in your terminal.


![Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display1.png)


## What/How to run

Only two files are needed to run the project2.


1) proj2_nps.py
2) advanced_expiry_caching.py


Those two files need to be contained in the same directory. Then simply run the python file, proj2_nps.py.


**IMPORTANT!: you need to replace the followings with yours!!!**


**1) Google Places API**


**2) Plotly username**


**3) Plotly API key**


**4) Mapbox access token**


Then you can simply run the python file and follow input prompts that will appear in your terminal!!! Hope it works!!!


## What/How to check the results

The results will show up in your terminal.


**The maps will be uploaded in YOUR Mapbox website!**
