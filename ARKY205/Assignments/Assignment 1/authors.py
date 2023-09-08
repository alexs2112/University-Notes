i = """
Kenoyer, J. Mark ; Price, T. Douglas ; Burton, James H.
"""

cons = i.split(' ; ')
out = []
out.append(cons[0])
for c in cons[1:]:
    if ',' in c:
        a, b = c.split(', ')
        new = f"{b} {a}"
    else:
        new = c
    out.append(new)

res = ''
for o in out:
    res += o + ', '

print(res)
