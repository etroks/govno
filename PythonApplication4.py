import sys
sys.stdin = open("input.txt", "r")
dic = {}
opa = True
firstElemDic = []

for i in range(int(input())):
    inputStr = input().split()
    predok = "".join(inputStr[0:1:1])
    if not predok in dic:
        if len(inputStr) > 1:#Создаю новую переменную с предками
            dic.setdefault("".join(inputStr[0:1:1]), set(inputStr[2:len(inputStr):1]))
        else:#Создаю новую пустую переменную, если у нее нет предков
            dic.setdefault("".join(inputStr), "")
    else:#Перезаписываю существующую переменную
        dic[predok] = set(inputStr[2:len(inputStr):1]).union(dic[predok])#
findDic = dic.copy()
print(dic)

while opa:
    opa = False
    for elemDic in dic.items():#Беру элементы мапы по очереди
        firstElemDic = findDic[elemDic[0]]
        if elemDic[1] is not "":
            for predkiElem in elemDic[1]:#Если у первого элемента есть предки, перебераю их
                if (predkiElem in dic):
                    if not (dic[predkiElem] in findDic[elemDic[0]]):
                        findDic[elemDic[0]] = elemDic[1].union(findDic[predkiElem])
        if not (firstElemDic == findDic[elemDic[0]]):#Если ничего не поменялось, продолжаем
            opa = True
        else:
            opa = False
print(findDic)

for i in range(int(input())):
    opa = False
    inputStr = input().split()
    a="".join(inputStr[1::1])
    b="".join(inputStr[0:1:1])
    if "".join(inputStr[1::1]) in findDic:
        for i in findDic["".join(inputStr[1::1])]:
            if i == "".join(inputStr[0:1:1]):
                opa = True
        if opa or (inputStr[0:1:1] == inputStr[0:1:1]):
            print("Yes")
        else:
            print("No")
    else:
        if (inputStr[0:1:1] == inputStr[2:len(inputStr):1]):
            print("Yes")
        else:
            print("No")

#for val in dic.keys():
#    finDic.update()