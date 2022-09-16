import copy # 깊은 복사를 위해 copy 모듈 import

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs =[]
        for char in s:  # 알파벳과 숫자만 추출해서 넣기
            if char.isalnum():  
                strs.append(char.lower())
        str_a = copy.deepcopy(strs) # 새로운 변수에 깊은 복사 실행
        strs.reverse() # 기존 리스트 뒤집기
        
        if str_a == strs: # 확인
            return True
        else:  
            return False