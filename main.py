import hashlib
from itertools import permutations

def find_hash(original_hash):
    word_file = open("words.txt","r")
    word_file = list(word_file)

    anagram = "i move lads"
    words = anagram.count(' ')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    for word in word_file:
        word = word.replace('\n','')
        word_chars = list(set(word))
        flag = False
        for c in word_chars:
            if(c not in char_list):
                flag = True
                break
        if(not flag):
            final_words.append(word)

    print(len(final_words))

    for elem in permutations(final_words, words):
        hash_elem = " ".join(elem)
        
        if(len(hash_elem) != len(anagram)):
            continue
        
        m = hashlib.md5()
        m.update(hash_elem.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return hash_elem

hash = 'ac3751fa101668c6de2002356d9a032b'
answer = find_hash(hash)
print(f"Collision!  The word corresponding to the given hash is '{answer}'")
