# you have string. calculate character epiring and output the most risent.
import operator
string = "you have string. calculate character epiring and output the most risent."
char_map = {}
result = {}

for i in string:
  if i in char_map:
    char_map[i] += 1
  else:
    char_map[i] = 1

for key in string:
  result[key] = result.get(key, 0) + 1


# for key, value in sorted(char_map.items(), key=operator.itemgetter(1), reverse=True):
#   print(key, ":", value)

print(sorted(char_map.items(), key=lambda elem: elem[1], reverse=True))