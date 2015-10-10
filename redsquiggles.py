#DP 234 Intermediat Squiggles

class Node:
    def __init__(self, data, children=[]):
        self.value = data
        self.children = children

tree_root = Node("")

def get_child(node, key):
    
    pass

def get_next_node(tree, key):
    return next(x for x in tree.children if x.value == key)

def add_word(word, current_node):
    """ Adds word to tree """
    if word == '':
        return 
    else:
        current_letter = word[0]
        if current_letter not in [x.value for x in current_node.children]:
            current_node.children.append(Node(current_letter, []))
        add_word(word[1:], get_next_node(current_node, current_letter))

def find_last_correct_letter(word, current_node):
    """ Finds the index of the last possible correct letter """

    if word == '':
        return 0
    else:
        current_letter = word[0]
        values = [x.value for x in current_node.children]
        if current_letter not in [x.value for x in current_node.children]:
            return 0
        else:
            return 1 + find_last_correct_letter(word[1:], get_next_node(current_node, current_letter))

def load_words(tree):
    """ loads wordlist into tree """

    word_file = open("enable1.txt")
    for word in word_file:
        add_word(word.rstrip(), tree_root)

def main():
    load_words(tree_root)
    print("Ctrl-C or equivalent on your platform to end")
    while(True):
        test_word = input("Word to check: ")
        num_correct = find_last_correct_letter(test_word, tree_root)
        print(test_word[:num_correct+1] + '<' + test_word[num_correct+1:])
    
