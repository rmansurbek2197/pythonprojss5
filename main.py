class SonlarKetmaKetligi:
    def __init__(self, sonlar):
        self.sonlar = sonlar

    def takroriy_elementlarni_olib_tashla(self):
        sonlar_set = set()
        yangi_sonlar = []
        for son in self.sonlar:
            if son not in sonlar_set:
                sonlar_set.add(son)
                yangi_sonlar.append(son)
        return yangi_sonlar

    def saralash(self):
        yangi_sonlar = self.takroriy_elementlarni_olib_tashla()
        yangi_sonlar.sort()
        return yangi_sonlar

def main():
    sonlar = [5, 2, 8, 5, 1, 9, 2, 7, 3, 8, 6, 4, 1, 5, 9]
    sonlar_ketma_ketligi = SonlarKetmaKetligi(sonlar)
    print("Dastlabki sonlar ketma-ketligi: ", sonlar)
    print("Takroriy elementlarni olib tashlangan va saralangan sonlar: ", sonlar_ketma_ketligi.saralash())

    sonlar = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
    sonlar_ketma_ketligi = SonlarKetmaKetligi(sonlar)
    print("Dastlabki sonlar ketma-ketligi: ", sonlar)
    print("Takroriy elementlarni olib tashlangan va saralangan sonlar: ", sonlar_ketma_ketligi.saralash())

    sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sonlar_ketma_ketligi = SonlarKetmaKetligi(sonlar)
    print("Dastlabki sonlar ketma-ketligi: ", sonlar)
    print("Takroriy elementlarni olib tashlangan va saralangan sonlar: ", sonlar_ketma_ketligi.saralash())

if __name__ == "__main__":
    main()