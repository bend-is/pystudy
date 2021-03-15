"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, a, bi):
        self.a = a
        self.bi = bi

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Second value must be a Complex")

        return Complex(self.a + other.a, self.bi + other.bi)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Second value must be a Complex")

        return Complex(
            self.a * other.a - self.bi * other.bi,
            self.a * other.bi + other.a * self.bi,
        )

    def __str__(self):
        return f"({self.a}{'+' if self.bi > 0 else ''}{self.bi}i)"


if __name__ == '__main__':
    c_1, c_2 = Complex(2, 3), Complex(3, -1)
    sm = c_1 + c_2
    ml = c_1 * c_2

    print(f"{c_1} + {c_2} = {sm}")
    print(f"{c_1} * {c_2} = {ml}")

    pc_1, pc_2 = complex(2, 3), complex(3, -1)
    psm = pc_1 + pc_2
    pml = pc_1 * pc_2

    assert sm.a == psm.real and sm.bi == psm.imag
    assert ml.a == pml.real and ml.bi == pml.imag
