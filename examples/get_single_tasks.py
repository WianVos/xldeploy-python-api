import xldeploy
import pprint
xld = xldeploy.connect_task()
tasks = xld.get_all_tasks()
print str(tasks)
for x in tasks:
    print "-----"
    print xld.get_task_by_id(x.id).to_dict()

