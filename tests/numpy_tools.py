import sys,os
sys.path.insert(0, os.path.abspath("../"))
import yagamee

arr = ["A","B","C","D"]
print(yagamee.numpy_tools.index_like(arr))
print(yagamee.numpy_tools.index_like(arr,start=2))