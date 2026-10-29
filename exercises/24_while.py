# <meta[replace] target=["_V_"] with=["i","x","n"]>
# <meta[select]>
# <meta[option]>
_V_ = 0# <meta[replace] p="1.0" target="0" with=["0","1","0"]/>
while _V_ < 3:# <meta[replace] p="1.0" target="3" with=["3","4","5"]/>
    print(_V_)
    _V_ += 1
# </meta[option]>
# <meta[option]>
_V_ = 0# <meta[replace] p="1.0" target="0" with=["0","1","0"]/>
while _V_ < 3:# <meta[replace] p="1.0" target="3" with=["3","4","5"]/>
    _V_ += 1
    print(_V_)
# </meta[option]>
# <meta[option]>
_V_ = 5# <meta[replace] p="1.0" target="5" with=["5","4","6"]/>
while _V_ > 2:# <meta[replace] p="1.0" target="2" with=["2","1","3"]/>
    print(_V_)
    _V_ -= 1
# </meta[option]>
# <meta[option]>
_V_ = 5# <meta[replace] p="1.0" target="5" with=["5","4","6"]/>
while _V_ > 2:# <meta[replace] p="1.0" target="2" with=["2","1","3"]/>
    _V_ -= 1
    print(_V_)
# </meta[option]>
# <meta[option]>
_V_ = 3# <meta[replace] p="1.0" target="3" with=["3","5","4"]/>
while _V_ < 3:# <meta[replace] p="1.0" target="< 3" with=["< 3","< 5","< 4"]/>
    print(_V_)
    _V_ += 1
print("z")
# </meta[option]>
# </meta[select]>
# </meta[replace]>
