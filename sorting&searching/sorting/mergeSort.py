class MergeSort:

    def __init__(self, array):
        self.array = array

    def set_arr(self, array):
        self.array = array

    def get_array(self):
        return self.array

    def merge_sort(self, array):
        length = len(array)
        if length <= 1: return
        
        middle = length // 2
        
        left_array = array[:middle]
        right_array = array[middle:]
        
        self.merge_sort(left_array)
        self.merge_sort(right_array)
        
        self.merge_arrays(left_array, right_array, array)
        
    def merge_arrays(self, left_array, right_array, array):
        left_size = len(array) // 2
        right_size = len(array) - left_size
        i, l, r = 0 , 0, 0
        
        while l < left_size and r < right_size:
            if left_array[l] < right_array[r]:
                array[i] = left_array[l]
                i += 1
                l += 1
            else:
                array[i] = right_array[r]
                i += 1
                r += 1
                
        while l < left_size:
            array[i] = left_array[l]
            i += 1
            l += 1
            
        while r < right_size:
            array[i] = right_array[r]
            i += 1
            r += 1


ms = MergeSort([17, 89, 5, 23, 66, 38, 91, 14, 57])
ms.merge_sort(ms.get_array())
print(ms.get_array())
