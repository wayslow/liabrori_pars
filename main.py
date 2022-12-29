import requests
import pathlib

def danlowd(name_directory):
    for book_id in range(1,11):
        params = {"id" : book_id}
        url = f"https://tululu.org/txt.php"
        filename = f'{name_directory}/id{book_id}.txt'

        response = requests.get(url, params=params)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)

def main():
    name_directory = "books"
    pathlib.Path(name_directory).mkdir(parents=True, exist_ok=True)
    danlowd(name_directory)

if __name__ == '__main__':
    main()