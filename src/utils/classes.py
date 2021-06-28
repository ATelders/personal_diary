class Diary_entry:
    def __init__(self, id, user_id, date, content, emotion):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.content = content
        self.emotion = emotion

    def get_text(self):
        return "Le texte de la date du {} est: \n{}.\n L'émotion est {}".format(self.date, self.content, self.emotion)

    def entry_data(self):
        return {
        'user_id': self.user_id,
        'date': self.date,
        'content': self.content,
        'emotion': self.emotion
        }