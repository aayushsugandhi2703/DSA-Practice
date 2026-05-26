# Function for encoding and decoding the string

def encode(strs):
    res = []
    for s in strs:
        encoded_word = ""
        for ch in s:
            encoded_word += chr(ord(ch) + 1)
        res.append(encoded_word)
    return res

def decode(strs):
    res = []
    for s in strs:
        decoded_word = ""
        for ch in s:
            decoded_word += chr(ord(ch) - 1)
        res.append(decoded_word)
    return res


def main():
    strs = ["hello", "world", "python"]
    encoded_strs = encode(strs)
    print("Encoded:", encoded_strs)
    decoded_strs = decode(encoded_strs)
    print("Decoded:", decoded_strs)

if __name__ == "__main__":
    main()