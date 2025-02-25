# MISW4406-SaludTechAlpes-2025

## Project Structure
```
/MISW4406-SaludTechAlpes-2025
├── src                # Source Code
│   ├── saludtechaples # First application
│       ├── api            # api de la aplicacion
│       ├── config            # config de la aplicacion
│       ├── modulos            # modulos de la aplicacion
│       └── seddwork            # seedwork de la aplicacion
│   ├── test            # test files
│   ├── Dockerfile      # Docker configuration for building the image
│   ├── Dockerfile      # Docker configuration for building the image
│   └── saludtechalpes.Dockerfile # Docker File de la aplicacion
└── README.md           # Project documentation
```

## Quality Attributes Scenarios
For detailed quality attributes scenarios, please refer to [this presentation](https://uniandes-my.sharepoint.com/:p:/g/personal/cc_pinzonh1_uniandes_edu_co/EfDx-boYJOVGtP66tJTykR0B6zxA1uMw7yVwcvNROGw_CQ?e=B87IiG).

## Running the App Locally with Docker Compose
To run the application locally using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Navigate to the project directory:
   ```sh
   cd ../MISW4406-SaludTechAlpes-2025
   ```
3. Build and start the containers:
   ```sh
   docker-compose up --build
   ```
4. The application should now be running and accessible at `http://localhost:5000`.

## Authors
- name="Cristian Pinzon", email="cc.pinzonh1@uniandes.edu.co"
- name="Juan Carlos De Jesus", email="j.dejesus@uniandes.edu.co"
- name="Edgar Melara", email="e.melara@uniandes.edu.co" 
- name="Andrés Sánchez", email="a.sanchez2001@uniandes.edu.co"