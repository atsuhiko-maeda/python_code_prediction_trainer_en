# <meta[replace] target=["_F_"] with=["greet","calc","show"]>
# <meta[replace] target=["_A_"] with=["a","x","n"]>
# <meta[replace] target=["_B_"] with=["b","y","m"]>
# <meta[select]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.15" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.15" target="    print" with=["print"]/>

_F_(3)# <meta[replace] p="1.0" target="3" with=["3","5","7"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.15" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.15" target="    print" with=["print"]/>

v = 4# <meta[replace] p="1.0" target="4" with=["4","6","8"]/>
_F_(v)
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.15" target=":" with=[""]/>
    return _A_ + 1# <meta[replace] p="1.0" target="1" with=["1","2","3"]/><meta[replace] p="0.15" target="    return" with=["return"]/>

print(_F_(3))# <meta[replace] p="1.0" target="3" with=["3","5","7"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_, _B_):# <meta[replace] p="0.15" target=":" with=[""]/>
    return _A_ + _B_# <meta[replace] p="0.15" target="    return" with=["return"]/>

v = 3# <meta[replace] p="1.0" target="3" with=["3","4","5"]/>
print(_F_(v, 2))# <meta[replace] p="1.0" target="2" with=["2","3","1"]/>
# </meta[option]>
# <meta[option]>
def _F_():# <meta[replace] p="0.15" target=":" with=[""]/>
    print("a")# <meta[replace] p="0.15" target="    print" with=["print"]/>

_F_()
_F_()
_F_()
# </meta[option]>
# <meta[option]>
def _F_(_A_):# <meta[replace] p="0.15" target=":" with=[""]/>
    return _A_ * 2# <meta[replace] p="1.0" target="2" with=["2","3","4"]/><meta[replace] p="0.15" target="    return" with=["return"]/>

r = _F_(3)# <meta[replace] p="1.0" target="3" with=["3","4","5"]/>
print(r)
print(_F_(6))# <meta[replace] p="1.0" target="6" with=["6","5","7"]/>
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
# </meta[replace]>
