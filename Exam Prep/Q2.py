def foo(l):
    q = []
    try:
        for i in l:
            q.append(i-1)
    except:
        print('A')
    else:
        print('B')
    finally:
        print('C')
        print(q)
foo([1,2,'X',3])