""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('bitcoin-abuse-db')


class BitcoinAbuseDB(object):

    def __init__(self, config):
        self.base_url = config.get('server').strip() + '/api'
        if not self.base_url.startswith('https://'):
            self.base_url = 'https://' + self.base_url
        self.api_token = config.get('api_token')

    def make_rest_call(self, endpoint=None, method='GET', params=None, csv_content=False):
        url = self.base_url + endpoint
        logger.debug('Final url to make rest call is: {0}'.format(url))
        try:
            logger.debug(
                'Making a request with {0} method, {1} params.'.format(method, params))
            response = requests.request(method, url, params=params)
            if response.status_code in [200]:
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    if csv_content:
                        response_data = response.text
                    else:
                        response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))

    def get_lookup_abuse_types(self, params):
        return self.make_rest_call(endpoint='/abuse-types')

    def get_lookup_distinct_reports(self, params):
        data = {'api_token': self.api_token, 'page': params.get('page'), 'reverse': params.get('reverse')}
        return self.make_rest_call(endpoint='/reports/distinct', params=data)

    def check_given_address(self, params):
        data = {'api_token': self.api_token, 'address': params.get('address')}
        return self.make_rest_call(endpoint='/reports/check', params=data)

    def get_all_reports(self, params):
        data = {'api_token': self.api_token}
        return self.make_rest_call(endpoint='/download/' + str(params.get('time_period')), params=data, csv_content=True)


def _run_operation(config, params):
    ba_obj = BitcoinAbuseDB(config)
    command = getattr(BitcoinAbuseDB, params['operation'])
    response = command(ba_obj, params)
    return response


def _check_health(config):
    try:
        ba_obj = BitcoinAbuseDB(config)
        server_config = ba_obj.make_rest_call(endpoint='/abuse-types')
        if server_config['status'] == 'Failure' or not ba_obj.api_token:
            logger.exception('Authentication Error, Check URL and API Token.')
            raise ConnectorError('Authentication Error, Check URL and API Token.')
        return True
    except Exception as Err:
        logger.exception('Health check failed with: {0}'.format(Err))
        raise ConnectorError('Health check failed with: {0}'.format(Err))

