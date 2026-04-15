import csv

def get_aggregates(data):

    if not (isinstance(data,str)):
        raise ValueError("Wrong type submitted to the function gat_aggregates --  need string")
    local_sum = 0
    local_count = 0
    try:
        with open (data, mode = 'r', encoding = 'utf-8') as f:
            lector = csv.reader(f)
            
            for ligne in lector:
                local_sum += int(ligne[1])
                local_count += 1
    except:
        raise ValueError("Error while fetching the file")
    
    assert type(local_sum) is int
    assert type(local_count) is int
    
    return local_sum, local_count


