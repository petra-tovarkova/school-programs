text = input("Zadejte text:")
i = 0
y = 0

for znak in text:
    if znak in "iíIÍ":
        i = i + 1

    elif znak in "yýYÝ":
        y = y + 1

if i > y:
	i-y = n
    print("počet měkkých i:",i)
    print("počet měkkých y:",y)
    print("V text je více měkkých i o",n,".")

elif y > i:
	y-i = n
    print("počet měkkých i:",i)
    print("V text je více tvrdých y.")
    print("V text je více tvrdých y o",n,".")

    
else:
    print("V text je stejný počet měkkých a tvrdých i/y.")