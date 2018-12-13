from final_project_functions_for_sql import *
import unittest

print('\n\n--------------------------------------------------------------\nWarning: If data is not in cache, \nthis will take more than couple minutes to complete the testing!\nSorry for the inconvenience!\n--------------------------------------------------------------')

class TestCompound(unittest.TestCase):

    def setUp(self):
        self.compound_ex = Compound('ZINC7',250.00,'@@@',3.56,80,'http')

    def testCompoundInst(self):
        self.assertEqual(self.compound_ex.name, 'ZINC7')
        self.assertEqual(self.compound_ex.smile, '@@@')

    def testCompoundInstDefault(self):
        self.assertEqual(self.compound_ex.institution, 'UM')

class TestCompoundFunc(unittest.TestCase):

    def setUp(self):
        self.compound = Compound('test999',250.00,"COc1cc(cc(OC)c1OC)C(F)(F)C(=O)N1CCCC[C@H]1C(=O)O[C@@H](CCCc1ccccc1)CCCc1cccnc1 |r,@:12|",3.56,80,'http')

    def testTypeReturn(self):
        unique_url = "http://zinc15.docking.org/substances/?page=1"
        result = get_data_of_each_compound(unique_url)
        self.assertEqual(type(result),type([]))

    def testPdbCompoundSearch(self):
        unique_url = "http://zinc15.docking.org/substances/?page=1"
        comp_inst_lst = [self.compound]
        result = get_zinc_compound_in_pdb(comp_inst_lst)
        self.assertEqual(result,['001'])

class TestProtein(unittest.TestCase):

    def setUp(self):
        self.protein_ex = Protein('Z19A',11111,15,2.5,'KRAS')

    def testProteinInst(self):
        self.assertEqual(self.protein_ex.name, 'Z19A')
        self.assertEqual(self.protein_ex.polymer_resolution, 2.5)

    def testProteinInstDefault(self):
        self.assertEqual(self.protein_ex.institution, 'PDB')

class TestProteinFunc(unittest.TestCase):

    def testGetPdbId(self):
        result = get_human_pdb_protein_ids()
        self.assertEqual(type(result),type([]))

    def testGetProteinWithShortPeptide(self):
        result = get_protein_with_short_peptide(1000,10,2)
        result2 = result[0].name
        self.assertEqual(type(result),type([]))
        self.assertEqual(type(result2),type('abc'))

class TestSqlFunc(unittest.TestCase):

    def setUp(self):
        self.protein_ex = Protein('Z19A',11111,15,2.5,'KRAS')
        self.compound_ex = Compound('ZINC7',250.00,'@@@',3.56,80,'http')

    def testMakeProteinDictionaryLst(self):
        inst_lst = []
        for el in range(3):
            inst_lst.append(self.protein_ex)
        result = make_protein_dictionary_lst(inst_lst)
        self.assertEqual(type(result),type(()))
        self.assertEqual(len(result),len((1,2,3)))

    def testMakeCompoundDictionaryLst(self):
        inst_lst = []
        for el in range(3):
            inst_lst.append(self.compound_ex)
        result = make_compound_dictionary_lst(inst_lst)
        self.assertEqual(type(result),type(()))
        self.assertEqual(len(result),len((1,2,3)))

if __name__ == "__main__":
    unittest.main(verbosity=2)
