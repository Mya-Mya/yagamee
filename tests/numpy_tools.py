import sys,os
sys.path.insert(0, os.path.abspath("../"))
import yagamee

arr = ["A","B","C","D"]
print(yagamee.numpy_tools.index_like(arr))
print(yagamee.numpy_tools.index_like(arr,start=2))

print(yagamee.numpy_tools.text2mat("3 1 4;1 5 9;2 6 5"))
print(yagamee.numpy_tools.text2mat("3 1 4;1 5 9;2 6 5.3"))
print(yagamee.numpy_tools.text2mat("3 1 4;1 5 9;2 6 5.0"))
print(yagamee.numpy_tools.text2mat("3 1 4;1 5 9;2 6 5e3"))
print(yagamee.numpy_tools.text2mat("3 1 4;1 5 9;a b"))
print(yagamee.numpy_tools.text2mat("3 1 4;1 5 9;2 6"))