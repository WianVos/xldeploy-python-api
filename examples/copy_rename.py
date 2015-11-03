import xldeploy

repo = xldeploy.connect_repository()


source_package = "Applications/tester/1.0.0"
ci = 'ls'
new_ci = 'ls2'
target_package = "Applications/tester2/1.0.0"


origin_ci = repo.get_ci_by_name("%s/%s" % (source_package, ci))
print origin_ci.to_dict()

cloned_ci = origin_ci.clone("%s/%s" % (target_package, new_ci))
print cloned_ci.to_xml_str()
print cloned_ci.to_xml()

repo.save_ci(cloned_ci)