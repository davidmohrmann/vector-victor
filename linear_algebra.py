
class ShapeError(Exception):
    pass

# needs to return a tuple
def shape(vector):
    return (len(vector),)

# needs to return a list
def vector_add(vector1, vector2):
    if shape(vector1) == shape(vector2):
        #list comprehension because can't use for loops
        # the for loop inside the brackets makes it list comphrension
        return [a+b for a,b in zip(vector1,vector2)]
    else:
        raise ShapeError

# needs to return a list
def vector_sub(vector1, vector2):
    if shape(vector1) == shape(vector2):
        return [a-b for a,b in zip(vector1,vector2)]
    else:
        raise ShapeError

def vector_sum(*args):
    if len(set(shape(i) for i in zip(*args)))>1:
        raise ShapeError
    else:
        return [sum(i) for i in zip(*args)]

def dot(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeError
    else:
        return sum(a * b for a, b in zip(vector1, vector2))

def vector_multiply (vector1, scalar):
    return [a * scalar for a in (vector1)]
