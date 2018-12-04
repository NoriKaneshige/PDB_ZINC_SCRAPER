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
		#print("\n------------------------------\nPDB ID Data in cache\n------------------------------")
		resp = c1.cache_diction.get(unique_url)
	else:
		#print("\n---------------------------------------------\nPDB ID Data NOT in cache, so making requests!\n---------------------------------------------")
		resp = requests.get(unique_url).text
		#obj = json.loads(resp)
		#Here, I did not make json data, just stored text data, is this OK?
		c1.cache_diction[unique_url] = resp
		c1.set(unique_url,resp)

	soup = BeautifulSoup(resp,'html.parser')
	pdb_id_human_lst = list(soup)[0].split('\n')

	return pdb_id_human_lst

#get_human_pdb_protein_ids()


def get_protein_with_short_peptide(num_of_protein_to_check,length_of_short_peptide,resolution_limit):
	protein_inst_list = []
	c1 = Cache(CACHE_FILE)
	base_url = 'https://www.rcsb.org/pdb/rest/describeMol?structureId='
	base_url_for_resolution = 'https://www.rcsb.org/pdb/rest/describePDB?structureId='
	for id_el in get_human_pdb_protein_ids()[:num_of_protein_to_check]:

		unique_url = base_url+str(id_el)
		if unique_url in c1.cache_diction:
			#print("\n------------------------------\nData of {} in cache\n------------------------------".format(id_el))
			resp = c1.cache_diction.get(unique_url)
		else:
			#print("\n---------------------------------------------\nData of {} NOT in cache, so making requests!\n---------------------------------------------".format(id_el))
			resp = requests.get(unique_url).text
			#obj = json.loads(resp)
			#Here, I did not make json data, just stored text data, is this OK?
			c1.cache_diction[unique_url] = resp
			c1.set(unique_url,resp)
		soup = BeautifulSoup(resp,'html.parser')
		molecular_weight_and_length_inst_lst = soup.find('structureid').find_all('polymer')

		unique_url_for_resolution = base_url_for_resolution+str(id_el)
		if unique_url_for_resolution in c1.cache_diction:
			#print("\n------------------------------\nResolution Data of {} in cache\n------------------------------".format(id_el))
			resp_res = c1.cache_diction.get(unique_url_for_resolution)
		else:
			#print("\n---------------------------------------------\nResolution Data of {} NOT in cache, so making requests!\n---------------------------------------------".format(id_el))
			resp_res = requests.get(unique_url_for_resolution).text
			#obj = json.loads(resp)
			#Here, I did not make json data, just stored text data, is this OK?
			c1.cache_diction[unique_url_for_resolution] = resp_res
			c1.set(unique_url_for_resolution,resp_res)
		soup_res = BeautifulSoup(resp_res,'html.parser')

		try:
			polymer_description = soup.find('macromolecule')['name']
			resolution = soup_res.find('pdb')['resolution']
			peptide_length_lst = []
			for el in molecular_weight_and_length_inst_lst:
				peptide_length_lst.append(int(el['length']))
			if min(peptide_length_lst) <= int(length_of_short_peptide):
				if float(resolution) <= float(resolution_limit):
					name = soup.find('structureid')['id']
					molecular_weight = el['weight']
					polymer_length = el['length']
					resolution = soup_res.find('pdb')['resolution']
					polymer_description = soup.find('macromolecule')['name']
					protein_inst = Protein(name,molecular_weight,polymer_length,resolution,polymer_description)
					protein_inst_list.append(protein_inst)
				else:
					pass
			else:
				pass
		except Exception as inst:
			#print(inst,id_el)
			pass

	return protein_inst_list

# for el in get_protein_with_short_peptide(1000,10,2):
# 	print(el)
