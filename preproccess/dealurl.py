import  json




def deal_json():
    with open('../data/url.json', 'r') as f:
        url_json_str = f.read()
        url_json_obj = json.loads(url_json_str)
        url_hits_json_obj = url_json_obj.get('hits')
        url_info_list = url_hits_json_obj.get('hits')
        for url_info in url_info_list:
            print(deal_url(url_info))

def deal_url(url):
    url_source = url.get('_source')
    url_info = {}
    url_info['client_ip'] = url_source.get('client_ip')
    #客户端ip是否在是内网ip、公网ip是否是装填
    url_info['method'] = url_source.get('method')
    url_info['path'] = url_source.get('path')
    url_info['request.host'] = url_source.get('request.host')
    url_info['request.params'] = url_source.get('request.params')
    url_info['request.referer'] = url_source.get('request.referer')
    url_info['request.user-agent'] = url_source.get('request.user-agent')
    url_info['response.code'] = url_source.get('response.code')
    url_info['unix_time'] = url_source.get('unix_time')
    return url_info
if __name__ == '__main__':
    deal_json()
