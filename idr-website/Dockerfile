FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY logo-black.png /usr/share/nginx/html/logo-black.png
COPY logo-white.png /usr/share/nginx/html/logo-white.png
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
