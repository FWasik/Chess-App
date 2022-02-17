W celu zainstalowania wymagań, nalezy użyć polecenie pip install -r requirements.txt LUB pipenv sync (w przypadku gotowego środowiska wirtualnego)
Można również przekonwertować Pipfile na requirements.txt za pomocą polecenia pipenv lock -r (?)

Aby uruchomić aplikacje należy skorzystać z polecenia py main.py. Aby użyć aplikacji, można korzystać z terminala, jednak osobiście używałem w tym celu Postman'a.
Alternatywą jest dołączenie w środowisku PyCharm, konfiguracji która umożliwia uruchomienie aplikacji.

Program został sprawdzony oraz sformatowany za pomocą Flake8 oraz Black. 

Program posiada podstawowe testy jednostkowe w pliku test_api.py. Testy uruchamia się za pomocą komendy pytest

Program posiada statyczne typowanie

