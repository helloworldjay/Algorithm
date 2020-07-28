def wordPattern(pattern, strList):
    for i in range(len(pattern)):
        for j in range(i+1, len(pattern)):
            if pattern[i] == pattern[j] :
                if strList[i] != strList[j]:
                    return False
    return True

def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    

if __name__ == "__main__":
    main()
