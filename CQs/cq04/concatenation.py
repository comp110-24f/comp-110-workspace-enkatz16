"""File for concatenation function"""

__author__ = "730748249"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(str1=word1, str2=word2))
