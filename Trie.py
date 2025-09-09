class Trie:
    """
    思路：用嵌套字典实现前缀树，字典的键为字符，值为下一层节点（仍是字典）；
    插入时逐字符下潜，若不存在则创建；在单词最后一个节点放置一个结束标记（如 '#': True）
    表示这里有完整单词；search 逐字符匹配并最终检查结束标记确保是完整词；startsWith
    仅检查路径是否存在，不要求结束标记。
    """

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                # 不在里面， 添加
                node[char] = {}
            node = node[char]
        node["#"] = True  # 结束标识符

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return node.get("#", False)

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
