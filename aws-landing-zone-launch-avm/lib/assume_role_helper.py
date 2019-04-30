######################################################################################################################
#  Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.                                           #
#                                                                                                                    #
#  Licensed under the Amazon Software License (the "License"). You may not use this file except in compliance        #
#  with the License. A copy of the License is located at                                                             #
#                                                                                                                    #
#      http://aws.amazon.com/asl/                                                                                    #
#                                                                                                                    #
#  or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES #
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions    #
#  and limitations under the License.                                                                                #
######################################################################################################################

# !/bin/python

import inspect
from lib.sts import STS


class AssumeRole(object):
    def __call__(self, logger, account):
        try:
            sts = STS(logger)
            role_arn = "arn:aws:iam::" + str(account) + ":role/AWSCloudFormationStackSetExecutionRole"
            session_name = "aws-landing-zone-role"
            # assume role
            credentials = sts.assume_role(role_arn, session_name)
            return credentials
        except Exception as e:
            message = {'FILE': __file__.split('/')[-1], 'CLASS': self.__class__.__name__,
                       'METHOD': inspect.stack()[0][3], 'EXCEPTION': str(e)}
            logger.exception(message)
            raise