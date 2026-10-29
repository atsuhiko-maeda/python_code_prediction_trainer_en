# <meta[replace] target=["_F_"] with=["func","check","total"]>
# <meta[replace] target=["_L_"] with=["nums","data","lst"]>
# <meta[replace] target=["_C_"] with=["cnt","c","n"]>
# <meta[replace] target=["_I_"] with=["i","v","x"]>
# <meta[select]>
# <meta[option]>
def _F_(_L_):# <meta[replace] p="0.1" target=":" with=[""]/>
    _C_ = 0
    for _I_ in _L_:# <meta[replace] p="0.1" target=":" with=[""]/>
        _C_ += 1
    return _C_

print(_F_([1, 2, 3, 4, 5]))# <meta[replace] p="1.0" target="\[1, 2, 3, 4, 5\]" with=["\[1, 2, 3, 4, 5\]","\[2, 4, 6, 8\]","\[1, 3, 5, 7\]"]/>
# </meta[option]>
# <meta[option]>
def _F_(_L_):# <meta[replace] p="0.1" target=":" with=[""]/>
    _C_ = 0
    for _I_ in _L_:# <meta[replace] p="0.1" target=":" with=[""]/>
        if _I_ % 2 == 0:# <meta[replace] p="0.1" target=":" with=[""]/>
            _C_ += 1
    return _C_

print(_F_([1, 2, 3, 4, 5]))# <meta[replace] p="1.0" target="\[1, 2, 3, 4, 5\]" with=["\[1, 2, 3, 4, 5\]","\[2, 4, 6, 8\]","\[1, 2, 4, 5\]"]/>
# </meta[option]>
# <meta[option]>
def _F_(_L_):# <meta[replace] p="0.1" target=":" with=[""]/>
    _C_ = 0
    for _I_ in _L_:# <meta[replace] p="0.1" target=":" with=[""]/>
        if _I_ % 2 != 0:# <meta[replace] p="0.1" target=":" with=[""]/>
            _C_ += 1
    return _C_

print(_F_([1, 2, 3, 4, 5]))# <meta[replace] p="1.0" target="\[1, 2, 3, 4, 5\]" with=["\[1, 2, 3, 4, 5\]","\[1, 3, 5, 7\]","\[1, 2, 4, 5\]"]/>
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
# </meta[replace]>
# </meta[replace]>
