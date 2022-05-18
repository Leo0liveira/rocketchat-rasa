FROM rasa/rasa-sdk:3.1.1

# Use subdirectory as working directory
WORKDIR /app

# Change back to root user to install dependencies
USER root

# Copy actions folder to working directory
COPY ./bot/actions /app/actions

# By best practices, don't run the code with root user
USER 1001