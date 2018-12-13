import psycopg2 # Library for interacting with Postgres. Need to install for your Python.
# Load the psycopg extras module:
import psycopg2.extras
from final_project_class import *
from final_project_functions_for_compounds import *
from final_project_functions_for_proteins import *
from final_project_functions_for_visual import *

"""setting up SQL and tables, I don't need to make functions in this setting up step"""
conn = psycopg2.connect("dbname='si508_final_project' user='Koitaro'") # No password on the databases yet -- wouldn't want to save that in plain text in the program, anyway
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

try:
    conn = psycopg2.connect("dbname='si508_final_project' user='Koitaro'") # No password on the databases yet -- wouldn't want to save that in plain text in the program, anyway
    print("db connect success")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
except:
    print("Unable to connect to the database. Check server and credentials.")
    exit() # Stop running program if there's no db connection.

cur.execute("DROP TABLE IF EXISTS Compounds;")
cur.execute("DROP TABLE IF EXISTS Proteins2;")
cur.execute("DROP TABLE IF EXISTS Proteins;")


try:
    cur.execute("CREATE TABLE IF NOT EXISTS Compounds(Name VARCHAR(256) PRIMARY KEY UNIQUE NOT NULL, Molecular_Weight DECIMAL(12,6), Smile VARCHAR(256), Price DECIMAL(12,6), Institution VARCHAR(64), Address VARCHAR(64), Url VARCHAR(64))") #"this is SQL query"
    cur.execute("CREATE TABLE IF NOT EXISTS Proteins(Name VARCHAR(256) PRIMARY KEY UNIQUE NOT NULL, Molecular_Weight DECIMAL(12,6), Polymer_Length INTEGER, Resolution DECIMAL(12,6), Polymer_Description VARCHAR(256), Price DECIMAL(12,6), Institution VARCHAR(64), Address VARCHAR(64), Url VARCHAR(64))")
    cur.execute("CREATE TABLE IF NOT EXISTS Proteins2(Name VARCHAR(256) PRIMARY KEY UNIQUE NOT NULL REFERENCES Proteins(Name), Molecular_Weight DECIMAL(12,6), Polymer_Length INTEGER, Resolution DECIMAL(12,6), Polymer_Description VARCHAR(256), Price DECIMAL(12,6), Institution VARCHAR(64), Address VARCHAR(64), Url VARCHAR(64))")
    print("create table success")
except:
    print('Unable to create tables')

"""I deleted Movie_Numbers table because this table doesn's have any dependancy.
Then I can delete Movie_Names table because this table doesn't have any dependancy anymore!
Also, when I type psql, I should type psql DATABASE_NAME so that I can enter only the specified database.
Otherwise, psql open all databases"""


def make_protein_dictionary_lst(inst_protein):
    protein_dictions_lst = []
    #print('here is run!')
    for inst_el in inst_protein:
        protein_diction = {}
        protein_diction['Name'] = inst_el.name
        protein_diction['Molecular_Weight'] = inst_el.mw
        protein_diction['Polymer_Length'] = inst_el.polymer_length
        protein_diction['Resolution'] = inst_el.polymer_resolution
        protein_diction['Polymer_Description'] = inst_el.polymer_description
        protein_diction['Price'] = inst_el.price
        protein_diction['Institution'] = inst_el.institution
        protein_diction['Address'] = inst_el.address
        protein_diction['Url'] = inst_el.url

        protein_dictions_lst.append(protein_diction)

    protein_dictions_tuple = tuple(protein_dictions_lst)
    return protein_dictions_tuple

