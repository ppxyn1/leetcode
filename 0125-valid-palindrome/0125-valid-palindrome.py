import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
#       s = s.replace(" ","").replace(",","").replace(":","").lower()
        
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        revStr = "".join(reversed(s)) # str형태는 join
        print(f's:{s}')
        print(f'revStr:{revStr}')
        
        return True if s == revStr else False
