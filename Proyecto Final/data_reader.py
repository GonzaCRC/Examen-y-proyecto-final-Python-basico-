class DataFilesReader:
    
    def __init__(self, first_names, last_names, provinces, languages, universities, mediums):
        self.first_names_file = first_names
        self.last_names_file = last_names
        self.provinces_file = provinces
        self.languages_file = languages
        self.universities_file = universities
        self.mediums_file = mediums
        
    def first_names_as_list(self):
        first_names = open(self.first_names_file, 'r')
        
        return first_names.read().splitlines()

    def last_names_as_list(self):
        last_names = open(self.last_names_file, 'r')

        return last_names.read().splitlines()
    
    def provinces_as_list(self):
        provinces = open(self.provinces_file, 'r')
        
        return provinces.read().splitlines()

    def languages_as_list(self):
        languages = open(self.languages_file, 'r')

        return languages.read().splitlines()

    def universities_as_list(self):
        universities = open(self.universities_file, 'r')

        return universities.read().splitlines()

    def mediums_as_list(self):
        mediums = open(self.mediums_file, 'r')

        return mediums.read().splitlines()
