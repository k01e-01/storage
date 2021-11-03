class Queue:
    """
    Queue instance
    """

    def __init__(self, inheritArray=[]):        # inheritArray -> array to inherit from
        """
        Create a Queue instance
        """

        if not isinstance(inheritArray, list):
            raise TypeError ("inheritArray was not set to a list!")

        self.array = inheritArray
    
    def pop(self):
        """
        Return and delete the value at position 0 in the array
        """

        if len(self.array) <= 0:
            raise IndexError ("Index 0 does not exist!")

        return self.array.pop(0)                # return value and delete
    
    def drop(self, value):
        """
        Add a new value to the end of the array
        """

        self.array.append(value)


if __name__ == "__main__":
   
    q = Queue(["foo","bar"])

    q.drop("value")

    print(q.array)
    print(q.pop())
    print(q.array)
