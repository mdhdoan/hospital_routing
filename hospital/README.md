# hospital_distribution_outline: 
* **Abstract**:
	In the real world, there are many problems in managing a supply chain. Hospital supply chain is but a small part of the industry, yet extremely vital. Without sufficient supplies of medicine and medical supplies, hospitals cannot function properly. In this situation, the task given is to design and implement a supply plan for hospitals, specifically in Ottawa-Gatineau. Given the propblem of supplying hospitals with their needs, this work is a description of an attempt to apply a generic greedy algorithm to find the optimal routes available to traverse and delivery supplies.
* **Introduction**:
	* Hospital supplying is an important aspect in keeping hospitals running and operating. A hospital needs many things to keep it running, but in this problem, they shall be refined into 5 categories:
	* Food: 
		* All staying patients will have 3 meals a day
		* Medical staffs will work in 3 shifts, each will have their own meal. Hence medical staffs will also require 3 meals a day. Those who work on the night shift (11:00pm-7:00am) are also volunteers, these numbers can be changed daily, due to patients' requirement
		* Hospital's staffs works from 9-5, therefore they will have 1 meal a day at the hospital
	* Medicine:
		* These are for the medical staffs usages only, to give to the patients
	* Medical Equipment:
		* These are for the medical staffs usages only
	* Office Supplies:
		* These are for the hospital's staffs usages only
	* Hospital Supplies:
		* These are for the hospital's staffs usages only
	* NOTE: As of right now, all these values shall be stored in a separate file, not yet implemented into the code.
* **Problem**:	
	* One need to find the path to delivery all supplies. Each hospital has a different amount of staffs and patients, therefore having different weight requirement.
	* Some constraints that can be put on are:
		* Time constraints: each hospital has a deadline that must be met
		* Weight constraints: each hospital has a certain amount of weight of required items that changes daily. This is because the patients number changes daily
		* Transport constraints: There are only a limited amount of transports. The problem is now how to arrange routes and orders of the hospitals to meet their demands
	* Optimizing of the solution can be done by:
		* Reusing transports as much as possible. This ensures that productivity is as high as possible
		* Reducing the cost as much as possible. This ensures that profit are as high as possible
* **Formulating the problem**:
	* This route finding problem is an application case of the vehicle routing problem. The problem shall be represented by the following:
		* Route's travelling time as weighted edges
		* Hospitals as vertices, each with a cost per delivery value . 
	* Find route(s) that can reach as many vertices within a time limit. The routes must satisfy both the time constraints and optimizes the cost.
* **Solution**:
	* Since this is a vehicle routing problem, one can attempt to brute force search for the most optimal path, or use a greedy approach to select only the most optimal paths between the hospitals.
	* Assume the followings:
		* The weights of the edges represent the time it takes to travel between hospitals.
		* Each hospital currently takes no time to unload goods and items
		* The supply centre will be next to the first hospital of the route, eliminating the time it takes to travel to it.
		* Between the time of supplies reaching the centre and the time that all hospitals must receive their supplies is fully available for delivery.
		* The graph is one whole complete and connected graph.
	* In this problem, the preferable method will be using a greedy algorithm. It shall be the first step that can guarantee a feasible solution. 
* **How to approach solution using the greedy algorithm**:
	* First of all, since this is a problem that can be occured anywhere, therefore the solution must be generic. 
	* The approach, for the greedy algorithm, would be to find available paths that would allow transports to reach the hospitals in time, yet cheapest to add to the delivery route.
	* Firstly, the algorithm would need to find all possible routes from a starting location. In this case, it is one of the hospitals.
	* After finding all possible routes from all hospitals, then the algorithm will begin to sort them and find the route that passes through the most hospitals before ending (satisfying the constraints), while taking the least amount of time (satisfying the optimization).
	* After having the route, the algorithm checks the route with the list of the hospitals to find if it has covered all the hospitals, or not. If not, then it repeats itself on the remaining hospitals and find the next optimal route to be added.
	* Only when there are no hospitals remaining, then would the algorithm stop.
