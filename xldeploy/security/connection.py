#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import logging
from os import path
from xml.etree import ElementTree as ET

from xldeploy.decorators import log_with, timer
from xldeploy.client     import XLDConnection

logger = logging.getLogger(__name__)


class SecurityConnection(XLDConnection):
    """
    provides a connection to xldeploy and lets the user interact with the security system
    """

    @log_with(logger)
    def __init__(self, url=None, username=None, password=None, **kwargs):

        super(SecurityConnection, self).__init__(url, username, password, **kwargs)


    @log_with(logger)
    def role_exists(self, name):
        '''
        :param name: string : name of the role to confirm
        :return: True/False
        '''

        output = self.http_get("security/role")
        xml = ET.fromstring(output)
        for role in xml.iter('string'):
            print role.text
            if role.text == name:
                return True

        return False

    @log_with(logger)
    def create_role(self, name):
        '''
        creates a role
        :param name: role name
        :return: True or False
        '''

        # check if the role exists
        if not self.role_exists(name):
        #if not create it
            self.http_put("security/role/%s" % name)
        # verify that the role was created
            if self.role_exists(name):
                logger.info('role: %s created' % name)
                return True
        else:
            logger.warn('role: %s already exists' % name)

        logger.warn('unable to create role: %s' % name)
        return False

    @log_with(logger)
    def delete_role(self, name):
        '''
        delete a role by name
        :param name: role name
        :return: True or False
        '''
        if self.role_exists(name):
            logger.info("role: %s exists. proceeding to delete " % name)
            self.http_delete("security/role/%s" % name)
            if not self.role_exists(name):
                logger.info("deletion of role: %s has succeeded" % name)
                return True
            else:
                logger.error('role: %s not deleted' % name)
                return False
        else:
            logger.warn('role: %s does not exists deletion not needed' % name)
            return True



    @log_with(logger)
    def rename_role(self, name, new_name):
        '''
        rename a role
        :param name: current name of the role
        :param new_name: new name of the role
        :return: True or False
        '''
        print "not yet implemented"
        return False

    @log_with(logger)
    def get_role_permissions(self, role):
        '''
        retrieve the granted permissions for a certain role
        :param role: str: role name
        :return: RoleObject
        '''

#GET	/security/security/	Lists the names of all available securitys in the security system.
#GET	/security/security/securitys	Lists the securitys of the currently logged in user.
#GET	/security/security/securitys/{username}	Lists the securitys of a user.
#PUT	/security/security/{security}	Creates a new security.
#POST	/security/security/{security}	Renames a security.
#DELETE	/security/security/{security}	Removes a security from the XL Deploy security system.
#PUT	/security/security/{security}/{principal}	Assigns a security to a user or group.
#DELETE	/security/security/{security}/{principal}	Removes a security from a user or group.