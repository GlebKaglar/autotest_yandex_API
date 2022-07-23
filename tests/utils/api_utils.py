import requests

from .expected_body import YandexDiskAPI as EB  # Expected Body


class YandexDiskApi():
    authorisation_token = 'OAuth AQAAAABe0hN3AAg-LFSmKXqvfENit5r6jqI73RU'
    headers = {'Authorization': authorisation_token}

    name_new_folder = 'Test API'
    file_to_copy = 'Файл для копирования.txt'
    new_name_file = 'File for API.txt'

    def create_folder(self):
        """Создает папку"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.name_new_folder}
        request = requests.put(url, headers=self.headers, params=params)
        expected_body = EB.expected_body_create_folder
        json = request.json()

        assert request.status_code == 201, 'Код ответа не соответсвует ожиданиям.'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям.'

    def copy_file(self):
        """Копирует файл в созданную папку"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/copy'
        params = {'from': self.file_to_copy, 'path': self.name_new_folder + '/' + self.file_to_copy}
        request = requests.post(url, headers=self.headers, params=params)
        expected_body = EB.expected_body_copy_file
        json = request.json()

        assert request.status_code == 201, 'Код ответа не соответсвует ожиданиям.'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям.'

    def rename_file(self):
        """Переименовывает файл"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/move'
        params = {'from': self.name_new_folder + '/' + self.file_to_copy, 'path': self.name_new_folder + '/' + self.new_name_file}
        request = requests.post(url, headers=self.headers, params=params)
        expected_body = EB.expected_body_rename_file
        json = request.json()

        assert request.status_code == 201, 'Код ответа не соответсвует ожиданиям.'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям.'

    def check_file_name(self):
        """Проверяет имя файла"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': self.name_new_folder}
        request = requests.get(url, headers=self.headers, params=params)
        json_file_name = request.json()['_embedded']['items'][0]['name']

        assert json_file_name == self.new_name_file, 'Имя файла не соответствует new_name_file.'
