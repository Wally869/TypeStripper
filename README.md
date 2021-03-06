# TypeStripper [![Build Status](https://travis-ci.com/Wally869/TypeStripper.svg?branch=master)](https://travis-ci.com/Wally869/TypeStripper)

Utility to delete all type hinting from a Python script.

NOTE: This is a WIP, but should be able to handle most cases. Let me know if you encounter an issue.
Currently, type hints with underscores or wich include a point (such as my_class or np.array) are NOT supported.   
Current recommended workaround is to use aliases for unsupported type hinting annotations, or put the preprocessing tag to mark the file as not to be stripped.

## Why?

I use type hinting a lot when writing Python but I stumbled upon a specific case where I need to strip the type hinting of my scripts to ensure the script can run.  

The typing package does not allow you to use the class you are defining as a type hint for one of its method. The following is allowed by using the annotations module of future since it converts the type annotations to strings to be ignored at runtime. 

```python
from __future__ import annotations

class Foo:
    def Bar() -> Foo:
        return Foo()
```

My use case is when using Transcrypt, or Bryton to use Python in the browser: the type hinting allowed by the annotations module and described above is not allowed and must be removed.

So instead of manually doing the work every time, this utility script takes a folder as input and outputs new python files stripped of all type hinting in a new folder.

## How to Use

This script was made with a Python 3.7.4 install and requires Pathlib which requires Python 3.5+.

Call the script from the CLI:

```command line
    python Main.py -i myPackageFolder -o outputFolder
```

![Help Argparse](ReadmeImages/argparse.JPG)


You can add a preprocessing directive to your files to signal that TypeStripper should not operate on them
and should just copy them with no modifications.  
Simply add: #NoTypeStripping anywhere in your file

```python
import argparse

#NoTypeStripping

def Foo():
    return "Bar"

```

## Currently Supported Patterns

Simple patterns are supported, which should cover most cases.
Currently unsupported:
- No support for type names containing underscores or points

See Below for details (type names are provided as illustrations).

```pythonregexp
    r":\s[a-zA-Z]+\[[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\]\]\]", # matches: ': List[Dict[str, Union[float, int]]]'
    r"\s->\s[a-zA-Z]+\[[a-zA-Z]+\[[a-zA-Z]+\],\s[a-zA-Z]+\[[a-zA-Z]+\]\]", # matches: ' -> Tuple[List[Note], List[Error]]'
    r":\s[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\]",       # matches ': Union[int, Note]'
    r":\s[a-zA-Z]+\[[a-zA-Z]+\[[a-zA-Z]+\],\s[a-zA-Z]+\]", # matches ': Union[List[Note], Note]'
    r":\s[a-zA-Z]+\[[a-zA-Z]+",                     # matches ': List[float]'
    r"\s->\s[a-zA-Z]+\[[a-zA-Z]+,\s[a-zA-Z]+\]",    # matches ' -> Union[int, Note]'
    r"\s->\s[a-zA-Z]+\[[a-zA-Z]+",                  # matches ' -> List[float]'
    r"\s->\s[a-zA-Z]+",                             # matches ' -> Note'
```

While previous types are simply subtracted from the parsed string, 
matching a simple type after colons, such as ': int' is trickier.

This case is handled with the following rules:
```python
    re.sub(r"(?<!\"):\s[a-zA-Z]+,", ",", currData)
    re.sub(r":\s[a-zA-Z]+\)", ")", currData)
    re.sub(r":\s[a-zA-Z]+\s\=(?!\=)", " =", currData)
```


## Known Issues

Composite type names (e.g. np.array)  
Underscores
