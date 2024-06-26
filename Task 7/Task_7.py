def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    words = data[1:]
    
    from collections import OrderedDict

    word_count = OrderedDict()
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(len(word_count))
    print(" ".join(map(str, word_count.values())))

if __name__ == "__main__":
    main()


"""
User input
"""