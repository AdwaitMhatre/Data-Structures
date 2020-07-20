from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['yaexample.com','goexample.com','example.com']

quotes = [  'Luck is what happens when preparation meets opportunity',
            'All cruelty springs from weakness',
            'Begin at once to live, and count each separate day as a separate life',
            'Throw me to the wolves and I will return leading the pack']

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_quotes(list_of_quotes):
    return choice(list_of_quotes)

def generate_records(length_of_name, list_of_domains, total_records, list_of_quotes):
    with open("data.txt", "w") as to_write:
        for num in range(total_records):
            key = generate_name(length_of_name)+"@"+get_domain(list_of_domains)
            value = get_quotes(quotes)
            to_write.write(key + ":" + value + "\n")
        to_write.write("mashrur@example.com:Don't let me leave Murph\n")
        to_write.write("evgeny@example.com:All I do is win win win no matter what!\n")

generate_records(10, list_of_domains, 100000, quotes)

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

first = HashMap(256)
with open("data.txt") as f:
    for line in f:
        key,value = line.split(":")
        first.gen_value(key,value)

first.get_value("mashrur@example.com")
first.get_value("ggeeemozvb@example.com")
first.get_value("evgeny@example.com")
