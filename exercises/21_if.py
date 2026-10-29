# <meta[replace] target=["_X_"] with=["x","a","n"]>
# <meta[select]>
# <meta[option]>
_X_ = 6# <meta[replace] p="1.0" target="6" with=["6","3","8"]/>
if _X_ > 4:# <meta[replace] p="0.2" target=":" with=[""]/><meta[replace] p="1.0" target="> 4" with=["> 4","< 4","== 4","> 2"]/>
    print("A")
# </meta[option]>
# <meta[option]>
_X_ = 6# <meta[replace] p="1.0" target="6" with=["6","3","8"]/>
if _X_ > 4:# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="> 4" with=["> 4","< 4","== 4"]/>
    print("A")
else:# <meta[replace] p="0.1" target=":" with=[""]/>
    print("B")
# </meta[option]>
# <meta[option]>
_X_ = 6# <meta[replace] p="1.0" target="6" with=["6","3","8"]/>
if _X_ > 7:# <meta[replace] p="0.07" target=":" with=[""]/><meta[replace] p="1.0" target="> 7" with=["> 7","< 3","== 6"]/>
    print("A")
elif _X_ > 4:# <meta[replace] p="0.07" target=":" with=[""]/><meta[replace] p="1.0" target="> 4" with=["> 4","< 7","== 3"]/>
    print("B")
else:# <meta[replace] p="0.07" target=":" with=[""]/>
    print("C")
# </meta[option]>
# <meta[option]>
_X_ = 6# <meta[replace] p="1.0" target="6" with=["6","3","8"]/>
if _X_ > 2:# <meta[replace] p="0.07" target=":" with=[""]/><meta[replace] p="1.0" target="> 2" with=["> 2","< 9","< 5"]/>
    if _X_ > 5:# <meta[replace] p="0.07" target=":" with=[""]/><meta[replace] p="1.0" target="> 5" with=["> 5","< 8","== 6"]/>
        print("A")
    else:# <meta[replace] p="0.07" target=":" with=[""]/>
        print("B")
else:
    print("C")
# </meta[option]>
# <meta[option]>
_X_ = 6# <meta[replace] p="1.0" target="6" with=["6","3","8"]/>
if _X_ > 4:# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="> 4" with=["> 4","< 8","== 6"]/>
    print("A")
if _X_ > 7:# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="> 7" with=["> 7","< 5","== 3"]/>
    print("B")
else:
    print("C")
# </meta[option]>
# <meta[option]>
_X_ = 6# <meta[replace] p="1.0" target="6" with=["6","2","9"]/>
if _X_ > 4:# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="> 4" with=["> 4","< 8","== 6"]/>
    if _X_ > 7:# <meta[replace] p="0.1" target=":" with=[""]/><meta[replace] p="1.0" target="> 7" with=["> 7","< 4","== 2"]/>
        print("A")
    print("B")
else:
    print("C")
# </meta[option]>
# </meta[select]>
# </meta[replace]>
