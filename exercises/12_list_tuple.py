# <meta[replace] target=["_A_"] with=["a","b","data"]>
# <meta[select]>
# <meta[option]>
_A_ = [10, 20, 30, 40, 50]# <meta[replace] p="1.0" target="\[10, 20, 30, 40, 50\]" with=["\[10, 20, 30, 40, 50\]","\[1, 2, 3, 4, 5\]","\[3, 6, 9, 12, 15\]"]/>
print(_A_[0])# <meta[replace] p="1.0" target="0" with=["0","2","4"]/>
# </meta[option]>
# <meta[option]>
_A_ = [10, 20, 30, 40, 50]# <meta[replace] p="1.0" target="\[10, 20, 30, 40, 50\]" with=["\[10, 20, 30, 40, 50\]","\[1, 2, 3, 4, 5\]","\[3, 6, 9, 12, 15\]"]/>
print(_A_[-1])# <meta[replace] p="1.0" target="-1" with=["-1","-2","-3"]/>
# </meta[option]>
# <meta[option]>
_A_ = (10, 20, 30, 40, 50)# <meta[replace] p="1.0" target="(10, 20, 30, 40, 50)" with=["(10, 20, 30, 40, 50)","(1, 2, 3, 4, 5)","(3, 6, 9, 12, 15)"]/>
print(_A_[0])# <meta[replace] p="1.0" target="0" with=["0","2","4"]/>
# </meta[option]>
# <meta[option]>
_A_ = (10, 20, 30, 40, 50)# <meta[replace] p="1.0" target="(10, 20, 30, 40, 50)" with=["(10, 20, 30, 40, 50)","(1, 2, 3, 4, 5)","(3, 6, 9, 12, 15)"]/>
print(_A_[-2])# <meta[replace] p="1.0" target="-2" with=["-2","-1","-3"]/>
# </meta[option]>
# <meta[option]>
_A_ = [10, 20, 30, 40, 50]# <meta[replace] p="1.0" target="\[10, 20, 30, 40, 50\]" with=["\[10, 20, 30, 40, 50\]","\[1, 2, 3, 4, 5\]","\[3, 6, 9, 12, 15\]"]/>
print(_A_[:3])# <meta[replace] p="1.0" target=":3" with=[":3",":2",":4"]/>
# </meta[option]>
# <meta[option]>
_A_ = [10, 20, 30, 40, 50]# <meta[replace] p="1.0" target="\[10, 20, 30, 40, 50\]" with=["\[10, 20, 30, 40, 50\]","\[1, 2, 3, 4, 5\]","\[3, 6, 9, 12, 15\]"]/>
print(_A_[2:])# <meta[replace] p="1.0" target="2:" with=["2:","1:","3:"]/>
# </meta[option]>
# <meta[option]>
_A_ = [10, 20, 30, 40, 50]# <meta[replace] p="1.0" target="\[10, 20, 30, 40, 50\]" with=["\[10, 20, 30, 40, 50\]","\[1, 2, 3, 4, 5\]","\[3, 6, 9, 12, 15\]"]/>
print(_A_[-2:])# <meta[replace] p="1.0" target="-2:" with=["-2:","-3:",":-2",":-1"]/>
# </meta[option]>
# <meta[option]>
_A_ = [10, 20, 30, 40, 50]# <meta[replace] p="1.0" target="\[10, 20, 30, 40, 50\]" with=["\[10, 20, 30, 40, 50\]","\[1, 2, 3, 4, 5\]","\[3, 6, 9, 12, 15\]"]/>
_A_[2] = 99# <meta[replace] p="1.0" target="99" with=["99","7","100"]/>
print(_A_)
# </meta[option]>
# <meta[option]>
_A_ = (10, 20, 30, 40, 50)# <meta[replace] p="1.0" target="(10, 20, 30, 40, 50)" with=["(10, 20, 30, 40, 50)","(1, 2, 3, 4, 5)","(3, 6, 9, 12, 15)"]/>
_A_[1] = 99# <meta[replace] p="1.0" target="99" with=["99","7","100"]/>
print(_A_)
# </meta[option]>
# </meta[select]>
# </meta[replace]>
