filepath="C:/Users/punti/dwhelper/query.txt"
#filepath = "notes.txt"


with open(filepath, "r") as f:
    #f.write(shared_string)
    string = f.read()

print(string)