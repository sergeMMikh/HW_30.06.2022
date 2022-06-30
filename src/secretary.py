def search_in_docs(key_1, val_1, key_2, *doc):
    for idx in doc:
        if val_1 == idx[key_1]:
            return f'The document owner is {idx[key_2]}'
    return 'No document found.'


def search_on_shelf(doc_num, directories):
    for idx in directories:
        if doc_num in directories[idx]:
            return f'the document is on shelf #{idx}'
    return 'No document found.'


def list_of_docs(*doc) -> list:
    doc_lst = []
    if len(doc) == 0:
        doc_lst.append('No documents found.')
    else:
        for idx in doc:
            # print(f'''{idx['type']} "{idx['number']}" {idx['name']}''')
            doc_lst.append(f'''{idx['type']} "{idx['number']}" {idx['name']}''')

    return doc_lst


def add_doc_on_shelf(doc_num, shelf_num, directories) -> int:
    while True:
        shelf_num_tmp = shelf_num
        if shelf_num not in directories:
            print(f"The shelf #{shelf_num} doesn't exist. \nChoose another one from list:")
            for keys in directories:
                print(keys, end=',')
            shelf_num = input("('q' for exit, 'a' to add anew shelf):\t")
            if shelf_num == 'q':
                print("Shelf doesn't exist. Adding canceled by user.")
                return 0
            elif shelf_num == 'a':
                make_new_shelf(shelf_num_tmp, directories)
                directories[shelf_num_tmp].append(doc_num)
                return shelf_num_tmp
        else:
            print('Ok #', shelf_num)
            directories[shelf_num].append(doc_num)
            return shelf_num


def add_doc(doc_num, doc_type, doc_owner, shelf_num, directories, doc):
    shelf_num = add_doc_on_shelf(doc_num, shelf_num, directories)
    if shelf_num == 0:
        return 'Error'
    else:
        doc.append({'type': doc_type, 'number': doc_num, 'name': doc_owner})
        return f'The document successfully added on shelf #{shelf_num}.'


def delete_from_shelf(doc_num, directories, doc):
    for idx in directories:
        if doc_num in directories[idx]:
            directories[idx].remove(doc_num)
            for idx_2 in doc:
                if doc_num in idx_2['number']:
                    doc.remove(idx_2)
            return f'The document number {doc_num} successfully removed.'
    return 'No documents found.'


def move_docs_on_shelfs(doc_num, shelf_num, directories):
    search_r = search_on_shelf(doc_num, directories)
    if search_r == 'No document found.':
        return search_r
    else:
        for idx in directories:
            if doc_num in directories[idx]:
                directories[idx].remove(doc_num)
        return f'the document is on shelf #{add_doc_on_shelf(doc_num, shelf_num, directories)}'


def make_new_shelf(shelf_num, directories):
    if shelf_num in directories:
        return f'The shell number {shelf_num} exist! No changes.'
    else:
        directories.setdefault(shelf_num, [])
        return f'Added a new shelf #{shelf_num}.'
