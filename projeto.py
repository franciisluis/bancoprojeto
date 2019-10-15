import csv
from aluno import Aluno

aluno = Aluno('101','Francis','10')

arquivo = open('teste.csv', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
print(conteudo)

conteudo.append('teste')   # insira seu conteúdo

arquivo = open('banco', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
arquivo.close()
