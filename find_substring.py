def count_substring(string, sub_string):
    ind=[]
    for i in range(len(string)):
        ind.append(string.find(sub_string,i,i+len(sub_string)))
    print(ind)



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    #print (count)
