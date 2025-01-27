import heapq
from collections import defaultdict

#frequency table for the input string
def frequency_table(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq

# build the Huffman Tree using a heap (priority queue)
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # comparison method for the heap
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # take two nodes with the lowest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # create a new internal node with the sum of the frequencies
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        # add the internal node back to the heap
        heapq.heappush(heap, internal_node)

    # root of the tree
    return heap[0]

# generate Huffman codes by traversing the tree
def generate_huffman_codes(root, prefix='', codebook=None):
    if codebook is None:
        codebook = {}

    if root is not None:
        # if the node is a leaf, it contains a character
        if root.char is not None:
            codebook[root.char] = prefix
        else:
            generate_huffman_codes(root.left, prefix + '0', codebook)
            generate_huffman_codes(root.right, prefix + '1', codebook)
    
    return codebook

# encoding the text using the Huffman codes
def encode(text, codebook):
    return ''.join(codebook[char] for char in text)

# decoding the encoded text using the Huffman tree
def decode(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        # traverse the tree
        current_node = current_node.left if bit == '0' else current_node.right
        
        # if it's a leaf, append the character
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return ''.join(decoded_text)

if __name__ == '__main__':
    text = "datastructures"
    
    freq = frequency_table(text)
    print("\nStep 1: Frequency Table:")
    print(freq)

    root = build_huffman_tree(freq)
    print("\nStep 2: Huffman Tree Built Successfully.")

    huffman_codes = generate_huffman_codes(root)
    print("\nStep 3: Huffman Codes Generated:")
    for char, code in huffman_codes.items():
        print(f"Character: {char} --> Code: {code}")

    encoded_text = encode(text, huffman_codes)
    print("\nStep 4: Encoded Text:")
    print(encoded_text)

    decoded_text = decode(encoded_text, root)
    print("\nStep 5: Decoded Text:")
    print(decoded_text)
