FROM nginx:alpine

# Copy static files
COPY . /usr/share/nginx/html/

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Generate version-specific HTML files for social media crawlers
WORKDIR /usr/share/nginx/html

RUN cp index.html index-v1.html && \
    cp index.html index-v2.html && \
    # index-v2 needs image and description updates
    sed -i 's/share-option-1.png/share-option-2.png/g' index-v2.html && \
    sed -i 's/property="og:description" content="Machines Don.t Die. Own Your Data. Save Your Future."/property="og:description" content="The proposed Data Savings Act. Your signature. Your voice. Public record."/g' index-v2.html && \
    sed -i 's/name="twitter:description" content="Machines Don.t Die. Own Your Data. Save Your Future."/name="twitter:description" content="The proposed Data Savings Act. Your signature. Your voice. Public record."/g' index-v2.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
