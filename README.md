### How to use this docker image :
The Utility searches for CoWin vaccination slots using DISTRICT_ID or PIN_CODE. DISTRICT_ID search is default. 
The utility only logs the aslot availability. No automatic notification mechanism is included. You can add your own notification mechanism code into the repo and build the image. _If there is a generic solution of some kind, feel free to send a PR to the repo._
__CoWin APIs implement rate limiting for good cause. Look at the original docs before running the code in loop.__
https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2
1. Set the environment variables as instructed and run the following DOCKER RUN command
    ```
    docker run -d \
        -e NUMBER_OF_DAYS_TO_LOOK=<how_many_days_in_future_to_check> \
        -e DISTRICT_ID=<district_id> \
        -e SEARCH_BY_PIN=<set_to_TRUE_if_searching_by_PIN_Code>
        -e PIN_CODE=<pin_code>
        -e INTERVAL_IN_SEC=<interval_between_next_check> \
        -e NOTIFY_FULL_CENTERS=<set_to_TRUE_if_full_centers_to_be_logged> \
        -e TZ=<timezone_of_log_timestamps> \
        -e LOG_FILE_NAME=<log_filename|optional:default_value=conwin.log>
        -v /path/to/host/folder:/log \
        --name <container_name> docker.pkg.github.com/royatanu/cowinchecker/cowinchecker:0.1
    ```
2. Check the docker logs of the container or the log file inside mapped path in host system
3. It will keep checking for available slots at fixed interval (as configured above)
4. When an available slot is found, information will be printed in log in below format
    ```
    Session available at: <conter_name> [<pin_code>] on <date>
    Avaliable Capacity: <#_of_slots> | Age Limit: <18_or_45> | Vaccine: <covishield_or_covaxin_or_else>
    ```
5. If it finds centers on a particular date but no empty slots, it will print below, to indicate already full centers. The already full center names can also be printed in logs by setting NOTIFY_FULL_CENTERS env var as TRUE
    ```
    Total centers found: <#_of_centers> | Date: <date>
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
### How to build docker image from source code :
Prerequisite: You should have ```python3``` and ```pip3``` installed in your machine
1. ```git clone``` the repo into your machine
2. Optional : Create a python virtual environment in the folder by running ```python3 -m venv .venv```
2. Run ```pip3 install -r requirements.txt```
2. Make necessary changes in the code and test it
3. Run below command to build the docker image
    ```
    docker build -t <image_name> .
    ```