def insert_proteins(name,molecular_weight,polymer_length,resolution,polymer_description,price,institution,address,url, conn, cur):
    """Returns True if succcessful, False if not"""
    sql_Proteins = """INSERT INTO Proteins(Name,Molecular_Weight,Polymer_Length,Resolution,Polymer_Description,Price,Institution,Address,Url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(sql_Proteins,(name,float(molecular_weight),int(polymer_length),float(resolution),polymer_description,float(price),institution,address,url))
    sql_Proteins2 = """INSERT INTO Proteins2(Name,Molecular_Weight,Polymer_Length,Resolution,Polymer_Description,Price,Institution,Address,Url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(sql_Proteins2,(name,float(molecular_weight),int(polymer_length),float(resolution),polymer_description,float(price),institution,address,url))
    conn.commit()
    return True

"""this is the main function for protein data"""
def get_protein_data_and_store_in_SQL(number_of_protein,length_of_peptide,resol):
    print('\n\n-------------------------------------------------------------------------\nNow checking all {} proteins and finding matches!\nWhen matches are found, these are stored into SQL database!\nSorry, this process might be more than couple minutes if you do not have data in cache...\n-------------------------------------------------------------------------'.format(number_of_protein))
    protein_counter = 1
    for diction in make_protein_dictionary_lst(get_protein_with_short_peptide(number_of_protein,length_of_peptide,resol)):
        try:
            #print(diction)
            insert_proteins(diction["Name"],diction["Molecular_Weight"],diction["Polymer_Length"],diction['Resolution'],diction['Polymer_Description'],diction["Price"],diction["Institution"],diction["Address"],diction["Url"], conn, cur) # Here: passing in actual conn and cur that exist
            #print("{} Success adding a protein to SQL: {}".format(protein_counter,diction["Name"]))
            protein_counter += 1
        except Exception as inst:
            print("Failed adding a protein, check problem")
            print(inst)
            pass
    print("\n\n-------------------------------------------------------------------------\n{} proteins were stored into Proteins Table in SQL database!\n-------------------------------------------------------------------------".format(protein_counter))
    return get_protein_with_short_peptide(number_of_protein,length_of_peptide,resol)
#get_protein_data_and_store_in_SQL(100,10,2)

def make_compound_dictionary_lst(inst_compound):
    compound_dictions_lst = []
    for inst_el in inst_compound:
        compound_diction = {}
        compound_diction['Name'] = inst_el.name
        compound_diction['Molecular_Weight'] = inst_el.mw
        compound_diction['Smile'] = inst_el.smile
        compound_diction['Price'] = inst_el.price
        compound_diction['Institution'] = inst_el.institution
        compound_diction['Address'] = inst_el.address
        compound_diction['Url'] = inst_el.url

        compound_dictions_lst.append(compound_diction)

    compound_dictions_tuple = tuple(compound_dictions_lst)
    return compound_dictions_tuple

def insert_compounds(name,molecular_weight,smile,price,institution,address,url, conn, cur):
    """Returns True if succcessful, False if not"""
    sql_Compounds = """INSERT INTO Compounds(Name,Molecular_Weight,Smile,Price,Institution,Address,Url) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(sql_Compounds,(name,float(molecular_weight),smile,float(price),institution,address,url))
    conn.commit()
    return True

"""this is the main function for compound data"""
def get_compound_data_and_store_in_SQL(num_of_page_to_scrape):
    print('\n\n-------------------------------------------------------------------------\nNow checking {} zinc pages and storing compound data into SQL database!\nSorry, this process might be more than couple minutes if you do not have data in cache...\n-------------------------------------------------------------------------'.format(num_of_page_to_scrape))
    compound_counter = 1
    for diction in make_compound_dictionary_lst(get_data_from_each_zinc_page(num_of_page_to_scrape)):
        try:
            insert_compounds(diction["Name"],diction["Molecular_Weight"],diction["Smile"],diction["Price"],diction["Institution"],diction["Address"],diction["Url"], conn, cur) # Here: passing in actual conn and cur that exist
            #print("{} Success adding a compound to SQL: {}".format(compound_counter,diction["Name"]))
            compound_counter += 1
        except Exception as inst:
            print("Failed adding a compound, check problem")
            print(inst)
            pass
    print("\n\n-------------------------------------------------------------------------\n{} compounds were stored into Compounds Table in SQL database!\n-------------------------------------------------------------------------".format(compound_counter))

    return get_data_from_each_zinc_page(num_of_page_to_scrape)
#get_compound_data_and_store_in_SQL(1)
"""return all info from Compounds"""
# cur.execute("SELECT * FROM Compounds")
# print(cur.fetchone())
"""return all info from Compounds"""
# cur.execute("SELECT * FROM Compounds")
# print(cur.fetchall())
"""return all info from Movie_Numbers"""
# cur.execute("SELECT * FROM Proteins2")
# print(cur.fetchall())
"""return all info from Movie_Numbers"""
# cur.execute("SELECT * FROM Proteins")
# print(cur.fetchall())
"""return only Title info from Movie_Names"""
# cur.execute("SELECT Name FROM Proteins WHERE Polymer_Length <= 4")
# print(cur.fetchall())
"""return only Rating_IMDB info from Movie_Numbers"""
# cur.execute("SELECT Rating_IMDB FROM Movie_Numbers")
# print(cur.fetchall())
"""return only Director info from Movie_Names"""
# cur.execute("SELECT Director FROM Movie_Names")
# print(cur.fetchall())
"""return US_Gross and Title info from Movie_Numbers"""
# cur.execute("SELECT Title,US_Gross FROM Movie_Numbers")
# print(cur.fetchall())
"""return all movie titles of Steven Spielberg from Movie_Names"""
# cur.execute("SELECT Title FROM Movie_Names WHERE Director = 'Steven Spielberg'")
# print(cur.fetchall()) #this one worked even though data in a column is list of list
"""return all info of Steven Spielberg from Movie_Names"""
# cur.execute("SELECT * FROM Movie_Names WHERE Director = 'Steven Spielberg'")
# print(cur.fetchall())
"""return the total number of movies from Movie_Names"""
# cur.execute("SELECT COUNT(*) FROM Movie_Names")
# print(cur.fetchone()) #fetchall() is the same
"""return the total number of Directors from Movie_Names"""
# cur.execute("SELECT COUNT(Director) FROM Movie_Names")
# print(cur.fetchone()) #fetchall() is the same
#This is counting everything, so not appropriate
"""return average number of US_Gross from Movie_Numbers"""
# cur.execute("SELECT US_Gross FROM Movie_Numbers") #AVG(US_Gross) doesn't work because US_Gross column contains list data
# us_gross_lst = cur.fetchall() #fetchall() is the same
# us_gross_str_lst = []
# for el in us_gross_lst:
#     us_gross_str_lst.append(int(el[0]))
# print(mean(us_gross_str_lst))
# cur.execute("SELECT AVG(US_Gross) FROM Movie_Numbers")
# print(cur.fetchone())
"""I can do MIN(),MAX(),SUM()"""
# cur.execute("SELECT MAX(US_Gross) FROM Movie_Numbers")
# print(cur.fetchone())
# cur.execute("SELECT MIN(US_Gross) FROM Movie_Numbers")
# print(cur.fetchone())
# cur.execute("SELECT AVG(US_Gross) FROM Movie_Numbers")
# print(cur.fetchone()) #why doesn't work?
"""Apparently that column is not a number but a character column. Do not store numbers in varchar (or char) columns.
Change the datatype to integer, numeric or whatever suits you best."""
# cur.execute("SELECT SUM(US_Gross) FROM Movie_Numbers")
# print(cur.fetchone()) #why doesn't work?
"""return all from Movie_Numbers where US_Gross >100000"""
# cur.execute("SELECT * FROM Movie_Numbers WHERE US_Gross > 10000")
# print(cur.fetchall()) #why doesn't work?
"""return titles from Movie_Names where a title shorter than 5 charactoers"""
# cur.execute("SELECT Title FROM Movie_Names WHERE LENGTH(Title) < 5")
# print(cur.fetchall())
"""return titles from Movie_Names where a title starts with a 'S'"""
# cur.execute("SELECT Title FROM Movie_Names WHERE Title LIKE 'S%'")
# print(cur.fetchall())
"""return titles from Movie_Names where a title has 'zz''"""
# cur.execute("SELECT Title FROM Movie_Names WHERE Title LIKE '%zz%'")
# print(cur.fetchall())
