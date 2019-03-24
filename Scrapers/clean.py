names = []
with open("filenames.txt", "r+") as f:
    names = f.readlines()

names = [name.replace(".txt", "") for name in names]
with open("titles.txt", "w+") as f:
    f.write(''.join(names))
