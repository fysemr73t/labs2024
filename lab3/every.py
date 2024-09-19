"""
Generate every string that can be typed less than 5 characters in length.
THis is ASCII characters 32..127, which we will compute in Base96.
"""


if __name__=="__main__":
    for count in range(1,6):
        for i in range(0,96**count):
            s = ''
            for j in range(count):
                val = (i // 96**j) % 96
                s += chr(val+32)
            print(s)
