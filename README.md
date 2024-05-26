# Infinite Dungeon

1) activate venv and install requirements
   ```commandline
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

### Использование IPython
1) создание и настройка конфига
    ```commandline
    ipython profile create
    nano ~/.ipython/profile_default/ipython_config.py
    ```
1) добавление авторелоуда в конфиг
    Добавить две строчки в конец файла
    ```python
    c.InteractiveShellApp.extensions = ['autoreload']
    c.InteractiveShellApp.exec_lines = ['%autoreload 2']
    ```
1) запуск консоли
    ```commandline
    python manage.py shell_plus --ipython
    ```
