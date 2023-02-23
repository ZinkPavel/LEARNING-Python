from math import factorial


def get_number_of_combination(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))


def main():
    n, k = map(int, input().split())
    result = get_number_of_combination(n, k)
    print(result)


if __name__ == "__main__":
    main()
