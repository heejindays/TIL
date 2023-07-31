## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre
    # Case1 : 하필이면 머리(head) 앞에 삽입 (다현, 화사)
    if (head.data == findData) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node) # 안 중요!
        return
    # Case2 : 중간 노드 앞에 삽입 (사나, 솔라)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node =  Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요!
            return
    # Case3 : 없는 노드 앞에 삽입(==추가) (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요!
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    # Case1 : 하필 머리를 삭제할 때. (다현)
    if (head.data == deleteData) :
        current = head
        head = head.link
        del(current)
        return
    # Case2 : 중간 노드를 삭제할 때. (쯔위)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == deleteData) :
            pre.link = current.link
            del (current)
            return
    # Case3 : 삭제할 노드가 없을 때 (재남)
    return

def  findNode(findData) :
    global memory, head, current, pre
    current = head
    if (current.data == findData) :
        return current
    while (current.link != None) :
        current = current.link
        if (current.data == findData) :
            return current
    return Node()

## 전역
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 실제 사용 데이터 모음

## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요!

for data in dataArray[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요!

printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)

# insertNode('사나', '솔라')
# printNodes(head)

# insertNode('재남', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)

# deleteNode('쯔위')
# printNodes(head)

# deleteNode('재남')
# printNodes(head)

fNode = findNode('사나')
print(fNode.data, '뮤비가 나옵니다. ~~ 쿵짝쿵짝')
