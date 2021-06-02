
# Leetcode String 68 HARD
def fullyJustify(words,maxWidth):
    #create hashmap d = {row_number:length of row}
    # Grouping words of the same row into list of list: rows=[word1,word2,word3 ], [word4,word5]...]
    d ={} #row_number:len
    rows=[]
    row=[]
    num = cur_len = 0
    for i in range(len(words)):
        d[num] = cur_len
        cur_len += len(words[i])
        #if current length is still less thant maxwith, keep addint into current row
        if cur_len <=maxWidth:
            row.append(words[i])
            cur_len+=1
        else:
            rows.append(row)
            d[num]-=1
            #start a new row
            row = [words[i]]
            num+=1
            cur_len = len(words[i])+1

    #last row isn't addet yet, so add it here:
    rows.append(row)
    d[num] = cur_len-1

    #step 2: Calculate needed space between words in each row with the folowwing 2 special case
    #left spaces have more space and right
    #last row is a special case without extra space
    output = []
    last_row = max(d.keys())
    for k,v in d.items():
        text=''
        if k!=last_row:
            extra = maxWidth -v
            betweens = len(rows[k])-1
            space = 1
            tail = 0
            if extra > 0 and betweens > 0:
                space = extra // betweens+1
                tail = extra % betweens #number of space can't distirbute evenly between words
            for i in range(len(rows[k])):
                text+=rows[k][i]+ ' '*space
                if i<tail:
                    text+=' '
        else: #last row has no extra space
            text= ' '.join(rows[k])
        text = text.rstrip()+' '*(maxWidth- len(text.rstrip()))
        output.append(text)
    return output





print(fullyJustify( ["This", "is", "an", "example", "of", "text", "justification."], 16))