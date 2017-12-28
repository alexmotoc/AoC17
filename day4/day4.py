def duplicate_words(phrase):
    """Returns whether a given passphrase contains duplicate words"""
    return len(set(phrase.split())) != len(phrase.split())

def anagrams(word1, word2):
    """Return whether two words are anagrams"""
    return sorted(word1) == sorted(word2)

no_duplicates = 0
no_anagrams = 0

with open('day4_input.txt') as file:
    for line in file:
        if not duplicate_words(line):
            no_duplicates += 1

        is_anagram = False
        for i in range(len(line.split()) - 1):
            for j in range(i + 1, len(line.split())):
                if anagrams(line.split()[i], line.split()[j]):
                    is_anagram = True

        if not is_anagram:
            no_anagrams += 1

print(no_duplicates)
print(no_anagrams)
