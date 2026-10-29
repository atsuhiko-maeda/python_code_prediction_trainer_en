# <meta[replace] target=["_X_"] with=["x","y","n"]>
# <meta[replace] target=["_P_"] with=["p","q","flag"]>
# <meta[select]>
# <meta[option]>
_X_ = 5# <meta[replace] p="1.0" target="5" with=["5","3","8"]/>
result = _X_ == 5# <meta[replace] p="1.0" target="==" with=["==","!=","<",">"]/><meta[replace] p="1.0" target="5" with=["5","3","8"]/>
print(result)
# </meta[option]>
# <meta[option]>
_X_ = 5# <meta[replace] p="1.0" target="5" with=["5","4","7"]/>
print(_X_ > 3 and _X_ < 8)# <meta[replace] p="1.0" target="and" with=["and","or"]/><meta[replace] p="1.0" target="> 3" with=["> 3","> 6","< 3"]/><meta[replace] p="1.0" target="< 8" with=["< 8","< 5","> 2"]/>
# </meta[option]>
# <meta[option]>
_P_ = True# <meta[replace] p="1.0" target="True" with=["True","False"]/>
r = False# <meta[replace] p="1.0" target="False" with=["False","True"]/>
print(_P_ and r)# <meta[replace] p="1.0" target="and" with=["and","or"]/>
# </meta[option]>
# <meta[option]>
_P_ = True# <meta[replace] p="1.0" target="True" with=["True","False"]/>
print(not _P_)
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
