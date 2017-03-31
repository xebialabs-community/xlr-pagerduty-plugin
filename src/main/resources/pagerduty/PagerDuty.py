#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json, requests, sys, traceback

class PagerDutyClient(object):
    def __init__(self, pagerduty_authentication):
        self.url = pagerduty_authentication["url"]
        self.headers = {
            'Content-Type' : 'application/json',
            'Authorization' : 'Token token=%s' % pagerduty_authentication["api_access_token"]
        }

    @staticmethod
    def get_client(pagerduty_authentication):
        return PagerDutyClient(pagerduty_authentication)

    def pagerduty_triggerevent(self, variables):
        try:
            event_data={
                "payload": {
                    "summary": "%s" % variables['event_summary'],
                    "source": "%s" % variables['event_source'],
                    "severity": "%s" % variables['event_severity']
                },
                "routing_key": "%s" % variables['routing_key'],
                "event_action": "trigger",
                "client": "XL Release Server",
                "client_url": "get task url?"
            }
            return self.get_response_for_endpoint('POST', '/enqueue', "Failed to trigger event.", json_data=event_data)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            sys.exit(1)

    def open_url(self, method, url, headers=None, data=None, json_data=None):
        if headers is None:
            headers = self.headers
        return requests.request('%s' % method, url, data=data, json=json_data, headers=headers, verify=False)

    def get_response_for_endpoint(self, method, endpoint, error_message, object_id=None, json_data=None, data=None, headers=None):
        full_endpoint_url = "%s/%s" % (self.url, endpoint)
        if object_id is not None and object_id:
            full_endpoint_url = "%s/%s" % (full_endpoint_url, object_id)
        response = self.open_url(method, full_endpoint_url, headers=headers, json_data=json_data, data=data)
        if not response.ok:
            raise Exception(error_message + " -- %s" % response.text)
        return response.text
