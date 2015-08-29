import xldeploy
from xldeploy.repository.configuration_item import CiSet

repo = xldeploy.connect_repository()


cis = repo.get_cis_by_query(parent = 'Infrastructure' )

## test iteration
for ci in cis:
    repo.update_ci(ci)

## test __str__
print str(cis)


for ci in cis:
    ci.update_ci_properties(tags = ['blah31', 'blah41', 'blah51'])

repo.update_cis(cis)

xcis = CiSet()
for ci in cis:
    nci = ci
    nci.update_id("%s_test2" % ci.get_id())
    xcis.add_ci(nci)

repo.create_cis(xcis)

