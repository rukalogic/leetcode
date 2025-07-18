class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_list = strs.copy()
        shortest = new_list.pop(new_list.index(min(new_list, key = len)))
        lenght_of_shortest = len(shortest)
        index_to_check = 0
        common_prefix = ''
        while index_to_check != lenght_of_shortest:
            for word in new_list:
                if word[index_to_check] != shortest[index_to_check]:
                    return common_prefix
            common_prefix += shortest[index_to_check]
            index_to_check += 1
        return common_prefix



        