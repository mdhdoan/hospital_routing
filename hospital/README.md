# hospital_distribution_outline: 
* **Abstract**:
	In the real world, there are many problems in managing a supply chain. Hospital supply chain is but a small part of the industry, yet extremely vital. Without sufficient supplies of medicine and medical supplies, hospitals cannot function properly. In this situation, we are given the task of designing and implementing a supply plan for hospitals, specifically in Ottawa-Gatineau. Given the propblem of supplying hospitals with their needs, we would attempt to apply a greedy algorithm to find the optimal routes available to traverse and delivery supplies.
* **Introduction**:
	Hospital supplying is an important aspect in keeping hospitals running and operating. A hospital needs many things to keep it running, but in this problem, they shall be refined into 5 categories:
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
* **Problem**:	
	* One need to find the path to delivery all supplies. Each hospital has a different amount of staffs and patients, therefore having different weight requirement.
	* Some constraints that can be put on are:
		* Time constraints: each hospital has a deadline that must be met
		* Weight constraints: each hospital has a certain amount of weight of required items that changes daily. This is because the patients number changes daily
		* Transport constraints: we only have a limited amount of transports. The problem is now how to arrange routes and orders of the hospitals to meet their demands
	* Optimizing of the solution can be done by:
		* Reusing transports as much as possible
		* Reducing the cost as much as possible
* **Formulating the problem**:
	* This route finding problem is an application case of the vehicle routing problem. We represent the problem on a graph with:
		* Route's travelling time as weighted edges
		* Hospitals as vertices, each with a cost per delivery value . 
	* Find route(s) that can reach as many vertices within a time limit. The routes must satisfy both the time constraints and optimizes the cost.
* **Solution**:
	* Since this is a vehicle routing problem, one can attempt to brute force search for the most optimal path, or use a greedy approach to select only the most optimal paths between the hospitals.
	* Let's assume the followings:
		* The weights of the edges represent the time it takes to travel between hospitals.
		* Each hospital currently takes no time to unload goods and items
		* The supply centre will be next to the first hospital of the route, eliminating the time it takes to travel to it.
		* Between the time of supplies reaching the centre and the time that all hospitals must receive their supplies is fully available for delivery.
		* The graph is one whole complete and connected graph.
	* In this problem, we will be performing the greedy algorithm. It shall be the first step that can guarantee a feasible solution. 
* **How to approach solution using the greedy algorithm**:
	* First of all, since this is a problem that can be occured anywhere, therefore our solution must be generic. 
	* Our approach, for the greedy algorithm, would be to find available paths that would allow us to reach the hospitals in time, yet cheapest to add to our route. 
	* To do this, we would need to find all possible routes from a starting location. In this case, we are assuming it to be one of the hospitals.
	* After finding all possible routes from all hospitals, we can then begin to sort them and find the route that passes through the most hospitals before ending (satisfying the constraints), while taking the least amount of time (satisfying the optimization).
	* After having the route, we can check it with the list of the hospitals to find if it has covered all the hospitals, or not. If not, then we can repeat our algorithm on the remaining hospitals and find the next optimal route to be added.
	* Only when we reach the stage where there are no hospitals remaining, then we would stop the algorithm.
* **More details on the greedy algorithm**:
	* Firstly, we categorized the graph into 3 parts: 
		* Vertices will be for the hospitals
		* Edges will be for the routing between hospitals
		* Graphs will be a connected component of vertices and edges. In some cases, there can be multiple graphs, for example if the city has hospitals but they are too far apart from each other to be reached within a contraint limit.
	* Our [vertices](Vertex.py) will have details of:
		* Hospital's name/code
		* All routes going from/to the vertices
	* Our [edges](Edge.py) will have details of:
		* Vertices that are the ends of the edge
		* Value of the edge (in this case, it would be the time travel between the hospitals)
	* Our [graphs](Graph.py) will have be consists of the set of vertices and edges that are connected to one another, along with the algorithm.
	* The algorithm be work by:
		* Going through the vertices one at a time, while performing the greedy algorithm to find all available routes from that vertex. 
			* Since we are considering the fact that the route between 2 hospitals are identical, this method would work for travelling both ways.
		* After retrieving all routes, then we proceed to re organized them by the number of hospitals passing through, and then by the time it takes to travel through the path. 
			* Currently, the most optimal route would be shown as the route that passes through the most hospitals, while consumes the least amount of time.
		* After retrieving all the paths, the graph then perform a comparison between all the vertices in the route and the graph. If not all vertices are processed, then the algorithm would then update the graph to construct a smaller graph with the remaining vertices and edges, before repeating the process again.
		* Only when we reach the stage where there are no vertices unprocessed, will we stop the algorithm. The result will contains of a list of routes that can reach as many hospitals as it can, within a time limit.
	* The algorithm is guaranteed to return a route, since it iterates through the whole graph, and check every vertices for possible routes.
