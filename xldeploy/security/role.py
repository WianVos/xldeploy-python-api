import logging
import xldeploy
from xldeploy.decorators import log_with, timer
from xldeploy.security import POSSIBLE_PERMISSIONS

logger = logging.getLogger(__name__)


class Role(object):
    
    @log_with(logger)
    def __init__(self, **kwargs):
        '''
        initialization method for the Role object
        :param name: str: name of the role
        :param permission_xml: str: string representation of the permissions of this role 
        :param permissions: list: list containing permissions objects             
        :return: Role Object Instance
        '''
        
        # cold variable initialization
        self.__name = None
        self.__xml = None
        self.__permissions = []
        
        try:
            self.__name = kwargs['name']
        except KeyError:
            self.__name = None
        
        try:
            self.__xml = kwargs['permission_xml']
        except KeyError:
            self.__xml = None
        
        
        try:
            self.__permissions = kwargs['permission']
        except KeyError:
            self.__permissions = []
        
        

    def parse_xml(self, xml):
        '''
        parse the xml as handed to the object at initialization
        :param xml:
        :return:
        '''
        print "not yet implemented"

class Permission(object):
    from os import path

    def __init__(self, **kwargs):
        '''
        Permission object initialization method
        :param Id: the id of the object to grant permissions on
        :param permissions: list of permissions to grant
        :param type: str: Global/Applications/Environments/Infrastructure
        :return: permission instance object
        '''

        self.__id = None
        self.__permissions = []
        self.__type = []


        try:
            self.__id = kwargs['id']
        except KeyError:
            self.__id = None

        try:
            self.__permissions = kwargs['permission']
        except KeyError:
            self.__permissions = []

        try:
            self.__type = kwargs['type']
        except KeyError:
            self.__type = []


    def get_type_from_id(self):
        if not self.__id == 'Global':
            return self.__id.split('/')[0]
        return 'Global'
    