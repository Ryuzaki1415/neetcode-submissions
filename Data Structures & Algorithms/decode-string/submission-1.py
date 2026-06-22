class Solution:
    def decodeString(self, s: str) -> str:

        # we need two stacks
        num_stack=[]
        string_stack=[]

        cur_num=0
        cur_str=""
        for char in s:
            if char.isdigit():
                cur_num= cur_num*10+ int(char)

            elif char=="[":
                num_stack.append(cur_num)
                string_stack.append(cur_str)

                cur_num=0
                cur_str=""
            
            elif char=="]":
                # once we see the closing bracket
                repeat=num_stack.pop()
                prev_string=string_stack.pop()
                cur_str=prev_string+cur_str*repeat

            else:
                cur_str+=char

        return cur_str








        