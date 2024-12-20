'''
Use http.server to serve the output of the program date 
-R on an available high port number. Tell the user what 
the port number is so that they can access the service
'''
# 1st run the program
# 2nd enter into the terminal curl http://localhost:(port number)

import http.server, socket, datetime

# Discover an available high port number
with socket.socket() as socket:
    socket.bind(("",0))
    port = socket.getsockname()[1]

# Serve the name of this program over HTTP:
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response ( 200 )
        self.end_headers ()

        ### not using this but this is from date_time_string() GMT
        from datetime import datetime, timezone
        time = self.date_time_string()  # to get the output of date -R
        # conversion of datetime object to date -R output
        time_reg = datetime.strptime(time, '%a, %d %b %Y %H:%M:%S %Z') # Wed, 13 Nov 2024 09:26:58 GMT
        time_reg = time_reg.replace(tzinfo=timezone.utc)
        time_R = datetime.strftime(time_reg, '%a, %d %b %Y %H:%M:%S %z') # Wed, 13 Nov 2024 01:38:14 -0800


        # will write output on server
        self.wfile.write ( f'{time_R}\n'.encode() )  


if __name__ == '__main__':
    server = ( '', port )  # (host,port)
    httpd = http.server.HTTPServer( server, Handler )

    # tell user the port number
    print(f'The server number is http://localhost:{httpd.server_address[1]}')

    httpd.serve_forever() # place at end so we do not exit