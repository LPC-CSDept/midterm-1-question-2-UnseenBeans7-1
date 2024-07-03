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

    ########################################
    # Do not delete the return statement
    ########################################
    return longest, shortest
##


if __name__ == '__main__':
    main()
