class Solution:
    def calc(self, part):
        part += "+" ## added tmp symbol in the end to sum last item within the loop
        start = x = n = 0
        coeff = 1
        for end, char in enumerate(part):
            # print("charIdx:", equation[end], "char: ", char, char == "+" or char == "-", "slice: ", equation[start:end])
            if char == "+" or char == "-":
                var = part[start:end]
                if var == "":
                    continue
                if "x" in var:
                    var = var[:-1]
                    if var in ["", "+"]:
                        var = 1
                    elif var == "-":
                        var = -1
                    x += int(var) * coeff
                    start = end
                else:
                    n += int(var) * coeff
                    start = end
        return x, n
    
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # how big is N
        # time vs. space complexity?
        
        # split by "=" to left and right; time complexity: O(N)
        # sums Xs and consts on both sides (left and right)
        # take a difference b/w the sides' sums
        # simplify dividing by X's coeff
        # if x==0 and n==0 on the other - infinite
        # if x==0 and a constant on the other - no solution
        # if x on one side, and a constant on the other - solution
 
        # test: 2-x+2x-x-x+1=x
        # test2: "x+5-3+x=6+x-2"
        # test2: "+5-3+x=6+x-2"
        # -x=-1

        left, right = equation.split("=")
        x1, n1 = self.calc(left) # O(leftN)
        x2, n2 = self.calc(right) # O(rightN)
        x, n = x1 - x2, n1 - n2
        n = n / x if (x != 0) else n
        x = 1 if (x != 0) else x
        if x == 0 and n != 0:
            return "No solution"
        if x == 0 and n == 0:
            return "Infinite solutions"
        return "x={}".format(int(-n))
        # time complexity O(N)


