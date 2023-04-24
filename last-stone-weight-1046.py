class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            curr_max = max(stones)
            stones.remove(curr_max)
            next_max = max(stones)
            
            if (curr_max == next_max):
                stones.remove(next_max)
            else:
                stones.remove(next_max)
                next_max = curr_max - next_max
                stones.append(next_max)
                
        
        if stones:
            return stones[0]
        else:
            return 0