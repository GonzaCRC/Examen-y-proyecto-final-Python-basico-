import random as rd


class RandomDataGenerator:

    def __init__(self, datastore, size=None):
        self.datastore = datastore
        if size is None:
            self.size = 100
        else:
            self.size = size

    def get_experience_years(self):
        return [rd.randint(0, 10) for year in range(self.size)]

    def get_names(self, counter=None):
        if counter is None:
            counter = self.size // 100
        if counter != 0:
            full_names = zip(rd.sample(self.datastore.first_names, 100), rd.sample(self.datastore.last_names, 100))

            return [' '.join(full_name) for full_name in full_names] + self.get_names(counter - 1)
        else:
            return []

    def get_provinces(self):
        return [rd.choice(self.datastore.provinces) for province in range(self.size)]

    def get_universities(self):
        return [rd.choice(self.datastore.universities) for university in range(self.size)]

    def get_languages(self):
        return [rd.choice(self.datastore.languages) for language in range(self.size)]

    def get_mediums(self):
        return [rd.choice(self.datastore.mediums) for medium in range(self.size)]