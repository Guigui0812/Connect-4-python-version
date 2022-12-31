import socket
import game_server

# Choses intéressantes à faire : 
# - joindre une base de données pour stocker les données des joueurs (victoires, compte etc...)
# - Docker-compose pour lancer le serveur et la base de données en même temps 
# - faire un système de chat pour les joueurs
# - faire un système de classement pour les joueurs (pour afficher les meilleurs joueurs)
# - faire un système de statistiques pour les joueurs (pour afficher les statistiques des joueurs)
# - faire un système de sauvegarde pour les joueurs (pour sauvegarder les parties des joueurs)

# En réalité faudra deux serveurs : 
# - un serveur pour le chat
# - un serveur pour le jeu

host, port = 'localhost', 12345
player_number = 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
print("server is listening on port", port)

while True:

    server_socket.listen() # the server listen for connections
    print("server is listening for connections")

    connection, address = server_socket.accept()
    print("connection from", address)

    game_server.ClientThread.number_of_clients += 1
    
    if game_server.ClientThread.number_of_clients % 2 == 1:
        game_server.Game.number_of_games.append(game_server.Game())

    client_thread = game_server.ClientThread(connection, game_server.Game.number_of_games[-1], player_number)
    player_number += 1
    client_thread.start()

    if player_number > 2:
        player_number = 1

#connection.close()
#server_socket.close()