#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from pagerduty.PagerDuty import PagerDutyClient

pagerduty = PagerDutyClient.get_client(pagerduty_authentication)
method = str(task.getTaskType()).lower().replace('.', '_')
call = getattr(pagerduty, method)
output = call(locals())