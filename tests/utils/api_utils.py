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
        url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        params_new_folder = {'path': self.name_new_folder}
        r_create_folder = requests.put(url_folder, headers=self.headers, params=params_new_folder)
        expected_body = EB.expected_body_create_folder
        json = r_create_folder.json()

        assert r_create_folder.status_code == 201, 'Код ответа не соответсвует ожиданиям'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям'

    def copy_file(self):
        """Копирует файл в созданную папку"""
        url_copy = 'https://cloud-api.yandex.net/v1/disk/resources/copy'
        params_copy = {'from': self.file_to_copy, 'path': self.name_new_folder + '/' + self.file_to_copy}
        r_copy_file = requests.post(url_copy, headers=self.headers, params=params_copy)
        expected_body = EB.expected_body_copy_file
        json = r_copy_file.json()

        assert r_copy_file.status_code == 201, 'Код ответа не соответсвует ожиданиям'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям'

    def rename_file(self):
        """Переименовывает файл"""
        url_move = 'https://cloud-api.yandex.net/v1/disk/resources/move'
        params_move = {'from': self.name_new_folder + '/' + self.file_to_copy, 'path': self.name_new_folder + '/' + self.new_name_file}
        r_move_file = requests.post(url_move, headers=self.headers, params=params_move)
        expected_body = EB.expected_body_rename_file
        json = r_move_file.json()

        assert r_move_file.status_code == 201, 'Код ответа не соответсвует ожиданиям'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям'

    def check_file_name(self):
        """Проверяет имя файла"""
        url_check = 'https://cloud-api.yandex.net/v1/disk/resources'
        params_check = {'path': self.name_new_folder}
        r_check_file_name = requests.get(url_check, headers=self.headers, params=params_check)
        json_file_name = r_check_file_name.json()['_embedded']['items'][0]['name']

        assert json_file_name == self.new_name_file, 'Имя файла не соответствует new_name_file'
