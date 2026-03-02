def duplicate_zeros(inventory):
    
    n = len(inventory)
    zeros = inventory.count(0)

    i = n - 1
    j = n + zeros - 1

    while i < j:
        if j < n:
            inventory[j] = inventory[i]

        if inventory[i] == 0:
            j -= 1
            if j < n:
                inventory[j] = 0

        i -= 1
        j -= 1