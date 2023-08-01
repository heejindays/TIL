## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node) # 안 중요!

for name in nameAry[1:] : # ['레드벨벳','마마무', ...
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if (name < current.data) :
            if (current.left == None) :
                current.left = node
                break
            else :
                current = current.left
        else :
            if (current.right == None):
                current.right = node
                break
            else:
                current = current.right
    memory.append(node)  # 안 중요!

print('이진 탐색 트리 완료!')