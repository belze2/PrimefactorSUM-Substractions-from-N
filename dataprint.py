import pickle

with open('file.txt', 'rb') as file:
    # Load the pickled data
    data = pickle.load(file)

with open('table.txt', 'w') as TABLE:

    for item in data.values():
        for v in item:
            if v != 0: TABLE.write(str(v)+'   ')
        TABLE.write('\n')

print('file.txt converted to table.txt.....done.')

