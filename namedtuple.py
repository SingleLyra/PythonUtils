from collections import namedtuple
Pair = namedtuple("pair", "first second")
pair_eg = Pair(first=233, second=666)
print(pair_eg.first) # pair_eg[1]
print(pair_eg.second) # pair_eg[2]
fi, se = pair_eg
print(fi, se)

# some materials: https://www.geeksforgeeks.org/namedtuple-in-python/
# https://qiubite31.github.io/2017/03/02/%E4%BD%BF%E7%94%A8collections%E4%B8%AD%E7%9A%84namedtuple%E4%BE%86%E6%93%8D%E4%BD%9C%E7%B0%A1%E5%96%AE%E7%9A%84%E7%89%A9%E4%BB%B6%E7%B5%90%E6%A7%8B/