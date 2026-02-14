from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        sorted_childs = sorted(g)
        sorted_cookies = sorted(s)

        max_cookie = sorted_cookies[-1]

        number = 0
        cookie_pointer = 0

        for child in sorted_childs:

            # If the cookie is enough for the child give them the cookie. 
            if sorted_cookies[cookie_pointer] >= child:
                number += 1
                cookie_pointer += 1

            # If the child greed is greater than the max_cookie size we can already return the number
            if child > max_cookie: return number
            else: # If it's not we have to reach the next valid cookie
                not_found_cookie = True
                while not_found_cookie:
                    cookie_pointer += 1
                    if sorted_cookies[cookie_pointer] >= child:
                        not_found_cookie = False
                        cookie_pointer += 1
                        number += 1
        return number