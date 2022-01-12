
# Villain Class
class Villain:
    def __init__(self, first, last, Minions):
        self.nameFirst = first
        self.nameLast = last
        self.nameFull = self.nameFirst + " " + self.nameLast
        self.miniontotals= Minions
    def giveIncrease(self, thePercentage):
        newtotal = self.miniontotals * thePercentage
        self.miniontotals = newtotal

# Villains inital amount of minions       
Minion1= Villain('Joe', 'Biden', 101)
Minion2 = Villain( 'Kamala', 'Harris', 101)

print(Minion1.nameFull + " has started with " + str(Minion1.miniontotals) + " minions!")
print(Minion2.nameFull + " has started with " + str(Minion1.miniontotals) + " minions!")

# Villains increased amount of minions
Minion1.giveIncrease(2)
Minion2.giveIncrease(2)

print(Minion1.nameFull + " now has " + str(Minion1.miniontotals) + " minions!")
print(Minion2.nameFull + " now has " + str(Minion1.miniontotals) + " minions!")

print("There are 2 villains in this class!")