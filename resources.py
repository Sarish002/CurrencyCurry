cacheList = []
inputs = []

# Decorator
def cache(function):
    global cacheList, inputs
    def wrapper(country1, country2, value):
        x = [country1, country2, value]
        if x in inputs:
            return cacheList[inputs.index(x)]
        y = function(country1, country2, value)
        inputs.append([country1, country2, value])
        cacheList.append(y)
        return y
    return wrapper
