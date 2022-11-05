class Fibonacci:

    def fib_loop(self, z):
        x = y = 1
        if z == 1 or z == 2:
            return 1
        for _ in range(z-2):
            y += x
            x = y-x
        return y

    def fib_recursivo(self, z):
        if z == 1 or z == 2:
            return 1
        return self.fib_recursivo(z-1) + self.fib_recursivo(z-2)
        
    def fib_cauda(self, z, a = 1, b = 1):
        if z <= 2:
            return b
        return self.fib_cauda(z - 1, b, a + b)


