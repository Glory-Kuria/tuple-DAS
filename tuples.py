

tuples= ("kenya", "somalia", "uganda", "rwanda", "cameroon", "ethiopia","india")
print(tuples)
print(tuples[:4])
print(len(tuples))
print(tuples[-1])
print(tuples[2:4])

if "india" in tuples:
  print("Yes, 'india' is in the tuple")
  
  
x = list(tuples)
x.append("pakistan")
x.reverse()
x.extend(["sweden","spain","somali land","burundi"])
x.pop()
x.remove("cameroon")
for i in x: print(i)
tuples = tuple(x)
print(tuples)

tuplestown= ("nairobi","kisumu","mumbai")
all_tuples= tuplestown+tuples
print(all_tuples)

print(type(all_tuples))



