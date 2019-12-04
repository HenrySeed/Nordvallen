from utils import text_wrap

class Quest():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_trim_description(self):
        if len(self.description) > 30:
            return self.description[0:30] + "..."
        else:
            return self.description

    def __str__(self):
        log = []
        log.append("="*10 + " " + self.name + " " + "="*5)
        log.append("")
        log.append("\n".join(text_wrap(self.description)))
        return "\n".join(log)


class Quests():
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def search_quests(self, search):
        simpleSearch = search.lower().replace(" ", "")
        best_option = None
        best_score = float("inf") # Lower is better

        for q in self.quests:
            simple_q_name = q.name.lower().replace(" ", "")
            if simpleSearch in simple_q_name:
                score = len(simple_q_name.replace(simpleSearch, ""))
                if score < best_score:
                    best_option = q
                    best_score = score

        return best_option

    def __str__(self):
        log = []
        log.append("\n+---------------------  Quests  ---------------------+")
        for quest in self.quests:
            log.append(quest.name + " -> " + quest.get_trim_description())

        log.append("")
        return "\n".join(log)
