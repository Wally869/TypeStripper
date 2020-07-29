from __future__ import annotations
from typing import List, Union, Tuple

from Expressions import PATTERNS

import re

def ProcessContent(dataFile: str, forceStripping: bool = False) -> str:
    currData = dataFile
    # look for preprocessing directive: #NoTypeStripping
    if not forceStripping:
        preprocessMatch = re.search(r"#NoTypeStripping", currData)
        if (preprocessMatch is None):
            for pattern in PATTERNS:
                currData = MatchPattern(currData, pattern)
    else:
        for pattern in PATTERNS:
            currData = MatchPattern(currData, pattern)
    return currData


def MatchPattern(inputString: str, pattern: Tuple[str]) -> str:
    return re.sub(pattern[0], pattern[1], inputString)