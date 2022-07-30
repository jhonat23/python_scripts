def truckTour(petrolpumps):
    truck_cap = [petrolpumps[i][0] - petrolpumps[i][1] for i in range(len(petrolpumps))]
    star_point = 0
    av_dist = 0
    new_start = 0
    while(new_start < len(truck_cap)):
        av_dist += truck_cap[new_start]
        if av_dist < 0:
            for _ in range(new_start + 1):
                truck_cap.append(truck_cap.pop(0))
            av_dist = 0
            star_point += new_start + 1
            new_start = 0
        else:
            new_start += 1                
    return star_point

    return max_pe, total_rec

if __name__ == '__main__':

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    print(result)
