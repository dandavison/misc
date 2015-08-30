class EncourageCaching(object):
    def process_response(self, request, response):
        if request.path.startswith('/site_media/'):
            response['Cache-Control'] = 'public, max-age=31556926'
        return response
