import csv

def get_aggregates(data):

    local_sum = 0
    local_count = 0

    with open (data, mode = 'r', encoding = 'utf-8') as f:
        lector = csv.reader(f)

        for ligne in lector:
            local_sum += int(ligne[1])
            local_count += 1

    return local_sum, local_count


