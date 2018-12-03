class Post():
	def __init__(self, name, molecular_weight, price, institution, address, url=None):
		self.name = name
		self.mw = molecular_weight
		self.institution = institution
		self.address = address
		self.price = price
		self.url = url

	def getName(self):
		return self.name

	def getMw(self):
		return self.mw

	def getInstitution(self):
		return self.institution

	def getAddress(self):
		return self.address

	def getUrl(self):
		return self.url

	def __str__(self):
		return "{} ({}): ${}".format(self.name,self.institution,self.price)
		#self.name+' ('+self.institution+'): '+self.price

class Compound(Post):
	def __init__(self, name, molecular_weight, smile, price='N/A', institution='Zinc', address='Zinc', url=None):
		super().__init__(name, molecular_weight, price, institution, address, url=None)
		self.smile = smile

	def getSmile(self):
		return self.smile

	def getStructure(self):
		pass

	def __str__(self):
		return "{} ({}): ${}: {}".format(self.name,self.institution,self.price,self.smile)

class Protein(Post):
	def __init__(self, name, molecular_weight, polymer_length, price='N/A', institution='PDB', address='PDB', url=None):
		super().__init__(name, molecular_weight, price, institution, address,  url=None)
		self.polymer_length = polymer_length

	def get_polymer_length(self):
		return self.polymer_length

	def getStructure(self):
		pass

	def __str__(self):
		return "{} ({}): ${}: {}".format(self.name,self.institution,self.price,self.polymer_length)

# p1 = Post("alcohol",35,"Umich","1431 McIntyre. St., Ann Arbor, MI",100)
# print(p1)
# print(p1.getName())
# c1 = Compound("water",18,"ccccccccccc@@@@@",0.1,"Umich","1431 McIntyre. St. Ann Arbor, MI")
# # print(c1)
# # print(c1.mw)
# # print(c1.smile)
# print(c1.getName())
# print(c1.getSmile())
# c1.getStructure()
# pro1 = Protein("STAT6",345674554,"aveaewofjapoefijaoewijfaoejf",2000,"Harvard U","Boston")
# # print(pro1.sequence)
# print(pro1.getName())
# print(pro1.getSequence())
# pro1.getStructure()
