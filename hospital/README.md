# hospital_distribution_outline: 
* **Abstract**:
	Given the propblem 
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
	* Our vertices will have details of:
		* Hospital's name/code
		* All routes going from/to the vertices
	* Our edges will have details of:
		* Vertices that are the ends of the edge
		* Value of the edge (in this case, it would be the time travel between the hospitals)
	* Our graphs will have be consists of the set of vertices and edges that are connected to one another, along with the algorithm.
	* The algorithm be work by:
		* Going through the vertices one at a time, while performing the greedy algorithm to find all available routes from that vertex. 
			* Since we are considering the fact that the route between 2 hospitals are identical, this method would work for travelling both ways.
		* After retrieving all routes, then we proceed to re organized them by the number of hospitals passing through, and then by the time it takes to travel through the path. 
			* Currently, the most optimal route would be shown as the route that passes through the most hospitals, while consumes the least amount of time.
		* After retrieving all the paths, the graph then perform a comparison between all the vertices in the route and the graph. If not all vertices are processed, then the algorithm would then update the graph to construct a smaller graph with the remaining vertices and edges, before repeating the process again.
		* Only when we reach the stage where there are no vertices unprocessed, will we stop the algorithm. The result will contains of a list of routes that can reach as many hospitals as it can, within a time limit.
	* The algorithm is guaranteed to return a route, since it iterates through the whole graph, and check every vertices for possible routes.
* **Example of Algorithm works**:
	Include pics and explanation
* **Current drawback of algorithm**:
	Current assumption:
		The whole graph is now a complete connected. What if it's not?
			How this can be address?
		The current total route time does not account for the window of delivery, as well as time for unloading
			How this can be address?
* **Conclusion**:
