from instabot import Bot

# Criar uma instância do bot
bot = Bot()

# Informar o nome de usuário e senha
usuario = 'lsinformatica2024'
senha = 'leo4061@L'

# Fazer login
bot.login(username=usuario, password=senha)

time.sleep(10)

# Informar o nome do perfil alvo
perfil_alvo = 'ps_distribuidora'

# Obter seguidores do perfil
seguidores = bot.get_user_followers(perfil_alvo)

# Imprimir os nomes de usuário dos seguidores
print("Seguidores de", perfil_alvo, ":", seguidores)