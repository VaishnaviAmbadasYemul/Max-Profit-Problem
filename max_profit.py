def max_profit(n):
    buildings = [
        ('T', 5, 1500),
        ('P', 4, 1000),
        ('C', 10, 2000)
    ]

    max_earning = 0
    best_combo = (0, 0, 0)

    for T in range(n // 5 + 1):
        for P in range(n // 4 + 1):
            for C in range(n // 10 + 1):

                times = (
                    ['T'] * T +
                    ['P'] * P +
                    ['C'] * C
                )

                total_build_time = (
                    T * 5 + P * 4 + C * 10
                )

                if total_build_time > n:
                    continue

                time_spent = 0
                earning = 0

                # simulate building one by one
                for b in times:
                    if b == 'T':
                        time_spent += 5
                        earning += (n - time_spent) * 1500
                    elif b == 'P':
                        time_spent += 4
                        earning += (n - time_spent) * 1000
                    else:
                        time_spent += 10
                        earning += (n - time_spent) * 2000

                if earning > max_earning:
                    max_earning = earning
                    best_combo = (T, P, C)

    return max_earning, best_combo


# Test cases
for time in [7, 8, 13]:
    profit, (T, P, C) = max_profit(time)
    print(f"Time Unit: {time}")
    print(f"Earnings: ${profit}")
    print(f"T: {T} P: {P} C: {C}")
    print()
