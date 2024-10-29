class Solution:
    def restoreIpAddresses(self, s):
        combinations_list = self.build_remaining_combinations(s, 3)
        return [".".join(c) for c in combinations_list]

    def build_remaining_combinations(self, s, remaining_dots):
        if s == "":
            return []
        if remaining_dots == 0:
            if self.is_valid_ip_section(s):
                return [[s]]
            else:
                return []
        remaining_combinations = []
        for offset in range(1, 4):
            if self.is_valid_ip_section(s[0:offset]):
                tmp_combinations = self.build_remaining_combinations(
                    s[offset:], remaining_dots - 1
                )
                if tmp_combinations != []:
                    tmp_combinations = [[s[0:offset]] + c for c in tmp_combinations]
                    remaining_combinations += tmp_combinations
        return remaining_combinations

    def is_valid_ip_section(self, s):
        if not 0 <= int(s) <= 255:
            return False
        if len(s) == 1:
            return True
        if s[0] == "0":
            return False
        return True
