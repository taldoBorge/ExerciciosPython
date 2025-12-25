open_doors = [21, 22, 80, 81, 443, 445, 3306, 8080]

pair = filter(lambda port: port % 2 == 0, open_doors) #filtering even ports

print("Even ports:", list(pair)) #Output: [22, 80, 3306, 8080] even ports

odd = filter(lambda port: port % 2 != 0, open_doors) #filtering odd ports

print("Odd ports:", list(odd)) #Output: [21, 81, 443, 445] odd ports