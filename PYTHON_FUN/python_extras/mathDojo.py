class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self.result

    def subtract(self, num, *nums):
        self.result = num
        for n in nums:
            self.result -= n
        return self.result

# create an instance:
md = MathDojo()
x = md.add(2.4,1.1)
print(f"x = {x}")

y = md.subtract(10,5,5,5)
print(f"y = {y}")
