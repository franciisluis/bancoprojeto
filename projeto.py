import csv
from aluno import Aluno
from datetime import datetime
class Main:
    alunos = []
    arquivo = open('teste.csv', 'r') # Abra o arquivo (leitura)
    pessoas=csv.DictReader(arquivo)
    for pessoas in pessoas:
        alunos.append(Aluno(pessoas["Cod"],pessoas["Nome"],pessoas["Nota"],pessoas["Controle"]))
        #print(pessoas["Cod"],pessoas["Nome"],pessoas["Nota"],pessoas["Controle"])
    #for aluno in alunos:
        #print(aluno.toString())
    arquivo.close()
    print("-!!!! SGDB Pythonzica !!!!-")

    op=input("Digite (1) para iniciar uma transação:\n")
    if op=='1':
        data=datetime.now()
        timestamp=datetime.timestamp(data)
        print(timestamp)
        try:
            arquivo_user=open(""+str(timestamp)+".csv",'w')
            writer=csv.writer(arquivo_user)
            writer.writerow(('Cod','Nome','Nota','Controle'))
           # for aluno in alunos:
                #writer.writerow(str(aluno.getCodigo()),str(aluno.getNome()),str(aluno.getNota()),str(aluno.getControle()))
        finally:
            arquivo_user.close()
    else:

        print("Opção inválida")





