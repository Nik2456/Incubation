class Class1:
    def process(self):
        return "Processed data"

class Class2:
    pass
def process_data(obj):
    if hasattr(obj, "process") and callable(obj.process):
        return obj.process()
    return None

object1 = Class1()
object2 = Class2()

print(process_data(object1))
print(process_data(object2))