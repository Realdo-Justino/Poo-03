class pessoa:
    def __init__(self,nome,dataNascimento,endereco):
        self.nome=nome
        self.dataNascimento=dataNascimento
        self.endereco=endereco

class aluno(pessoa):
    def __init__(self,nome,dataNascimento,endereco,cd_Matricula,curso,nota1,nota2,nota3):
        super().__init__(nome,dataNascimento,endereco)
        self.cd_Matricula=cd_Matricula
        self.curso=curso
        self.soma=nota1+nota2+nota3
        self.media=(self.soma)/3
        if(self.media>7):
            self.resultado="Aprovado"
        elif(self.media>5):
            self.resultado="Recuperação"
        else:
            self.resultado="Reprovado"
    

class professor(pessoa):
    def __init__(self,nome,dataNascimento,endereco,cd_Funcionario,curso,disciplina):
        super().__init__(nome,dataNascimento,endereco)
        self.cd_Funcionario=cd_Funcionario
        self.curso=curso
        self.disciplina=disciplina

Aluno1=aluno("Realdo","25/04/03","Turvo",46643,"Informatica",10,2,5)
Aluno2=aluno("Otavio","13/07/04","Timbe",46687,"Quimica",10,9,5)
Aluno3=aluno("Eduardo","21/03/05","Timbe",46867,"Quimica",1,9,2)
Professor1=professor("Cris","23/09/89","Criciuma",76234,"Informatica","MySQL")

print("\nAluno: ",Aluno1.nome,"\nData de nascimento: ",Aluno1.dataNascimento,"\nEndereço: ",Aluno1.endereco,"\nMatricula: ",Aluno1.cd_Matricula,"\nCurso: ",Aluno1.curso,"\nMedia: ",Aluno1.media,"\nResultado: ",Aluno1.resultado)
print("\n\n")
print("Aluno: ",Aluno2.nome,"\nData de nascimento: ",Aluno2.dataNascimento,"\nEndereço: ",Aluno2.endereco,"\nMatricula: ",Aluno2.cd_Matricula,"\nCurso: ",Aluno2.curso,"\nMedia: ",Aluno2.media,"\nResultado: ",Aluno2.resultado)
print("\n\n")
print("Aluno: ",Aluno3.nome,"\nData de nascimento: ",Aluno3.dataNascimento,"\nEndereço: ",Aluno3.endereco,"\nMatricula: ",Aluno3.cd_Matricula,"\nCurso: ",Aluno3.curso,"\nMedia: ",Aluno3.media,"\nResultado: ",Aluno3.resultado)
print("\n\n")
print("Professor: ",Professor1.nome,"\nData de nascimento: ",Professor1.dataNascimento,"\nEndereço: ",Professor1.endereco,"\nFuncionario: ",Professor1.cd_Funcionario,"\nCurso: ",Professor1.curso,"\nDisciplina: ",Professor1.disciplina)
print("\n\n")