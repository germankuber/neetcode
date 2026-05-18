# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # "1,2,3,4,5,N"
        dq = deque([root])
        serialization = ""
        while dq:   
            # [1]
            for _ in range(len(dq)):
                node = dq.popleft()
                if node:
                    serialization += str(node.val) + ","
                
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    serialization += "N,"
                # [2, 3]
                # [3, null, null]
                # [null, null, 4, 5]

        # "1,2,3,N,N,4,5,N,N,N,N,"
        split_in = 0
        for i in range(len(serialization) - 1, 0, -1):
            if serialization[i] != "N" and serialization[i] != ",":
                split_in = i
                break

        return serialization[0:split_in + 1]


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        data = data.split(",")
        print(data)
        dq = deque()

        if data[0] == "N":
            return None

        root = TreeNode(int(data[0]))
        if data:
            dq.append(root)
        
        index = 1

        while index < len(data):
            
            node = dq.popleft()

            left = data[index]
            right = "N"
            if index + 1 < len(data):
                right = data[index + 1]

            if left != "N":
                node.left = TreeNode(int(left))
                dq.append(node.left)

            if right != "N":
                node.right = TreeNode(int(right))
                dq.append(node.right)

            index += 2


        return root