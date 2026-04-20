FROM nginx:alpine

# Remover configuração padrão
RUN rm /etc/nginx/nginx.conf

# Copiar configuração multi-site
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar todos os projetos para a estrutura do Nginx
COPY drumwave /usr/share/nginx/html/drumwave
COPY idr-website /usr/share/nginx/html/idr-website
COPY data-savings /usr/share/nginx/html/data-savings
COPY idr2-website /usr/share/nginx/html/idr2-website

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
