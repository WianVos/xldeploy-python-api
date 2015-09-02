import xldeploy
import pprint
xld = xldeploy.connect_deployment()
deployment = xld.get_initial_deployment_spec("Environments/testEnv1", "Applications/tester2/testcomp")
#pprint.pprint(deployment.deployment_spec_dict)
#pprint.pprint(deployment.to_xml())
# print deployment.__ds_xml
#
# print deployment.to_dict()

deploymentplan = xld.get_deployment_plan_preview(deployment)

pprint.pprint(deploymentplan.preview_dict)