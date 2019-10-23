import csv
from aluno import Aluno
class Main:
    aluno = Aluno('101','Francis','10')
    aluno1= Aluno('102','Gustavo','8')
    aluno2= Aluno('103','Filipe','9')

    arquivo = open('teste.csv', 'w') # Abra o arquivo (leitura)
    try:
        writer=csv.writer(arquivo)
        writer.writerow(('Cod','Nome','Nota'))
        writer.writerow((aluno.codigo,aluno.nome,aluno.nota))
        writer.writerow((aluno1.codigo,aluno1.nome,aluno1.nota))
        writer.writerow((aluno2.codigo,aluno2.nome,aluno2.nota))
    finally:
        arquivo.close()
    print(open('teste.csv','rt').read())
    conteudo = open('teste.csv','rt').read()

    print(conteudo)


    transa1 = Transacao()
