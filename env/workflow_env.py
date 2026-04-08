from typing import Tuple
from pydantic import BaseModel

from env.tasks.email_task import EmailTask
from env.tasks.bug_task import BugTask
from env.tasks.code_review_task import CodeReviewTask


class Observation(BaseModel):
    task: str
    input_data: list


class Action(BaseModel):
    output: list


class WorkflowEnv:

    def __init__(self):
        self.current_task = None
        self.task_obj = None
        self.step_count = 0
        self.done = False
        self.task_index = 0  # ✅ for rotation

    def reset(self):
        self.step_count = 0
        self.done = False

        tasks = [
            ("email_triage", EmailTask),
            ("bug_prioritization", BugTask),
            ("code_review", CodeReviewTask)
        ]

        task_name, task_class = tasks[self.task_index % len(tasks)]

        self.current_task = task_name
        self.task_obj = task_class()

        self.task_index += 1

        return Observation(
            task=self.current_task,
            input_data=self.task_obj.get_data()
        )

    def step(self, action: Action) -> Tuple[Observation, float, bool, dict]:

        self.step_count += 1

        score = self.task_obj.evaluate(action.output)

        reward = 0
        reward += score*0.7

        if score == 1.0:
            reward += 0.3
            self.done = True

        if self.step_count >3:
            reward -=0.1

        return (
            Observation(
                task=self.current_task,
                input_data=self.task_obj.get_data()
            ),
            reward,
            self.done,
            {}
        )

    def state(self):
        return {
            "task": self.current_task,
            "step": self.step_count,
            "done": self.done
        }