# Use an official Apache base image from the Docker repository
FROM httpd:2.4

# Set the working directory to the default Apache web directory
WORKDIR /usr/local/apache2/htdocs/

# Copy website files from the local machine to the container
# Replace `./my-website/` with the path to your website files
COPY . /usr/local/apache2/htdocs/

# Expose port 80 (default port for HTTP)
EXPOSE 80

# Start Apache in the foreground to keep the container running
CMD ["httpd-foreground"]


