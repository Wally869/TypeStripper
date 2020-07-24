from __future__ import annotations
from typing import List

from itertools import combinations_with_replacement, permutations

import argparse

maxDepth = 2
maxWidth = 4

# need to match single type, List[single type], Union[multiple types (up to maxDepth)]
# and compounded types
# also underscores?


SINGLE_TYPE_PATTERN = r"[a-zA-Z]+" # matches 'int' / full word
SINGLE_TYPE_LIST = r"[a-zA-Z]+\[[a-zA-Z]+\]" # matches 'List[float]'

FULL_WORD_NO_UNDERSCORE = r"[a-zA-Z]+"

COMBINATIONS = [
    SINGLE_TYPE_PATTERN,
    SINGLE_TYPE_LIST
]

def GenerateToWidth(width: int = 4):
    generated = r""
    for i in range(width):
        generated += FULL_WORD_NO_UNDERSCORE
        if i != width - 1:
            generated += r"\s"
    return generated


# recursively generate type trees
def GenerateToDepth(currentDepth: int, targetDepth: int = 2, targetWidth: int = 4) -> List:
    if currentDepth == targetDepth:
        outputs = []
        for currentWidth in range(1, targetWidth):
            currCombinations = list(combinations_with_replacement(COMBINATIONS, currentWidth))
            for comb in currCombinations:
                currPermutations = list(permutations(comb, currentWidth))
                for idPermutation in range(len(currPermutations)):
                    currPattern = r""
                    #print(currPermutations)
                    for idElem, elem in enumerate(currPermutations[idPermutation]):
                        currPattern += elem
                        if idElem < len(currPermutations[idPermutation]) - 1:
                            currPattern += r",\s"
                    outputs.append(currPattern)
        prunedOutputs = []
        for output in outputs:
            if output not in prunedOutputs:
                prunedOutputs.append(output)
        #return prunedOutputs
    else:
        patterns = GenerateToDepth(currentDepth + 1, targetDepth, targetWidth)
        # keep patterns, and append the next ones which are generated from them
        # yeah just need to perform combinations, and add r"[a-zA-Z]+\[" at beginning and r"\]" at end
        newPatterns = []
        for currentWidth in range(1, targetWidth):
            currCombinations = list(combinations_with_replacement(patterns, currentWidth))
            for comb in currCombinations:
                currPattern = r"[a-zA-Z]+\["
                for idElem, elem in enumerate(comb):
                    currPattern += elem
                    if idElem != len(comb) - 1:
                        currPattern += r",\s"
                currPattern += r"\s"
                newPatterns.append(currPattern)
        newPatterns = patterns + newPatterns
        prunedOutputs = []
        for output in newPatterns:
            if output not in prunedOutputs:
                prunedOutputs.append(output)
        # sort per length, longest first
        prunedOutputs.sort(key=len, reverse=True)
        #prunedOutputs = prunedOutputs[::-1]
    # reverse patterns to get more complex ones first? might not go too well
    return prunedOutputs

#    else:
#        GenerateToDepth(currentDepth + 1, targetDepth)

# for prefixPattern in [r":\s", r"\s->\s"]:




if __name__ == "__main__":
    import json
    patterns = GenerateToDepth(0, 2, 3)
    usablePatterns = []
    for pattern in patterns:
        usablePatterns.append(r":\s" + pattern)
        usablePatterns.append(r"\s->\s" + pattern)
    with open("Expressions2.py", "w+") as f:
        f.write("PATTERNS = " + str(usablePatterns))
        #json.dump("PATTERNS = " + str(usablePatterns), f)
