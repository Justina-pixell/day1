from collections import Counter

with open("C:\\Users\\just0\\Documents\\all_txt\\requirement.txt","r") as file:
    text=file.read()
    words = text.split(" ")
    #print(words)
    new=[]
    duplicates=[]
    for i in words:
        #print(i)
        if i=='':
            words.remove('')
    a=len(words)
    print(a)
    print(words)

    word_counts = Counter(words)
    print("Top 5:", word_counts.most_common())

    for word in words:
        if word not in new:
            new.append(word)
        else:
            duplicates.append(word)

    
    if len(duplicates)==0:
        print("No duplicates")

    else:
        print(f"duplicate words:{duplicates}")


        



