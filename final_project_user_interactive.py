from final_project_functions_for_sql import *

play_again = 'y'
while play_again == 'y':

	command_input = input('\n\nHello! Please explore Zinc molecule site and Protein Data Bank! Those are commands you can input! \n\n*Zinc\n*PDB\n*exit\n*help\n\nPlease input a command here: ')
	if command_input.lower() == 'zinc':
		page_input = input('How many pages do you want to scrape?\nZinc has tons of pages, so Please input 1 for now!\nPlease type the number of page here - e.g. 1: ')
		# for el in get_compound_data_and_store_in_SQL(int(page_input)):
		# 	print(el.name)
		try:
			inst_lst = get_compound_data_and_store_in_SQL(int(page_input))
		except Exception as inst:
			print(inst)
			print('Sorry! Please start over again and type a valid input!')
			break
		command_input_zinc = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*ListALL\n*Query\n*FindPDB\n*exit\n\nPlease input a command here: ')
		if command_input_zinc.lower() == 'plotall':
			plot_compounds_plotly(inst_lst)
			command_input_zinc_plotall = input('\n\nThose are commands you can type now! \n\n*ListALL\n*Query\n*exit\n\nPlease input a command here: ')
			if command_input_zinc_plotall.lower() == 'listall':
				for el in inst_lst:
					print(el.name)
				command_input_zinc_plotall_listall = input('\n\nThose are commands you can type now! \n\n*Query\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
				if command_input_zinc_plotall_listall.lower() == 'query':
					mw_lowest_input = input('Please input the lowest molecular weight here e.g. 200: ')
					mw_highest_input = input('Please input the highest molecular weight here e.g. 250: ')
					try:
						cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
						pass
					except Exception as inst:
						print(inst)
						print('Sorry! Please start over again and type a valid input!')
						break
					#cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
					id_lst = []
					print('Molecules whose molecular weight is between {} and {}!'.format(mw_lowest_input,mw_highest_input))
					for el in cur.fetchall():
						#print("Zinc_ID: {}".format(el))
						id_lst.append(''.join(el))
						print(''.join(el))
					gen_exp = (''.join(list(el.name)) for el in inst_lst)
					# print(gen_exp)
					# print(id_lst)
					list_comp_min_max = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
					#list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
					#somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
					command_input_zinc_plotall_listall_query = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
					if command_input_zinc_plotall_listall_query.lower() == 'plotall':
						plot_compounds_plotly(list_comp_min_max)
						command_input_zinc_plotall_listall_query_plotall = input('\n\nThose are commands you can type now! \n\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
						if command_input_zinc_plotall_listall_query_plotall.split()[0].lower() == 'look':
							el_counter = 0
							for el in command_input_zinc_plotall_listall_query_plotall.split():
								if el_counter == 0:
									el_counter += 1
									pass
								else:
									open_zinc_site(str(el))
									el_counter += 1
							print('Thank you for searching! This is the end of compound search!')
							break
						elif command_input_zinc_plotall_listall_query_plotall.lower() == 'exit':
							print('See you!')
							break
						else:
							print('Sorry! Please start over again and type a valid input!')
							break
					elif command_input_zinc_plotall_listall_query.split()[0].lower() == 'look':
						el_counter = 0
						for el in command_input_zinc_plotall_listall_query.split():
							if el_counter == 0:
								el_counter += 1
								pass
							else:
								open_zinc_site(str(el))
								el_counter += 1
						print('Thank you for searching! This is the end of compound search!')
						break
					elif command_input_zinc_plotall_listall_query.lower() == 'exit':
						print('See you!')
						break
					else:
						print('Sorry! Please start over again and type a valid input!')
						break
				elif command_input_zinc_plotall_listall.split()[0].lower() == 'look':
					el_counter = 0
					for el in command_input_zinc_plotall_listall.split():
						if el_counter == 0:
							el_counter += 1
							pass
						else:
							open_zinc_site(str(el))
							el_counter += 1
					print('Thank you for searching! This is the end of compound search!')
					break
				elif command_input_zinc_plotall_listall.lower() == 'exit':
					print('See you!')
					break
				else:
					print('Sorry! Please start over again and type a valid input!')
					break
			elif command_input_zinc_plotall.lower() == 'query':
				mw_lowest_input = input('Please input the lowest molecular weight here e.g. 200: ')
				mw_highest_input = input('Please input the highest molecular weight here e.g. 250: ')
				cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
				id_lst = []
				print('Molecules whose molecular weight is between {} and {}!'.format(mw_lowest_input,mw_highest_input))
				for el in cur.fetchall():
					#print("Zinc_ID: {}".format(el))
					id_lst.append(''.join(el))
					print(''.join(el))
				gen_exp = (''.join(list(el.name)) for el in inst_lst)
				# print(gen_exp)
				# print(id_lst)
				list_comp_min_max = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
				#list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
				#somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
				command_input_zinc_plotall_query = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
				if command_input_zinc_plotall_query.lower() == 'plotall':
					plot_compounds_plotly(list_comp_min_max)
					command_input_zinc_plotall_query_plotall = input('\n\nThose are commands you can type now! \n\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
					if command_input_zinc_plotall_query_plotall.split()[0].lower() == 'look':
						el_counter = 0
						for el in command_input_zinc_plotall_query_plotall.split():
							if el_counter == 0:
								el_counter += 1
								pass
							else:
								open_zinc_site(str(el))
								el_counter += 1
						print('Thank you for searching! This is the end of compound search!')
						break
					else:
						print('See you for now!')
						break
				elif command_input_zinc_plotall_query.split()[0].lower() == 'look':
					el_counter = 0
					for el in command_input_zinc_plotall_query.split():
						if el_counter == 0:
							el_counter += 1
							pass
						else:
							open_zinc_site(str(el))
							el_counter += 1
					print('Thank you for searching! This is the end of compound search!')
					break

				else:
					print('See you working now!')
					break
			else:
				print('Sorry! Please type a valid input! Could you start over again?')
				break
		elif command_input_zinc.lower() == 'listall':
			for el in inst_lst:
				print(el.name)
			command_input_zinc_listall = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Query\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
			if command_input_zinc_listall.lower() == 'plotall':
				plot_compounds_plotly(inst_lst)
				command_input_zinc_listall_plotall = input('\n\nThose are commands you can type now! \n\n*Query\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
				if command_input_zinc_listall_plotall.lower() == 'query':
					mw_lowest_input = input('Please input the lowest molecular weight here e.g. 200: ')
					mw_highest_input = input('Please input the highest molecular weight here e.g. 250: ')
					cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
					id_lst = []
					print('Molecules whose molecular weight is between {} and {}!'.format(mw_lowest_input,mw_highest_input))
					for el in cur.fetchall():
						#print("Zinc_ID: {}".format(el))
						id_lst.append(''.join(el))
						print(''.join(el))
					gen_exp = (''.join(list(el.name)) for el in inst_lst)
					# print(gen_exp)
					# print(id_lst)
					list_comp_min_max = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
					#list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
					#somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
					command_input_zinc_listall_plotall_query = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
					if command_input_zinc_listall_plotall_query.lower() == 'plotall':
						plot_compounds_plotly(list_comp_min_max)
						command_input_zinc_listall_plotall_query_plotall = input('\n\nThose are commands you can type now! \n\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
						if command_input_zinc_listall_plotall_query_plotall.split()[0].lower() == 'look':
							el_counter = 0
							for el in command_input_zinc_listall_plotall_query_plotall.split():
								if el_counter == 0:
									el_counter += 1
									pass
								else:
									open_zinc_site(str(el))
									el_counter += 1
							print('Thank you for searching! This is the end of compound search!')
							break
						elif command_input_zinc_listall_plotall_query_plotall.lower() == 'exit':
							print('See you!')
							break
						else:
							print('Sorry! Please start over again and type a valid input!')
							break
					elif command_input_zinc_listall_plotall_query.split()[0].lower() == 'look':
						el_counter = 0
						for el in command_input_zinc_listall_plotall_query.split():
							if el_counter == 0:
								el_counter += 1
								pass
							else:
								open_zinc_site(str(el))
								el_counter += 1
						print('Thank you for searching! This is the end of compound search!')
						break
					elif command_input_zinc_listall_plotall_query.lower() == 'exit':
						print('See you!')
						break
					else:
						print('Sorry! Please start over again and type a valid input!')
						break
				elif command_input_zinc_listall_plotall.split()[0].lower() == 'look':
					el_counter = 0
					for el in command_input_zinc_listall_plotall.split():
						if el_counter == 0:
							el_counter += 1
							pass
						else:
							open_zinc_site(str(el))
							el_counter += 1
					print('Thank you for searching! This is the end of compound search!')
					break
				elif command_input_zinc_listall_plotall.lower() == 'exit':
					print('See you!')
					break
				else:
					print('Sorry! Please start over again and type a valid input!')
					break

			elif command_input_zinc_listall.lower() == 'query':
				mw_lowest_input = input('Please input the lowest molecular weight here e.g. 200: ')
				mw_highest_input = input('Please input the highest molecular weight here e.g. 250: ')
				cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
				id_lst = []
				print('Molecules whose molecular weight is between {} and {}!'.format(mw_lowest_input,mw_highest_input))
				for el in cur.fetchall():
					#print("Zinc_ID: {}".format(el))
					id_lst.append(''.join(el))
					print(''.join(el))
				gen_exp = (''.join(list(el.name)) for el in inst_lst)
				# print(gen_exp)
				# print(id_lst)
				list_comp_min_max = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
				#list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
				#somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
				command_input_zinc_listall_query = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
				if command_input_zinc_listall_query.lower() == 'plotall':
					plot_compounds_plotly(list_comp_min_max)
					command_input_zinc_listall_query_plotall = input('\n\nThose are commands you can type now! \n\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
					if command_input_zinc_listall_query_plotall.split()[0].lower() == 'look':
						el_counter = 0
						for el in command_input_zinc_listall_query_plotall.split():
							if el_counter == 0:
								el_counter += 1
								pass
							else:
								open_zinc_site(str(el))
								el_counter += 1
						print('Thank you for searching! This is the end of compound search!')
						break
					else:
						print('See you for now!')
						break
				elif command_input_zinc_listall_query.split()[0].lower() == 'look':
					el_counter = 0
					for el in command_input_zinc_listall_query.split():
						if el_counter == 0:
							el_counter += 1
							pass
						else:
							open_zinc_site(str(el))
							el_counter += 1
					print('Thank you for searching! This is the end of compound search!')
					break
				else:
					print('See you now working')
					break
			elif command_input_zinc_listall.split()[0].lower() == 'look':
				el_counter = 0
				for el in command_input_zinc_listall.split():
					if el_counter == 0:
						el_counter += 1
						pass
					else:
						open_zinc_site(str(el))
						el_counter += 1
				print('Thank you for searching! This is the end of compound search!')
				break
			elif command_input_zinc_listall.lower() == 'exit':
				print('See you!')
				break
			else:
				print('Sorry! Please start over again and type a valid input!')
				break

		elif command_input_zinc.lower() == 'query':
			mw_lowest_input = input('Please input the lowest molecular weight here e.g. 200: ')
			mw_highest_input = input('Please input the highest molecular weight here e.g. 250: ')
			try:
				cur.execute("SELECT Name FROM Compounds WHERE (Molecular_Weight >= {}) AND (Molecular_Weight <= {})".format(mw_lowest_input,mw_highest_input))
			except Exception as inst:
				print(inst)
				print('Sorry! Please start over again and type a valid input!')
				break
			id_lst = []
			print('Molecules whose molecular weight is between {} and {}!'.format(mw_lowest_input,mw_highest_input))
			for el in cur.fetchall():
				#print("Zinc_ID: {}".format(el))
				id_lst.append(''.join(el))
				print(''.join(el))
			gen_exp = (''.join(list(el.name)) for el in inst_lst)
			# print(gen_exp)
			# print(id_lst)
			list_comp_min_max = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
			#list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
			#somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
			command_input_zinc_query = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
			if command_input_zinc_query.lower() == 'plotall':
				plot_compounds_plotly(list_comp_min_max)
				command_input_zinc_query_plotall = input('\n\nThose are commands you can type now! \n\n*Look <Zinc_ID> - e.g. Look Zinc10 zinc15 zinc75\n*exit\n\nPlease input a command here: ')
				if command_input_zinc_query_plotall.split()[0].lower() == 'look':
					el_counter = 0
					for el in command_input_zinc_query_plotall.split():
						if el_counter == 0:
							el_counter += 1
							pass
						else:
							open_zinc_site(str(el))
							el_counter += 1
					print('Thank you for searching! This is the end of compound search!')
					break
				elif command_input_zinc_query_plotall.lower() == 'exit':
					print('See you!')
					break
				else:
					print('Sorry! Please start over again and type a valid input!')
					break
			elif command_input_zinc_query.split()[0].lower() == 'look':
				el_counter = 0
				for el in command_input_zinc_query.split():
					if el_counter == 0:
						el_counter += 1
						pass
					else:
						open_zinc_site(str(el))
						el_counter += 1
				print('Thank you for searching! This is the end of compound search!')
				break
			elif command_input_zinc_query.lower() == 'exit':
				print('See you!')
				break
			else:
				print('Sorry! Please start over again and type a valid input!')
				break
		elif command_input_zinc.lower() == 'findpdb':
			get_zinc_compound_in_pdb(inst_lst)
			print('Please run the program again for the next search!')
			play_again = 'n'
		elif command_input_zinc.lower() == 'exit':
			print('See you!')
			play_again = 'n'
		# elif command_input_zinc.lower() == 'help':
		# 	print('-------------------------------------------------\nPlotALL: You can make a scatter plot of compounds in plotly!')
		# 	print('-------------------------------------------------\nListALL: You can list all compounds!')
		# 	print('-------------------------------------------------\nQuery: You can sort compounds based on molecular weight!')
		else:
			print("\n---------------------------------\nPlease input a valid command!\nLets start all orver again!\n---------------------------------")
			#play_again = 'n'
			break
	elif command_input.lower() == 'pdb':
		num_proteins_input = input('How many PDB co-crystal protein structures do you want to get?\nPDB has over 40,000 human protein crystal structures, so Please input 1000 for now!\nPlease type the number of proteins here - e.g. 1000: ')
		length_of_peptide_input = input('How long is the maximum length of short peptides co-crystalized with proteins?\nMany proteins were co-crystalized with short peptides! Please input 10 for now!\nPlease type the maximum length of short peptides here - e.g. 10: ')
		resolution_input = input('How big is the maximum resolution?\nUsually proteins with less than 2 resolution are considered high resolution proteins! Please input 2 for now!\nPlease type the maximum resolution here - e.g. 2: ')

		inst_lst_pdb = get_protein_data_and_store_in_SQL(int(num_proteins_input),int(length_of_peptide_input),int(resolution_input))
		command_input_pdb = input('\n\nThose are commands you can type now! \n\n*ListALL\n*exit\n\nPlease input a command here: ')
		if command_input_pdb.lower() == 'listall':
			for el in inst_lst_pdb:
				print(el.name)
			command_input_pdb_listall = input('\n\nThose are commands you can type now! \n\n*Query\n*Look <PDB_ID> - e.g. Look 1A10 1C5L 1een\n*exit\n\nPlease input a command here: ')
			if command_input_pdb_listall.lower() == 'query':
				short_peptide_length_input = input('Please input the longest length of short peptides here: ')
				cur.execute("SELECT Name,Polymer_Description FROM Proteins WHERE Polymer_Length <= {}".format(short_peptide_length_input))
				id_lst_pdb = []
				print('Proteins whose length of co-crystalized short peptides is shorter than {}!'.format(short_peptide_length_input))
				for el in cur.fetchall():
					#print("Zinc_ID: {}".format(el))
					# id_lst_pdb.append(''.join(el))
					# print(''.join(el))
					print(el)
				# gen_exp = (''.join(list(el.name)) for el in inst_lst_pdb)
				# # print(gen_exp)
				# # print(id_lst)
				# list_comp_polymer_length = [el for zinc_id_max_min in id_lst for el in inst_lst if el.name == zinc_id_max_min]
				# #list_comp_min_max is a list of instances that sorted by sql query, min molecular_weight and max molecular_weight
				# #somehow, generator_expression doesn't generate plot in plotly, probably because data disappear
				# command_input_zinc_plotall_listall_query = input('\n\nThose are commands you can type now! \n\n*PlotALL\n*Look <Zinc_ID> - e.g. Look Zinc10\n*exit\n\nPlease input a command here: ')
				# if command_input_zinc_plotall_listall_query.lower() == 'plotall':
				# 	plot_compounds_plotly(list_comp_min_max)
				command_input_pdb_listall_query = input('\n\nThose are commands you can type now! \n\n*Look <PDB_ID> - e.g. Look 1A10 1C5L 1een\n*exit\n\nPlease input a command here: ')
				if command_input_pdb_listall_query.split()[0].lower() == 'look':
					el_counter = 0
					for el in command_input_pdb_listall_query.split():
						if el_counter == 0:
							el_counter += 1
							pass
						else:
							open_pdb_site(str(el))
							el_counter += 1
					print('Thank you for searching! This is the end of compound search!')
					break
				elif command_input_pdb_listall_query.lower() == 'exit':
					print('See you!')
					break
				else:
					print('Sorry! Please start over again and type a valid input!')
					break

			elif command_input_pdb_listall.split()[0].lower() == 'look':
				el_counter = 0
				for el in command_input_pdb_listall.split():
					if el_counter == 0:
						el_counter += 1
						pass
					else:
						open_pdb_site(str(el))
						el_counter += 1
				print('Thank you for searching! This is the end of compound search!')
				break
			elif command_input_pdb_listall.lower() == 'exit':
				print('See you!')
				break
			else:
				print('Sorry! Please start over again and type a valid input!')
				break
		elif command_input_pdb.lower() == 'exit':
			print('See you!')
			break
		else:
			print('Sorry! Please start over again and type a valid input!')
			break
	elif command_input.lower() == 'exit':
		print('See you!')
		play_again = 'n'
	elif command_input.lower() == 'help':
		print('-------------------------------------------------\nZinc: you can search and scrape compounds data from zinc!\nZINC is a free database of commercially-available compounds for virtual screening.\nZINC contains over 230 million purchasable compounds.\nZINC also contains over 750 million purchasable compounds you can search for analogs.')
		print('-------------------------------------------------\nPDB: you can search proteins in protein databank by using REAT API.\n147073 Biological Macromolecular Structures Enabling Breakthroughs in Research and Education!')
	else:
		print("\n---------------------------------\nPlease input a valid command!\n---------------------------------")
		#play_again = 'n'
		pass
