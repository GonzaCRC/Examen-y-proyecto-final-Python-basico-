class DataStore:

    def __init__(self, data_reader):
        self.first_names = data_reader.first_names_as_list()
        self.last_names = data_reader.last_names_as_list()
        self.provinces = data_reader.provinces_as_list()
        self.languages = data_reader.languages_as_list()
        self.universities = data_reader.universities_as_list()
        self.mediums = data_reader.mediums_as_list()
