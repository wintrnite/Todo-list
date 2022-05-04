import logging
from typing import List, Tuple

from flask import Flask, render_template, request

from app.constants import IO, Files, QueryParams
from app.utils import get_filter_function, Task

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, filename=Files.logs.value, filemode='w', format='%(message)s'
)

todo_list: List[Task] = []


@app.route('/', methods=['GET', 'POST'])
def index() -> Tuple[str, int]:
    show_todo_list = todo_list
    if request.method == 'POST':
        current_requests = request.form
        if 'task' not in current_requests or request.form.get('task') == '':
            return IO.post_request_error.value, 400
        new_task = request.form.get('task')

        todo_list.append(Task(finished=False, description=new_task, id=len(todo_list)))
        logger.info('Task added: %s', new_task)
    filter_substring = request.args.get(QueryParams.filter_substring.value, '')
    task_status = request.args.get(QueryParams.task_status.value)
    filter_func = get_filter_function(task_status, filter_substring)
    show_todo_list = list(filter(filter_func, show_todo_list))
    return (
        render_template(
            Files.main_page.value, todo_list=show_todo_list, length=len(show_todo_list)
        ),
        200,
    )


@app.route('/add', methods=['GET'])
def add_new_task() -> str:
    print(len(todo_list) // 10 if len(todo_list) >= 10 else '')
    return render_template(Files.add_task_page.value, todo_list_length=len(todo_list))


@app.route('/finish_task', methods=['POST'])
def finish_task() -> Tuple[str, int]:
    try:
        i = int(str(request.args.get('index')))
        if not 0 <= i <= len(todo_list):
            raise IndexError
        for k in range(i, len(todo_list)):
            if not todo_list[k].finished:
                todo_list[k].finished = True
                logger.info('Task finished: %s', todo_list[k].description)
                break
        return IO.added_task.value, 200
    except IndexError:
        logger.exception('Excpection occured')
        return IO.add_task_error.value, 400
