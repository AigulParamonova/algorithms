"""A. Полиномиальный хеш. Хеш функции.
Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей написать функцию, вычисляющую хеш
строки s. В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.
Полиномиальный хеш считается по формуле:
h(s) = (s_{1}a^n-1 + s_{2}a^n-2 + ... + s_{n-1}a + s_{n}) mod m
"""
def polynomial_hash(base, module, string):
    hash = 0
    for char in string:
        hash = (hash * base + ord(char)) % module
    return hash

def main():
    base = int(input())
    module = int(input())
    string = input()
    print(polynomial_hash(base, module, string))

if __name__ == '__main__':
    main()