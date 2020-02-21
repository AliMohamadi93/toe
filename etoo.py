def getBert(variable):
    word_array = (variable.lower()).split("bert")
    print(word_array)
    if len(word_array) > 2:
        i = "".join(word_array[1])
        return i[::-1]
    else:
        return ""
print(getBert("abcdebertfcbarcelonabertabcde"))