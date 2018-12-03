from bs4 import BeautifulSoup
import requests
# from secrets import google_places_key
from advanced_expiry_caching import *
from final_project_class import *
import json

CACHE_FILE = "final_project_cache.json"

def get_human_pdb_protein_ids():

	c1 = Cache(CACHE_FILE)
	unique_url = 'http://www.rcsb.org/pdb/resultsV2/sids.jsp?qrid=3BB4340C'
	if unique_url in c1.cache_diction:
		print("\n------------------------------\nPDB ID Data in cache\n------------------------------")
		resp = c1.cache_diction.get(unique_url)
	else:
		print("\n---------------------------------------------\nPDB ID Data NOT in cache, so making requests!\n---------------------------------------------")
		resp = requests.get(unique_url).text
		#obj = json.loads(resp)
		#Here, I did not make json data, just stored text data, is this OK?
		c1.cache_diction[unique_url] = resp
		c1.set(unique_url,resp)

	soup = BeautifulSoup(resp,'html.parser')
	pdb_id_human_lst = list(soup)[0].split('\n')

	return pdb_id_human_lst

#get_human_pdb_protein_ids()


def get_protein_info(num_of_protein):
	protein_inst_list = []
	c1 = Cache(CACHE_FILE)
	base_url = 'https://www.rcsb.org/pdb/rest/describeMol?structureId='
	for id_el in get_human_pdb_protein_ids()[:num_of_protein]:
		unique_url = base_url+str(id_el)
		if unique_url in c1.cache_diction:
			print("\n------------------------------\nData of {} in cache\n------------------------------".format(id_el))
			resp = c1.cache_diction.get(unique_url)
		else:
			print("\n---------------------------------------------\nData of {} NOT in cache, so making requests!\n---------------------------------------------".format(id_el))
			resp = requests.get(unique_url).text
			#obj = json.loads(resp)
			#Here, I did not make json data, just stored text data, is this OK?
			c1.cache_diction[unique_url] = resp
			c1.set(unique_url,resp)
		soup = BeautifulSoup(resp,'html.parser')
		name = soup.find('structureid')['id']
		molecular_weight_and_length_inst_lst = soup.find('structureid').find_all('polymer')
		mw_lst = []
		polymer_length_lst = []
		for el in molecular_weight_and_length_inst_lst:
			mw_lst.append(el['weight'])
			polymer_length_lst.append(el['length'])
		protein_inst = Protein(name,mw_lst,polymer_length_lst)
		protein_inst_list.append(protein_inst)
	return protein_inst_list

print(len(get_protein_info(1000)))
