def print_squared_values(n):
    for i in range(n):
        print(i**2)

def print_odd_squared_values(n):
    for i in range(n):
        if i % 2 != 0:
            print(i**2)

n = int (input("Masukkan nilai n: "))
print("Hasil Bagian A:")
print_squared_values(n)

print("\nHasil Bagian B:")
print_odd_squared_values(n)