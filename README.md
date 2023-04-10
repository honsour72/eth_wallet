## Тестовое задание в компанию O.dev

[Исходное задание](test_issue.pdf)

### Содержание

1. Быстрый старт
2. Тестирование
3. Примечания

### 1. Быстрый старт

Для старта проекта необходимо:
1) Клонировать репозиторий:
   ```commandline
   git clone https://github.com/honsour72/eth_wallet.git
   ```
2) Создать базу данных в СУБД `PostgreSQL` а также пользователя, наделить его правами 
3) Поместить в папку проекта файл `project.toml` следующего содержания

    ```toml
    [django]
        debug = True
        secret_key = your_key
        trendly_access_key = trendly_access_key
        main_net_https_endpoint = "https://mainnet.gateway.tenderly.co/{trendly_access_key}"
    
    [database]
        name = name
        host = 127.0.0.1
        port = 5432
        user = user
        password = password
    ```
4. Создать виртуальное окружение:
   ```commandline
   python3.11 -m venv eth_env
   ```
5. Установить зависимости:
   ```commandline
   pip install -r requiremetns.txt
   ```
6. Создать файлы миграции БД:
   ```commandline
   python manage.py makemigrations wallet_api
   ```
7. Запустить миграцию БД:
   ```commandline
   python manage.py migrate
   ```
8. Запустить проект:
   ```commandline
   python manage.py runserver
   ```

### 2. Тестирование

Для запуска тестов необходимо дать команду:

```commandline
pytest apps/wallet_api/tests.py -v
```

### 3. Примечание

#### 3.1 Ожидаемый результат
1. Код должен быть выложен в репозиторий и предоставлен доступ ✅
2. Сервис должен быть написан на базе Python3.11 + Django4 + DRF ✅
   ```commandline
   Python3.11.3
   Dango                 4.2
   djangorestframework   3.14.0
   ```
3. Сервис должен быть поĸрыт [юнит-тестами](eth_wallet/apps/wallet_api/tests.py) (с помощью pytest). Это самое важное!
(юнит-тесты значит, что в тестах запросы ĸ БЧ должны быть замоĸаны) ✅
4. Должно быть [описание АПИ](eth_wallet/apps/wallet_api/urls.py) с помощью drf-spectacular ✅
5. Должно быть ĸратĸое описание ĸаĸ запустить сервис, тесты и ĸаĸ увидеть
доĸументацию ĸ API ✅
6. Реализовать необходимо тольĸо 2 из 3 endpoint`ов - создание и получения
списĸа ĸошельĸов. Endpoint для перевода средств между ĸошельĸами строго
опционально и выполняется ĸандидатом по желанию. ✅

#### 3.2 Получение схемы в формате `.yaml` при помощи `drf_spectacular`

Команда:

```commandline
python manage.py spectacular --color --file schema.yml
```

#### 3.3 Визуальная часть АПИ (Swagger-UI, Redoc)

Представлены по адресам: `api/v1/schema/swagger-ui/` и `api/v1/schema/redoc/` соответственно