* **More details on the greedy algorithm**:
	* Firstly, we categorized the graph into 3 parts: 
		* Vertices will be for the hospitals
		* Edges will be for the routing between hospitals
		* Graphs will be a connected component of vertices and edges. In some cases, there can be multiple graphs, for example if the city has hospitals but they are too far apart from each other to be reached within a contraint limit.
	* [Vertices](https://github.com/Merith997/hospital_dist/blob/master/hospital/python/Vertex.py) will have details of:
		* Hospital's name/code
		* All routes going from/to the vertices
	* [Edges](https://github.com/Merith997/hospital_dist/blob/master/hospital/python/Edge.py) will have details of:
		* Vertices that are the ends of the edge
		* Value of the edge (in this case, it would be the time travel between the hospitals)
	* [Graphs](https://github.com/Merith997/hospital_dist/blob/master/hospital/python/Graph.py) will have be consists of the set of vertices and edges that are connected to one another, along with the algorithm.
	* The algorithm be work by the following order:
		The algorithm goes through the vertices one at a time, while performing the greedy algorithm to find all available routes from that vertex. 

		![Iterate hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-08-40.png)

		Since the assumption is that the route between 2 hospitals are identical, and the travelling time difference in both directions are negligible, this method would work for travelling to and from any vertices.

		![Time is the same back and forth](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-08-44.png)

		After retrieving all routes, then the algorithm proceed to re organized them by the number of hospitals passing through, and then by the time it takes to travel through the path. 
		
		![Reordered lists](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-08-51.png)
		
		Currently, the most optimal route would be shown as the route that passes through the most hospitals, while consumes the least amount of time.

		![Optimal](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-08-27.png)

		After retrieving all the paths, the graph then perform a comparison between all the vertices in the route and the graph. If not all vertices are processed, then the algorithm would then update the graph to construct a smaller graph with the remaining vertices and edges, before repeating the process again.
		
		![Update Graph](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-08-32.png)
		
		Only when reaching the stage where there are no vertices unprocessed, will the algorithm terminate. The result will contains of a list of routes that can reach as many hospitals as it can, within a time limit.
		
		![Last step](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-08-36.png)
	
	The algorithm is guaranteed to return a route, since it iterates through the whole graph, and check every vertices for possible routes.

* **Example of Algorithm works**:
	In the file, there include [a test data file](https://github.com/Merith997/hospital_dist/blob/master/hospital/python/Test_data.py). In there are the test necessary to test 4 cases:
	* A complete connect graph of 2 hospitals
	
	![2 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-36-47.png)
	![2 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-28-16.png)

	From the pathing of the illustration above, there exists a path between 2 hospitals, and since the time travel is within time limit, the algorithm returns a valid path with total time as 12, and the path travels from MF to CH, indicated in red color. As there are only 2 hospitals, the only available - and optimal - path is the path between them.
	
	* A complete connect graph of 3 hospitals
	
	![3 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-36-45.png)
	![3 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-29-04.png)

	Based on the pathing of the illustration above, there exists a path between 3 hospitals, and since the time travel is within our limit, the algorithm returns a valid path with total time as 23, and the path travels from OC to MF to CH, indicated in red color. Given the fact that there are 3 hospitals, it would take at least 2 paths to travel between them all. In this case, the path can be ranked by their time and the algorithm would take the one with shortest time. 
	
	* A complete connect graph of 4 hospitals
	
	![4 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-36-35.png)
	![4 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-29-27.png)

	The pathing of the illustration above, there exists a path between 3 hospitals, and since the time travel is within our limit, the algorithm returns a valid path with total time as 24, and the path travels from OC to MF to OG to CH, indicated in red color. In the case of a more complicated problem than the 2 before, the algorithm can demonstrates the benefit of re-ordering the results to return the optimal result.
		
	* A complete connect graph of all hospitals in Ottawa-Gatineau region
	
	![all hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-11%2011-36-32.png)
	![all hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-30-17.png)
	
	From the pathing of the illustration above, there exists a path between all hospitals, and since it is not possible to travel all the hospitals in one route within time limit, the algorithm returns the most optimal path, before giving repeating on the last hospital. The valid path was with total time of 53 minutes, marked in red color. The graph illustrated shows an ordering of the paths such that it is outside of all the other path, not intersecting any other edges. This is purely a portrait of the graph, not any assumption on a real application of the problem.
		
* **Current drawback of algorithm**:

	The algorithm currently can traverse through the graph, checking if each time applying the algorithm, if the optimal route has covered all vertices or not. If it had not, then the algorithm would update the graph, and then perform the algorithm on it again.
	However, there are many drawbacks from the current version of the algorithm. Firstly, the weights of the edges represent the time it takes to travel between hospitals. This can actually be fluctuate with the traffic and constructions. In a future update of this algorithm would have to account fo this. Secondly, each hospital currently takes no time to unload goods and items. This is an unrealistic thing in the real world. Each time of unloading would be proportional to the delivery load that the location is receiving. In the future, perhaps the time for unloading at each hospital can be calculated in proportion to their speed, and then each vertex would have an additional weight to account for this in the calculation. Thirdly,the supply centre will be next to the first hospital of the route, eliminating the time it takes to travel to it. In real life, this is not feasible, as there are no guarantee that there would be spaces enough next to a hospital to have for a centre. In the future, there would also be needing another calculation of time travel to the first hospital, as well as adjustment to the time traveling. This could also affect the algorithm, as it now need to account for the location of the centre for feasible location. Next, between the time of supplies reaching the centre and the time that all hospitals must receive their supplies is fully available for delivery. In real life, it takes time for supplies and materials to arrive at the centre. Then it has to store those until the time of delivery. This would actually increase the cost of operating of the centre, now needed to upgrade itself to account for the materials it would store. In addition to the time the supplies are delivered, there must also be time to process the items prior to shipping them to the hospitals. This would cost more time to process, and greatly lower the available time for delivery. Lastly, the delivery also varies based on what day does the material arrives, and how they can be distributed without too many trucks clogging the traffic, enlarging the time it takes to travel to hospitals. The graph is one whole complete and connected graph. In real life, and accounting for the fact stated in previous point, there might not be time to travel between two hospitals. Instead of including these paths in our calculation, thus slowed down the calculation, we can omit them from the graph. This would bring situations where many optimal routes of a graph pass through a hospital. If that point is reserved for other routes, and its removal in the algorithm step cause the graph to be disconnected, the algorithm must then consider this, and perform in accordance to this obstacle
* **Conclusion**:
	* From researches online, there have been many attempts to solve this problem. Some of them, such as the research by Duque-Uribe, Sarache, and Gutiérrez [1] and by Li, Ma, Shi and Qian [2], both shows how other algorithm can be used to solve the problem. This, however, is only an attempt at solving the hospital supply problem, using a primitive greedy algorithm to solve. While the algorithm is primitive, not fully taken into account the wide variety of other factors of the real world, it achieved the goal of resulting a list of routes between hospitals that is optimal. It is fully understood that there are many improvements that can be made for this algorithm, but that is for another update in the future of this algorithm. 

[1] - https://www.researchgate.net/publication/336820797_Sustainable_Supply_Chain_Management_Practices_and_Sustainable_Performance_in_Hospitals_A_Systematic_Review_and_Integrative_Framework

[2] - https://www.hindawi.com/journals/mpe/2016/6153898/
