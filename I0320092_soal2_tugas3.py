dict_rana = {'Nama':'Rana', 'Hobi':['main voli','tidur','paralayang'],
             'sosial media':['slsbl.rana','slsablanana', 'ranranawayy'],
             'lagu fav':['who that be', 'blue jeans', 'rehat'],
             'makanan fav': ['Tempe','ayam lalapan', 'telur gulung']}

#mengubah hobi dan sosmed
dict_rana['Hobi'][1] = ('berenang')
dict_rana['sosial media'][2] = ('salsabilarana')


#menghapus 2 makanan fav
del dict_rana['makanan fav'][0:2]

#menambah 1 hobi
dict_rana.update({'Hobi':['main voli','berenang','paralayang','jalan']})

print(dict_rana)






