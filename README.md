# hospital_dist_outline: 
* **Abstract**:

* **Introduction**:
	Hospital supplying is an important aspect in keeping hospitals running and operating. A hospital needs many things to keep it running, but in this problem, they shall be refined into 5 categories:
	* Food: 
		* All staying patients will have 3 meals a day
		* Medical staffs will work in 3 shifts, each will have their own meal. Hence medical staffs will also require 3 meals a day. Those who work on the night shift (11:00pm-7:00am) are also volunteers, these numbers can be changed daily, due to patients' requirement
		* Administration staffs works from 9-5, therefore they will have 1 meal a day at the hospital
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
* **Solution**:
	This route finding problem is an application case of the vehicle routing problem, on a graph represented with:
	  * Route's travelling time as weighted edges
		* Hospitals as vertices, each with a cost per delivery value . 
	Find route(s) that can reach as many vertices within a time limit. The routes must satisfy both the time constraints and optimizes the cost.
* **How to approach solution**:
	Find routes that would satisfies the time constraints before optimizing the cost.
* **How to approach algorithm**:
	Since we need to create routes to traverse all hospitals, this is an application case of the vehicle routing problem. 
	An option on tackling this problem is by using a greedy algorithm: 
		Given all the hospitals, we must first check the graph's connectivity. Right now, we assume the graph is a complete connected graph. This is a fair assumption, since you can take any roads to go from one hospital to another.
		Afterward, we perform the greedy algorithm on all vertices in the component to find the longest route, and then reorganized to find one with the shortest time
* **Example of Algorithm works**:
	Include pics and explanation
* **Current drawback of algorithm**:
	Current assumption:
		The whole graph is now a complete connected. What if it's not?
			How this can be address?
		The current total route time does not account for the window of delivery, as well as time for unloading
			How this can be address?
* **Conclusion**:
