# <meta[replace] target=["_F_"] with=["judge","check","score"]>
# <meta[replace] target=["_A_"] with=["a","x","n"]>
# <meta[select]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.1" target=":" with=[""]/>
    if _A_ > 3:# <meta[replace] p="0.05" target=":" with=[""]/><meta[replace] p="1.0" target="> 3" with=["> 3","> 5","> 2"]/>
        return "a"
    else:# <meta[replace] p="0.05" target=":" with=[""]/>
        return "b"

print(_F_(4))# <meta[replace] p="1.0" target="4" with=["4","6","1"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.1" target=":" with=[""]/>
    if _A_ > 5:# <meta[replace] p="0.05" target=":" with=[""]/><meta[replace] p="1.0" target="> 5" with=["> 5","> 7","> 4"]/>
        return "a"
    elif _A_ > 3:# <meta[replace] p="0.05" target=":" with=[""]/><meta[replace] p="1.0" target="> 3" with=["> 3","> 5","> 2"]/>
        return "b"
    else:# <meta[replace] p="0.2" target=":" with=[""]/>
        return "c"

print(_F_(4))# <meta[replace] p="1.0" target="4" with=["4","6","2"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.1" target=":" with=[""]/>
    if _A_ > 7:# <meta[replace] p="0.03" target=":" with=[""]/><meta[replace] p="1.0" target="> 7" with=["> 7","> 8","> 6"]/>
        return "a"
    elif _A_ > 5:# <meta[replace] p="0.03" target=":" with=[""]/><meta[replace] p="1.0" target="> 5" with=["> 5","> 6","> 4"]/>
        return "b"
    elif _A_ > 3:# <meta[replace] p="0.03" target=":" with=[""]/><meta[replace] p="1.0" target="> 3" with=["> 3","> 4","> 2"]/>
        return "c"
    else:# <meta[replace] p="0.2" target=":" with=[""]/>
        return "d"

print(_F_(6))# <meta[replace] p="1.0" target="6" with=["6","8","4"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.1" target=":" with=[""]/>
    if _A_ > 3:# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="> 3" with=["> 3","> 5","> 2"]/>
        return "a"

print(_F_(4))# <meta[replace] p="1.0" target="4" with=["4","6","1"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.1" target=":" with=[""]/>
    if _A_ > 3:# <meta[replace] p="0.05" target=":" with=[""]/><meta[replace] p="1.0" target="> 3" with=["> 3","> 5","> 4"]/>
        return "a"
    if _A_ > 1:# <meta[replace] p="0.05" target=":" with=[""]/><meta[replace] p="1.0" target="> 1" with=["> 1","> 2","> 0"]/>
        return "b"

print(_F_(4))# <meta[replace] p="1.0" target="4" with=["4","2","1"]/>
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
