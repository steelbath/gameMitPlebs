
# Object oriented pooling system

from typing import List
from collections import OrderedDict


class Pool():
    class InvalidObject(Exception):
        pass

    def _validate_object(self, obj):
        errors = []

        if getattr(obj, "update", None) is None:
            errors.append("update")
        if getattr(obj, "remove", None) is None:
            errors.append("remove")
        if getattr(obj, "reset", None) is None:
            errors.append("reset")

        raise self.InvalidObject("Object does not contain %s functions"
                                 % ", ".join(errors))

    def __init__(self, *objects):
        for obj in objects:
            self._validate_object(obj)
        self.objects = set(objects)
        self.inactive_objects = set()

    def update(self):
        for obj in self.objects:
            obj.update()

    def remove(self, *objects):
        for obj in objects:
            self.inactive_objects.add(obj)
            self.objects.remove(obj)
            obj.remove()

    def add(self, *objects):
        for obj in objects:
            self._validate_object(obj)
            self.objects.add(obj)

    def activate_object(self, *args, **kwargs):
        """Sets item active if any items left in pool.

        Returns: None if no items left in pool
            None | True
        """
        if not self.inactive_objects:
            return None

        obj = self.inactive_objects.pop()
        obj.reset(*args, **kwargs)
        return True
    

class PoolManager():
    # Use ordered dict, so the update order wont change when adding new pool
    _pools = OrderedDict()

    @classmethod
    def update(cls):
        for pool in cls._pools.values():
            pool.update()

    @classmethod
    def add(cls, pool_name: str, *objects: [List(object)]):
        if pool_name in cls._pools:
            cls._pools[pools_name].add(objects)
        else:
            cls._pools[pools_name] = Pool(objects)

    @classmethod
    def remove(cls, pool_name: str, *objects: [List(object)]):
        # No error handling so any programing error gets raised
        cls._pools[pools_name].remove(objects)

    @classmethod
    def activate_object(cls, pool_name: str, *args, **kwargs):
        return cls._pools[pool_name].activate_object(*args, **kwargs)
