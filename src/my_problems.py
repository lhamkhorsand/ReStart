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










#
# ✔ json.dump() → Creates a file
# ✔ json.dumps() → Does not create a file, only generates a JSON string
# ✔ json.load() → Reads from a JSON file
# ✔ json.loads() → Reads from a JSON string, not a file