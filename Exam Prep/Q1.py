def foo():
    try:
        s = 'Five_Go_To_Mystery_Moor'
        print('A: {}'.format(len(s.split('M'))))
        print('B: {}'.format(s[12::2]))
        s.replace('M', 'N')
        print('C: {}'.format(s))
    except:
        print('Something went wrong!')
foo()