# <meta[replace] target=["_A_"] with=["a","x","n"]>
# <meta[replace] target=["_B_"] with=["b","y","m"]>
# <meta[select]>
# <meta[option]>
_A_ = 8# <meta[replace] p="1.0" target="8" with=["8","6","12"]/>
_B_ = 3# <meta[replace] p="1.0" target="3" with=["3","2","4"]/>
print(_A_ + _B_)
print(_A_ - _B_)
print(_A_ * _B_)
# </meta[option]>
# <meta[option]>
_A_ = 12
_B_ = 4# <meta[replace] p="1.0" target="4" with=["4","3","6","2"]/>
print(_A_ / _B_)
print(_A_ // _B_)
print(_A_ % 5)# <meta[replace] p="1.0" target="5" with=["5","7","8"]/>
# </meta[option]>
# <meta[option]>
_A_ = 4# <meta[replace] p="1.0" target="4" with=["4","2","6"]/>
print(_A_)
_A_ = _A_ + 3# <meta[replace] p="1.0" target="3" with=["3","5","10"]/>
print(_A_)
_A_ = _A_ * 2# <meta[replace] p="1.0" target="2" with=["2","3"]/>
print(_A_)
# </meta[option]>
# <meta[option]>
_A_ = 10# <meta[replace] p="1.0" target="10" with=["10","8","6"]/>
print(_A_)
_A_ += 5# <meta[replace] p="1.0" target="+=" with=["+=","-=","*="]/>
print(_A_)
_A_ %= 4# <meta[replace] p="1.0" target="4" with=["4","3","6"]/>
print(_A_)
# </meta[option]>
# <meta[option]>
_A_ = 5# <meta[replace] p="1.0" target="5" with=["5","3","7"]/>
_B_ = 2# <meta[replace] p="1.0" target="2" with=["2","4","6"]/>
_A_ =+ _B_# <meta[replace] p="0.5" target="=+" with=["=+","+="]/>
print(_A_)
_A_ == 10# <meta[replace] p="0.5" target="==" with=["==","="]/>
print(_A_)
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
