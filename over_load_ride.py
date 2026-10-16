class cricketer:

    def __init__(self, name, run):
        self.name = name
        self.run = run

    def __add__(self, other):
            return ('combine', self.run + other.run)

        
    def __str__(self):
            return f'{self.name}: run: {self.run}'
        

class Bowler(cricketer):
      def __init__(self, name, run, wicked):
            super().__init__(name, run)
            self.wicked = wicked

      def __str__(self):
              return f"{self.name}: run = {self.run} wicked = {self.wicked}"



mustafiz = Bowler('musta', 500, 300)

print(mustafiz)
# sakib = cricketer('sakib', 500)
# musi = cricketer('musi', 800)

# combined = sakib + musi

# print(combined)
        



