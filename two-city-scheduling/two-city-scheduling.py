class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result = 0
        visited = []
        for x,y in costs:
            # Adding all costs of travelling to city A
            result = result + x
            # Append all differences between travelling to B and A
            visited.append(y-x)
        # Sort the difference list
        visited = sorted(visited)
        
        # Traverse half of the visited list and append the results
        for i in range(0, len(costs)//2):
            result = result + visited[i]
        
        return result
            