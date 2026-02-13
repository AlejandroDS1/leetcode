class Solution:

    def isValid(self, s: str) -> bool:

        CLOSING_MAP = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack_of_open = []

        for c in s:
            
            # Check if we are at a open or closing parentheses
            if c not in CLOSING_MAP: # We are in a open parentheses
                # So we have to add 1 open parentheses
                stack_of_open.append(c)

            else: 

                # If we are in a closing parenthesis and stack_of_open is empty we can return False
                if not stack_of_open: return False
                
                # If we are in a closing parentheses we have to know which is the opening corresponding
                open_char = CLOSING_MAP[c]

                # Also if the last open one wasn't this type of parentheses we can return False
                if stack_of_open[-1] != open_char:
                    return False
                
                # If there was any open one we can delete that one
                else:
                    stack_of_open.pop()

        return len(stack_of_open) == 0