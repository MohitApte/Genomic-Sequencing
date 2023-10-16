#python3
import sys

import collections


def prefix(string):
    return string[:len(string)-1]


def suffix(string):
    return string[1:]



def de_bruijn(k, text):
    """Creates a de Bruijn graph from a string given a value of k

    Args:
        k:          the length of strings represented by edges in the
                    de Bruijn graph
        text:       the string from which the de Bruijn grpah will be
                    constructed

    Returns:
        a string containing an adjacency list representation of the de Bruijn
        graph as described in the problem specification
    """
    # TODO: your code here
    
    start = 0
    answer = {}
    while start + k <= len(text):
        window = text[start:start+k]
        pre = prefix(window)
        suf = suffix(window)
        if pre not in answer:
            answer[pre] = (suf,)
        else:
            answer[pre] += (suf,)
        start += 1
        
    od = collections.OrderedDict(sorted(answer.items()))
    string = ""
    for key in od.keys():
        string += str(key) + " -> "
        if len(answer[key]) == 1:
            string += answer[key][0] + "\n"
        else:
            answer[key] = sorted(answer[key])
            string += answer[key][0]
            del answer[key][0]
            for item in answer[key]:
                string += ("," + str(item))
                
            string += "\n"
    print(string)



if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())
    text = sys.stdin.readline().strip()

    de_bruijn(k, text)
