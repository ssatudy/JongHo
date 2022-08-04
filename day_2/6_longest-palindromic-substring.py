def longestPalindrome(s) :
        result =""
        
        if len(s) < 2 or s == s[::-1]:  
            return s
        
        for start in range(len(s)):  
            for end in range(start + 1, len(s) + 1):  
                word = s[start:end]
                if word == word[::-1]:  
                    if len(word) > len(result):  
                        result = word
        return result