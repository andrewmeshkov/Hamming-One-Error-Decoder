class HammingCode:

    def __init__(self, code):
        self.code = code
        self.bools = {}
        self.check_error()
        self.fill_dict()
        self.ind_error = 0
        self.s_array = []
        self.s_matrix = []
        self.s_values = []
        self.visualize()
        self.find_error()
        self.correct_code()

    def check_error(self):
        if (len(self.code) != (self.code.count("0") + self.code.count("1"))) \
                or (bin(len(self.code))[2:].count("0") != 0):
            self.code = input("Введите валидный код")
            self.check_error()
            self.fill_dict()

    def fill_dict(self):
        r = 1
        i = 1
        for ind in range(len(self.code)):
            if bin(ind+1).count("1") == 1:
                self.bools[f"r{r}"] = self.code[ind]
                r += 1
            else:
                self.bools[f"i{i}"] = self.code[ind]
                i += 1

    def from_str_to_bool(self, string):
        res = 0
        for i in range(len(self.code)):
            if string[i] == "#":
                res ^= int(self.code[i])
        return res

    def visualize(self):
        print("".join([str(i) for i in self.bools.values()]))
        for i in range(len(bin(len(self.code))[2:])):
            temp = ""
            temp += ((2 ** i) - 1) * ' '
            temp += ((2 ** i) * '#' + (2 ** i) * ' ') * \
                    ((len(self.code) - (2 ** i)) // ((2 ** (i + 1))) )
            temp += (2 ** i) * '#'
            self.s_matrix.append(temp)
            self.s_values.append(self.from_str_to_bool(temp))
            print(temp, self.s_values[-1])

    def find_error(self):
        for ind in range(len(self.code)):
            flag = True
            for i in range(len(self.s_matrix)):
                if self.s_matrix[i][ind] == "#" and self.s_values[i] == 0:
                    flag = False
                    break
                if self.s_matrix[i][ind] == " " and self.s_values[i] == 1:
                    flag = False
                    break
            if flag:
                self.ind_error = ind
        print(list(self.bools.keys())[self.ind_error])

    def correct_code(self):
        ind_error = list(self.bools.keys())[self.ind_error]
        self.bools[ind_error] = str(1 - int(self.bools[ind_error]))
        self.code = "".join(self.bools.values())
        self.visualize()


hamming = HammingCode(input())

#"111101011001000"