def main():
    t = 1

    for _ in range(t):
        solve()

def solve():
    n = int(input())
    errors = list(map(int, input().split()))
    errors.sort()

    errors_removed_1 = list(map(int, input().split()))
    errors_removed_1.sort()

    first_error = None

    for i in range(len(errors_removed_1)):
        if errors_removed_1[i] != errors[i]:
            first_error = errors[i]
            errors.pop(i)
            break

    if first_error is None:
        first_error = errors[-1]
        errors.pop()

    errors_removed_2 = list(map(int, input().split()))
    errors_removed_2.sort()

    second_error = None

    for i in range(len(errors_removed_2)):
        if errors_removed_2[i] != errors[i]:
            second_error = errors[i]
            break

    if second_error is None:
        second_error = errors[-1]
    
    print(first_error)
    print(second_error)

main()