# <meta[replace] target=["_F_"] with=["greet","calc","show"]>
# <meta[replace] target=["_A_"] with=["a","x","n"]>
# <meta[select]>
# <meta[option]>
def _F_(_A_=1):# <meta[replace] p="1.0" target="1" with=["1","2","3"]/><meta[replace] p="0.1" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.1" target="    print" with=["print"]/>

_F_(5)# <meta[replace] p="1.0" target="5" with=["5","7","10"]/>
# </meta[option]>
# <meta[option]>
def _F_(_A_=1):# <meta[replace] p="1.0" target="1" with=["1","2","3"]/><meta[replace] p="0.1" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.1" target="    print" with=["print"]/>

_F_()
# </meta[option]>
# <meta[option]>
def _F_(_A_=1):# <meta[replace] p="1.0" target="1" with=["1","2","3"]/><meta[replace] p="0.1" target=":" with=[""]/>
    return _A_ + 1# <meta[replace] p="1.0" target="+ 1" with=["+ 1","* 2","+ 3"]/><meta[replace] p="0.2" target="    return" with=["    return","return"]/>

print(_F_(5))# <meta[replace] p="1.0" target="5" with=["5","4","6"]/>
print(_F_())
# </meta[option]>
# <meta[option]>
def _F_(_A_=1):# <meta[replace] p="1.0" target="1" with=["1","2","3"]/><meta[replace] p="0.1" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.1" target="    print" with=["print"]/>

_F_(5)# <meta[replace] p="1.0" target="5" with=["5","7","10"]/>
_F_()
# </meta[option]>
# <meta[option]>
def _F_(_A_="hello"):# <meta[replace] p="1.0" target='"hello"' with=['"hello"','"world"','"hi"']/><meta[replace] p="0.1" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.1" target="    print" with=["print"]/>

_F_("bye")# <meta[replace] p="1.0" target='"bye"' with=['"bye"','"ok"','"yes"']/>
# </meta[option]>
# <meta[option]>
def _F_(_A_="hello"):# <meta[replace] p="1.0" target='"hello"' with=['"hello"','"world"','"hi"']/><meta[replace] p="0.1" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.1" target="    print" with=["print"]/>

_F_()
# </meta[option]>
# <meta[option]>
def _F_(_A_="hello"):# <meta[replace] p="1.0" target='"hello"' with=['"hello"','"world"','"hi"']/><meta[replace] p="0.1" target=":" with=[""]/>
    print(_A_)# <meta[replace] p="0.1" target="    print" with=["print"]/>

_F_("bye")# <meta[replace] p="1.0" target='"bye"' with=['"bye"','"ok"','"yes"']/>
_F_()
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
