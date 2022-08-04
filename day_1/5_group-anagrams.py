class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 단어 별로 리스트 만들고 분리
        re_strs = []
        for i in strs:  
            re_strs.append(sorted(list(i)))
        
        # 단어 합치기(leetcode에서 ''.join이 실행 안되는 줄 알았어서 아래 처럼 진행)
        sor_str = ""
        new_strs = []
        for j in re_strs:  
            for k in j:  
                sor_str += k
            new_strs.append(sor_str)
            sor_str=""
        
        # 딕셔너리로 분류
        dic_str = {}
        for l in range(len(new_strs)):  
            if new_strs[l] in dic_str:  
                dic_str[new_strs[l]] += [strs[l]]
            else:  
                dic_str[new_strs[l]] = [strs[l]]
        
        return list(dic_str.values())