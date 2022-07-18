import requests


class YandexDiskApi():
    authorisation_token = 'OAuth AQAAAABe0hN3AAg-LFSmKXqvfENit5r6jqI73RU'
    headers = {'Authorization': authorisation_token}

    name_new_folder = 'Test API'
    file_to_copy = 'Файл для копирования.txt'
    new_name_file = 'File for API.txt'

    def create_folder(self):
        print('\nСоздаем папку')
        url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
        params_new_folder = {'path': self.name_new_folder}
        r_create_folder = requests.put(url_folder, headers=self.headers, params=params_new_folder)
        expected_body = {
            'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTest+API',
            'method': 'GET',
            'templated': False
        }
        json = r_create_folder.json()

        assert r_create_folder.status_code == 201, 'Код ответа не соответсвует ожиданиям'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям'
        print('Код и тело ответа соответсвуют ожиданиям\n')

    def copy_file(self):
        print('Копируем файл в созданную папку')
        url_copy = 'https://cloud-api.yandex.net/v1/disk/resources/copy'
        params_copy = {'from': self.file_to_copy, 'path': self.name_new_folder + '/' + self.file_to_copy}
        r_copy_file = requests.post(url_copy, headers=self.headers, params=params_copy)
        expected_body = {
            'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTest+API%2F%D0%A4%D0%B0%D0%B9%D0%BB+%D0%B4%D0%BB%D1%8F+%D0%BA%D0%BE%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.txt',
            'method': 'GET',
            'templated': False
        }
        json = r_copy_file.json()

        assert r_copy_file.status_code == 201, 'Код ответа не соответсвует ожиданиям'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям'
        print('Код и тело ответа соответсвуют ожиданиям\n')

    def rename_file(self):
        print('Переименовываем файл')
        url_move = 'https://cloud-api.yandex.net/v1/disk/resources/move'
        params_move = {'from': self.name_new_folder + '/' + self.file_to_copy, 'path': self.name_new_folder + '/' + self.new_name_file}
        r_move_file = requests.post(url_move, headers=self.headers, params=params_move)
        expected_body = {
            'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTest+API%2FFile+for+API.txt',
            'method': 'GET',
            'templated': False
        }
        json = r_move_file.json()

        assert r_move_file.status_code == 201, 'Код ответа не соответсвует ожиданиям'
        assert json == expected_body, 'Тело ответа не соответствует ожиданиям'
        print('Файл успешно переименован')
        print('Код и тело ответа соответсвуют ожиданиям\n')
