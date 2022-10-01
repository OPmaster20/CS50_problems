class Jar:
    def __init__(self, capacity=12):
        if capacity<0 and capacity != int(capacity) and capacity>12:
            raise ValueError("capacityerror")
        self.cookie_jar=capacity
        self.cookie=0
    def __str__(self):
        k='🍪'
        return f"{self.cookie*k}"
    def deposit(self, n):
        if self.cookie>self.cookie_jar:
            raise ValueError("Too many cookie")
        self.cookie+=n
    def withdraw(self, n):
        if self.cookie<n:
            raise ValueError("Not much cookie")
        self.cookie-=n
    @property
    def capacity(self):
        return f"{self.cookie_jar}"
    @property
    def size(self):
        return f"{self.cookie}"
def main():
    n=Jar()
    print(n)
if __name__=='__main__':
    main()
