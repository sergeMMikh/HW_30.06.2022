from data_source.data_base import documents, directories

from src.secretary import search_in_docs, search_on_shelf, list_of_docs, add_doc_on_shelf, add_doc, delete_from_shelf
from src.secretary import move_docs_on_shelfs, make_new_shelf

if __name__ == '__main__':
    while True:
        print()
        print("Input yor command: \n'p' (person), \t's' (shelf), \t'l' (list), \t'a' (to add doc.),")
        print("'d' (delete doc.), \t'm' (move doc. on shelfs), \t'as' (add shelf)")
        user_input = input(" or 'q' to quit')\t")
        if user_input == 'p':
            print(search_in_docs('number',
                                 input('Input document number:\t'),
                                 'name',
                                 *documents))
        elif user_input == 's':
            print(search_on_shelf(input('Input document number:\t'),
                                  directories))
        elif user_input == 'l':
            tmp_list = list_of_docs(*documents)
            for item in tmp_list:
                print(item)
        elif user_input == 'a':
            print(add_doc(input('Input document number:\t'),
                          input('Input document type:\t'),
                          input('Input person name:\t'),
                          input('Input shelf number:\t'),
                          directories,
                          documents))
        elif user_input == 'd':
            print(delete_from_shelf(input('Input document number:\t'),
                                    directories,
                                    documents))
        elif user_input == 'm':
            doc_num_ = input('Input document number:\t')
            doc_status = search_on_shelf(doc_num_,
                                         directories)
            print(doc_status)
            if doc_status != 'No document found.':
                print(move_docs_on_shelfs(doc_num_,
                                          input('Input a new shelf number:\t'),
                                          directories))
        elif user_input == 'as':
            print(make_new_shelf(input('Input a new shelf number:\t'), directories))
        elif user_input == 'q':
            print('Quit.')
            break
        else:
            print('Unknown command. Try again.')
