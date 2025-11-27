def maximizeRentalRevenue(vmStock, m):
    revenue = 0

    for _ in range(m):
        vmStock.sort(reverse=True)
        if vmStock[0] == 0:
            break

        revenue += vmStock[0]
        vmStock[0] -= 1
    return revenue
vmStock = [2, 1, 1,3]
m = 4
print(maximizeRentalRevenue(vmStock, m))