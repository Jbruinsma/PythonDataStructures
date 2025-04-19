class SelectionSort:

    def __init__(self, array= None):
        if array is None:
            self.reset_array()
        else:
            self.array = array

    def set_array(self, array):
        self.array = array

    def reset_array(self):
        self.array = [42, 17, 89, 5, 23, 66, 38, 91, 14, 57]

    def sort_ascending(self):
        for i in range(len(self.array) - 1):
            smallest_val_index = self.get_smallest_val_index(i)
            self.swap(smallest_val_index, i)
        print(self.array)
        return self.array

    def sort_descending(self):
        for i in range(len(self.array) - 1):
            largest_val_index = self.get_largest_val_index(i)
            self.swap(i, largest_val_index)
        print(self.array)
        return self.array

    def get_largest_val_index(self, start_from):
        largest_val_index = start_from
        for i in range(start_from + 1, len(self.array)):
            if self.array[i] > self.array[largest_val_index]:
                largest_val_index = i
        return largest_val_index

    def get_smallest_val_index(self, start_from):
        smallest_val_index = start_from
        for i in range(start_from + 1, len(self.array)):
            if self.array[i] < self.array[smallest_val_index]:
                smallest_val_index = i
        return smallest_val_index

    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]




ss = SelectionSort()
ss.sort_descending()
ss.reset_array()
ss.sort_ascending()
