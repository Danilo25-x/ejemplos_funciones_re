import re


# -------------------------
# 1. re.match()
# -------------------------
print("=== re.match() ===")
resultado = re.match(r"a(b|c)*", "abbc")
print(resultado)

resultado2 = re.match(r"a(b|c)*", "babbc")
print(resultado2)


# -------------------------
# 2. re.search()
# -------------------------
print("\n=== re.search() ===")
resultado = re.search(r"b(c|d)", "abce")
print(resultado)

resultado2 = re.search(r"b(c|d)", "axby")
print(resultado2)


# -------------------------
# 3. re.findall()
# -------------------------
print("\n=== re.findall() ===")
resultado = re.findall(r"\d+", "abc123def456")
print(resultado)


# -------------------------
# 4. re.sub()
# -------------------------
print("\n=== re.sub() ===")
resultado = re.sub(r"\s+", " ", "Hola   mundo")
print(resultado)