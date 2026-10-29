# <meta[replace] target=["_S_"] with=["s","t","name"]>
# <meta[replace] target=["_W_"] with=["hello","world","python"]>
# <meta[select]>
# <meta[option]>
_S_ = "_W_"# <meta[replace] p="1.0" target=['"_W_"'] with=['"_W_"','"_W_"',"_W_"]/>
print(_S_)
# </meta[option]>
# <meta[option]>
"_W_" = _S_
print(_S_)
# </meta[option]>
# <meta[option]>
a = 3# <meta[replace] p="1.0" target="3" with=["3","5","7"]/>
b = 4# <meta[replace] p="1.0" target="4" with=["4","2","6"]/>
print(a + b)
print(str(a) + str(b))# <meta[replace] p="0.25" target="str(a) + str(b)" with=["str(a) + str(b)","a + str(b)","str(a) + b","a + b"]/>
# </meta[option]>
# <meta[option]>
_S_ = "_W_"
print(_S_[0])# <meta[replace] p="1.0" target="0" with=["0","1","2"]/>
print(_S_[1:4])# <meta[replace] p="1.0" target="1:4" with=["1:4","0:3","2:5"]/>
# </meta[option]>
# <meta[option]>
_S_ = "_W_"
n = 2# <meta[replace] p="1.0" target="2" with=["2","5","7"]/>
print(f"_S_={_S_}, n={n}")# <meta[replace] p="0.3" target='f"' with=['"']/>
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
