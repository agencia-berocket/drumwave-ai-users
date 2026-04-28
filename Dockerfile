FROM nginx:alpine
COPY . /usr/share/nginx/html/
EXPOSE 80
CMD ["/bin/sh", "-c", "cp /usr/share/nginx/html/${START_PAGE:-index-dsa.html} /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"]
