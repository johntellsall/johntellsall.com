# Apachebench

https://github.com/scubism/todo_center/blob/master/docs/benchmark-with-ab.md

docker run --rm --net=vagrant_back russmckendrick/ab ab -k -n <number_request> -c <number_concurrency> <url>:<port>


eval $(./init.sh | grep config_)
docker run --rm --net=vagrant_back russmckendrick/ab ab -k -n 100 -c 10 http://$config_host:$config_todo_api_gateway_port/



# Nginx

FROM nginx

# File Author / Maintainer
MAINTAINER Anand Mani Sankar

# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf