class bunga:
    def first(self):
        print("Banyak sekali spesies atau jenis bunga yang ada di dunia")

    def second(self):
        print("Ada beberapa jenis bunga yang terdapat di Indonesia")

class tulip(bunga):
    def second(self):
        print("Bunga Tulip ada di Indonesia, namun berasal dari Negara Belanda")

class mawar(bunga):
    def second(self):
        print("Bunga mawar ada di Indonesia dan ada yang berasal dari Indonesia")

obj_bunga = bunga()
obj_tulip = tulip()
obj_mawar = mawar()

print("\n")

obj_bunga.first()
obj_bunga.second()

print("\n")

obj_tulip.first()
obj_tulip.second()

print("\n")

obj_mawar.first()
obj_mawar.second()

        
    