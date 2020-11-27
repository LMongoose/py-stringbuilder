
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

    def __getitem__(self, index: int):
        if(not isinstance(index, int)):
            raise ValueError("The parameter \"index\" must be an integer.")
        
        return self._array[index]

    def append(self, item) -> None:
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
            for value in item._array:
                self._array.append(str(value))

        else:
            self._array.append(str(item))

    def append_join(self, separator: str, item: list) -> None:
        if(not isinstance(separator, str)):
            raise ValueError("The parameter \"separator\" must be a string.")

        if(not isinstance(separator, list)):
            raise ValueError("The parameter \"item\" must be a list.")

        self._array.extend(separator.join(str(x) for x in item))

    def char_at(self, index: int) -> str:
        if(not isinstance(index, int)):
            raise ValueError("The parameter \"index\" must be an integer.")

        return self._array[index]

    def clear(self) -> None:
        self._array.clear()

    def delete(self, start: int, end: int) -> None:
        if(not isinstance(start, int)):
            raise ValueError("The parameter \"start\" must be an integer.")

        if(not isinstance(end, int)):
            raise ValueError("The parameter \"end\" must be an integer.")

        del self._array[start:end]

    def delete_char_at(self, index: int) -> None:
        if(not isinstance(index, int)):
            raise ValueError("The parameter \"index\" must be an integer.")

        self._array.pop(index)

    def index_of(self, string: str, start = 0) -> int:
        if(not isinstance(string, str)):
            raise ValueError("The parameter \"string\" must be a string.")

        if(not isinstance(start, int)):
            raise ValueError("The parameter \"start\" must be an integer.")

        return self._array.index(string, start)

    def insert(self, index: int, item) -> None:
        if(not isinstance(index, int)):
            raise ValueError("The parameter \"index\" must be an integer.")

        self._array.insert(index, str(item))

    def remove(self, item) -> None:
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

    def replace(self, old: str, new: str) -> None:
        if(not isinstance(old, str)):
            raise ValueError("The parameter \"old\" must be a string.")

        if(not isinstance(new, str)):
            raise ValueError("The parameter \"new\" must be a string.")

        for item in self._array:
            item.replace(old, new)

    def reverse(self) -> None:
        self._array.reverse()

    def substring(self, start: int, end: int = None) -> str:
        if(not isinstance(start, int)):
            raise ValueError("The parameter \"start\" must be an integer.")

        if(not isinstance(end, int)):
            raise ValueError("The parameter \"end\" must be an integer.")

        if(end == None):
            end = (len(self) - 1)

        return "".join(self._array[start:end])
