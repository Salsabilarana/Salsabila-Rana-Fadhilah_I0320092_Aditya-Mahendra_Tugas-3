list_ranafriends = ['sarah','septi','thoriq','alpath','dapa','rela','zedi','rio','hany','ica']

print('Nama pada indeks 4 :', list_ranafriends[4])
print('Nama pada indeks 6 :', list_ranafriends[6])
print('Nama pada indeks 7 :', list_ranafriends[7])

#mengganti nama pada list 3,5,9
print("list awal:", list_ranafriends)

list_ranafriends[3]= "rara"
list_ranafriends[5]= "ceong"
list_ranafriends[9]= "aura"
print("list setelah diganti:", list_ranafriends)

#menambah 2 teman
list_ranafriends.append('fajar')
list_ranafriends.append('riyan')
print("list setelah ditambah :", list_ranafriends)

#menampilkan dengan perulangan
print("semua teman rana ada", (len(list_ranafriends)), "orang")
for friends in list_ranafriends:
    print(friends)

