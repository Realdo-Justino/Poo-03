class pessoa:
    def __init__(self,nome,dataNascimento,endereco):
        self.nome=nome
        self.dataNascimento=dataNascimento
        self.endereco=endereco
class funcionario(pessoa):
    def __init__(self,nome,dataNascimento,endereco,cd_Funcionario,):
        super().__init__(nome,dataNascimento,endereco)
        self.cd_Funcionario = cd_Funcionario

class vendedor(funcionario):
    def __init__(self,nome,dataNascimento,endereco,cd_Funcionario,nr_tempo_trabalho,nr_vendas):
            super().__init__(nome,dataNascimento,endereco,cd_Funcionario,)
            self.nr_tempo_trabalho = nr_tempo_trabalho
            self.nr_vendas=nr_vendas
            if(self.nr_tempo_trabalho>5):
                self.comissao=(nr_vendas/100)*10
                self.salario=4000
            else:
                self.comissao=(nr_vendas/100)*5
                self.salario=2000
            self.salarioTotal=self.salario+self.comissao

Vendedor1=vendedor("Realdo","25/04/03","Turvo",46365,6,500)
Vendedor2=vendedor("Eduardo","05/05/03","Cocal Do Sul",33355,5,1000)

print("\nNome: ",Vendedor1.nome,"\nData de Nascimento: ",Vendedor1.dataNascimento,"\nEndereco: ",Vendedor1.endereco,"\nCodigo: ",Vendedor1.cd_Funcionario,"\nTempo de Trabalho: ",Vendedor1.nr_tempo_trabalho,"\nSalario Fixo: ",Vendedor1.salario,"\nComissao: ",Vendedor1.comissao,"\nSalario Total: ",Vendedor1.salarioTotal)
print("\nNome: ",Vendedor2.nome,"\nData de Nascimento: ",Vendedor2.dataNascimento,"\nEndereco: ",Vendedor2.endereco,"\nCodigo: ",Vendedor2.cd_Funcionario,"\nTempo de Trabalho: ",Vendedor2.nr_tempo_trabalho,"\nSalario Fixo: ",Vendedor2.salario,"\nComissao: ",Vendedor2.comissao,"\nSalario Total: ",Vendedor2.salarioTotal)