import os



# current dir:
path = os.getcwd()
print(path)

# current file dir:
path = os.path.dirname(os.path.realpath(__file__))
print(path)


# create subpath:
new_path = os.path.join(path,'temp','test')
print(new_path)