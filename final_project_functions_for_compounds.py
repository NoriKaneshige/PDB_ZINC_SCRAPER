from bs4 import BeautifulSoup
import requests
# from secrets import google_places_key
from advanced_expiry_caching import *
from final_project_class import *
import json
import sys
import csv
csv.field_size_limit(100000000)

# """Google Places API"""
# Places_API_key = 'AIzaSyCiTClfVeCIzLFeSUhov3-7e0Y89kWB07I'
# """for plotly,mapbox"""
# import plotly
# plotly.tools.set_credentials_file(username='nori-kaneshige', api_key='0fNsdJGLmxNwbfBL0l8f')
# import plotly.plotly as py
# import plotly.graph_objs as go
# mapbox_access_token = 'pk.eyJ1Ijoibm9yaS1rYW5lc2hpZ2UiLCJhIjoiY2pvbmJ1ZnB6MWE1ZjN2bnZ5ZXFpYzUzNSJ9.3wRYA_HNrpFi9tw1OullOg'
# """this is the end of setting for plotly"""

CACHE_FILE = "final_project_cache.json"

def get_data_of_each_compound(unique_url):
	c1 = Cache(CACHE_FILE)
	compound_inst_lst = []
	resp = c1.cache_diction.get(unique_url)
	soup = BeautifulSoup(resp,'html.parser')
	#get url info for each comp in a page
	compounds_block_inst = soup.find('div',id='print')
	compound_lst_inst = compounds_block_inst.find_all('div',class_='col-xs-6')

	for el in compound_lst_inst:
		compound_href = el.find('a')['href']
		try:
			compound_zinc_id = el.find('a').text
			#print(compound_zinc_id.split()[0])
		except Exception as inst:
			print('Zinc ID was not abtained!')
			print(inst)
		#generate unique_url_for_compound
		unique_url_for_each_compound = 'http://zinc15.docking.org'+str(compound_href)

		#get compound data and do caching
		if unique_url_for_each_compound in c1.cache_diction:
			#print("\n------------------------------\nunique url for {} in cache\n------------------------------".format(compound_zinc_id.split()[0]))
			resp = c1.cache_diction.get(unique_url_for_each_compound)

		else:
			#print("\n---------------------------------------------\nunique url for {} NOT in cache, so making requests!\n---------------------------------------------".format(compound_zinc_id.split()[0]))
			resp = requests.get(unique_url_for_each_compound).text
			#obj = json.loads(resp)
			#Here, I did not make json data, just stored text data, is this OK?
			c1.cache_diction[unique_url_for_each_compound] = resp
			c1.set(unique_url_for_each_compound,resp)

		#get neccessary information of each compound
		try:
			soup = BeautifulSoup(resp,'html.parser')
			name = soup.find('div',class_='col-sm-9').find('a').text.split()[0]
			molecular_weight = soup.find('tbody').find_all('td')[3].text
			smile = soup.find('div',class_='input-sm').find('input')['value']
			logp = soup.find('tbody').find_all('td')[4].text
			tpsa = soup.find('div',class_='protomers').find_all('td')[4].text
			structure = soup.find('div',class_='col-sm-3').find('img')['src']
			compound_inst = Compound(name,molecular_weight,smile,logp,tpsa,structure)
			compound_inst_lst.append(compound_inst)
			#generate a compound instance and make a list of compound instances
		except Exception as inst:
			pass
			#print(inst)
	return compound_inst_lst

def get_data_from_each_zinc_page(num_of_pages):
	all_compounds_inst_lst = []

	c1 = Cache(CACHE_FILE)
	page_counter = 1
	while page_counter <= num_of_pages:
		for i in range(int(num_of_pages)):
			unique_url = "http://zinc15.docking.org/substances/?page="+str(page_counter)
			if unique_url in c1.cache_diction:
				print("\n------------------------------\nData from Zinc page {} in cache\n------------------------------".format(page_counter))
				resp = c1.cache_diction.get(unique_url)
				page_counter += 1
				for inst_el in get_data_of_each_compound(unique_url):
					all_compounds_inst_lst.append(inst_el)

			else:
				print("\n---------------------------------------------\nData from Zinc page {} NOT in cache, so making requests!\n---------------------------------------------".format(page_counter))
				resp = requests.get(unique_url).text
				#obj = json.loads(resp)
				#Here, I did not make json data, just stored text data, is this OK?
				c1.cache_diction[unique_url] = resp
				c1.set(unique_url,resp)
				page_counter += 1
				for inst_el in get_data_of_each_compound(unique_url):
					all_compounds_inst_lst.append(inst_el)
	return all_compounds_inst_lst

"""Generator expression is used in the function below"""
def get_zinc_compound_in_pdb(zinc_compound_inst_lst):
#read smile in pdb_csv file
	pdb_ligand_smile_id_lst_lst = []
	with open('PDB_ligands.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		#while line_count < 100:
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				pass
			elif line_count != 0:
				try:
					pdb_ligand_smile_id_lst = []
					pdb_ligand_smile_id_lst.append(row[5])
					pdb_ligand_smile_id_lst.append(row[0])
					pdb_ligand_smile_id_lst_lst.append(pdb_ligand_smile_id_lst)
					line_count += 1
					pass
				except Exception as inst:
					#print(inst)
					line_count += 1
					pass
#generator expression
	gen_exp = (el[1] for zinc_comp in zinc_compound_inst_lst for el in pdb_ligand_smile_id_lst_lst if el[0] == zinc_comp.smile)
	if list(gen_exp):
		print(list(gen_exp))
		print('Go search the fetched PDB ids in PDB site!')
	else:
		print('No match in between zinc compounds and PDB ligands!!!')

	return list(gen_exp)

#print(len(get_zinc_compound_in_pdb(get_data_from_each_zinc_page(1))))
#print(get_data_from_each_zinc_page(1)[0].tpsa) #cache is working!
# print(get_data_from_each_zinc_page(1)[0].tpsa[4].text)
# print(get_data_from_each_zinc_page(1)[0].logp)
# print(get_data_from_each_zinc_page(1)[0].structure)
#print(len(get_data_from_each_zinc_page(1)))
#print(get_data_from_each_zinc_page(1)[0].smile)
# for el in get_data_from_each_zinc_page(1)[0].tpsa:
# 	print(type(el))

# counter = 1
# for el in get_data_from_each_zinc_page(1)[0].tpsa:
# 	print(el)
# 	print(counter)
# 	print('---------------------')
# 	counter += 1

#print(len(get_data_from_each_zinc_page(1)))

# for el in get_data_from_each_zinc_page(1):
# 	print(el.mw)
# for el in get_data_from_each_zinc_page(1):
# 	print(el.tpsa)
# for el in get_data_from_each_zinc_page(1):
# 	print(el.logp)
