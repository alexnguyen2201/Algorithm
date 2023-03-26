from sortedcontainers import SortedDict
from collections import OrderedDict
from collections import defaultdict

d = SortedDict()
d2 = OrderedDict()


d[1] = "good"
d[3] = 'hello3'
d[4] = 'hello4'
d[2] = 'hello2'
d[-1] = 'negative1'
d[-100] = 'negative100'
print(d)

s = d.values()

for i in s:
    print(i)

d2[1] = "good"
d2[3] = 'hello3'
d2[4] = 'hello4'
d2[2] = 'hello2'
d2[-1] = 'negative1'
d2[-100] = 'negative100'
print(d2)
s2 = OrderedDict(sorted(d2.items()))
print(s2)
print(s2[-100])

s = d2.values()

for i in s:
    print(i)


d2 = defaultdict(str)
d2[1] = "good"
d2[3] = 'hello3'
d2[4] = 'hello4'
d2[2] = 'hello2'
d2[-1] = 'negative'
d2[-100] = 'negative100'

print(d2)
