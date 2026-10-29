# <meta[replace] target=["_I_"] with=["i","j","m"]>
# <meta[replace] target=["_J_"] with=["k","n","l"]>
# <meta[select]>
# <meta[option]>
for _I_ in range(3):# <meta[replace] p="1.0" target="3" with=["3","2","2"]/>
    for _J_ in range(2):# <meta[replace] p="1.0" target="2" with=["2","3","2"]/>
        print("a")
# </meta[option]>
# <meta[option]>
for _I_ in range(3):# <meta[replace] p="1.0" target="3" with=["3","2","2"]/>
    for _J_ in range(2):# <meta[replace] p="1.0" target="2" with=["2","3","2"]/>
        print("a")
    print("b")
# </meta[option]>
# <meta[option]>
for _I_ in range(1, 4):# <meta[replace] p="1.0" target="1, 4" with=["1, 4","1, 3","2, 4"]/>
    for _J_ in range(_I_):
        print("a")
# </meta[option]>
# <meta[option]>
for _I_ in range(1, 4):# <meta[replace] p="1.0" target="1, 4" with=["1, 4","1, 3","2, 4"]/>
    for _J_ in range(_I_):
        print("a")
    print("b")
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
