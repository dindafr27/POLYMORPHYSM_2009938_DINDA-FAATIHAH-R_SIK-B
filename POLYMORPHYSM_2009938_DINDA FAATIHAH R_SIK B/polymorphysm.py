class tulip:
    def __init__(self, warna, jenis, fungsi):
        self.warna = warna
        self.jenis = jenis
        self.fungsi = fungsi

    def aroma (self):
        print("harum, my color is ", self.warna, "im a kind of flower", self.jenis, "and my function is ", self.fungsi)

class mawar:
    def __init__(self, warna, jenis, fungsi):
        self.warna = warna
        self.jenis = jenis
        self.fungsi = fungsi

    def aroma (self):
        print("kurang harum, my color is", self.warna, "im a kind of flower", self.jenis, "and my function is", self.fungsi)

tulip1 = tulip("pink", "tulip gesneriana", "usually used for celebrate an important moment")
mawar1 = mawar("merah", "rose canina", "rose can be a valentine flower ")      

for bunga in (tulip1, mawar1):
    bunga.aroma()
        
        
            