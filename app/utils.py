from typing import Callable, Optional, List
# from pathlib import Path
#
# import pickle
from pydantic import BaseModel

from app.constants import TaskStatus


class Task(BaseModel):
    finished: bool
    description: str
    id: int


def get_filter_function(status: Optional[str], substr: str) -> Callable[[Task], bool]:
    if status == TaskStatus.active.value:
        return lambda task: not task.finished and substr in task.description
    if status == TaskStatus.finished.value:
        return lambda task: task.finished and substr in task.description
    return lambda task: substr in task.description

# def save_current_tasks_to_file(data: List):
#     with Path.open('')