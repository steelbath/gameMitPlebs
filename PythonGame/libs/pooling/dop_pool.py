
# Data oriented pooling system


class Pool():
    def __init__(self):
        self.inactive_objects = list()

    def add(self, *objects):
        self.objects.extend(obj)

    def get_object(self):
        """Returns last item from pool.

        Returns: None if no items left in pool
            None | {index, data}
        """
        if not self.inactive_objects:
            return None

        return self.inactive_objects.pop()


class StaticListPool():
    """Pool intended for object lists that cannot change size"""
    def __init__(self):
        self.inactive_indices = list()

    def add(self, index):
        self.inactive_indices.append(index)

    def get_object(self):
        """Returns first index to item from pool.

        Returns: None if no items left in pool
            None | index
        """
        if not self.inactive_indices:
            return None

        return self.inactive_indices.pop()
