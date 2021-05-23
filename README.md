### Docker Build command :

```
docker build -t <image_name> .
```

### Docker Run command :

```
docker run -d \
    -e DISTRICT_ID=<district_id> \
    -e NUMBER_OF_DAYS_TO_LOOK=<how_many_days_in_future_to_check> \
    -e INTERVAL_IN_SEC=<interval_between_next_check> \
    -e TZ=<timezone_of_log_timestamps> \
    -v /path/to/host/folder:/log \
    --name <container_name> <image_name>
```
### How to find DISTRICT_ID
1. Navigate to following URL in browser and find the state_id
    ```
    https://cdn-api.co-vin.in/api/v2/admin/location/states
    ```
2. Navigate to following URL in browser by replacing the state_id from previous step and find the district_id
    ```
    https://cdn-api.co-vin.in/api/v2/admin/location/districts/<state_id>
    ```
