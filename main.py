def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    i = 0
    longest = shortest = ''
    words = []
    
    while True:
        word = input("Enter a word: ")
        word = word.lower()
        if word == 'stop':
            break
        words.append(word)
        
    longest = shortest = words[0]
    i = len(words)
        
    for j in range(i):
        word = words[j]
        if len(word) > len(longest):
            longest = word
        elif len(word) < len(shortest):
            shortest = word
        
    print(longest, shortest)

    ########################################
    # Do not delete the return statement
    ########################################
    return longest, shortest
##


if __name__ == '__main__':
    main()
