class Agenda:
    
    def __init__(self, nome):
        self.agenda = dict()
        self.telefones = list()
        self.nome_user = nome
    
    def adicionar_contato(self, nome_cntt, phone):
        
        self.nome_contato = nome_cntt

        self.telefones.append(phone)

        self.agenda[self.nome_contato] = self.telefones

        return f'\nPerfeito {self.nome_user}, o número foi adicionado !'

    def apagar_contato(self, nome_cntt):

        if nome_cntt in self.agenda.keys():
            del self.agenda[nome_cntt]
            return f'\n{nome_cntt} foi deletado(a) com sucesso!'
        
        else:
            return f'\nContato Inexistente!'