import string
import time
import multiprocessing

count_two_word_palindromes = 0
def is_palindrome(s):
    """ Determines if the string s is a palindrome """
  
    return s == s[::-1]
    

def main():
    """ Takes in a list of words and outputs if they are
    palindromes"""

    # open file
    file = open('input.txt', 'r')

    #Loop through input, concatenating it into a string
    s = ""
    for word in file:
        for char in word:
            #Only take letters, and lower case them
            if char.isalpha():
                s += char.lower() 

    print( "Palindrome" if is_palindrome(s) else "Not a palindrome")

def fill_dicts(words, start, end):
    for word in words:  
        first, second = word[0], word[1]
        if first not in start:
            start[first] = {}
        if second not in start[first]:
            start[first][second] = []
        start[first][second].append(word)
        
        first, second = word[-1], word[-2]
        if first not in end:
            end[first] = {}   
        if second not in end[first]:
            end[first][second] = []
        end[first][second].append(word)
    
def get_keys(start, end):
    #Pulling keys out like this lets me only check those keys
    #actually present
    keys = {}
    for k_outer in start.keys():
        for k_inner in start[k_outer].keys():
            if k_outer in end and k_inner in end[k_outer]:
                if k_outer not in keys:
                    keys[k_outer] = []
                keys[k_outer].append(k_inner)
    return keys

def test_word(first_words, second_words, count_two_word_palis):
    for w1 in first_words:
        for w2 in second_words:
            if w1==w2:
                pass
            else:
                testword = w1+w2
                if testword == testword[::-1]:
                    with count_two_word_palis.get_lock():
                        count_two_word_palis.value += 1 
                
def bonus():
    file = open('wordlist.txt')

    wordlist = [(x.rstrip()).lower() for x in list(file)]
    print(str(len(wordlist)) + " words in list")

    #build dicts
    end_letter_dict   = {}
    start_letter_dict = {}
    fill_dicts(wordlist, start_letter_dict, end_letter_dict)

    print("Dicts built")

    keys = get_keys(start_letter_dict, end_letter_dict)
    outer_keys = keys.keys()
    print("Key list built")
    print("--------------")

    t0 = time.time()

    jobs = []
    count_two_word_palis = multiprocessing.Value('i', 0)
    for k1 in outer_keys:
        for k2 in keys[k1]:
            first_words = start_letter_dict[k1][k2]
            last_words  = end_letter_dict[k1][k2]
            p = multiprocessing.Process(target = test_word,
                                        args = (first_words,last_words,
                                                count_two_word_palis))
            jobs.append(p)
            p.start()
    while len(multiprocessing.active_children()) > 0:
        True
            
    t1 = time.time()
    print("Scantime {} ".format(t1-t0))
    return count_two_word_palis.value

def bonus_time():
    t0 = time.time()
    
    print("Palindromes Found: {}".format(bonus()))
    t1 = time.time()
    total_time = t1-t0
    print("Total time: {}".format(total_time))
    return total_time

if __name__ == "__main__":
    bonus_time()
    
