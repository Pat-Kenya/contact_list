def fizz_buzz(start, end):
    result = []
    for fizz_buzz in range(1, 101):
        if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
            result.append("FizzBuzz")
        elif fizz_buzz % 3 == 0:
            result.append("Fizz")
        elif fizz_buzz % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(fizz_buzz))
    return result
def main():
    print("fizz_buzz from 1 to 100:")
    print('\n'.join(fizz_buzz(1, 100)))
if __name__ == "__main__":
    main()