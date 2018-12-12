from final_project_functions_for_sql import *


# get_compound_data_and_store_in_SQL(1)
# get_protein_data_and_store_in_SQL(1000,10,2)
#plot_compounds_plotly(get_data_from_each_zinc_page(1))
# open_zinc_site('zinc76')
# open_pdb_site('5Y64')

"""return all info from Compounds"""
# cur.execute("SELECT * FROM Compounds")
# print(cur.fetchone())
"""return all info from Proteins"""
# cur.execute("SELECT * FROM Proteins")
# print(cur.fetchone())
"""return all info from Proteins2"""
# cur.execute("SELECT * FROM Proteins2")
# print(cur.fetchone())
"""return only Name info from Proteins"""
# cur.execute("SELECT Name FROM Proteins WHERE Polymer_Length <= 4")
# print(cur.fetchall())
"""return only Name info from Proteins"""
# cur.execute("SELECT Name FROM Proteins WHERE Polymer_Length <= 4")
# for el in cur.fetchall():
#     print("PDB_ID: {}".format(el))
"""return only Name info from Compounds"""
# cur.execute("SELECT Name FROM Compounds WHERE Molecular_Weight <= 250")
#print(cur.fetchall())
# for el in cur.fetchall():
#     print("Zinc_ID: {}".format(el))
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


play_again = 'y'
while play_again == 'y':
	command_input = input('\n\nHello! Please explore Zinc molecule site and Protein Data Bank! Those are commands you can input! \n\n*Zinc\n*PDB\n*exit\n*help\n\nPlease input a command here: ')
	if command_input.lower() == 'zinc':
		page_input = input('How many pages do you want to scrape?\nPlease type the number of page here - e.g. 1: ')
		# for el in get_compound_data_and_store_in_SQL(int(page_input)):
		# 	print(el.name)
		inst_lst = get_compound_data_and_store_in_SQL(int(page_input))
		command_input_2 = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*ListALL\n*Query\n*exit\n*help\n\nPlease input a command here: ')
		if command_input_2.lower() == 'plotall':
			plot_compounds_plotly(inst_lst)
		elif command_input_2.lower() == 'listall':
			for el in inst_lst:
				print(el.name)
		elif command_input_2.lower() == 'query':
			mw_lowest_input = input('Please input the lowest molecular weight here: ')
			mw_highest_input = input('Please input the highest molecular weight here: ')
			cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
			id_lst = []
			for el in cur.fetchall():
				print("Zinc_ID: {}".format(el))
				id_lst.append(''.join(el))
			gen_exp = (''.join(list(el.name)) for el in inst_lst)
			# print(gen_exp)
			# print(id_lst)
			list_comp_min_max = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
			#list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
			#somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
			plot_compounds_plotly(list_comp_min_max)
		else:
			pass
		command_input_2 = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Z\n*SearchAgain\n*exit\n*help\n\nPlease input a command here: ')
		if command_input_2.lower() == 'plotall':
			gen_exp = (el for cur_zinc_id in cur.fetchall() for el in inst_lst if list(el.name) == cur_zinc_id)
			for el in gen_exp:
				print(el)
			#plot_compounds_plotly(inst_lst)
		else:
			print("See you2!")
			play_again = 'n'
	else:
		print("See you!")
		play_again = 'n'

# inst_lst = get_compound_data_and_store_in_SQL(1)
# cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= 200) AND (Molecular_Weight <= 250)")
# id_lst = []
# for el in cur.fetchall():
# 	print("Zinc_ID: {}".format(el))
# 	id_lst.append(''.join(el))
# #gen_exp = (el for cur_zinc_id in cur.fetchall() for el in inst_lst if list(el.name) == cur_zinc_id)
# #lst_comp = [el for cur_zinc_id in cur.fetchall() for el in get_compound_data_and_store_in_SQL(1) if list(el.name) == cur_zinc_id]
# list_comp = [''.join(list(el.name)) for el in inst_lst]
# print(list_comp)
# print(id_lst)
#
# list_comp_2 = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
# print(len(list_comp_2))
# print(len(inst_lst))
# for el in list_comp_2:
# 	print(el.name)


# inst_lst = get_compound_data_and_store_in_SQL(1)
# cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= 200) AND (Molecular_Weight <= 250)")
# id_lst = []
# for el in cur.fetchall():
# 	print("Zinc_ID: {}".format(el))
# 	id_lst.append(''.join(el))
#gen_exp = (el for cur_zinc_id in cur.fetchall() for el in inst_lst if list(el.name) == cur_zinc_id)
#lst_comp = [el for cur_zinc_id in cur.fetchall() for el in get_compound_data_and_store_in_SQL(1) if list(el.name) == cur_zinc_id]
# gen_exp = (''.join(list(el.name)) for el in inst_lst)
# print(gen_exp)
# print(id_lst)

# gen_exp_2 = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
# print(len(gen_exp_2))
# print(len(inst_lst))

# for el in gen_exp_2:
# 	print(float(el.mw))
# 	print(int(el.tpsa))
# 	print(float(el.logp))
# 	print(el.structure)

