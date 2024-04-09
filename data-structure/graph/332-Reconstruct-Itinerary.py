class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flight_map = {src:[] for src, des in tickets}
        result =[]

        for src, des in tickets:
            flight_map[src].append(des)
            
        for src in flight_map:
            flight_map[src].sort(reverse=True)

        def dfs(src):
            des = flight_map.get(src)
            while des:
                dfs(des.pop())
                  
            result.append(src)   
           
        dfs("JFK")
        return result[::-1]
