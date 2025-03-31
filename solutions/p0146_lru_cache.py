"""
LeetCode #146: LRU Cache
Difficulty: Medium
Topics: Hash Table, Linked List, Design, Doubly Linked List
Companies: Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Oracle, eBay, Palo Alto Networks, Gartner
URL: https://leetcode.com/problems/lru-cache/
"""

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.map = dict()  # {key, Node}

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map.get(key)
        # update d-linked list
        self.remove_node(node)
        self.add_node(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.used < self.capacity:  # still has capacity
                new_node = Node(key, value)
                self.map[key] = new_node
                self.add_node(new_node)
                self.used += 1
            else:  # no more capacity
                # remove the least used node
                removing_node = self.tail.prev
                self.remove_node(removing_node)
                removing_key = removing_node.key
                del self.map[removing_key]
                # add new node
                new_node = Node(key, value)
                self.map[key] = new_node
                self.add_node(new_node)
        else:
            updating_node = self.map.get(key)
            # update the value
            updating_node.value = value
            # update the d-linked list
            self.remove_node(updating_node)
            self.add_node(updating_node)


    def remove_node(self, node: Node) -> None:
        # clean up the selected node
        prev_node = node.prev
        next_node = node.next
        node.prev = None
        node.next = None

        # connect prev and next nodes
        prev_node.next = next_node
        next_node.prev = prev_node
    

    def add_node(self, node: Node) -> None:
        prev_first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = prev_first_node
        prev_first_node.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)