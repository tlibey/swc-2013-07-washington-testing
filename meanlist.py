def meanlist(a):
    r""" doc

    a is list

    """
    import nose.tools as nt
    try:
        nt.assert_is_instance(a,list)
    except AssertionError:
        raise TypeError("Not a list!")
        
    
    try:
        assert len(a) > 0
    except AssertionError:
        raise TypeError("List not populated!")
    
    
        
        
    n = len(a)
    m = 0.0
    for i in a:
        try:
            i = float(i)
            m+=i
        except ValueError as e:
            return "failure: string not convertable to #"
        except Exception as e:
            return e
        #assert type(i)!=str  
    return m/float(n)