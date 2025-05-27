import string
from faker import Faker

fake = Faker()

class DataGenerator:
    """
    Фейкер для генерации рандомных данных
    """
    @staticmethod
    def fake_project_id():
        first_latter = fake.random.choice(string.ascii_letters)
        rest_char = ''.join(fake.random.choices(string.ascii_letters + string.digits, k=10))
        project_id = first_latter + rest_char
        return project_id


    @staticmethod
    def fake_name():
        return fake.first_name()
