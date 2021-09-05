# 단일 연결 리스트 구현

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # 노드 삽입
    def append(self,node):
        # 단일연결리스트 첫 노드 생성
        if self.head == None:
            self.head = node
        # 마지막 노드 까지 커서 옮기고 연결
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # data 위치 찾기 (일치하는것 중 가장 먼저 위치한 노드의 인덱스 반환)
    def getDataIndex(self,data):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1  # data가 존재하지 않는 경우

    # 주어진 위치에 노드 삽입
    def insertNodeAtIndex(self, idx, node):
        cur = self.head
        prevn = None
        cur_idx = 0

        # (1) 리스트 맨 앞에 삽입
        if idx == 0:
            # 리스트가 생성되어 있는 경우(head 노드가 있을 때) - head 앞에 추가
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn

            # 리스트가 비어있는 경우 - 새로 리스트 만들기
            else:
                self.head = node
        else:
            # (2) 리스트 내에 삽입 &
            # (3) 리스트 마지막에 삽입
            while cur_idx < idx:
                if cur:
                    prevn = cur
                    cur = cur.next
                else:
                    break
                cur_idx += 1
            if cur_idx == idx:
                node.next = cur
                prevn.next = node
            else:
                return -1

    # 주어진 data의 위치에 노드 삽입하기
    def insertNodeAtData(self, data, node):
        idx = self.getDataIndex(data)
        if idx >= 0:
            self.insertNodeAtIndex(idx, node)
        else:
            return -1

    # 주어진 위치의 노드 삭제
    def deleteAtIndex(self, idx):
        cur_idx = 0
        cur = self.head
        prevn = None
        nextn = self.head.next
        if idx == 0:
            self.head = nextn
        else:
            while cur_idx < idx:
                if cur.next:
                    prevn = cur
                    cur = nextn
                    cur = nextn.next
                else:
                    break
                cur_idx += 1
            if cur_idx == idx:
                prevn.next = nextn
            else:
                return -1

    # 리스트 초기화
    def clear(self):
        self.head = None

    # 출력
    def print(self):
        cur = self.head
        s = ""
        while cur:
            s += str(cur.data)
            if cur.next:
                s += "->"
            cur = cur.next
        print(s)

if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insertNodeAtIndex(3, Node(4))
    sl.print()
    print(sl.getDataIndex(1))
    print(sl.getDataIndex(2))
    print(sl.getDataIndex(3))
    print(sl.getDataIndex(4))
    print(sl.getDataIndex(5))
    sl.insertNodeAtData(1, Node(0))
    sl.print()

