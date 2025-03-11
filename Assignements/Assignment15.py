# დაწერეთ პროგრამა, რომლის მეშვეობით ერთი ფაილიდან წაიკითხავთ კონტენტს.
# ჩაწერეთ მთლიანი კონტენტი მეორე (ახალ) ფაილში ერთ ხაზზე. მითითება: თუ
# პირველ ფაილში არის 3 სტრიქონი, ახალ ფაილში ჩაწერეთ ერთ სტრიქონზე და
# გამოყავით სივრცით.


def content_to_another_file(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
        joined_content = " ".join([line.strip() for line in lines])
        # file_content = []
        # for line in lines:
        #     file_content.append(line.strip())
        # joined_content = " ".join(file_content)

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(joined_content)
        return "Copying content to another file was successful!"
    except FileNotFoundError as error_message:
        return error_message
    except Exception as e:
        return e


in_file = "C:/Users/Artemis/Documents/Artemis/მზიური/Mziuri-Python1/Topics/files/food.txt"
out_file = "food2.txt"
print(content_to_another_file(in_file, out_file))

