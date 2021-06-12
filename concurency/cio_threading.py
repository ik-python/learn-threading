#!/usr/bin/env python3

import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    '''
    So each thread will create a single session the first time it calls get_session() and then will simply use that session on each subsequent call throughout its lifetime.
    '''
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def get_counter():
    '''
    So each thread will create a single session the first time it calls get_session() and then will simply use that session on each subsequent call throughout its lifetime.
    '''
    if not hasattr(thread_local, "counter"):
        thread_local.counter = 0
    return thread_local.counter

def download_site(url):
    session = get_session()
    counter = get_counter()
    with session.get(url) as response:
        counter += 1
        print(f"status: {response.status_code}, content: {len(response.content)}, count: {counter}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
