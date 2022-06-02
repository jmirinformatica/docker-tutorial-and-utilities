from dump import app

#
# Main que farà servir wsgi per desplegar l'aplicació
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
#
# NGINX:
# location /dump/ {
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_buffering off;
#         proxy_pass http://localhost:9981;
# }

if __name__ == "__main__":
    app.run()