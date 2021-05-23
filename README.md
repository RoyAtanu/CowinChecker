### Docker Build command :

```
docker build -t <image_name> .
```

### Docker Run command :

```
docker run -d \
    -e NUMBER_OF_DAYS_TO_LOOK=<how_many_days_in_future_to_check> \
    -e DISTRICT_ID=<district_id> \
    -e SEARCH_BY_PIN=<set_to_TRUE_if_searching_by_PIN_Code>
    -e PIN_CODE=<pin_code>
    -e INTERVAL_IN_SEC=<interval_between_next_check> \
    -e NOTIFY_FULL_CENTERS=<set_to_TRUE_if_full_centers_to_be_logged> \
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
