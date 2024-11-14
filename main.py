import math

def solve_quadratic(a, b, c):
    def validate_coefficients(a, b, c):
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise TypeError("Коэффициенты должны быть числами.")
        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть нулевым.")

    def calculate_discriminant(a, b, c):
        return b ** 2 - 4 * a * c

    validate_coefficients(a, b, c)
    discriminant = calculate_discriminant(a, b, c)

    if discriminant < 0:
        return None

    sqrt_discriminant = math.sqrt(discriminant)
    divisor = 2 * a

    if discriminant == 0:
        return (-b / divisor,)

    x1 = (-b + sqrt_discriminant) / divisor
    x2 = (-b - sqrt_discriminant) / divisor
    return (x1, x2)
