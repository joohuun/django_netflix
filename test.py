immutable = "String is immutable!!"
mutable = ["list is mutable!!"]
 
string = immutable
list_ = mutable

string += " immutable string!!"
list_.append("mutable list!!")

print(immutable)
print(mutable)
print(string)
print(list_)

# 해당 코드를 실행했을 때 나오는 결과를 유추하고
# mutable 자료형과 immutable 자료형은 어떤 게 있는지 알아야 함