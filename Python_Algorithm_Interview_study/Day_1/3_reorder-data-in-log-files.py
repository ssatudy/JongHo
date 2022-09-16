class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 단어, 숫자 시작 인자 구분
        word = []
        nums =[]
        for i in logs:  
            if i.split()[1].isdigit():  
                nums.append(i)
            else:  
                word.append(i)
        
        # 정렬
        for j in range(len(word)-1):  # 지정값 범위
            idx = j
            for k in range(idx+1, len(word)):  # 비교값 범위 
                if word[j].split()[1:] == word[k].split()[1:]:  # 구분자 뒤에가 같을 때
                    if word[j].split()[0] > word[k].split()[0]:  
                        word[j], word[k] = word[k], word[j]
                elif word[j].split()[1:] > word[k].split()[1:]:  # 구분자 뒤에가 다를 때
                    word[j], word[k] = word[k], word[j]
        
        return word + nums
        