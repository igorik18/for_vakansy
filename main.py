def num_of_buyers(n_customers, n_first_id=0):
    res = {}
    for i in range(n_first_id, n_customers + n_first_id):
        total = sum(map(int, str(i)))
        if res.get(total) is None:
            res[total] = 1
        else:
            res[total] += 1
    return res


if __name__ == '__main__':
    print(num_of_buyers(1000))
    print(num_of_buyers(200, 10000))
