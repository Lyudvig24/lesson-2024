import re
def get_argument(fname):
    with open(fname) as f:
        punctuation_pattern = r'[^\w\s]'        
        return re.sub(punctuation_pattern, "", f.read()).split()




def filter_words():
    with open('filter_file.txt','r') as file:
        text = file.read().split()
        filter_text = {}
    
        for i in text:
            if i.isalpha():
                filter_text.setdefault(i,0)
                filter_text[i] += 1
            
        sorted_words = sorted(filter_text.items(),key=lambda x: x[1],reverse=True)
        
        top_ten = sorted_words[:10]
        return top_ten

        
                
top_words = filter_words()
for k,w in top_words:
    print(k,w)









