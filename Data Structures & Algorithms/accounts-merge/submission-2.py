from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            parent = self.parent[node]
            grandparent = self.parent[parent]

            self.parent[node] = grandparent

            node = grandparent

        return node

    def union(self, node_a: int, node_b: int) -> bool:
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a == root_b:
            return False

        self.parent[root_a] = root_b
        return True
    
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(len(accounts))
        
        email_to_account : dict[str, int] = {}
        
        for index, account in enumerate(accounts):

            for email in account[1:]:
                
                if email not in email_to_account:
                    email_to_account[email] = index
                else:
                    union_find.union(index, email_to_account[email])
                    
        
        email_group =  defaultdict(list)
        
        for email, index in email_to_account.items():
            account_owner =  union_find.find(index)
            email_group[account_owner].append(email)
            
        result = []
        
        for index, _ in email_group.items():
            name = accounts[index][0]
            result.append([name] + sorted(email_group[index]))
            
        return result