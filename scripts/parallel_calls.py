import json
import requests
import random
import multiprocessing as mp

num_cpus = 4
num_requests = 10
url = "http://localhost:8080/api/v0.1/dowork"

dummy_data = [random.randint(1, 100) for j in range(1000)]

# api call
def callapi(numbers):
    data = { 'data' : numbers }
    r = requests.post(url, json=data)
    return r

pool = mp.Pool(processes=num_cpus)
results = [pool.apply(callapi, args=(dummy_data,)) for i in range(num_requests)]
pool.close()
pool.join()

for d in results:
    #print(d.text)
    print(json.loads(d.text)['result'])