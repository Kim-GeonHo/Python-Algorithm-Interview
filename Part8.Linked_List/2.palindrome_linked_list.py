from typing import List

input_list = input()

list_ = input_list.split('->')


class isPalindrome:
    def by_list(self, p_list : List[str]) -> bool:
        length = len(p_list)

        for i in range(length // 2):
            if p_list[i] != p_list[length - 1 - i]:
                return False
        
        return True

    def by_list_pop(self, p_list : List[str]) -> bool:
        while len(p_list) > 1:
            if p_list.pop(0) != p_list.pop():
                return False
        
        return True

iP = isPalindrome()

print(iP.by_list(list_))
print(iP.list_conversion(list_))
