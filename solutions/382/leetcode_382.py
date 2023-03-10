#------------------------------------------------------
# Solution 1 - array of nodes
#------------------------------------------------------

# Runtime:  79.00%
# Memory:   15.80%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = []

        node = head
        while node:
            self.nodes.append(node)
            node = node.next
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nodes)-1)
        return self.nodes[index].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()



#------------------------------------------------------
# Solution 2 - array of nodes (cache len)
#------------------------------------------------------

# Runtime:  59.85%
# Memory:   15.80%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = []

        node = head
        while node:
            self.nodes.append(node)
            node = node.next

        self.node_count = len(self.nodes) - 1
        

    def getRandom(self) -> int:
        return self.nodes[random.randint(0, self.node_count)].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()




#------------------------------------------------------
# Solution 3 - array of node values
#------------------------------------------------------

# Runtime:  76.39%
# Memory:   15.80%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = []

        node = head
        while node:
            self.nodes.append(node.val)
            node = node.next
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nodes)-1)
        return self.nodes[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()



#------------------------------------------------------
# Solution 4 - set of nodes
#------------------------------------------------------

# Runtime:  24.35%
# Memory:   05.39%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodes = set()

        node = head
        while node:
            self.nodes.add(node)
            node = node.next
        

    def getRandom(self) -> int:
        node = random.sample(self.nodes, 1)
        return node[0].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()



#------------------------------------------------------
# Solution 5 - random offset in init
#------------------------------------------------------

# Runtime:  16.73%
# Memory:   97.21%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.node = head

        offset = random.randint(0, 10000)
        
        for i in range(offset):
            self.node = self.node.next
            if self.node == None:
                self.node = head
        

    def getRandom(self) -> int:
        offset = random.randint(0, 100)

        for i in range(offset):
            self.node = self.node.next
            if self.node == None:
                self.node = self.head

        return self.node.val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()



#------------------------------------------------------
# Solution 6 - random offset in init w/ cached len
#------------------------------------------------------

# Runtime:  40.89%
# Memory:   35.13%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.node = head

        offset = random.randint(0, 10000)
        self.count = 0
        
        for i in range(offset):
            self.node = self.node.next
            self.count += 1
            if self.node == None:
                self.node = head
                
                offset = random.randint(0, self.count)
                for i in range(offset):
                    self.node = self.node.next
                    if self.node == None:
                        self.node = self.head
                break

        
        

    def getRandom(self) -> int:
        offset = random.randint(0, self.count)

        for i in range(offset):
            self.node = self.node.next
            if self.node == None:
                self.node = self.head

        return self.node.val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
