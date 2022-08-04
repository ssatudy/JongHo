import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 문자열 클렌징 -> 정규 표현식 사용해서 특수문자 공백 처리
        re_para = [char for char in re.sub(r"[^a-zA-Z0-9]", ' ', paragraph)
                  .lower().split() if char not in banned] # 이후 banned 단어가 아닌 것을 소문자로 넣음
        
        # 단어 별 카운트
        count_para = {}
        for j in list(re_para):  
            if j in count_para:  
                count_para[j] += 1
            else:  
                count_para[j] = 1
        
        # 딕셔너리 키 리스트 생성
        key_ls = list(count_para.keys())

        # 빈 str 변수 만들고 최대 key 찾기
        most_key = "" # 없어도 됨
        basic_key = key_ls[0]
        for k in range(1, len(key_ls)):  
            if count_para[key_ls[k-1]] > count_para[basic_key]:
                basic_key = key_ls[k-1]
                most_key = key_ls[k-1]
            elif count_para[key_ls[k-1]] == count_para[basic_key]:  
                most_key = basic_key
            else:  
                pass
        
        return most_key