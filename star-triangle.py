def print_star_triangle(height):
    for i in range(height):
        stars = "*" * (i+1)
        print(stars)
    for i in range(height, 0, -1):
        stars = "*" * (i - 1)
        print(stars)

try:
    height = int(input("Masukkan height: "))
    print_star_triangle(height)
except ValueError:
    print("Masukkan angka yang valid .")
