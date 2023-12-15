from random import choice


def read_file():
    with open("text_sample.txt", "a") as file:
        # lines = file.readlines()
        try:
            file.write("\nadding to the file...")
            return "Successfully written to the file!"
        except:
            return "Failed to write!"

    
def trigger():
    print("started!")
    print(read_file())
    





if __name__ == "__main__":
    trigger()
