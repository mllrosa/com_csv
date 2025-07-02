import csv
"""with open("dados.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        print(linha)
"""
"""exemplefile = open("dados.csv")
exemplereader = csv.reader(exemplefile)
exampledata = list(exemplereader)
exampledata
print(exampledata[1] [0])
print(exampledata[1] [1])
print(exampledata[1] [2])
print(exampledata[1] [3])
print(exampledata[1] [4])
dados.csv.close()"""


"""examplefile = open('dados.csv')
examplereader = csv.reader(examplefile)

for row in examplereader:
    print('Row #' + str(examplereader.line_num) + '' + str(row))
# printa com o numero de cada linha"""

with open('dados.csv', 'w') as arquivo:
    #info = ['Esmalte Azul', 'RisquÃ©', 'Azul', 'Glitter', '7.50']
    #arquivo = csv.writer(arquivo, list=info)

    arquivo_csv = csv.writer(arquivo)
    #arquivo_csv.writerow(['Esmalte Azul', 'RisquÃ©', 'Azul', 'Glitter', '7.50'])
    arquivo_csv.writerow(["cor \t idade"])
    arquivo_csv.writerow(["corr \t idadee"])

    