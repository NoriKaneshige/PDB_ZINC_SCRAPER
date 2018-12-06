import psycopg2 # Library for interacting with Postgres. Need to install for your Python.
# Load the psycopg extras module:
import psycopg2.extras
from final_project_class import *
from final_project_functions_for_compounds import *
from final_project_functions_for_proteins import *

try:
    conn = psycopg2.connect("dbname='si508_final_project' user='Koitaro'") # No password on the databases yet -- wouldn't want to save that in plain text in the program, anyway
    print("db connect success")
except:
    print("Unable to connect to the database. Check server and credentials.")
    exit() # Stop running program if there's no db connection.
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("DROP TABLE IF EXISTS Compounds;")
cur.execute("DROP TABLE IF EXISTS Proteins;")
"""I deleted Movie_Numbers table because this table doesn's have any dependancy.
Then I can delete Movie_Names table because this table doesn't have any dependancy anymore!
Also, when I type psql, I should type psql DATABASE_NAME so that I can enter only the specified database.
Otherwise, psql open all databases"""

try:
    cur.execute("CREATE TABLE IF NOT EXISTS Compounds(Name VARCHAR(256) PRIMARY KEY UNIQUE NOT NULL, Molecular_Weight DECIMAL(12,6), Smile VARCHAR(256), Price DECIMAL(12,6), Institution VARCHAR(64), Address VARCHAR(64), Url VARCHAR(64))") #"this is SQL query"
    cur.execute("CREATE TABLE IF NOT EXISTS Proteins(Name VARCHAR(256) PRIMARY KEY UNIQUE NOT NULL, Molecular_Weight DECIMAL(12,6), Polymer_Length INTEGER, Resolution DECIMAL(12,6), Polymer_Description VARCHAR(256), Price DECIMAL(12,6), Institution VARCHAR(64), Address VARCHAR(64), Url VARCHAR(64))")
    print("create table success")
except:
    print('Unable to create tables')

# for el in get_protein_with_short_peptide(1000,10,2):
# 	print(el)

compound_dictions_lst = []
protein_dictions_lst = []

for inst_el in get_protein_with_short_peptide(1000,10,2):
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

for inst_el in get_data_from_each_zinc_page(1):
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
protein_dictions_tuple = tuple(protein_dictions_lst)
# print(compound_dictions_tuple)
# print(protein_dictions_tuple)

def insert_compounds(name,molecular_weight,smile,price,institution,address,url, conn, cur):
    """Returns True if succcessful, False if not"""
    sql_Compounds = """INSERT INTO Compounds(Name,Molecular_Weight,Smile,Price,Institution,Address,Url) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(sql_Compounds,(name,float(molecular_weight),smile,float(price),institution,address,url))
    conn.commit()
    return True

def insert_proteins(name,molecular_weight,polymer_length,resolution,polymer_description,price,institution,address,url, conn, cur):
    """Returns True if succcessful, False if not"""
    sql_Proteins = """INSERT INTO Proteins(Name,Molecular_Weight,Polymer_Length,Resolution,Polymer_Description,Price,Institution,Address,Url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(sql_Proteins,(name,float(molecular_weight),int(polymer_length),float(resolution),polymer_description,float(price),institution,address,url))
    conn.commit()
    return True

# def insert_Movies(title, distributor, genre, director, us_gross, rating_imdb, rating_rotten_tomatoes, conn, cur):
#     """Returns True if succcessful, False if not"""
#     sql_Movie_Names = """INSERT INTO Movie_Names(Title,Distributor,Genre,Director) VALUES(%s, %s, %s, %s)"""
#     cur.execute(sql_Movie_Names,(title, distributor,genre,director))
#     sql_Movie_Numbers = """INSERT INTO Movie_Numbers(Title,US_Gross,Rating_IMDB,Rating_Rotten_Tomatoes) VALUES(%s, %s, %s, %s)"""
#     cur.execute(sql_Movie_Numbers,(title, us_gross,float(rating_imdb),float(rating_rotten_tomatoes)))
#     conn.commit()
#     return True

compound_counter = 1
for diction in compound_dictions_tuple:
    try:
        insert_compounds(diction["Name"],diction["Molecular_Weight"],diction["Smile"],diction["Price"],diction["Institution"],diction["Address"],diction["Url"], conn, cur) # Here: passing in actual conn and cur that exist
        print("{} Success adding a compound to SQL: {}".format(compound_counter,diction["Name"]))
        compound_counter += 1
    except Exception as inst:
        print("Failed adding a compound, check problem")
        print(inst)
        pass

protein_counter = 1
for diction in protein_dictions_tuple:
    try:
        insert_proteins(diction["Name"],diction["Molecular_Weight"],diction["Polymer_Length"],diction['Resolution'],diction['Polymer_Description'],diction["Price"],diction["Institution"],diction["Address"],diction["Url"], conn, cur) # Here: passing in actual conn and cur that exist
        print("{} Success adding a protein to SQL: {}".format(protein_counter,diction["Name"]))
        protein_counter += 1
    except Exception as inst:
        print("Failed adding a protein, check problem")
        print(inst)
        pass
