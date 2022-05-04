from enum import Enum  # pragma: no cover (trivial code)


class IO(Enum):  # pragma: no cover (trivial code)
    added_task = (
        'Задание закончено, вернитесь на '
        '<a href="/">главную страницу</a>,'
        ' чтобы увидеть, что ещё осталось сделать'
    )
    add_task_error = (
        'Вы пытаетесь удалить несуществующую задачу, '
        '<a href="/"> вернуться на главную страницу</a>'
    )
    post_request_error = (
        'Неправильно передали данные, <a href="/"> вернуться на главную страницу</a>'
    )


class Files(Enum):  # pragma: no cover (trivial code)
    main_page = 'index.html'
    add_task_page = 'add_new_task.html'
    logs = 'app.log'


class QueryParams(Enum):  # pragma: no cover (trivial code)
    filter_substring = 'substring'
    task_status = 'status'
    page_index = 'page'


class TaskStatus(Enum):  # pragma: no cover (trivial code)
    active = 'active'
    finished = 'finished'
