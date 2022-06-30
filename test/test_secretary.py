import unittest

from parameterized import parameterized

from test.database_4_tests import t_documents, const_t_documents, t_directories
from src.secretary import search_in_docs, search_on_shelf, list_of_docs, add_doc_on_shelf, add_doc, delete_from_shelf
from src.secretary import move_docs_on_shelfs, make_new_shelf


class TestFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # before all tests
        print("Start test")

    @classmethod
    def tearDownClass(cls) -> None:  # after all tests
        print("End tests")

    @parameterized.expand(
        [
            ('number', '11-2', 'name', const_t_documents, 'The document owner is Геннадий Покемонов'),
            ('number', '321', 'name', const_t_documents, 'No document found.'),
            ('number', '2207 876234', 'name', const_t_documents, 'The document owner is Василий Гупкин')
        ]
    )
    def test_search_in_docs(self, key_1, val_1, key_2, doc, result):
        self.assertMultiLineEqual(search_in_docs(key_1, val_1, key_2, *doc), result)

    @parameterized.expand(
        [
            ('11-2', t_directories, 'the document is on shelf #1'),
            ('321', t_directories, 'No document found.')
        ]
    )
    def test_search_on_shelf(self, doc_num, directories, result):
        self.assertMultiLineEqual(search_on_shelf(doc_num, directories), result)

    @parameterized.expand(
        [
            (const_t_documents, ['passport "2207 876234" Василий Гупкин',
                                 'invoice "11-2" Геннадий Покемонов',
                                 'insurance "10006" Аристарх Павлов']),
            ([], ['No documents found.'])
        ]
    )
    def test_list_of_docs(self, doc_list, result):
        self.assertListEqual(list_of_docs(*doc_list), result)

    @parameterized.expand(
        [
            ('1111', '1', t_directories, '1')
        ]
    )
    def test_add_doc_on_shelf(self, doc_num, shelf_num, directories, result):
        self.assertEqual(add_doc_on_shelf(doc_num, shelf_num, directories), result)

    @parameterized.expand(
        [
            ('123', '1', t_directories, '1'),
            # ('123', '-1', t_directories, 0) # Needs to push batton 'q'
        ]
    )
    def test_add_doc_on_shelf(self, doc_num, shelf_num, directories, result):
        self.assertEqual(add_doc_on_shelf(doc_num, shelf_num, directories), result)

    @parameterized.expand(
        [
            ('123', 'Pass', 'Yuriy Yojigiff', '1', t_directories, t_documents,
             'The document successfully added on shelf #1.')
        ]
    )
    def test_add_doc(self, doc_num, doc_type, doc_owner, shelf_num, directories, documents, result):
        self.assertMultiLineEqual(add_doc(doc_num, doc_type, doc_owner, shelf_num, directories, documents), result)

    @parameterized.expand(
        [
            ('1106', t_directories, t_documents, 'No documents found.'),
            ('2207 876234', t_directories, t_documents, 'The document number 2207 876234 successfully removed.')
        ]
    )
    def test_delete_from_shelf(self, doc_num, directories, doc, result):
        self.assertMultiLineEqual(delete_from_shelf(doc_num, directories, doc), result)

    @parameterized.expand(
        [
            ('106', '2', t_directories, 'No document found.'),
            ('10006', '1', t_directories, 'the document is on shelf #1')
        ]
    )
    def test_move_docs_on_shelfs(self, doc_num, shelf_num, directories, result):
        self.assertMultiLineEqual(move_docs_on_shelfs(doc_num, shelf_num, directories), result)

    @parameterized.expand(
        [
            ('2', t_directories, 'The shell number 2 exist! No changes.'),
            ('5', t_directories, 'Added a new shelf #5.')
        ]
    )
    def test_make_new_shelf(self, shelf_num, directories, result):
        self.assertMultiLineEqual(make_new_shelf(shelf_num, directories), result)
