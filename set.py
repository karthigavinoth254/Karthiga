'''#set
s={1,2,3,4,5,6,7}
print(s)
#add and update
s={1,2,3,4,5,6,7}
s.add(3.5)
print(s)
s={1,2}
s.update([3,4,5])
print(s)
#remove
s={1,2,'true',4.5,0,'false'}
s.remove(2)
print(s)
s={1,2,'true',4.5,0,'false'}
s.remove(1)
print(s)
#discard---not generate error if not found
s={1,2,'true',4.5,0,'false'}
s.discard(125)
print(s)
#pop
s={9,8,1,5,3,2}
s.pop()
print(s)
#clear()
s={9,8,1,5,3,2}
s.clear()
print(s)
#del
s={9,8,1,5,3,2}
del s
print(s)
#set methods
#union
#union for a
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.union(b)
print(c)
#union for b
a={1,2,3,4,5}
b={4,5,6,7,8}
c=b.union(a)
print(c)
#intersection for a
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.intersection(b)
print(c)
#intersection for b
a={1,2,3,4,5}
b={4,5,6,7,8}
c=b.intersection(a)
print(c)
#intersection update(a)
a={1,2,3,4,5}
b={4,5,6,7,8}
a.intersection_update(b)
print(a)
#intersection update(b)
a={1,2,3,4,5}
b={4,5,6,7,8}
b.intersection_update(a)
print(b)
#difference for a
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.difference(b)
print(c)
#difference for b
a={1,2,3,4,5}
b={4,5,6,7,8}
c=b.difference(a)
print(c)
#difference update(a)
a={1,2,3,4,5}
b={4,5,6,7,8}
a.difference_update(b)
print(a)
#difference update(b)
a={1,2,3,4,5}
b={4,5,6,7,8}
b.difference_update(a)
print(b)
#symmetric difference(a)
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.symmetric_difference(b)
print(c)
#symmetric difference(b)
a={1,2,3,4,5}
b={4,5,6,7,8}
c=b.symmetric_difference(a)
print(c)
#subset---false
a={1,2,3,4,5}
b={4,5,6,7,8}
print(b.issubset(a))
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.issubset(b))
#subset---true
a={1,2,3,4,5}
b={1,2,3,4,5,6,7}
print(a.issubset(b))
a={1,2,3,4,5,6,7,8}
b={1,2,3,4,5,6,7}
print(b.issubset(a))
#superset
a={1,2,3,4,5,6,7,8}
b={4,5,6,7,8}
print(b.issuperset(a))
a={1,2,3,4,5,6,7,8}
b={4,5,6,7,8}
print(a.issuperset(b))'''

















