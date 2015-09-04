import xldeploy
import pprint
xld = xldeploy.connect_task()
tasks = xld.get_all_tasks_export()
print str(tasks)
for x in tasks:
   pprint.pprint(x.to_dict())
