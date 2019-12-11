from random import randint
from utils import get_wrap
import os
from time import sleep

intros = [
            "NAME is standing on the corner",
            "NAME is leaning against the old oak tree",
            "NAME is just over there",
            "NAME is sitting on the park bench"
        ]

class NPC():
    def __init__(self, name="Kev the Ledge", dialog_start=None):
        self.name = name
        self.dialog_start = dialog_start
        self.intro = intros[randint(0, len(intros)-1)].replace("NAME", self.name)

    def start_dialog(self, area):
        os.system("clear")
        print(area)

        current_dialog = self.dialog_start
        left_convo = False

        while not left_convo:
            os.system("clear")
            print(area)
            print(self.name + " ------- ")
            print(str(current_dialog))

            invalid_num = True
            while invalid_num:
                prompt = input("    > ")
                invalid_num = False

                if prompt == "q":
                    invalid_num = True
                    left_convo = True
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
                    os.system("clear")
                    print(area)
                    print(self.name + " ------- ")
                    print("\nAlrighty then, see you around\n")
                    sleep(1)
                    left_convo = True
                    break
                else:
                    current_dialog = current_dialog.responses[prompt][1]

    def __str__(self):
        return self.intro


class DialogNode(): 
    def __init__(self, text, end_point=None, responses=[]):
        self.text = text
        self.responses = responses
        self.end_point = end_point

    def add_response(self, text, dialogNode):
        self.responses.append([text, dialogNode])

    def __str__(self):
        if self.end_point != None:
            self.responses = self.end_point.responses
            
        log = []
        log.append("\n" + get_wrap(self.text) + "\n")
        index = 1
        for response in self.responses:
            log.append("    " + str(index) + ") " + get_wrap(response[0], 7))
            index += 1

        log.append("    " + str(index) + ") Farewell\n")

        return "\n".join(log)