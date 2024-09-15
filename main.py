# module_1_6.py
# 15.09.2024 Словари и множества.
my_dict = {"Vladimir" : 1990, "Nastya" : 1992, "Bonaparte" : 1812}
print("Dict:", my_dict)
print("Existing value:", my_dict["Vladimir"])
print("Not existing value:", my_dict.get("Napoleon"))
my_dict.update({"Gogol" : 1809, "Tolstoy" : 1828})
print("Deleted value:", my_dict.pop("Bonaparte"))
print("Modified dictionary:", my_dict)
my_set={"W", "W", "W", "Leningrad", "SPB", ".ru"}
print("Set:", my_set)
my_set.add("Vincent van Gogh")
my_set.add(7)
my_set.remove(".ru")
print("Modified set:", my_set)