import logging

from utils.tools import run_external_applicaton


def run(load, test_id):
    driver = "locustfile.py"
    # print(driver)
    host = "http://192.168.2.12:32677"  # current_configuration["locust_host_url"]
    # load = 200  # current_configuration["load"]
    spawn_rate = 50  # current_configuration["spawn_rate_per_second"] user spawn / second
    run_time = 240  # current_configuration["run_time_in_seconds"]
    log_file = "output/locust_test.log"  # os.path.splitext(driver)[0] + ".log"
    out_file = "output/locust_test.out"  # os.path.splitext(driver)[0] + ".out"
    csv_prefix = "output/result"  # os.path.join(os.path.dirname(driver), "result")
    logging.info(f"Running the load test for {test_id}, with {load} users, running for {run_time} seconds.")

    print(test_id, load, spawn_rate)
    run_external_applicaton(
        f'locust --locustfile {driver} --host {host} --users {load} --spawn-rate {spawn_rate} --run-time {run_time}s '
        f'--headless --only-summary --csv {csv_prefix} --csv-full-history --logfile "{log_file}" --loglevel DEBUG >> '
        f'{out_file} 2> {out_file}',
        False)