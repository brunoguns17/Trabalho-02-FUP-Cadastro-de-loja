# NOME:        Bruno Gustavo
# Matrícula:	 517117
# Curso:	     ENGENHARIA DE SOFTWARE
import os
cadastro = []
lista =[]
def cadastrar(): # Reponsavel por cadastrar cliente no sistema.
  while True:
      dados = {}
      
      dados["nome"] = str(input("\033[1;92mNOME: \033[m"))
      print("")
      
      login = str(input("\033[1;92mLOGIN: \033[m"))

      for i in cadastro:
         while (i["login"] == login):# verifica se o login, digitado pelo o usuario, ja existe.
          print("\033[1;31mEsse login pertence a outro usuário :/  \033[m")
          print()
          login = str(input("\033[1;92mLOGIN: \033[m"))
        
      print()
      dados["login"] = login
      print("")
      dados["senha"] = str(input("\033[1;92mSENHA: \033[m"))
      print("")
      dados["email"] = str(input("\033[1;92mE-MAIL: \033[m"))
      print("")
      dados["data de nascimento"] = str(input("\033[1;92mDATA DE NASCIMENTO: \033[m"))
      print()
      dados["número de telefone"] = int(input("\033[1;92mNÚMERO DE TELEFONE: \033[m"))
      print("")
      

      continuar = str(input("\033[1;33m DESEJA CONTINUAR? [S / N] \033[m ")).lower() #verifica se o usuario deseja continuar fazendo novos
      if(continuar == "s"):
          cadastro.append(dados)
          print("="*160)
          print(cadastro)

          print("="*160)
      elif(continuar == "n"):
          cadastro.append(dados)
          print("\033[1;35m=\033[m"*160)

          for  c in cadastro:
              print(c)
              print()

          print("\033[1;96mFIM DO CADASTRO!\033[m  ")
          print("\033[1;35m=\033[m"*160)
          break
      else:
          print("\033[1;31m error!! :/ inicie novamente.\033[m")
          break
      
  return cadastro


def Adicionar_endereco():# adiciona endereço a um clinte     
    for i in cadastro: #SERVER PARA MOSTRAR OS NOMEES DOS USUÁRIOS CADASTRADO
         nick = i 
         print(f'nome: {nick["nome"]}')
    
    print()
    
    seleciona = str(input("\033[1;92m Em Qual usuário, você deseja adicionar endereço?  \033[m"))
    for i in cadastro:
        if i["nome"] == seleciona:
        
            logradouro = {}
            print("\033[1;96mUsuário encontrado com sucesso! :D \033[m")
            print()
            logradouro["Endereço de"] = seleciona
            logradouro["rua"] = str(input("\033[1;92m Rua: \033[m"))
            logradouro["número"] = int(input("\033[1;92m número: \033[m"))
            logradouro["complemento"] = str(input("\033[1;92m complemento: \033[m"))
            logradouro["bairro"] = str(input("\033[1;92m Bairro: \033[m"))
            logradouro["cidade"] = str(input("\033[1;92m Cidade: \033[m"))
            logradouro["cep"] = str(input("\033[1;92m Cep: \033[m"))
            logradouro["ponto de referência"] = str(input("\033[1;92m Ponto de referência: \033[m"))
            
            lista.append(logradouro)

           
            print("\033[1;96mENDEREÇO CADASTRADO!\033[m  ")
            print()
            break

    else:
      print("\033[1;33mUsuário não existe :/ \033[m")
      print()
            
def Mostrar_dados_clientes(): #Função que mostra os dados dos clientes cadastrados
  while True:
    continuar = str(input("\033[1;96mMostrar dados do cliente: \033[m  \033[1;33m [S / N] \033[m ")).lower()
    print()

    if continuar == "s":
      busca = str(input("\033[1;96mDIGITE O LOGIN DO USUARIO: \033[m "))
      print()
      os.system('cls')#limpa o terminal

      for i in cadastro:
        if i["login"] == busca:
            print(i)
            for x in lista:
                if i["nome"] == x["Endereço de"]: #verifica se o nome cadastrado é igual ao da variavel que seleciona.
                    print()
                    print(f'\033[1;92mENDEREÇO DE:\033[m{x["Endereço de"]}  \033[1;92mRUA:\033[m {x["rua"]}  \033[1;92mNÚMERO DA CASA:\033[m {x["número"]}  \033[1;92mCOMPLEMENTO:\033[m {x["complemento"]}  \033[1;92mBAIRRO:\033[m {x["bairro"]}  \033[1;92mCIDADE:\033[m {x["cidade"]}  \033[1;92mCEP:\033[m {x["cep"]} \033[1;92mPONTO DE REFERENCIA:\033[m {x["ponto de referência"]}')

            print()
            break
      else:
          print("\033[1;31mEsse login não existe! Por favor, tente novamente. \033[m ")     

    elif continuar =="n":
      break 
def Mostrar_clientes_cadastrados():#Função que mostra lista de clientes cadastrados
    print("\033[1;96mLISTA DE ÚSUARIOS CADASTRADOS.\033[m")
    global cad
    cad = cadastro
    for i in cad:
       print(f'Nome: {i["nome"]}  Login: {i["login"]}')
    


while True: #Menu principal

 try: # sistema de tramento de erros
    opcao = int(input(
        " ****************** Loja do zé seboso ********************"
        "\n *                                                       *"
        "\n *" "[1]  Cadastrar cliente                                 *"
        "\n *" "[2]  Adicionar endereço a cliente                      *"
        "\n *" "[3]  Mostrar dados do cliente                          *"
        "\n *" "[4]  Mostrar clientes cadastrados                      *"
        "\n *" "[0]  Sair                                              *"
        "\n *                                                       *"
        "\n *********************************************************\n  DIGITE UM DOS COMANDOS:"))
   
       

    os.system('cls') #serva apenas para limpar o terminal
 
    if (opcao == 1):
      print("Cadastrar cliente ")
      cadastrar()

    elif (opcao == 2):
      print("Adicionar endereço a cliente")
      print()
      Adicionar_endereco()

    elif (opcao == 3):
      Mostrar_dados_clientes()

    elif (opcao == 4):
      Mostrar_clientes_cadastrados()

    elif (opcao == 0):
      print("\033[1;96mFIM DO PROGRAMA!!\033[m")
      break 

    else:
      print("ESSE COMANDO NÃO EXISTE!")
 except:
     print("ERRO! TENTE NOVAMENTE!")