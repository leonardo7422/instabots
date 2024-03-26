from instapy import InstaPy

# Crie uma instância do InstaPy
session = InstaPy(username='lsinformatica2024', password='leo4061@L')

# Inicie a sessão
session.login()

# Defina o perfil alvo
perfil_alvo = 'ps_distribuidora'

# Extraia os seguidores do perfil alvo
seguidores = session.grab_followers(username=perfil_alvo, amount="full", live_match=True, store_locally=True)

# Imprima os seguidores
print("Seguidores de", perfil_alvo, ":", seguidores)

# Encerre a sessão
session.end()