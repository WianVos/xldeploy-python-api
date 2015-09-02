#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import logging
from os import path
import urllib2, urllib, base64
from xml.etree import ElementTree as ET

import xldeploy
import xldeploy.exceptions

from xldeploy.decorators import log_with, timer
from xldeploy.client     import XLDConnection
from xldeploy.deployment.deployment import DeploymentSpec, DeploymentPlan


HAVE_HTTPS_CONNECTION = False
try:
    import ssl

    if hasattr(ssl, 'SSLError'):
        HAVE_HTTPS_CONNECTION = True
except ImportError:
    pass

logger = logging.getLogger(__name__)


class DeploymentConnection(XLDConnection):

    """
    provides a connection to xldeploy and lets the user interact with the repository
    """
    @timer(logging)
    @log_with(logger)
    def __init__(self, url=None, username=None, password=None, **kwargs):

        super(DeploymentConnection, self).__init__(url, username, password, **kwargs)


    @timer(logging)
    @log_with(logger)
    def get_initial_deployment_spec(self,environment_id, package_id):
        logger.debug("retrieving initial deployment spec for %s onto %s" % (package_id, environment_id))
        try:
            deployment_spec = self.http_get("deployment/prepare/initial?environment=%s&version=%s" % (environment_id, package_id))
        except Exception:
            raise xldeploy.exceptions.XldeployDeploymentSpecError("unable to obtain deployment specification")

        deployment = DeploymentSpec(environment_id = environment_id, package_id = package_id , ds_xml = deployment_spec, type = "initial")
        logger.debug("created deployment object")
        return deployment


    @timer(logging)
    @log_with(logger)
    def get_deployment_plan_preview(self,deployment_spec):
        try:
            deployment_plan = self.http_post("deployment/previewblock", deployment_spec.to_xml())
        except Exception:
            raise xldeploy.exceptions.XldeployDeploymentPlanPreview("unable to obtain deployment plan preview")

        logger.debug("succesfully retrieved deployment plan preview")
        deploymentplan = DeploymentPlan(xml = deployment_plan)
        return deploymentplan

    @timer(logging)
    @log_with(logger)
    def get_deployment_mapping(self, deployment_spec):
        try:
            output = self.http_post("/deployment/prepare/deployeds", deployment_spec.to_xml())
            deployment_spec.deployment_spec_xml = output
        except Exception:
            raise xldeploy.exceptions.XldeployDeploymentSpecError("unable to obtain deployment specification")
            return False

        return True
