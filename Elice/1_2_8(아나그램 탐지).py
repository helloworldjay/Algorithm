def isAnagram(str1, str2):
    dict1 = {}
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        dict1[str1[i]] = dict1.get(str1[i],0) + 1
    for i in range(len(str2)):
        if dict1.get(str2[i], 0) == 0 :
            return False
        else:
            dict1[str2[i]] -= 1

    return True

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
