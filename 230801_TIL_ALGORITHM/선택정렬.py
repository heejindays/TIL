## 함수
import random
def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1) : # 사이클
        minIdx = i
        for k in range(i+1, n) : # 작은 반복문
            if (ary[minIdx] > ary[k]) :
                minIdx = k
        ary[minIdx], ary[i] = ary[i], ary[minIdx]
    return ary

## 변수
dataAry = [random.randint(30, 190) for _ in range(8)]

## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)