'''thunks are datatypes that do not yield values until evaluated, but are not generators.
Stream-nodes are thunked (that is, functions that when run give) 2-tuples of a value
and a thunk for making a successor stream-node.'''

def makethunk(x):
    '''gives a function that will return the value x'''
    return lambda : x

def makestream(val, fun):
    '''imitating Dan Goodman's Racket streams.  It will return a function.
    That function when executed gives a stream-node whose 0-member is the value of this node
    and whose 1-member is a makestream function giving the next node'''
    return (lambda : (val, makestream(fun(val), fun) ))


def first_n_of_stream (startval, fun, n):
    ''' gives a list of first n values of the stream'''
    stream = makestream(startval, fun)
    outlist = [startval] # was [str()[0]]
    counter = 1
    while counter < n:
        counter += 1                   # raise counter by one
        stream = stream()[1]           # that is, the next stream node
        outlist.append (stream()[0])   # append value thereof to outlist
    return outlist

 #  ============== for testing ===================

def double (x):
    return 2 * x

str = makestream(1, double)

output = first_n_of_stream (1, double, 5)

print(output)

# Should give [1, 2, 4, 8, 16]
