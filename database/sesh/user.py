"""
Модуль для рядовых действий в БД.
"""
from aiogram.types import Message

from database.psql.psql import PSQL
from database.sesh.constants import TASKS_LIST_FORMAT, ADD_TASK_SQL, GET_TASKS_SQL,\
    CLEAR_TASKS_SQL, USERNAME, USER_ID, TASK


class PSQLUser(PSQL):
    """
    Класс для работы с данными в БД.
    """
    def __init__(self, message: Message) -> None:
        super().__init__()

        self._username, self._user_id = message.from_user.username, message.from_user.id

        self._connect_to_db()

    def add_task(self, task: str) -> None:
        """
        Метод добавляет задачу в таблицу.
        
        :param task: Название задачи.
        :return:
        """
        self._query(ADD_TASK_SQL, {USERNAME: self._username, USER_ID: self._user_id, TASK: task})

    # def get_tasks(self) -> list[str]:
    def get_tasks(self) -> str:
        """
        Метод для получения списка задач юзера и перевод его в отформатированную строку.
        
        :return: Список с кортежами, нулевой индекс которых содержит порядковый номер задачи, а
                 первый - её название.
        """
        self._query(GET_TASKS_SQL, {USER_ID: self._user_id})
        return '\n'.join(TASKS_LIST_FORMAT.format(item[0], item[1]) for item in self._fetchall())

    def clear_tasks(self) -> None:
        """
        Метод для удаления всех задач юзера из БД.
        
        :return:
        """
        self._query(CLEAR_TASKS_SQL, {USER_ID: self._user_id})
