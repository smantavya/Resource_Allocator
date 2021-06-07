#Resource Allocator

#defining servers and nos of cpus
servers = {'large':1,
			'xlarge':2,
			'2xlarge':4,
			'4xlarge':8,
			'8xlarge':16,
			'10xlarge':32}

def get_costs(instances, cpus, hours):
	total_cost = 0
	count_server = {}
	result = []

	regions = list(instances.keys())	
	cpus1 = cpus

	#servers
	for r in regions:
		cpus = cpus1
		count_server = {}
		total_cost = 0

		while cpus > 0:
			regional_servers = list(instances[r].keys())
			for a in regional_servers[::-1]:
				if cpus >= servers[a]:
					max_server = a

					count_server[max_server] = cpus//(servers[max_server])
					cpus = cpus%(servers[max_server])

	#cost
					cal_rate = instances[r][max_server] #2.82
					total_cost += cal_rate*(count_server[max_server]) #11.28
			

				else:
					continue

			# print(f"cost: ${total_cost:.2f}")
			# print(r, ':', count_server1)
			
			count_server1 = list(count_server.items())

			res_dict = {"region":r,
						"total_cost":round(total_cost,2),
						"servers":count_server1}


			result.append(res_dict)
			print(result)




min_cpus = int(input("enter minimum number of cpus = "))
max_hour = int(input("enter number of hours = "))
instances = {
        "us-east": {
            "large": 0.12,
            "xlarge": 0.23,
            "2xlarge": 0.45,
            "4xlarge": 0.774,
            "8xlarge": 1.4,
            "10xlarge": 2.82
        },
        "us-west": {
            "large": 0.14,
            "2xlarge": 0.413,
            "4xlarge": 0.89,
            "8xlarge": 1.3,
            "10xlarge": 2.97
        },
    }
get_costs(cpus = min_cpus, instances = instances, hours = max_hour)
