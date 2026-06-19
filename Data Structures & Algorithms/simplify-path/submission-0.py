class Solution:
    def simplifyPath(self, path: str) -> str:


        stack=[]
        
        directories=path.split("/")


        for dir in directories:

            if dir =="..":
                if stack :
                    stack.pop()
            elif dir == "." or dir =="":
                pass
            
            else:
                stack.append(dir)
        

        result="/"+"/".join(stack)
        return result

        