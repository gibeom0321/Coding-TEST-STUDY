def solution(rank, attendance):
    index_list = [i for i in range(len(rank))]
    tuple_list = []
    for pair in zip(rank, index_list):
        if attendance[pair[1]]:
            tuple_list.append(pair)
    tuple_list.sort()      
    return 10000*tuple_list[0][1] + 100*tuple_list[1][1] + tuple_list[2][1]