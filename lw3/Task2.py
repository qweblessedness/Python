def maxRepeating(str):
 
    l = len(str)
    count = 0
 
    res = str[0]
    for i in range(l):
         
        cur_count = 1
        for j in range(i + 1, l):
     
            if (str[i] != str[j]):
                break
            cur_count += 1
 
        if cur_count > count :
            count = cur_count
    return count
 
if __name__ == "__main__":
 
    str = "oaaam"
    print("Word: ",str)
    print(maxRepeating(str))
