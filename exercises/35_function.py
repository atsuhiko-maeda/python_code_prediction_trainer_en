# <meta[replace] target=["_FA_"] with=["f1","g1","p1"]>
# <meta[replace] target=["_FB_"] with=["f2","g2","p2"]>
# <meta[replace] target=["_FC_"] with=["f3","g3","p3"]>
# <meta[replace] target=["_FD_"] with=["f4","g4","p4"]>
# <meta[select]>
# <meta[option]>
def _FC_():
    print("c")

def _FB_():
    _FC_()
    print("b")

def _FA_():
    _FB_()
    print("a")

_FA_()
# </meta[option]>
# <meta[option]>
def _FB_():
    print("b")

def _FC_():
    print("c")

def _FA_():
    print("a")
    _FB_()
    _FC_()

_FA_()
# </meta[option]>
# <meta[option]>
def _FD_():
    print("d")

def _FC_():
    print("c")

def _FB_():
    _FC_()
    print("b")

def _FA_():
    _FB_()
    _FD_()
    print("a")

_FA_()
# </meta[option]>
# <meta[option]>
def _FD_():
    print("d")

def _FC_():
    _FD_()
    print("c")

def _FB_():
    _FC_()
    print("b")

def _FA_():
    _FB_()
    print("a")

_FA_()
# </meta[option]>
# </meta[select]>
# </meta[replace]>
# </meta[replace]>
# </meta[replace]>
# </meta[replace]>
