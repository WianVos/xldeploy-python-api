import xldeploy
import pprint
xld = xldeploy.connect_task()
tasks = xld.get_all_tasks()
print tasks[1].state
print xld.start_task(tasks[1])
print tasks[1].state
pprint.pprint(tasks[1].to_dict())
print tasks[1].execution_plan