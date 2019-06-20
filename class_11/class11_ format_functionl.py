print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
print('{},{},{}'.format('apple','banana','carrot'))
print('{2},{1},{0}'.format('apple','banana','carrot'))
print('{2},{1},{1},{0}'.format('apple','banana','carrot'))
print('{2},{1},{0}'.format(*'abcd'))
print('{0},{1},{0}'.format('apple','banana','carrot'))
print('coordinates:{lattitude},{longitude}'.format(lattitude='37.24N',longitude='-115.84W'))
print('wellcome:{name},your college is:{college}'.format(name='harsh',college='vips'))
coord={'lattitude':'37.24N','longitude':'-115.84W'}
print('coordinate:{lattitude},{longitude}'.format(**coord))
c=3-5j
print('the complex number {0} is formed from the real\
part {0.real} and imaginary part{0.imag}'.format(c))
coord=(3,5)
abc=(2,9)
print('x:{0[0]};y:{0[1]};abc:{1[0]},{1[1]}'.format(coord,abc))
coord=[(3,9),(2,4)]
print('first tuple:{0[0]},{0[1]},second tuple:{1[0]},{1[1]}'.format(*coord))
print('{:#<30}'.format('apple'))
print('{:*>30}'.format('apple'))
print('{:^30}'.format('apple'))
print('{:*^30}'.format('apple'))
print("int:{0:d};hex:{0:x};oct:{0:o};bin{0:b}".format(42,55))
print("int:{1:d};hex:{1:x};oct:{1:0o};bin{1:b}".format(42,55))
print('{:,}'.format(123467890))
point=19.0;total=22
print('correct answers:{:.4%}'.format(point/total))
