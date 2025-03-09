# # MY PROBLEM:
# import timeit
#
# sampleDict = {i: i**2 for i in range(10**6)}
#
# time_keys = timeit.timeit(
#     stmt="for k in sampleDict: val = sampleDict[k]",
#     globals=globals(),
#     number=10
# )
#
# time_values = timeit.timeit(
#     stmt="for v in sampleDict.values(): val = v",
#     globals=globals(),
#     number=10
# )

# print(f"Time for first loop (keys): {time_keys:.5f} seconds")
# print(f"Time for second loop (values): {time_values:.5f} seconds")








for num in range(1006):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)