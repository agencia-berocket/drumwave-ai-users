FROM nginx:alpine
COPY drumwave-ai-users.html /usr/share/nginx/html/index.html
COPY logo.avif /usr/share/nginx/html/logo.avif
