# Apachebench

https://github.com/scubism/todo_center/blob/master/docs/benchmark-with-ab.md

docker run --rm --net=vagrant_back russmckendrick/ab ab -k -n <number_request> -c <number_concurrency> <url>:<port>


eval $(./init.sh | grep config_)
docker run --rm --net=vagrant_back russmckendrick/ab ab -k -n 100 -c 10 http://$config_host:$config_todo_api_gateway_port/



## install in host

`sudo apt install -y apache2-utils`



# TESTING

## guest-guest
## host bench, guest web

`ab -t 30 -c 10 localhost:8888/`


sudo apt install -y lynx

# host-bench to host-web

ab -t 30 -c 10 localhost/ 


sudo service nginx stop
docker run --rm -d --network=host  nginx



# B3: host-web to guest-bench
sudo service nginx start
docker run --rm --network=host russmckendrick/ab ab -t 30 -c 10 localhost/

