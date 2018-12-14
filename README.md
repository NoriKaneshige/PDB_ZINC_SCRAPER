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


### Prerequisites/Installing/Database_SetUp


num | libraries/modules | url
------------ | -------------------- | ----------------------------------------------------
1 | Beautiful Soup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2 | Plotly | https://plot.ly/python/getting-started/
3 | Psycopg | http://initd.org/psycopg/docs/install.html
4 | Numpy | https://docs.scipy.org/doc/numpy-1.15.0/user/install.html
5 | PostgreSQL | More details below


The libraries/modules in the table need to be installed. Please go to the sources below if you need them.
You can go to the links below and follow the instructions to install those libraries/modules.


**Plotly**: If you don't have a Plotly account, please have **user name** and **api key** to use plotly.


**PostgreSQL**: the installation of PosgreSQL might be little bit complicated. Please follow the instructions.
1) First, get homebrew. Please go to this link: https://brew.sh/
Copy and paste this line onto your terminal:

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com_/Homebrew/install/master/install)"


2) Then, Database setup: use the Homebrew package managaer to install the postgresql database.


  **brew install postgres**


3) type the following statement.


  **pg_ctl -D /usr/local/var/postgres start**


  You can also type


  **pg_ctl -D /usr/local/var/postgres status**


  to see the status of the searver.
  Also,


  **pg_ctl -D /usr/local/var/postgres stop**


  to stop running posgreSQL.
  #While you run this SI508-FinalProject files, you need to start the server by typing


  **pg_ctl -D /usr/local/var/postgres start**


4) You need to create a database to run SI508-FinalProject files. The name should be "SI508-FinalProject files". Please type


**psql**


 in your terminal, then type


 **createdb SI508-FinalProject files**


 to create a database.


### Other libraries/modules

You will be importing requests/json/datetime/sys/csv/webbrowser/unittest when you run the program.


### Secret information
You need to replace two things in py files with your secret information. So please have your plotly usename and plotly api_key. You will be cloning all files from Github repository.
1) Please open the file, final_project_functions_for_sql, and replace username with yours.
e.g. user='YOUR_USER_NAME'
2) Please open the file, final_project_functions_for_visual, and replace plotly username and plotly api_key. e.g. username='YOUR_PLOTLY_USER_NAME', api_key='YOUR_PLOTLY_API_KEY'


## Running the tests

This time, tests were not written.


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
