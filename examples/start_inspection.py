import xldeploy
import xldeploy.inspection.inspection
# xld = xldeploy.connect_inspection()
# result = xld.prepare_inspection(type = 'was.DeploymentManager', host = 'Infrastructure/was1', id = 'Infrastructure/was1/test1', wasHome="/opt/test")
# #result = xld.prepare_inspection(type = 'was.DeploymentManager', host = 'Infrastructure/was1')
# print result.to_xml()
# pprint.pprint(result['was.DeploymentManager'])
string = '<inspection> <inspectable>\
    <was.DeploymentManager id="Infrastructure/was1/test1">\
      <tags /> \
      <host ref="Infrastructure/was1" />\
      <wasHome>/opt/test</wasHome>\
      <port>0</port>\
      <nodeAgents />\
      <clusters />\
      <updateGlobalPlugin>false</updateGlobalPlugin>\
      <unmanagedWebServers />\
    </was.DeploymentManager>\
  </inspectable>\
  <inspectable>\
    <was.DeploymentManager id="Infrastructure/was2/test2">\
      <tags />\
      <host ref="Infrastructure/was2" />\
      <wasHome>/opt/test</wasHome>\
      <port>0</port>\
      <nodeAgents />\
      <clusters />\
      <updateGlobalPlugin>false</updateGlobalPlugin>\
      <unmanagedWebServers />\
    </was.DeploymentManager>\
  </inspectable>\
</inspection>'

inspection = xldeploy.inspection.inspection.Inspection(xml=string)

inspectable = inspection.inspectables()[0]
print "blahh"
print inspectable
print dir(inspectable)
inspectable.host = {'ref': 'Infrastructure/was3'}

print "blashsafhsdfa"
print inspection.to_xml()
# pprint.pprint(inspection)
# print inspection.to_dict()
# print inspection.to_xml()
# print vars(inspection)
