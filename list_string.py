kalimat = "Selamat pagi, nama saya Aliefa Indira. Teman-teman memanggilku AL. Usiaku 21 tahun. Salam kenal"
print(kalimat)

kalimat1=kalimat.split(" ")
print(kalimat1)

for indeks, kata in enumerate(kalimat1):
    print(f"Indeks kata '{kata}': {indeks}")
    
kalimat1[10] = int(kalimat1[10])
print(kalimat1)
print(type(kalimat1[10]))