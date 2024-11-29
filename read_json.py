import json

def caminho(file):
    try:
        ficheiro = open(file, "rt", encoding="utf-8")

        json_data = ficheiro.read()
        data = json.loads(json_data)
        ficheiro.close()
        print(data)

    except:
        print("Ocorreu um erro!")

    finally:
        print("Processo concluído!\n")

escolha = input()

caminho(escolha)