from __future__ import annotations
from typing import List, Union, Tuple

from ProcessingFunctions import ProcessContent, MatchPattern

from glob import glob

import argparse
from pathlib import Path


def Main(inputFolder: str, outputFolder: str, forceStripping: bool = False) -> None:
    # create outputfolder
    Path(outputFolder).mkdir(parents=True, exist_ok=True)

    foldersToExplore = []
    explorationDepth = 1
    while True:
        newFound = glob("{}/{}".format(inputFolder, "*/" * explorationDepth), recursive=True)
        if len(newFound) > 0:
            foldersToExplore += newFound
            explorationDepth += 1
        else:
            break

    foldersToExplore = [inputFolder] + foldersToExplore
    for currFolder in foldersToExplore:
        # create subfolder
        Path("{}/{}".format(outputFolder, currFolder)).mkdir(parents=True, exist_ok=True)
        # get all files in subfolder, prune them if .py and write to output folder
        folderFiles = glob("{}/*.py".format(currFolder))
        for currFile in folderFiles:
            with open(currFile, "r") as f:
                currData = f.read()

            currData = ProcessContent(currData, forceStripping)

            with open("{}/{}".format(outputFolder, currFile), "w+") as f:
                f.write(currData)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Strip type hinting from a python project.')
    parser.add_argument('-i', type=str, help='str, input folder')
    parser.add_argument('-o', type=str, help='str, output folder, defaults to output', default="output")
    parser.add_argument('-f', help='force stripping', action='store_true')
    args = parser.parse_args()

    Main(args.i, args.o, args.f)