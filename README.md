# Presence Light Home Assistant API Bridge

Creates a [FastAPI](https://github.com/tiangolo/fastapi) bridge to [Home Assistant](https://www.home-assistant.io/) for use with the simplified Custom API interface in [Presence Light](https://github.com/isaacrlevin/PresenceLight)

## How to use

1. Download the Docker file from [here](https://hub.docker.com/r/loganjlong/presence-light-ha-api)
2. Run the Docker file on a server of your choice (including your local machine)
3. Get a [Long-lived Access Token](https://www.atomicha.com/home-assistant-how-to-generate-long-lived-access-token-part-1/) from your Home Assistant installation
4. Set the following environment variables in Docker:
    - HA_IP: The IP Address of FQDN of your Home Assistant installation that the Docker container will be able to access
    - HA_PORT: The port that your Home Assistant installation runs on (Normally, this is `8123`)
    - HA_ENTITY: The entity name of the light you want to use in the `<domain>.<name>` format. (I use `light.office_status_light` in mine.)
        - Note: This light must support RGB, or this application will fail
    - HA_TOKEN: The long-lived access token you generated earlier
5. Run the Docker container with the command `docker run -d --restart=unless-stopped -e "HA_IP=<your-ip>" -e "HA_PORT=<your-port>" -e "HA_ENTITY=<domain>.<name>" -e "HA_TOKEN=<your-token>" loganjlong/presence-light-ha-api`
6. Set the Custom API values in Presence Light. You should replace the IP and port seen below with the IP and port of this Docker container (not your Home Assistant installation). All calls in this application use POST.
![Example Custom API Config](example-custom-api-config.png)

## API Behavior

- `/available`: Sets the light green
- `/away`: Sets the light yellow
- `/busy`: Sets the light red
- `/offline`: Turns the light off
