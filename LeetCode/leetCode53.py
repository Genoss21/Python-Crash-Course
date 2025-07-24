def lastWord(s: str) -> int:
    return len(s.strip().split()[-1])

s = "Hello Wolrd"
# s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
print("Lenght of the last word: ", lastWord(s))