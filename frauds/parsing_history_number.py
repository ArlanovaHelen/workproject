from workproject.celery1 import app


@app.task(bind=True)
def read_file_task(self, name_file):
    try:
        with open(name_file, "r") as input_file:
            num = input_file.read().splitlines()[:1]
            nums1 = [line.split(" ")[1] for line in num if line]
            nums = nums1[0]
        with open(name_file, "r") as input_file:
            imei = input_file.read().splitlines()[2:]
            imeis = [line.split("\t")[1].split(" ")[0]
                     for line in imei if line]
        x = imeis.index("IMSI")
        imei_1 = imeis[:x]
        final_string = ""
        for i in imei_1:
            final_string = final_string + f"{nums}\t{i}\n"
        with open("historycomb.txt", "a") as input_file:
            input_file.write(final_string)
        return nums, imei_1
    except:
        pass


# print(read_file(fr'D:\History\{i}'))


# with open(name_file, 'r') as input_file:
#     data = input_file.read()
# with open('historycomb.txt', 'a') as input_file:
#     input_file.write(data)
