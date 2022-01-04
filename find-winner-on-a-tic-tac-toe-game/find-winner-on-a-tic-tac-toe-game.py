class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = []
        B = []
        
        for i, k in enumerate(moves):
            if i % 2 == 0:
                A.append(k)
            else:
                B.append(k)
        
        winner = [[[0,0], [1,1], [2,2]],
                  [[0,0], [0,1], [0,2]],
                  [[0,0], [1,0], [2,0]],
                  [[0,2], [1,1], [2,0]],
                  [[1,0], [1,1], [1,2]],
                  [[2,0], [2,1], [2,2]],
                  [[0,1], [1,1], [2,1]],
                  [[0,2], [1,2], [2,2]]]
             
        for j in winner:
            if(all(a in A for a in j)):
                return "A"
            if(all(a in B for a in j)):
                return "B"
            
        if (len(A) + len(B) == 9):
            return "Draw"
        else:
            return "Pending"
        
            