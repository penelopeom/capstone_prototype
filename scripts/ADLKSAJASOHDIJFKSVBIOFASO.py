owner = "A   B  D"

while owner.count("  ") > 0:
    owner = owner.replace("  ", " ").strip()
print(owner)