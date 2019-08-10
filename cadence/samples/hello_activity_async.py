import sys
import logging
from time import sleep

from cadence.activity_method import activity_method
from cadence.workerfactory import WorkerFactory
from cadence.workflow import workflow_method, Workflow, WorkflowClient

logging.basicConfig(level=logging.DEBUG)

TASK_LIST = "HelloActivity-python-tasklist"
DOMAIN = "sample"


# Activities Interface
class GreetingActivities:
    @activity_method(task_list=TASK_LIST, schedule_to_close_timeout_seconds=2)
    def compose_greeting(self, greeting: str, name: str) -> str:
        raise NotImplementedError


# Activities Implementation
class GreetingActivitiesImpl:
    def compose_greeting(self, greeting: str, name: str):
        return greeting + " " + name + "!"


# Workflow Interface
class GreetingWorkflow:
    @workflow_method(execution_start_to_close_timeout_seconds=10, task_list=TASK_LIST)
    def get_greeting(self, name: str) -> str:
        raise NotImplementedError


# Workflow Implementation
class GreetingWorkflowImpl:

    def __init__(self):
        self.greeting_activities: GreetingActivities = Workflow.new_activity_stub(GreetingActivities)

    @workflow_method(impl=True)
    async def get_greeting(self, name):
        print("Workflow executed args:" + name)
        return await self.greeting_activities.compose_greeting("Hello", name)


if __name__ == '__main__':
    factory = WorkerFactory("localhost", 7933, DOMAIN)
    worker = factory.new_worker(TASK_LIST)
    worker.register_activities_implementation(GreetingActivitiesImpl(), "GreetingActivities")
    worker.register_workflow_implementation_type(GreetingWorkflowImpl, "GreetingWorkflow")
    factory.start()

    client = WorkflowClient.new_client(domain=DOMAIN)
    greeting_workflow: GreetingWorkflow = client.new_workflow_stub(GreetingWorkflow)
    execution = WorkflowClient.start(greeting_workflow.get_greeting, "Python")
    print("Started: workflow_id={} run_id={}".format(execution.workflow_id, execution.run_id))
    print("Result: " + str(client.wait_for_close(execution)))

    print("Stopping workers....")
    worker.stop()
    print("Workers stopped...")
    sys.exit(0)
