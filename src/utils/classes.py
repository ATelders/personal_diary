class Diary_entry:
    def __init__(self, user_id, date, content, emotion):
        self.user_id = user_id
        self.date = date
        self.content = content
        self.emotion = emotion

    def get_text(self):
        return "Le texte de la date du {} est: \n{}.\nL'émotion est {}".format(self.date, self.content, self.emotion)

    def entry_data(self):
        return {
        'user_id': self.user_id,
        'date': self.date,
        'content': self.content,
        'emotion': self.emotion
        }