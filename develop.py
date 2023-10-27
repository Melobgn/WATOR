# 1 récupérer LES positions des requins et des poissons
class Position:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

# position des requins
class Requins(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.items = 2

# position des poissons
class Poissons(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 1

# matrice 
'''partie à supprimer '''
monde = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
for row in monde:
    # print(*row)
    '''partie à supprimer '''

# renvoyer les positions
    def trouver_position(matrice, items):
        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                if matrice[i][j] == items:
                    yield i, j

poisson = trouver_position(monde, 1)
requin = trouver_position(monde, 2)

# retourne la position des poissons et des requins 'x, y'
for i, j in poisson:
    print(i, j)

for i, j in requin:
    print(i, j)

# 2 créer une condition : si le requin se place sur un poisson (2 remplace 1)
    # le requin gagne 1 chronons (c.à.d. de l'énergie = 6 chronons au max)
    # le poisson meurt et disparait