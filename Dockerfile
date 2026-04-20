FROM nginx:alpine
COPY idr-website/index.html /usr/share/nginx/html/index.html
COPY idr-website/logo-black.png /usr/share/nginx/html/logo-black.png
COPY idr-website/logo-white.png /usr/share/nginx/html/logo-white.png
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
