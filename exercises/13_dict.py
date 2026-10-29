# <meta[replace] target=["_D_"] with=["d","info","data"]>
# <meta[select]>
# <meta[option]>
_D_ = {"name": "Alice", "age": 20}# <meta[replace] p="1.0" target='"Alice"' with=['"Alice"','"Bob"','"Carol"']/>
print(_D_["name"])# <meta[replace] p="0.25" target='"name"' with=['"name"','"name"',"name",'"age"']/>
# </meta[option]>
# <meta[option]>
_D_ = {"name": "Alice", "age": 20}# <meta[replace] p="1.0" target='"Alice"' with=['"Alice"','"Bob"','"Carol"']/>
print(_D_["score"])# <meta[replace] p="0.5" target='"score"' with=['"score"','"name"']/>
# </meta[option]>
# <meta[option]>
_D_ = {"name": "Alice", "score": 85}# <meta[replace] p="1.0" target="85" with=["85","70","95"]/>
print("name" in _D_)# <meta[replace] p="0.5" target='"name"' with=['"name"','"age"']/>
# </meta[option]>
# <meta[option]>
_D_ = {"name": "Alice", "score": 85}# <meta[replace] p="1.0" target="85" with=["85","70","95"]/>
_D_["score"] = 90# <meta[replace] p="1.0" target="90" with=["90","60","100"]/>
print(_D_["score"])
# </meta[option]>
# <meta[option]>
_D_ = {"name": "Alice", "score": 85}# <meta[replace] p="1.0" target="85" with=["85","70","95"]/>
_D_["age"] = 20# <meta[replace] p="1.0" target="20" with=["20","18","22"]/>
print(_D_["age"])
# </meta[option]>
# </meta[select]>
# </meta[replace]>
