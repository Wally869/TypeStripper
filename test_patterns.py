from Expressions import PATTERNS

import re


####### IN HEADER DECLARATION INPUT #######
def test_single_simple_type_function_header_declaration():
    # testing for annotation of a single variable:
    inputSentence = "def InvertIntervals(self, inversion: int = 0):"
    targetSentence = "def InvertIntervals(self, inversion = 0):"
    # we'll use all patterns imported from Expressions
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


def test_multiple_simple_type_function_header_declaration():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote: Note, inversion: int = 0, fromRoot: bool = True):"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


def test_list_single_simple_type_function_header_declaration():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote: List[int], inversion = 0, fromRoot = True):"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


def test_list_multiple_simple_type_function_header_declaration():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote: List[int, bool], inversion = 0, fromRoot = True):"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


####### IN HEADER DECLARATION OUTPUT #######
def test_list_single_simple_type_function_header_output():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True) -> List[Error]:"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)

def test_list_double_simple_type_function_header_output():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True) -> List[Error, int]:"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


def test_list_single_complex_simple_type_function_header_output():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True) -> List[List[Error]:"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


def test_list_single_complex_double_type_function_header_output():
    # testing for annotation of multiple variables with single types in function header:
    inputSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True) -> List[List[Error, int]:"
    targetSentence = "def __call__(self, rootNote, inversion = 0, fromRoot = True):"
    temp = inputSentence
    for pattern in PATTERNS:
        temp = re.sub(pattern, "", temp)
    assert(temp == targetSentence)


