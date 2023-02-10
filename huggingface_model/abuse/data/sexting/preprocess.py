f = open('sexting_dataset.txt')
lines = f.readlines()
f.close()
new_lines = []
for line in lines:
  if line[0:2] == 'He':
    new_lines.append(line[3:])
  elif line[0:3] == 'She':
    new_lines.append(line[4:])
  elif line[0:2] == 'Me':
    new_lines.append(line[3:])
  else:
    continue
f = open('sexting_clean.txt', 'w')
f.writelines(new_lines)
f.close()

