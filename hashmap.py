class HashMap:

    def __init__(self,size):
        self.size = size
        self.hashmap = self.gen_buckets()

    def gen_buckets(self):
        return [[] for i in range(self.size)]

    def gen_value(self,key,value):
        hash_index = hash(key)%self.size
        instance = self.hashmap[hash_index]
        found_key = False
        for index,record in enumerate(instance):
            key_already, value_already = record
            if key == key_already:
                found_key = True
                break
        if found_key:
            instance[index] = (key,value)
        else:
            instance.append((key,value))

    def get_value(self,key):
        hash_index = hash(key)%self.size
        instance = self.hashmap[hash_index]
        found_key = False
        for index,record in enumerate(instance):
            key_already, value_already = record
            if key == key_already:
                found_key = True
                break
        if found_key:
            return print(value_already)
        else:
            return print("No such email address found")

    def __str__(self):
        return "".join(str(item) for item in self.hashmap)

first = HashMap(20)
first.gen_value("adwait","footballer")
first.gen_value("ayush","pianist")
first.gen_value("da vinci","painter")
print(first)
first.get_value("adwait")