# plot_compounds_plotly(gen_exp_2)
#x,y,z,info= [float(el.mw) for el in gen_exp_2],[int(el.tpsa) for el in gen_exp_2],[float(el.logp) for el in gen_exp_2],[el.structure for el in gen_exp_2]

# x = [float(el.mw) for el in gen_exp_2]


	#
	#     counter = 1
	# 	for el_inst in get_sites_for_state(state_part.lower()):
	# 		print(str(counter)+': '+str(el_inst))
	# 		counter += 1
	# 	search_again = 'y'
	# 	while search_again == 'y':
	# 		look_up = input('\n\nThose are commands you can input now! \n\n*nearby <result_number> - e.g. nearby 2\n*map - e.g. map\n*exit\n*help\n\nPlease input a command here: ')
	# 		try:
	# 			look_up_number = look_up[-1]
	# 			look_up_num_int = int(look_up_number)
	# 		except:
	# 			look_up_num_int = 99
	# 			pass
	# 		if look_up_num_int in range(int(len(get_sites_for_state(state_part.lower())))+1):
	# 			try:
	# 				get_nearby_places_for_site(get_sites_for_state(state_part.lower())[look_up_num_int-1])
	# 				search_again = 'n'
	# 				look_up_2 = input('\n\nThose are commands you can input now! \n\n*map - e.g. map\n*other search\n*exit\n*help\n\nPlease input a command here: ')
	# 			except:
	# 				look_up_2 = 'xxx'
	# 				pass
	# 			if look_up_2 == 'map':
	# 				try:
	# 					plot_nearby_for_site(get_sites_for_state(state_part.lower())[look_up_num_int-1])
	# 					pass
	# 				except:
	# 					print('\n\n------------------------------------------\nSorry! The nearby location information of {} for the map generation was not obtainable!\nPlease try other location search!\n------------------------------------------'.format(get_sites_for_state(state_part.lower())[look_up_num_int-1]))
	# 					pass
	# 			elif look_up_2 == 'other search':
	# 				pass
	# 			elif look_up_2 == 'exit':
	# 				play_again = 'n'
	# 				play_again = 'n'
	# 				break
	# 			elif look_up_2 == 'help':
	# 				print('\n\n------------------------------------------\n1) When you type "map", you will see nearby park locations in the map! You can go to YOUR plotly site to see the map! \n\n2) When you type "other search", you can continue to search other states!\n\n3) When you type "exit", you will get out from this program! \n\n4) When you type "help", you will see command instructions like this!\n------------------------------------------\n\nPlease choose state park number again to search nearby places!')
	# 				search_again = 'y'
	# 				pass
	# 			elif look_up_2 == 'xxx':
	# 				print('\n\n------------------------------------------\nSorry! The nearby location data for {} ({}) was not obtainable!\nPlease choose other sites!\n------------------------------------------'.format(get_sites_for_state(state_part.lower())[look_up_num_int-1].name,get_sites_for_state(state_part.lower())[look_up_num_int-1].type))
	# 				pass
	# 			else:
	# 				print('something wrong here. Please input a valid number!')
	# 				search_again = input('Do you still want to search state parks of {}(y/n)?: '.format(state_part.upper()))
	# 				if search_again != 'y':
	# 					pass
	# 				else:
	# 					search_again = 'y'
	# 					pass
	#
	# 		elif look_up == 'map':
	# 			plot_sites_for_state(state_part.lower())
	# 			pass
	# 		elif look_up == 'exit':
	# 			play_again = 'n'
	# 			break
	# 		elif look_up == 'help':
	# 			print('\n\n------------------------------------------\n1) When you type a displayed state park number with "nearby" command such as "nearby 2", you will see nearby parks around the state park you specified!\n\n2) When you type "map", you will see state park locations in the map! You can go to YOUR plotly site to see the map! \n\n3) When you type "exit", you will get out from this program! \n\n4) When you type "help", you will see command instructions like this!\n------------------------------------------')
	# 			pass
	# 		else:
	# 			print('something wrong here. Please input a valid number!')
	# 			search_again = input('Do you still want to search state parks of {}(y/n)?: '.format(state_part.upper()))
	# 			if search_again != 'y':
	# 				pass
	# 			else:
	# 				search_again = 'y'
	# 				pass
	# 	#play_again = input('Do you want to take a look at other states(y/n)?:')
	# 	if play_again != 'y':
	# 		print('See you!')
	# 		break
	# 	else:
	# 		pass
	# elif command_input == 'exit':
	# 	play_again = 'n'
	# 	print('See you!')
	# 	break
	#
	# elif command_input == 'help':
	# 	print('\n\n------------------------------------------\n1) When you type any two letter state abbreviation with "list" command such as "list mi", you will see national state parks in the state you typed!\n\n2) When you type "exit", you will get out from this program! \n\n3) When you type "help", you will see command instructions like this!\n------------------------------------------')
	# 	pass
	# else:
	# 	print('\n\n------------------------------------------\nPlease input a valid abbreviation!!!\n------------------------------------------')
	# 	pass
