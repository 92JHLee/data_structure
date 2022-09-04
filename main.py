def bubble_sort(list):
    unsorted_until_index = len(list) -1 #어떤 인덱스까지 아직 정렬되지 않았는지 기록함. 처음에는 전체 배열이 정렬되지 않았으므로 마지막 인덱스로 변수를 초기화함
                                        # unsorted_until_index = 7-1 = 6
    sorted = False #배열의 정렬여부를 기록함. 물론 처음 실행될 때는 정렬되지 않은 상태

    while not sorted: #not sorted : 배열이 정렬될때까지 while문을 돌린다.
        sorted = True #값을 교환하는 즉시 sorted를 False로 변경할 것
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted=False
                list[i],list[i+1] = list[i+1],list[i]
        unsorted_until_index = unsorted_until_index-1

list = [65,55,45,35,25,15,10]
bubble_sort(list)
print(list)
