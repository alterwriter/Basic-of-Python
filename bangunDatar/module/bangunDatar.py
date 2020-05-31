#luas bangun datar
def luasLingkaran():
	print("silahkan pilih : \n", "r (jari jari) \n d (diameter)")
	lebar=str(input("mau yang mana ? "))

	if lebar == "r" :
		r=int(input("masukkan jari-jari : "))
		circle = 3.14 * r ** 2 
	if lebar == "d" :
		d=int(input("masukkan diameter : "))
		circle = 1/4 * 3.14 * d ** 2
	return circle

def luasPersegi():
	s=int(input("masukkan nilai sisi : "))
	square = s**2
	return square

def luasSegitiga():
	a=int(input("masukkan nilai alas : "))
	t=int(input("masukkan nilai tinggi : "))
	triangle = 1/2*a*t
	return triangle

#keliling bangun datar

def kelilingLingkaran():
	print("silahkan pilih : \n", "r (jari jari) \n d (diameter)")
	lebar=str(input("mau yang mana ? "))

	if lebar == "r" :
		r=int(input("masukkan jari-jari : "))
		circle = 2 * 3.14 * r
	if lebar == "d" :
		d=int(input("masukkan diameter : "))
		circle = 3.14 * d
	return circle

def kelilingPersegi():
	s=int(input("masukkan nilai sisi : "))
	square = 4*s
	return square

def kelilingSegitiga():
	a=int(input("masukkan nilai a : "))
	b=int(input("masukkan nilai b : "))
	c=int(input("masukkan nilai c : "))
	triangle = a+b+c
	return triangle
