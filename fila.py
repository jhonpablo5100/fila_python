class fila:
    def __init__(self):
 
        a=5
        usuario=[]
        
        #adicionar usuario
        while a>0:
            print("nome de usuario")
            nome = input();
            usuario.append(nome)
            a=a-1;

        for ver_user in usuario:
            print("Usuario: "+ver_user)

        
        #modificar lista
        while True:
            print("digite 1 para deletar um elemento e 0 para sair")
            opcao = input()
            if opcao == "1":
                print("deletar")
               
                ultimo_elemento = len(usuario)-1

                usuario.pop()
                
                print("===========================")

                for listar_user in usuario:
                    print("usuario: "+listar_user)

                if ultimo_elemento == 0:
                    print("todos usuarios deletados com sucesso")
                    break
            if opcao =="0":
                print("sair")
                break
            if opcao!="0" or opcao !="1":
                print("digite um valor valido")


sistema_fila = fila()

