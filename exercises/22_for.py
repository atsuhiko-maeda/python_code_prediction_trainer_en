# <meta[replace] target=["_I_"] with=["i","j","k"]>
# <meta[select]>
# <meta[option]>
for _I_ in [1, 3, 5]:# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="\[1, 3, 5\]" with=["\[1, 3, 5\]","\[2, 4, 6\]","\[10, 20, 30\]"]/>
    print(_I_)
# </meta[option]>
# <meta[option]>
for _I_ in [1, 3, 5]:# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="\[1, 3, 5\]" with=["\[1, 3, 5\]","\[2, 4, 6\]","\[10, 20, 30\]"]/>
    print(_I_)
    print("a")
# </meta[option]>
# <meta[option]>
for _I_ in [1, 3, 5]:# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="\[1, 3, 5\]" with=["\[1, 3, 5\]","\[2, 4, 6\]","\[10, 20, 30\]"]/>
    print(_I_)
print("z")
# </meta[option]>
# <meta[option]>
for _I_ in range(4):# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="4" with=["4","3","5"]/>
    print("a")
print("z")
# </meta[option]>
# <meta[option]>
for _I_ in range(4):# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="4" with=["4","3","5"]/>
    print("a")# <meta[replace] p="0.1" target="    print" with=["print"]/>
# </meta[option]>
# <meta[option]>
for _I_ in range(1, 5):# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="1, 5" with=["1, 5","2, 5","0, 4"]/>
    print(_I_)
# </meta[option]>
# <meta[option]>
for _I_ in range(1, 8, 2):# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="1, 8, 2" with=["1, 8, 2","0, 6, 2","2, 9, 3"]/>
    print(_I_)
# </meta[option]>
# <meta[option]>
for _I_ in range(6, 0, -2):# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="6, 0, -2" with=["6, 0, -2","5, 0, -1","8, 0, -2"]/>
    print(_I_)
# </meta[option]>
# </meta[select]>
# </meta[replace]>
