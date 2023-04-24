def sort_anagrams(list_of_strings):
    # create an empty dictionary
    anagram_dict = {}

    # loop through each word in the list
    for word in list_of_strings:
        # sort the letters of the word and use it as a key in the dictionary
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            # if the key already exists, add the word to the value list
            anagram_dict[sorted_word].append(word)
        else:
            # if the key doesn't exist, create a new key-value pair
            anagram_dict[sorted_word] = [word]

    # convert the dictionary values to a list and return it
    return list(anagram_dict.values())


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless',
                 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
