class LRUCache:
    """Least Recent Cache"""

    class DoublyLinkedList:
        """Doubly-linked list"""

        class Node:
            """Node in a doubly-linked list"""

            def __init__(self, key: int, value: int, prev=None, next=None):
                self.key = key
                self.value = value
                self.prev = prev
                self.next = next

        def __init__(self, node: Node | None = None):
            self.head = node
            self.tail = node
            if node is None:
                self.length = 0
            else:
                self.length = 1

        def _push(self, node: Node) -> Node:
            if not isinstance(node, self.Node):
                raise TypeError("Argument must be a Node")
            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.length += 1
            return node

        def append(self, key: int, value: int) -> Node:
            node = self.Node(key, value, self.tail, None)
            return self._push(node)

        def _pop(self, node: Node) -> Node:
            if not isinstance(node, self.Node):
                raise TypeError("Argument must be a Node")
            # If not the head, point the previous node to the next node.
            # Otherwise, move the head to the next node.
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            # If not the tail, point the next node to the previous node.
            # Otherwise, point the tail to the previous node.
            if node.next is not None:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            node.prev = self.tail
            node.next = None
            self.length -= 1
            return node

        def move_to_end(self, node: Node):
            self._push(self._pop(node))

        def evict_lru(self) -> int:
            # If empty, return.
            if self.head is None:
                return -1
            # If not empty, move head to next node.
            evicted = self.head
            self.head = evicted.next
            # If new head is not None, fix back-pointer to None.
            # Otherwise, fix tail to None.
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.length -= 1
            return evicted.key

    def __init__(self, capacity: int):
        self.cache: dict[int, LRUCache.DoublyLinkedList.Node] = {}
        self.capacity: int = capacity
        self.access_history: LRUCache.DoublyLinkedList = \
            self.DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.access_history.move_to_end(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.access_history.move_to_end(node)
        else:
            if self.access_history.length == self.capacity:
                if (evicted_key := self.access_history.evict_lru()) != -1:
                    self.cache.pop(evicted_key)
            self.cache[key] = self.access_history.append(key, value)

    def __str__(self) -> str:
        cursor = self.access_history.head
        string_prefix = "{"
        string_suffix = "}"
        string = ""
        while cursor is not None:
            if len(string) != 0:
                string += ", "
            string += f"{cursor.key}={cursor.value}"
            cursor = cursor.next
        return string_prefix + string + string_suffix

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
