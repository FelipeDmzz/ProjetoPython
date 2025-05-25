from data.context.postgre_sql_context import Postgre_Sql_Context

def Escola():
    print("1 - Adicionar aluno")
    print("2 - Deletar aluno")
    print("3 - Adicionar nota")
    print("4 - Atualizar nota")
    print("5 - Deletar nota")
    print("6 - Consultar notas")
    print("7 - Sair")

    opcao_selecionada =verifica_opcao_selecionada(input("Informe a opção desejada: "))

    if (opcao_selecionada == 0):
        Escola()
    else:
        db_pg_context = Postgre_Sql_Context()
        db_pg_context.conectar()

        if (opcao_selecionada == 1):
            matricula = input("Insira a matricula do Aluno: ").strip()
            nome = input("Insira o nome do aluno: ").strip().title()
            try:
                query = (f"INSERT INTO public.alunos (matricula, nome) VALUES ('{matricula}', '{nome}')")
                db_pg_context.executar_uptade_sql(query)
                print("Aluno inserido com sucesso")
            except Exception as e:
                print("Não foi possível Inserir aluno")
                print(f"Erro -> {e}")

        elif (opcao_selecionada == 2):
            matricula = input("Informe a matricula a ser removida: ").strip()
            try:
                query =(f"DELETE from public.alunos WHERE matricula = '{matricula}'")
                db_pg_context.executar_uptade_sql(query)
                print("Aluno removido com sucesso")
            except Exception as e:
                print("Não foi possível remover aluno")
                print(f"Erro -> {e}")

        elif (opcao_selecionada == 3):
            matricula = input("Insira a matricula do Aluno: ").strip()
            disciplina = input("Insira o nome da disciplina: ").strip().capitalize()
            nota = input("Insira a nota do aluno: ").strip()
            try:
                query = (f"INSERT INTO public.notas (matricula, disciplina, nota) VALUES ('{matricula}', '{disciplina}', {nota})")
                db_pg_context.executar_uptade_sql(query)
                print("Nota adicionada com sucesso")

            except Exception as e:
                print("Não foi possível adicionar nota")
                print(f"Erro -> {e}")

        elif (opcao_selecionada == 4):
            matricula = input("Insira a matricula do aluno: ").strip()
            disciplina = input("Insira a disciplina: ").strip().capitalize()
            nova_nota = input("Insira a nova nota: ").strip()
            try:
                query = (f"UPDATE public.notas SET nota = {nova_nota} WHERE matricula = '{matricula}' AND disciplina ='{disciplina}'")
                db_pg_context.executar_uptade_sql(query)
                print("Nota atualizada com sucesso")

            except Exception as e:
                print("Não foi possível atualizar nota")
                print(f"Erro -> {e}")

        elif (opcao_selecionada == 5):
            matricula = input("Insira a matricula: ").strip()
            disciplina = input("Insira a disciplina: ").strip().capitalize()
            try:
                query = (f"DELETE from public.notas WHERE matricula = '{matricula}' AND disciplina = '{disciplina}'")
                db_pg_context.executar_uptade_sql(query)
                print("Nota removida com sucesso")

            except Exception as e:
                print("Não foi possível remover nota ")
                print(f"Erro -> {e}")

        elif (opcao_selecionada == 6):
            matricula =input("Insira a matricula: ").strip()
            try:
                query = (f"SELECT disciplina,nota FROM public.notas WHERE matricula = '{matricula}'")
                resultados = db_pg_context.executar_query_sql(query)
                if resultados:
                    print(f"\nNotas do aluno {matricula}:")
                    for disciplina, nota in resultados:
                        print(f"{disciplina}: {nota}")
                else:
                    print(f"Nenhuma nota encontrada para esse aluno")
            except Exception as e:
                print("Não foi possível consultar notas")
                print(f"Erro -> {e}")

        elif opcao_selecionada == 7:
            print("Saindo do sistema")
            db_pg_context.desconectar()
            return

        db_pg_context.desconectar()
        Escola()

def verifica_opcao_selecionada(opcao_selecionada):
    try:
        e_numero = int(opcao_selecionada)
        if (e_numero >=1 and e_numero <=7):
            return e_numero

        else:
            return 0
    except Exception as e:
        print("A opção informada não é válida.")
        return 0

Escola()