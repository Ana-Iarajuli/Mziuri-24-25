# input_file = open('numbers.txt', 'r')
# output_file = open('squared_numbers.txt', 'w')
#
# """
# ციკლი ტრიალებს ფაილში.
# """
#
# for line in input_file:
#     output_file.write(str(int(line) ** 2) + "\n")
#
# input_file.close()
# output_file.close()
#
#
#
# # lazare
# # with open('numbers.txt', 'r') as file:
# #     numbers = file.readlines()
# #
# # with open('squared_numbers.txt', 'w') as output_file:
# #     for number in numbers:
# #         num = int(number.strip())
# #         squared = num * num
# #
# #
# #         output_file.write(f"{squared}\n")

oscars_data = [
    "2020,F,30,Renée Zellweger,Judy",
    "2020,M,38,Joaquin Phoenix,Joker",
    "2019,F,33,Olivia Colman,The Favourite",
    "2019,M,44,Rami Malek,Bohemian Rhapsody"
]

with open("oscars.txt", "w") as file:
    for line in oscars_data:
        file.write(f"{line}\n")

def find_oscar_winners_by_year(input_filename, year):

    with open(input_filename, 'r') as file:
        lines = file.readlines()

    winners = []

    for line in lines:
        fields = line.strip().split(',')
        file_year = fields[0]

        if file_year == str(year):
            name = fields[3]
            winners.append(name)

    if winners:
        print(f"Oscar winners for {year}:")
        for winner in winners:
            print(winner)
    else:
        print(f"No Oscar winners found for the year {year}.")

    year = input("Enter a year to search for Oscar winners: ")
    find_oscar_winners_by_year("oscars.txt", year)