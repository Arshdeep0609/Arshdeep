def test_fun(stream,course,fee):
    print("arg1:",stream)
    print("arg2:",course)
    print("arg3:",fee*2)
    return
tup1=('programming','python',20000)
test_fun(*tup1)
