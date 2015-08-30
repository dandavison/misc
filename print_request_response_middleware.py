from clint.textui.colored import green, blue, red, yellow


class PrintRequestResponse(object):
    def process_request(self, request):
        print
        print blue("---------------------------------------------------------")
        print blue("%s %s\n%s" % (request.method, request.path,
                                  request.body))
        print blue("---------------------------------------------------------")

    def process_response(self, request, response):
        if 200 <= response.status_code < 300:
            col = green
        elif 300 <= response.status_code < 400:
            col = yellow
        else:
            col = red

        print
        print col("---------------------------------------------------------")
        print col("%s %s %d" %
                  (request.method, request.path, response.status_code))
        print col("---------------------------------------------------------")
        return response
