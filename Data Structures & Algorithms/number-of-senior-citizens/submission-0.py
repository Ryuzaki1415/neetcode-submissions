class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count=0
        for detail in details:
            ph=detail[:10]
            gender=detail[10]
            age=int(detail[11:13])

            if age>60:
                count+=1
        return count
                
        