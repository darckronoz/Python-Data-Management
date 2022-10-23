dictionar = [('toto', 'sisi'), ('turupes', 'aweno'), ('menta', 'dosporfavor'), ('suspiro', 'uwu')]
#to unzip something use zip function with this operator '*'.
questions, answers = zip(*dictionar)

print(dictionar)
print(questions)
print(answers)