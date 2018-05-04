names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
no_dups = []
def remove(names):
    for name in names:
        if name not in no_dups: 
            no_dups.append(name)
    return no_dups        


print(remove(names))