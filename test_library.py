import easyGlobalVariable as gv
import unittest
import os
import pickle

class TestEasyGlobalVariable(unittest.TestCase):
    def setUp(self):
        # Clear globals before each test
        from easyGlobalVariable.core import gv_table_globals
        gv_table_globals.clear()

    def tearDown(self):
        # Cleanup files
        for f in ['test_save.pkl']:
            if os.path.exists(f):
                os.remove(f)

    def test_set_get_variable(self):
        gv['test_var'] = 'testing'
        self.assertEqual(gv['test_var'], 'testing')

    def test_get_type(self):
        gv['int_var'] = 123
        self.assertEqual(type(gv['int_var']), int)

    def test_store_function(self):
        def my_func():
            return "hello"
        gv['my_func'] = my_func
        retrieved_func = gv['my_func']
        self.assertEqual(retrieved_func(), "hello")

    def test_delete_methods(self):
        gv['to_delete'] = 1
        gv.delete('to_delete')
        with self.assertRaises(KeyError):
            _ = gv['to_delete']

        gv['to_del'] = 1
        del gv['to_del']
        with self.assertRaises(KeyError):
            _ = gv['to_del']

    def test_startswith(self):
        gv['prefix_1'] = 1
        gv['prefix_2'] = 2
        gv['other'] = 3
        subset = gv.startswith('prefix_')
        self.assertEqual(len(subset.data), 2)
        self.assertIn('prefix_1', subset.data)
        self.assertIn('prefix_2', subset.data)
        self.assertNotIn('other', subset.data)

    def test_endswith(self):
        gv['file1.txt'] = 1
        gv['file2.log'] = 2
        gv['file3.txt'] = 3
        subset = gv.endswith('.txt')
        self.assertEqual(len(subset.data), 2)
        self.assertIn('file1.txt', subset.data)
        self.assertIn('file3.txt', subset.data)

    def test_contains(self):
        gv['ab_mid_cd'] = 1
        gv['xy_mid_zw'] = 2
        gv['none'] = 3
        subset = gv.contains('_mid_')
        self.assertEqual(len(subset.data), 2)
        self.assertIn('ab_mid_cd', subset.data)

    def test_save_load(self):
        gv['save_me'] = 'important'
        gv['skip_me'] = 'ignore'
        
        # Save only 'save_me'
        gv.startswith('save_').save('test_save.pkl')
        
        # Clear and load
        from easyGlobalVariable.core import gv_table_globals
        gv_table_globals.clear()
        
        gv.load('test_save.pkl')
        self.assertEqual(gv['save_me'], 'important')
        with self.assertRaises(KeyError):
            _ = gv['skip_me']

if __name__ == '__main__':
    unittest.main()
