import xldeploy
import pprint
xld = xldeploy.connect_deployment()
deployment = xld.get_initial_deployment_spec("Environments/testEnv1", "Applications/tester/1.0.0")
#pprint.pprint(deployment.deployment_spec_dict)
#pprint.pprint(deployment.to_xml())
# print deployment.__ds_xml
#
# print deployment.to_dict()
deploymentplan = xld.get_deployment_mapping(deployment)

pprint.pprint(deploymentplan.deployment_spec_dict)

pprint.pprint(deploymentplan.get_validation_messages())

print xld.create_deployment_task(deploymentplan)
