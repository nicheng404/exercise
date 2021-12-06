li = ['alex1', 'taibai2', 'wusir3', 'egon4']
demo = []
for i in li:
    length = len(i)
    subStr = i[0:length - 1]
    str = i[length - 1] + subStr
    demo.append(str)
demo.sort()

resDemo = []

for i in demo:
    word = i[1:len(i)]
    resDemo.append(word)
res = ' '.join(resDemo)
print(res)
