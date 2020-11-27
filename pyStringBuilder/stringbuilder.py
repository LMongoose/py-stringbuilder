
class StringBuilder():
    """Python equivalent of Java and C# StringBuilders to help who is used to work with them."""

    def __init__(self, obj=None):
        self._array = []
        if(obj is not None):
            self.append(obj)

    def __hash__(self):
        return hash(self._array)

    def __len__(self):
        return len(self._array)

    def __str__(self):
        return "".join(self._array)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return self._array

    ## TODO: validate method parameters and raise TypeError if is wrong

    def clear(self):
        self._array.clear()

    def size(self):
        return len(self)

    def append(self, item):
        if(isinstance(item, bool)):
            self._array.append(str(item))

        elif(isinstance(item, int)):
            self._array.append(str(item))

        elif(isinstance(item, float)):
            self._array.append(str(item))

        elif(isinstance(item, str)):
            for char in item:
                self._array.append(char)

        elif(isinstance(item, list)):
            for element in item:
                self._array.append(str(element))

        elif(isinstance(item, dict)):
            for value in item.values():
                self._array.append(str(value))

        elif(isinstance(item, StringBuilder)):
            for value in item:
                self._array.append(str(value))

        else:
            self._array.append(str(item))

    def append_join(self, separator: str, item: list):
        if(not isinstance(separator, str)):
            raise ValueError(f"The parameter \"separator\" must be a string.")
        if(not isinstance(separator, list)):
            raise ValueError(f"The parameter \"item\" must be a list.")
        self._array.extend(separator.join(str(x) for x in item))

    def char_at(self, index: int):
        if(not isinstance(index, int)):
            raise ValueError(f"The parameter \"index\" must be an integer.")
        return self._array[index]

    def delete(self, start: int, end: int):
        if(not isinstance(start, int)):
            raise ValueError(f"The parameter \"start\" must be an integer.")
        if(not isinstance(end, int)):
            raise ValueError(f"The parameter \"end\" must be an integer.")
        del self._array[start:end]

    def delete_char_at(self, index: int):
        if(not isinstance(index, int)):
            raise ValueError(f"The parameter \"index\" must be an integer.")
        self._array.pop(index)

    def index_of(self, string: str, start: int = 0):
        if(not isinstance(string, str)):
            raise ValueError(f"The parameter \"string\" must be a string.")
        if(not isinstance(start, int)):
            raise ValueError(f"The parameter \"start\" must be an integer.")
        return self._array.index(string, start)

    def insert(self, index: int, item):
        if(not isinstance(index, int)):
            raise ValueError(f"The parameter \"index\" must be an integer.")
        self._array.insert(index, str(item))

    def remove(self, item):
        if(isinstance(item, int)):
            self._array.remove(item)

        elif(isinstance(item, float)):
            self._array.remove(item)

        elif(isinstance(item, str)):
            for char in item:
                self._array.remove(char)

        elif(isinstance(item, list)):
            for element in item:
                self._array.remove(element)

        elif(isinstance(item, dict)):
            for value in item.values():
                self._array.remove(value)

        else:
            self._array.remove(item)

    def replace(self, old: str, new: str):
        if(not isinstance(old, str)):
            raise ValueError(f"The parameter \"old\" must be a string.")
        if(not isinstance(new, str)):
            raise ValueError(f"The parameter \"new\" must be a string.")
        for item in self._array:
            item.replace(old, new)

    def reverse(self):
        self._array.reverse()

    def substring(self, start: int):
        if(not isinstance(start, int)):
            raise ValueError(f"The parameter \"start\" must be an integer.")
        return "".join(self._array[start:])
