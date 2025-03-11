year = input("Enter a year: ")

with open("oscars.txt", "r") as file:
    age = 200
    line_list = [line.strip().split(",") for line in file]
    # print(line_list)
    for line in line_list:
        if line[0] == year:
            print(line[3])
        if age > int(line[2]):
            age = int(line[2])
            name = (line[2], line[3])

    print(name)