* **Example of Algorithm works**:
	In the file, there include [a test data file].(Testdata.py). In there are the test necessary to test 4 cases: 
	* A complete connect graph of 2 hospitals
	
	![2 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-28-16.png)
	
	As you can see from the pathing, there exists a path between 2 hospitals, and since the time travel is within our limit, the algorithm returns a valid path with total time as 12, and the path travels from MF to CH
	
	* A complete connect graph of 3 hospitals
	
	![3 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-29-04.png)
	
	As you can see from the pathing, there exists a path between 3 hospitals, and since the time travel is within our limit, the algorithm returns a valid path with total time as 23, and the path travels from OC to MF to CH 
	Due to the fact that it takes the same amount of time going both way in a path, there is no difference in the order of the hospitals in the path
	
	* A complete connect graph of 4 hospitals
	
	![4 hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-29-27.png)
	
	As you can see from the pathing, there exists a path between 3 hospitals, and since the time travel is within our limit, the algorithm returns a valid path with total time as 24, and the path travels from OC to MF to OG to CH
	Due to the fact that it takes the same amount of time going both way in a path, there is no difference in the order of the hospitals in the path
	
	* A complete connect graph of all hospitals in Ottawa-Gatineau region
	
	![all hospitals](https://github.com/Merith997/hospital_dist/blob/master/hospital/images/Screenshot%20from%202020-05-10%2021-30-17.png)
	
	As you can see from the pathing, there exists a path between all hospitals, and since the time travel is within our limit, the algorithm returns a valid path with total time as 53
	Due to the fact that it takes the same amount of time going both way in a path, there is no difference in the order of the hospitals in the path
	
* **Current drawback of algorithm**:
	* Current assumption:
		* The weights of the edges represent the time it takes to travel between hospitals:
			* This can actually be fluctuate with the traffic and constructions. In a future update of this algorithm would have to account fo this.
		* Each hospital currently takes no time to unload goods and items:
			* This is an unrealistic thing in the real world. Each time of unloading would be proportional to the delivery load that the location is receiving. 
			* In the future, perhaps the time for unloading at each hospital can be calculated in proportion to their speed, and then each vertex would have an additional weight to account for this in the calculation.
		* The supply centre will be next to the first hospital of the route, eliminating the time it takes to travel to it:
			* In real life, this is not feasible, as there are no guarantee that there would be spaces enough next to a hospital to have for a centre.
			* In the future, there would also be needing another calculation of time travel to the first hospital, as well as adjustment to the time traveling. This could also affect the algorithm, as it now need to account for the location of the centre for feasible location.
		* Between the time of supplies reaching the centre and the time that all hospitals must receive their supplies is fully available for delivery:
			* In real life, it takes time for supplies and materials to arrive at the centre. Then it has to store those until the time of delivery. This would actually increase the cost of operating of the centre, now needed to upgrade itself to account for the materials it would store.
			* In addition to the time the supplies are delivered, there must also be time to process the items prior to shipping them to the hospitals. This would cost more time to process, and greatly lower the available time for delivery.
			* Lastly, the delivery also varies based on what day does the material arrives, and how they can be distributed without too many trucks clogging the traffic, enlarging the time it takes to travel to hospitals.
		* The graph is one whole complete and connected graph.
			* In real life, and accounting for the fact stated in previous point, there might not be time to travel between two hospitals. Instead of including these paths in our calculation, thus slowed down the calculation, we can omit them from the graph. 
			* This would bring situations where many optimal routes of a graph pass through a hospital. If that point is reserved for other routes, and its removal in the algorithm step cause the graph to be disconnected, the algorithm must then consider this, and perform in accordance to this obstacle
* **Conclusion**:
	* From researches online, there have been many attempts to solve this problem. Some of them, such as the research by Duque-Uribe, Sarache, and Gutiérrez [1] and by Li, Ma, Shi and Qian [2], both shows how other algorithm can be used to solve the problem. This, however, is only an attempt at solving the hospital supply problem, using a primitive greedy algorithm to solve.

[1] - https://www.researchgate.net/publication/336820797_Sustainable_Supply_Chain_Management_Practices_and_Sustainable_Performance_in_Hospitals_A_Systematic_Review_and_Integrative_Framework

[2] - https://www.hindawi.com/journals/mpe/2016/6153898/
