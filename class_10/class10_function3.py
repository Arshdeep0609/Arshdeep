def test_fun(stream,course,fee):
    print("arg1:",stream)
    print("arg2:",course)
    print("arg3:",fee*2)
    return
dict1={"fee":30000,"course":"animation","stream":'multimedia'}
test_fun(**dict1)
