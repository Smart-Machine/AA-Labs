import decimal


class FibonacciNthTerm:

    @classmethod
    def multiply(cls, F, M):
        x = (F[0][0] * M[0][0] +
             F[0][1] * M[0][1])
        y = (F[0][0] * M[0][1] +
             F[0][1] * M[1][1])
        z = (F[1][0] * M[0][0] +
             F[1][1] * M[1][0])
        w = (F[1][0] * M[0][1] +
             F[1][1] * M[1][1])
        
        F[0][0] = x
        F[0][1] = y
        F[1][0] = z
        F[1][1] = w

    @classmethod
    def power(cls, F, n):
        M = [[1, 1], [1, 0]]
        for i in range(2, n+1):
            cls.multiply(F, M)

    @classmethod
    def recursive_method(cls, n):
        if n <= 1:
            return n 
        else:
            return cls.recursive_method(n-1) + cls.recursive_method(n-2)

    @classmethod
    def iterative_method(cls, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else: 
            n1 = 0
            n2 = 1
            for _ in range(2, n+1):
                y = n1 + n2
                n1 = n2 
                n2 = y
            return y

    @classmethod 
    def dp_method(cls, n):
        term_list = [0, 1]
        for i in range(2, n+1):
            term_list.append(term_list[i-1] + term_list[i-2])
        return term_list[n]
    
    @classmethod
    def matrix_power_method(cls, n):
        F = [[1, 1], [1, 0]]
        if n == 0: return 0
        cls.power(F, n-1)
        return F[0][0]

    @classmethod
    def binet_formula_method(cls, n):
        ctx = decimal.Context(prec=60, rounding=decimal.ROUND_HALF_EVEN)
        phi = decimal.Decimal((1 + decimal.Decimal(5**(1/2))))
        phi2 = decimal.Decimal((1 - decimal.Decimal(5**(1/2))))
        return int(
            (ctx.power(phi, decimal.Decimal(n)) - ctx.power(phi2, decimal.Decimal(n)))
            /(2**n * decimal.Decimal(5**(1/2)))
        )

    @classmethod 
    def tail_recursive_method(cls, n, a = 0, b = 1):
        if n == 0: 
            return a
        if n == 1:
            return b
        return cls.tail_recursive_method(n-1, b, a+b)