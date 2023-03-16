kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

lines = kata.keys()
for line in lines:
    print(line + " was created by " + kata[line]) if isinstance(kata[line], str) else print("The value must be a String")
