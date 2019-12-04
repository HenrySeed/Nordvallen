from random import randint
from utils import get_wrap

class NPC():
    def __init__(self, name="Kev the Ledge", dialog_start=None):
        self.name = name
        self.dialog_start = dialog_start

    def start_dialog(self):

        current_dialog = self.dialog_start
        left_convo = False

        while not left_convo:
            print(str(current_dialog))

            invalid_num = True
            while invalid_num:
                prompt = input("    > ")
                invalid_num = False

                if prompt == "q":
                    left_convo = True;
                    break;

                try:
                    prompt = int(prompt)
                    prompt -= 1
                    if prompt < 0 or prompt > len(current_dialog.responses):
                        print("Enter a number between 0 and", len(current_dialog.responses))
                        invalid_num = True
                except:
                    print("Enter a number between 0 and", len(current_dialog.responses)), 
                    invalid_num = True

            if not invalid_num:
                if prompt == len(current_dialog.responses):
                    left_convo = True
                    break
                else:
                    current_dialog = current_dialog.responses[prompt][1]

    def __str__(self):
        intros = [
            "NAME is standing on the corner",
            "NAME is leaning against the old oak tree",
            "NAME is just over there",
            "NAME is sitting on the park bench"
        ]

        return intros[randint(0, len(intros)-1)].replace("NAME", self.name)


class DialogNode(): 
    def __init__(self, text, responses=[]):
        self.text = text
        self.responses = responses

    def add_response(self, text, dialogNode):
        self.responses.append([text, dialogNode])

    def __str__(self):
        log = []
        log.append("\n" + get_wrap(self.text) + "\n")

        index = 1
        for response in self.responses:
            log.append("    " + str(index) + ") " + response[0])
            index += 1

        log.append("    " + str(index) + ") Farewell\n")

        return "\n".join(log)