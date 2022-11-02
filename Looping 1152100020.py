string = ""
bar = 1

p = int(input("Masukkan angka :"))

# Looping Baris
while bar <= p:
	kol = bar

	# Looping Kolom
	while kol > 0:
		string = string + " * "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar + 1
print (string)
