import os
import shutil

# 1. Define o nome da pasta que será organizada
pasta_alvo = "./pasta_teste"

# 2. Define quais extensões vão para cada pasta
tipos_arquivos = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".pptx"],
    "Planilhas": [".xlsx", ".csv"],
    "Compactados": [".zip", ".rar"]
}

# 3. Cria a pasta de teste caso ela ainda não exista
if not os.path.exists(pasta_alvo):
    os.makedirs(pasta_alvo)

# 4. Olha cada arquivo dentro da pasta e move para o lugar certo
for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)

    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        for pasta_destino, extensoes in tipos_arquivos.items():
            if extensao in extensoes:
                caminho_destino = os.path.join(pasta_alvo, pasta_destino)

                if not os.path.exists(caminho_destino):
                    os.makedirs(caminho_destino)

                shutil.move(caminho_arquivo, os.path.join(caminho_destino, arquivo)) #comentario
                print(f"Movido: {arquivo} -> {pasta_destino}/")
                break