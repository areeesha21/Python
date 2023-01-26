x={1,2,3,4,5,6}
y={4,5,6,7,8,9,10}

print(x)
print(y)
print('union')
print(x|y)
print('intersection')
print(x &y)
print('difference')
print('unique values in x=>,x - y')
print('unique values in y=>,y -x')
print('symmetric difference')
print('x ^ y') #same as x.symmetric_difference
z={10,11,12,13}

print('disjoint sets')
print('kya x or y me kuch common nhi hai=>',x.isdisjoint(y))
print('kya x or z me kuch common nhi hai=>',x.isdisjoint(z))
print('kya z or y me kuch common nhi hai=>',z.isdisjoint(y))

items={'apple','orange','banana','potato','tomato','brinjal'}
fruits={'apple','orange','banana'}
vegetables={'potato','tomato','brinjal','cucumber'}
print('subset')
print('fruits belong to item',fruits.issubset(items))
print('vegetables belong to item',vegetables.issubset(items))
