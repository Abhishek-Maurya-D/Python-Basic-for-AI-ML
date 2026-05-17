playerCount = 0;
class Player():
    def __init__(self, name, level):
        global playerCount;
        self.name = name;
        self.level = level;
        playerCount += 1;

p1 = Player("Abhishek", 1);
p2 = Player("Amit", 2);
p3 = Player("Anuj", 3);

print(playerCount);