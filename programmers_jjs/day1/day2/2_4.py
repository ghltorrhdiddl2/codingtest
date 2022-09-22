def solution(num):
    count = 0

    while(1):
        if (count >= 500):
            return -1

        if (num == 1):
            return count;

        if (not num % 2):
            num /= 2
            count += 1
        else:
            num = (num * 3) + 1
            count += 1