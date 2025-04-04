"""
Huffman Coding - Lossless Compression using a Greedy Algorithm

Huffman coding is a **greedy algorithm** that assigns **shorter binary codes** to more frequent characters
and **longer binary codes** to less frequent characters, ensuring optimal compression.

It constructs a **prefix-free binary tree**, meaning no code is a prefix of another, allowing unique decoding.

### Steps:
1. **Count character frequencies** in the input text.
2. **Build a priority queue (min-heap)** where the lowest frequency characters have the highest priority.
3. **Merge two smallest frequency nodes** repeatedly to form a Huffman tree.
4. **Assign binary codes**: Left branch = `0`, Right branch = `1`.
5. **Generate Huffman codes** and encode the text.
6. **Decode using the Huffman tree** (ensuring lossless recovery).

This example demonstrates the greedy approach of **assigning shorter codes to more frequent characters.**
"""

import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return build_huffman_codes(heap[0]), heap[0]

def build_huffman_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_decoding(encoded_str, root):
    decoded_str = ""
    node = root
    for bit in encoded_str:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_str += node.char
            node = root
    return decoded_str

# Example usage
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_codes, root = huffman_coding(frequencies)
print("Huffman Codes:", huffman_codes)

# Encoding example
text = "abcdef"
encoded_text = "".join(huffman_codes[char] for char in text)
print("Encoded Text:", encoded_text)

# Decoding example
decoded_text = huffman_decoding(encoded_text, root)
print("Decoded Text:", decoded_text)

"""
### Summary:
- **Huffman coding assigns shorter binary codes to more frequent characters**, ensuring efficient compression.
- **This greedy algorithm constructs a binary tree** where smaller frequency characters are merged first.
- **Encoded text is smaller in size**, and **prefix codes prevent decoding ambiguity**.

This method is widely used in file compression formats like **ZIP, JPEG (lossless parts), and MP3**.
"""