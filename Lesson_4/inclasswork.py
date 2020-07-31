
def divide(a, b):
    try:
        print(a/b)
    except:
        print('Cannot divide by 0')

divide(10,2)


f = open('d:/TEKWILL/PYTHON/MARATHON/Lesson_4/key.txt')
r = f.read()
print(r)
f.close()

with open('D:\TEKWILL\PYTHON\MARATHON\Lesson_4\key.txt') as f:
    data = f.read()
    print(data)
    f.close