from turtle import pen


class Stationery:
    def __init__(self, title="Somthing that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")

class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")


stat = Stationery()
pen = Pen("Parker")
pencil = Pencil("Attache")
marker = Marker("Stabilo")

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()
