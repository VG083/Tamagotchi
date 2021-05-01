class EstruturaTamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 10
        self.saude = 70
        self.idade = 1
    def AlterarNome(self, novoNome):
        self.nome = novoNome
    def AlterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def AlterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def AlterarIdade(self):
        self.idade += 1
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude + self.fome
        return humor

nomeTamagotchi = input('Qual o nome que deseja colocar no seu Tamagotchi? ')
Tamagotchi = EstruturaTamagotchi(nome = nomeTamagotchi)
while (Tamagotchi.saude > 0) and (Tamagotchi.fome < 100):
    Tamagotchi.AlterarFome(+2)
    Tamagotchi.AlterarSaude(-2)
    Tamagotchi.AlterarIdade()
    resposta = input(f"""\n------------------------------------------\n          
     \_____/
    | º - º |
  _ |_______| _
 | ||       || |
 |_||       ||_|
    |_______|
     |_| |_|
     \nOi, eu sou o {Tamagotchi.nome}. O que você deseja fazer comigo? \n1- Visualizar humor\n2- Visualizar idade\n3- Visualizar fome\n4- Visualizar saúde\n5- Alimentar (-10 de fome)\n6- Dormir (+10 de saúde)\nResposta: """)
    print('\n')
    if resposta == '1':
        print("Humor: ", Tamagotchi.RetornarHumor())
    elif resposta == '2':
        print("Idade: ", Tamagotchi.RetornarIdade())
    elif resposta == '3':
        print("Fome: ", Tamagotchi.RetornarFome())
    elif resposta == '4':
        print("Saude: ", Tamagotchi.RetornarSaude())
    elif resposta == '5':
        Tamagotchi.AlterarFome(-10)
        print("-10 de fome! Obrigado!")
    elif resposta == '6':
        Tamagotchi.AlterarSaude(+10)
        print("+10 de saúde! Obrigado!")
    else:
        print('Escolha um número válido!')
else:
    print("""\n------------------------------------------\n          
     \_____/
    | x - x |
  _ |_______| _
 | ||       || |
 |_||       ||_|
    |_______|
     |_| |_|\nVocê me deixou morrer!\n""")