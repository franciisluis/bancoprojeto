class Aluno:
    id = 0
    codigo = 0
    nome = ""
    nota = 0.0
    controle=0

    def __init__(self,codigo,nome,nota,controle):
        self.codigo = codigo
        self.nome = nome
        self.nota = nota
        self.controle=controle

    def setCodigo(self,codigo):
        self.codigo = codigo
    def getCodigo(self):
        return self.codigo
    def setNome(self,nome):
        self.nome=nome
    def getNome(self):
        return self.nome
    def setNota(self,nota):
        self.nota=nota
    def getNota(self):
        return self.nota
    def setControle(self,controle):
        self.controle=controle

    def getControle(self):
        return self.controle
    def toString(self):
        return ""+"\nCodigo="+self.codigo+"\nNome="+self.nome+"\nNota="+self.nota+"\nControle="+self.controle





#https://stackoverflow.com/questions/48504316/regex-or-split-in-python-for-shell-awk-equivalent

