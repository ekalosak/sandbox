import pdb

def debuggable(function):

    def inner(*args, **kwargs):
        print "Running function debuggable: {}".format(function)
        try:
            function(*args, **kwargs)
        except Exception as ee:
            pdb.set_trace()

    return inner

@debuggable
def messedup(a, b, c):
    print a, b, c
    print "Got args"
    return d

if __name__ == '__main__':
    messedup(1, 2, 3)
