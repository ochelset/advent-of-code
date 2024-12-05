import hashlib

inputdata = "reyedfim"

password = []
password2 = [None, None, None, None, None, None, None, None]
i = 0

while True:
    i += 1
    p = inputdata + str(i)
    h = hashlib.md5(p.encode("utf-8")).hexdigest()
    if h[:5] == "00000":
        if len(password) < 8:
            password.append(h[5])

        pos = int(h[5], base=16)
        if pos >= 8 or password2[pos] != None:
            continue

        password2[pos] = h[5]
        if not None in password2:
            break

print("Part 1:", "".join(password))
print("Part 2:", "".join(password2))