"""Module to generate random data"""
from faker import Faker


class RandomDataGenerator:
    """
    Class to generate random information
    Methods:
        project_create_generator
        project_update_generator
    """
    def __init__(self):
        self.faker = Faker()

    def project_create_generator(self):
        """
        Method to generate random information to create a project
        return
        ------
        dict: {name}
        """
        name = self.faker.name()
        return {'name': name}

    def project_update_generator(self):
        """
        Method to generate random information to create a project
        return
        ------
        dict: {name, description}
        """
        name = self.faker.name()
        description = self.faker.name()
        return {'name': name, 'description': description}

    def story_generator(self):
        """
        Method to generate random information to create a story
        return
        ------
        dict: {name}
        """
        name = self.faker.name()
        return {'name': name}

    def epic_generator(self):
        """
        Method to generate random information to create a project
        return
        dict: {name, description}
        """
        name = self.faker.name()
        return {'name': name}
