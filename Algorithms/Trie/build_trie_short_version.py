WORD_KEY = '$'

words = ["oath", "dig", "dog", "dogs"]

trie = {}
for word in words:
    node = trie
    for letter in word:
        # retrieve the next node; If not found, create a empty node.
        node = node.setdefault(letter, {})
    # mark the existence of a word in trie node
    node[WORD_KEY] = word

print(trie)