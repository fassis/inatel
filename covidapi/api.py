import requests

class CovidAPI:
    """
    class for representing and manipulation Covid API
    No authentication required
    """
    URL = 'https://covid19-brazil-api.now.sh/api/report/v1'
    URL_STATUS_API = 'https://covid19-brazil-api.vercel.app/api/status/v1'

    def __build_url_by_state(self, state):
        """Returns the Covid Cases by Brazillian State in a query URL."""
        return '{}/brazil/uf/{}'.format(CovidAPI.URL, state)
    
    def __status_api(self):
        """Returns the API status"""
        try:
            response = requests.request("GET", self.URL_STATUS_API)
            data = response.json()
            if data['status']=="ok":
                return True
        except:
            return False
    
    def request(self, state=''):
        """Makes a request to the API."""
        if state:
            url = self.__build_url_by_state(state)
        else:
            url = self.URL
        if not self.__status_api:
            return {'status_code': 404, 'error': 'unavailable'}
        try:
            response = requests.request("GET", url)
            data = response.json()
            if 'data' in data:
                return data['data']
            else:
                return [data]
        except Exception as err:
            return {'status_code': 400, 'error': str(err)}