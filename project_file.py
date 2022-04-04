print("Text IN Image")
print("\n")
c = input("E for write\nR for read :").capitalize()
if c == "E":
    img = input("path of a image : ")
    msg = input("your message : ")

    with open(img, "rb") as f:
        new_dt = f.read()
        new_dt = new_dt.split("©®SH".encode("utf-32"))[0]
        new_dt += "©®SH".encode("utf-32")
        new_dt += msg.encode("utf-16")
    with open(img, "wb") as f:
        f.write(new_dt)

elif c == "R":
    img = input("path of image : ")
    with open(img, "rb") as f:
        d = f.read().split("©®SH".encode("utf-32"))
        print(f"\nyour msg is : \n{d[1].decode('utf-16')}")
