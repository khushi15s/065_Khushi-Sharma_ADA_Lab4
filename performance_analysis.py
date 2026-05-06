import time

text = "A" * 10000 + "B"
pattern = "AB"

start = time.time()
"AB" in text
print("Time:", time.time() - start)
