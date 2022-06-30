from data_source.data_base import documents, directories


def search_in_docs(key_1, val_1, key_2, *doc):
    for idx in doc:
        if val_1 == idx[key_1]:
            return f'The document owner is {idx[key_2]}'
    return 'No document found.'


def search_on_shelf(doc_num, drct):
    for idx in drct:
        if doc_num in drct[idx]:
            return f'the document is on shelf #{idx}'
    return 'No document found.'


def list_of_docs(*doc):
    if len(doc) == 0:
        print('No documents found.')
    for idx in doc:
        print(f'''{idx['type']} "{idx['number']}" {idx['name']}''')


def add_doc_on_shelf(doc_num, shelf_num, drct):
    while True:
        shelf_num_tmp = shelf_num
        if shelf_num not in drct:
            print(f"The shelf #{shelf_num} doesn't exist. \nChoose another one from list:")
            for keys in drct:
                print(keys, end=',')
            shelf_num = input("('q' for exit, 'a' to add anew shelf):\t")
            if shelf_num == 'q':
                print("Shelf doesn't exist. Adding canceled by user.")
                return 0
            elif shelf_num == 'a':
                make_new_shelf(shelf_num_tmp, drct)
                drct[shelf_num_tmp].append(doc_num)
                return shelf_num_tmp
        else:
            print('Ok #', shelf_num)
            drct[shelf_num].append(doc_num)
            return shelf_num


def add_doc(doc_num, doc_type, doc_owner, shelf_num, drct, doc):
    shelf_num = add_doc_on_shelf(doc_num, shelf_num, drct)
    if shelf_num == 0:
        return 'Error'
    else:
        doc.append({'type': doc_type, 'number': doc_num, 'name': doc_owner})
        return f'The document successfully added on shelf #{shelf_num}.'


def delete_from_shelf(doc_num, drct, doc):
    for idx in drct:
        if doc_num in drct[idx]:
            drct[idx].remove(doc_num)
            for idx_2 in doc:
                if doc_num in idx_2['number']:
                    doc.remove(idx_2)
            return f'The document number {doc_num} successfully removed.'
    return 'No documents found.'


def move_docs_on_shelfs(doc_num, shelf_num, drct):
    search_r = search_on_shelf(doc_num, drct)
    if search_r == 'No document found.':
        return search_r
    else:
        for idx in drct:
            if doc_num in drct[idx]:
                drct[idx].remove(doc_num)
        return f'the document is on shelf #{add_doc_on_shelf(doc_num, shelf_num, drct)}'


def make_new_shelf(shelf_num, drct):
    if shelf_num in drct:
        return f'The shell number {shelf_num} exist! No changes.'
    else:
        drct.setdefault(shelf_num, [])
        return f'Added a new shelf #{shelf_num}.'


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
            list_of_docs(*documents)
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
