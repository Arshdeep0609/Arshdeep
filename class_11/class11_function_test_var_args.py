def test_var_args(f_arg,*argv,**kwargs):
    print("first normal arg:",f_arg)
    if argv is not None:
        for arg in argv:
            print("another arg through *argv:",arg)
    if kwargs is not None:
        for(key,value) in kwargs.items():
            print(key,value)
test_var_args("training")
test_var_args('learning','python','third','day')
test_var_args('learning','python',name="praveen")
test_var_args('programming',name="praveen",profession="trainer")
