#  Robert Call
#  Program 6.1
#  Generates 5 random strings from context free grammar



from collections import defaultdict
import random


class CFG:

    def __init__(self, _grammar):
        self.grammar = _grammar
        self.start_state = self.grammar[0][0]
        self.rules = defaultdict(list)
        self.add_rule("*", " ")

        for x in _grammar:
            self.add_rule(x[0], x[1])

    def add_rule(self, lh, rh):
        rule_set = rh.split('|')
        for rules in rule_set:
            self.rules[lh].append(tuple(rules.split()))

    def gen_string(self):
        stack = random.choice(self.rules[self.start_state])
        stack = list(stack)
        word = ""
        while len(stack)> 0:
            char = stack.pop()
            if char not in self.rules.keys():
                word += char
            else:
                for r in random.choice(self.rules[char]):
                    stack.insert(0,r)
        return word


    def display(self):
        print("Grammer: ", self.grammar)
        wordlist = []
        while len(wordlist) < 6:
            w = self.gen_string()
            if w not in wordlist and w is not '':
                wordlist.append(w)
        print("Randomly Generated strings: ", wordlist)
        print()
        return wordlist



def test():
    print()
    prompt = "Testing list of grammars"
    print("%s\n%s" % (prompt, '-'*len(prompt)))
    print()

    grammar1 = ["S aSb|X|Y", "X aX|a", "Y Yb|b"]
    grammar2 = [['S', 'a S a | b S b | X'], ['X', 'a Y b | b Y a'], ['Y', 'a Y | b Y| *']]
    grammar3 = [['S', 'a S b | *']]
    g = CFG(fix_rules(grammar1))
    g.display()
    g1 = CFG(grammar2)
    g1.display()
    g2 = CFG(grammar3)
    g2.display()
    fg = CFG(parse_input("grammar.txt"))
    fg.display()
    f = CFG(parse_input("grammar2.txt"))
    f.display()


def fix_rules(lines):
    all_rules = []
    for x in lines:
        rhs, lhst = x.split()
        lhs = " ".join(lhst)
        all_rules.append([rhs, lhs])
    return all_rules

def parse_input(g):
    print("Parsing File", g)
    lines = []
    f_grammar = []
    with open(g, 'r+') as f:
        s = f.read()
        lines = s.splitlines()
    return fix_rules(lines)





if __name__ == '__main__':
    test()

