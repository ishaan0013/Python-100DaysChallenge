def my_generator():
    yield from range(5000)


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# for j in gen:
#     print(j)
