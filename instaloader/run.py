import instaloader

# Crie uma instância do Instaloader
loader = instaloader.Instaloader()

# Insira o nome de usuário e senha
usuario = 'lsinformatica2024'
senha = 'leo4061@L'

try:
    # Tente carregar a sessão a partir do arquivo, se existir
    loader.load_session_from_file(usuario)
except FileNotFoundError:
    # Se o arquivo de sessão não existir, faça login
    loader.context.log("Session file does not exist yet - Logging in.")
    loader.login(usuario, senha)
    # Salve a sessão em um arquivo para reutilização
    loader.save_session_to_file()

# Após o login bem-sucedido, você pode usar as funcionalidades do Instaloader

# Informar o nome do perfil alvo
perfil_alvo = 'oatacadodomarmorista'

# Carregar o perfil
perfil = instaloader.Profile.from_username(loader.context, perfil_alvo)

# Coletar os seguidores do perfil
seguidores = []
for seguidor in perfil.get_followers():
    seguidores.append(seguidor.username)

# Exibir os seguidores
print("Seguidores de", perfil_alvo, ":", seguidores)