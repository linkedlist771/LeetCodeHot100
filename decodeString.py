class Solution:
    def decodeString(self, s: str) -> str:
        """
        思路，维护两个栈， 一个prev_str stack， 一个是num_stack。 # 用于处理嵌套的
        维护一个current_str 就是当前的string。
        维护一个current_number 用于统计数字
        如果是数字，那么乘以10 加上去。
        遇到[:

        代表进入新的重复了。 进栈 current_str 还有current_num 重置

        遇到了]:

        代表结束了， 弹出num 还有prev str， 连接起来。

        其他情况;
        字符串，直接添加。
        """
        prev_str_stack = []
        num_stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == "[":
                prev_str_stack.append(current_str)
                num_stack.append(current_num)
                current_str = ""
                current_num = 0
            elif char == "]":
                prev_str = prev_str_stack.pop()
                num = num_stack.pop()

                current_str = prev_str + num * current_str
            else:
                current_str += char
        return current_str
