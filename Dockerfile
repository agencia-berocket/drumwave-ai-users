FROM nginx:alpine
COPY . /usr/share/nginx/html
RUN mv /usr/share/nginx/html/index-dsa.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
