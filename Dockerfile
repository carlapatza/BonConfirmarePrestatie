# Use the official Python image for Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set the working directory
WORKDIR /app

# Install Python
RUN powershell -Command \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe -OutFile python-installer.exe; \
    Start-Process -Wait -FilePath python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1'; \
    Remove-Item -Force python-installer.exe

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Set the entry point to run the Flask application
ENTRYPOINT ["python", "app.py"]
