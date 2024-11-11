# Use a base image with httpd (Apache)
FROM httpd:latest

# Copy website files into the default web directory in the container
COPY . /usr/local/apache2/htdocs/

# Expose the default HTTP port
EXPOSE 80

# Start httpd service when the container starts
CMD ["httpd-foreground"]
