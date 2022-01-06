class Solution:
    def maxDiff(self, num: int) -> int:
        max_num = -math.inf
        min_num = math.inf
        str_num = str(num)
        integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for i in set(str_num):
            for j in integers:
                new_num = str_num.replace(i,j)
                if(new_num[0] != '0'):
                    new_num = int(new_num)
                    if(new_num > max_num):
                        max_num = new_num
                    if(new_num < min_num):
                        min_num = new_num
                        
        return max_num - min_num
                    