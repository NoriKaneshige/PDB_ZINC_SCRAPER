# Atsunori_Kaneshige SI508-FinalProject

This is SI508 Final project README.


### What this program does?


You will be getting data from two sites. **Zinc** and **Protein Data Bank(PDB)**.
Zinc (http://zinc15.docking.org/) is  a free database of commercially-available compounds for virtual screening. You will be scraping Zinc Substances pages (http://zinc15.docking.org/substances/). PDB (http://www.rcsb.org/) stores data of biological macromolecular structures, mostly protein crystal structures.
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

3) When you type **\l**, you should see a database table as shown. Then, database is ready now.


![Image of psql_createdb_result](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display_sql_createdb_result.png)


### Other libraries/modules

You will be importing **requests**/**json**/**datetime**/**sys**/**csv**/**webbrowser**/**unittest** when you run the program.


### Secret information
You need to replace two things in py files with your secret information. So please have your plotly usename and plotly api_key. You will be cloning all files from Github repository.


1) Please open the file, final_project_functions_for_sql, and replace username with yours.


**e.g. user='YOUR_USER_NAME'**


2) Please open the file, final_project_functions_for_visual, and replace plotly username and plotly api_key.


**e.g. username='YOUR_PLOTLY_USER_NAME', api_key='YOUR_PLOTLY_API_KEY'**


## Instructuions about how to run the project (ZINC)!

Here, let me demonstrate the final project to show you typical steps and outcomes!


After cloning all necessary files into the same directory, please run final_project_user_interactive.py


You should see the result like this in your terminal.


![Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display1.png)


Here, you can type one of 4 commands shown in the terminal. Let's explore Zinc to get molecule information and do simple query.


Please type **Zinc** and hit enter (case insensitive). You will be asked about how many pages you want to scrape in Zinc. Here, you can scrape as many as you want, but **please type 1 for now** because it turned out that scraping takes a lot of time. To demonstrate, I input 3 to scrape 3 pages from Zinc. The result is shown below. In this case, data of page 1 and 2 was already in cache, but the program made a request for page 3. If a compound has complete data to make an instance, the instance will be created and will be stored into Compound table in the database, si508_final_project.


![Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display2.png)


Here, you have 5 commands to type. Let's type **PlotALL** (case insensitive). If you correctly replace plotly username and plotly aip key in final_project_functions_for_visual, you will be opening your plotly site and a 3D scatter plot will show up automatically as shown below. Compound instances are 3D scatter plotted here based on properties of compounds.


![Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display3.png)



If you type **ListAll**, simply names (compounds' Zinc code) will be displayed in the terminal as shown below.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display4.png)


Now, you can do Query or Look command. Let's do Query to narrow down the compounds.

Please type **Query**, then you will be asked the minimum molecular weight and the maximum molecular weight. For now, please input **200** for the minimum and **250** for the maximum. Only compounds that have molecular weight between 200 and 250 will be shown in your terminal.


From here, you can do 3D scatter plot again, or you can look up the individual compound site in Zinc.
Let's try it. Here, you can choose as many compounds as you want. For example, please type **Look zinc10 zinc99 zinc136 zinc215 zinc401**. The websites of all of those zinc compounds will be automatically opened as shown below.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display5.png)


Basically this is it about Zinc search. I want to mention one more thing about Zinc search.
Let me explain it here. PDB (protein data bank) has also compound data. Basically compounds in PDB are molecules that were co-cryltalized with proteins. You can check if zinc compounds that you scraped from Zinc are found in PDB. To do that, I used SMILES. SMILES is simplified molecular-input line-entry system. You can go to wikipedia site to know more details (https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system). Long story short, each molecule has distinct SMILES and compounds in Zinc and compounds in PDB have SMILES data, so I used SMILES to find matches between zinc compounds that the program scraped and all compounds in PDB (I made JSON file that contains all PDB compounds' SMILES). Let's try this.


Let me demonstrate here.
I typed **zinc** and input **3** to scrape 3 zinc pages (all data in the cache this time because I scraped once before). Then I typed **ZincPDB** and hit enter. Here, the program opens PDB_ligands.csv and find any matches between zinc compounds just I got and PDB compounds by using SMILES. The result looks like this in this case. I found that PDB compound that has 2DL (PDB compound ID). You can simply go to PDB site and type 2DL to look up this compound as shown below.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display6.png)


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display7.png)



## Instructuions about how to run the project (PDB)!


Please run final_project_user_interactive.py as we did in Zinc search above.


Here, the program will read final_project_human_protein_id.json and create unique url for each protein and get data by using PDB's REST API. PDB has over 40,000 human protein crystal structures. The main purpose of this program is to find proteins that are co-crystalized with short peptides.


After typing **PDB**, you will be asked 3 things.


1) the number of proteins: I demonstrate searching 2000 proteins here. Scraping PDB site by using REAT API takes some time, so please DO NOT input huge number! 1000 proteins still need more than couple minutes.
2) the length of short peptides: I use 10 in this demonstration.
3) resolution: below 2 is considered high quality resolution, I use 2 in this demonstration.


Here, I found 43 proteins that are co-crystalized with short peptides that have less than equal 10 peptide length as shown blow.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display8.png)


Now, you can do **ListALL** to see PDB IDs of those proteins.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display9.png)


Let's do **Query** next. Those 43 protein instances are stored in tables, Proteins and Ptoteins2 that have a relationship each other in sql database called si508_final_project. You can further limit the maximum length of short peptide. Let's input 5, for example. The result looks like the one below.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display10.png)



Here you can see not only PDB ID, but also the descriptions of proteins. Depending on your interests, you can look up as many protein websites as you want. Let's try **look 1a09 1a1a 1bhf 1eb1 1h9o**.
The result is show below.


[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display11.png)


## How to run unittest


You can simply run **final_project_test_suites.py**


The result should be like this.
[Image of terminal](https://github.com/NoriKaneshige/SI508-FinalProject/blob/master/display_unittest.png)


I wrote 5 test classes.

1) test for Compound
2) test for functions of Compound
3) test for Protein
4) test for functions of Protein
5) test for functions of SQL


## List of final project requirements fulfilled

points | requirements | comments
------------ | -------------------- | --------------------------------------------------------------------------
1 | Beautiful Soup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2 | Plotly | https://plot.ly/python/getting-started/
3 | Psycopg | http://initd.org/psycopg/docs/install.html
4 | Numpy | https://docs.scipy.org/doc/numpy-1.15.0/user/install.html
5 | PostgreSQL | If necessary, please look at Lecture18_Postgres_Database_setup.pdf
1 | Beautiful Soup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2 | Plotly | https://plot.ly/python/getting-started/
3 | Psycopg | http://initd.org/psycopg/docs/install.html
4 | Numpy | https://docs.scipy.org/doc/numpy-1.15.0/user/install.html
5 | PostgreSQL | If necessary, please look at Lecture18_Postgres_Database_setup.pdf
