FROM python

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY . .

## Step 3:

# Install packages from requirements
RUN pip install -r requirements.txt
CMD [ "python3", "api.py", "--host=0.0.0.0"]
