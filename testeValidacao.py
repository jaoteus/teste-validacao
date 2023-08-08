opcaoMenu = senha = username = ''; lacoNome = True; loopPrincipal = True; lacoSenha = True; lacoLoginNome = True
lacoLoginSenha = True
try:
    while lacoNome:
        username = input('Digite seu nome de usuário: ')
        username = username.lower()
        if username.isprintable() == False or username == False:
            print('Seu nome tem que possuir apenas letras!')
            continue
        else:
            break
    while lacoSenha:
        senha = input('Digite sua senha: ')
        if senha.isalnum() == False or senha == False:
            print('Sua senha deve ter letras e números!')
            continue
        else:
            print('Conta criada com sucesso!')
            break
    while loopPrincipal:
        # Funções
        def main():
            global opcaoMenu
            opcaoMenu = ''
            print('1 - Ver dados\n2 - Alterar dados\n3 - Teste de login\n4 - Sair ')

        def verDados():
            global opcaoMenu
            opcaoMenu = ''
            print(f'Sua senha é {senha}')
            print(f'Seu nome de usuário é {username}')
            opcaoMenu = input('Digite ENTER para voltar pro menu: ')

        def alterarDados():
            global opcaoMenu, username, mostrarNome, alterarNome, mostrarSenha, alterarSenha, senha
            opcaoMenu = ''
            opcaoMenu = input('Qual você quer alterar ?\n1 - Nome de usuário\n2 - Senha\nDigite: ')
            if opcaoMenu == '1':
                mostrarNome = 'Seu nome de usuário atual: {}'
                mostrarNome = mostrarNome.format(username)
                print(mostrarNome)
                while lacoNome:
                    alterarNome = input('Digite o novo nome de usuário ou clique em ENTER para cancelar: ')
                    if alterarNome.isprintable() == False or alterarNome == False:
                        print('Seu nome tem que possuir apenas letras!')
                        continue
                    else:
                        username = ''
                        username = alterarNome
                        alterarNome = ''
                        mostrarNome = 'Seu novo nome de usuário: {}'
                        mostrarNome = mostrarNome.format(username)
                        print(mostrarNome)
                        break

            elif opcaoMenu == '2':
                mostrarSenha = 'Sua senha atual é {}'
                mostrarSenha = mostrarSenha.format(senha)
                print(mostrarSenha)
                while lacoSenha:
                    alterarSenha = input('Digite a nova senha ou: ')
                    if alterarSenha.isalnum() == False or alterarSenha == False:
                        print('Sua senha deve ter letras e números!')
                        continue
                    else:
                        senha = ''
                        senha = alterarSenha
                        alterarSenha = ''
                        mostrarSenha = 'Sua nova senha: {}'
                        mostrarSenha = mostrarSenha.format(senha)
                        print(mostrarSenha)
                        break

        def testeLogin():
            global lacoLoginNome, loginNome, lacoLoginSenha, loginSenha, opcaoMenu
            while lacoLoginNome:
                loginNome = ''
                loginNome = input('Digite seu nome de usuário: ')
                if loginNome != username:
                    print('Nome de usuário incorreto, tente novamente!')
                    continue
                elif loginNome == username:
                    break

            while lacoLoginSenha:
                loginSenha = input('Digite sua senha: ')
                if loginSenha != senha:
                    print('Senha incorreta, tente novamente!')
                    continue
                elif loginSenha == senha:
                    break
            print('login efetuado com sucesso!')
            opcaoMenu = input('Digite ENTER para voltar pro menu: ')

        # Opções
        main()
        opcaoMenu = input('Digite: ')
        if opcaoMenu == '1':
            verDados()
        elif opcaoMenu == '2':
            alterarDados()
        elif opcaoMenu == '3':
            testeLogin()
        elif opcaoMenu == '4':
            print('Deslogando...')
            loopPrincipal = False
except:
    print('Algo deu errado :(')