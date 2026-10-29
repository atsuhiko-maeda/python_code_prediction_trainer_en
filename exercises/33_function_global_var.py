# <meta[replace] target=["_VAR_"] with=["count","score","total"]>
# <meta[replace] target=["_FUNC_"] with=["update","add","change"]>
# <meta[select]>
# <meta[option]>
_VAR_ = 10# <meta[replace] p="1.0" target="10" with=["10","5","20"]/>
def _FUNC_():# <meta[replace] p="0.2" target=":" with=[""]/>
    print(_VAR_)

_FUNC_()
print(_VAR_)
# </meta[option]>
# <meta[option]>
_VAR_ = 10# <meta[replace] p="1.0" target="10" with=["10","5","20"]/>
def _FUNC_():# <meta[replace] p="0.2" target=":" with=[""]/>
    _VAR_ = 99# <meta[replace] p="1.0" target="99" with=["99","0","1"]/>
    print(_VAR_)

_FUNC_()
print(_VAR_)
# </meta[option]>
# <meta[option]>
_VAR_ = 10# <meta[replace] p="1.0" target="10" with=["10","5","20"]/>
def _FUNC_():# <meta[replace] p="0.2" target=":" with=[""]/>
    global _VAR_# <meta[skipLine] p="0.5"/>
    _VAR_ = 99# <meta[replace] p="1.0" target="99" with=["99","0","1"]/><meta[replace] p="1.0" target="=" with=["=","+=","= _VAR_+"]/>
    print(_VAR_)

_FUNC_()
print(_VAR_)
# </meta[option]>
# <meta[option]>
_VAR_ = 10# <meta[replace] p="1.0" target="10" with=["10","5","20"]/>
def _FUNC_():# <meta[replace] p="0.2" target=":" with=[""]/>
    _VAR_ = 3# <meta[replace] p="1.0" target="3" with=["3","2","4"]/>
    _VAR_ = _VAR_ + 1
    print(_VAR_)

_FUNC_()
print(_VAR_)
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
