# A simple script to add some fairly trivial data to our database for testing

# Import needed classes from py2neo
from py2neo import Graph, Node, Relationship

# Import random
import random as r

# Create and connect to our graph (assumed localhost for testing)
graph = Graph()

# Create some bogas users

usernames = ["Keith", "Harry", "Barry", "Rod"]

users = []

for name in usernames:
    users = users + [Node("User", username=name)]

graph.create(users)

# Create some bougus anime and some random relationships

animelist = ["Baccano", "Bacomonogatari", "Girls und Panzer", "Working", "Death Parade"]

for anime in animelist:
    animenodes = graph.merge("Anime", "name", anime)
    for node in animenodes:
        for user in users:
            if (r.random() > 0.4): # 60% chance each user will have watched the anime
                graph.create(Relationship(user, "WATCHED", node, rating="F")
