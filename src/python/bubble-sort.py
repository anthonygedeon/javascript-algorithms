def bubble_sort(unordered_list):
    """
        Summary
            Bubble sort is a sorting algorithm that repeatedly steps through the list, 
            compares adjacent elements and swaps them 
            if they are in the wrong order. 
            The pass through the list is repeated until the list is sorted.

        Example:
            Given:  [9, 21, 39, 12, 28, 45, 6, 27, 9, 46]

                =>    [9, 21, 39, 12, 28, 45, 6, 27, 9, 46]

                =>    [9, 21, 12, 39, 28, 45, 6, 27, 9, 46]
                    
                =>    [9, 21, 12, 28, 39, 45, 6, 27, 9, 46]
                    
                =>    [9, 21, 12, 28, 39, 6, 45, 27, 9, 46]
                    
                =>    [9, 21, 12, 28, 39, 6, 27, 45, 9, 46]
                    
                =>    [9, 21, 12, 28, 39, 6, 27, 9, 45, 46]
            ...

        Returns:
            [Array]: a sorted array in place
    """

    pass_counter = 0

    while True:
        for i in range(0, len(unordered_list)):
            if (len(unordered_list) - i) == 1: # prev element is offset by 1 from last element
                break

            prev_pos = unordered_list[i]
            next_pos = unordered_list[i + 1]

            if prev_pos > next_pos:
                unordered_list[i + 1] = prev_pos
                unordered_list[i] = next_pos
                pass_counter = 0
            elif prev_pos < next_pos:
                pass_counter += 1

                if pass_counter == len(unordered_list):
                    return unordered_list

                continue