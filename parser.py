"""
This script takes all .xml files of the folder, prettyPrint them, and search for a specific word inside.

    Prerequisites:
        pip install lxml

    Args:
        x: word to search

    Returns:
        The lines matching the word we are searching for
"""

import os
import sys
from lxml import etree

def prettyPrintXml(xmlFilePathToPrettyPrint):
    """Save/Replace the .xml file after prettyPrinting it"""
    assert xmlFilePathToPrettyPrint is not None
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    document = etree.parse(xmlFilePathToPrettyPrint, parser)
    return document.write(xmlFilePathToPrettyPrint, pretty_print=True, encoding='utf-8')

def lines_that_contain(fp, string):
    """Return lines that contain a specific string"""
    return [line for line in fp if string in line]

def main(word):

    """Open the .xml files of the folder"""
    for file in os.listdir(os.getcwd()):
        if file.endswith(".xml"):

            """PrettyPrint the xml file if it's not"""
            prettyPrintXml(file)

            """Header"""
            print('+' + '-' + '-' * len(file) + '-' +  '+')
            print('|' + ' ' +  file + ' ' + '|')
            print('+' + '-' +  '-' * len(file) + '-' +  '+')      
            print(f"Lines inside {file} matching the word: {word} \n")

            """Open the file, search inside, and print lines if word found"""
            with open(file, mode='rt', encoding='utf-8') as f:
                Lines = lines_that_contain(f, word)
                print(*Lines, sep=" ")

if __name__ == '__main__':
    main(word=sys.argv[1])