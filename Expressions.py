# Go from most complex to simplest to avoid partial matching and deletion
PATTERNS = [
    r":\s[a-zA-Z]+\[[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\]\]\]", # matches: ': List[Dict[str, Union[float, int]]]'
    r"\s->\s[a-zA-Z]+\[[a-zA-Z]+\[[a-zA-Z]+\],\s[a-zA-Z]+\[[a-zA-Z]+\]\]", # matches: ' -> Tuple[List[Note], List[Error]]'
    r":\s[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\]", # matches ': Union[int, Note]'
    r":\s[a-zA-Z]+\[[a-zA-Z]+\[[a-zA-Z]+\],\s[a-zA-Z]+\]", # matches ': Union[List[Note], Note]'
    r":\s[a-zA-Z]+\[[a-zA-Z]+\]", # matches ': List[float]'
    r"\s->\s[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\]", # matches ' -> Union[int, Note]'
    r"\s->\s[a-zA-Z]+\[[a-zA-Z]+\]", # matches ' -> List[float]'
    r"\s->\s[a-zA-Z]+" # matches ' -> Note'
    #r":\s[a-zA-Z]+" # matches ': int'
]

