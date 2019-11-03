class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^%s]" % (string.ascii_lowercase + ' '), " ", paragraph)
        dic = dict()
        for word in paragraph.split(" "):
            print(word)
            if word in dic:
                dic[word] += 1
            elif word is not '':
                dic[word] = 1
        
        for word in banned:
            if word in dic:
                del dic[word]
        
        inverse = [(value, key) for key, value in dic.items()]
        
        return max(inverse)[1]
