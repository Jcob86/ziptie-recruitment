# Ziptie Recruitment

Welcome to the solution for the recruitment task. Here’s how to get started:

## Setup Instructions

1. **Create a `.env` File**
   - rename `.env-dist` file to `.env`.
   - Update the `.env` file with your database credentials.

2. **Build and Run with Docker**
   - To build the Docker image and start the application, use:
     ```bash
     docker-compose build
     docker-compose up
     ```
   - This will set up both the FastAPI application and the MySQL database.

3. **Run Locally Without Docker**
   - If you prefer to run the application locally, make sure you have all dependencies installed.
   - Start the application using:
     ```bash
     uvicorn app:app --reload
     ```

## Code Formatting

- **Formatters**: The repository includes basic formatters to maintain code quality and consistency.
- **Integration with GitHub Actions**: Formatters can be added to GitHub Actions for automated checks during the pipeline.

## Additional Notes

- Ensure that port 3306 is available or adjust the port mapping in the `docker-compose.yml` if necessary.
- The application and database are configured to use Docker networking, so make sure Docker is running correctly.