# Programming_Vax_COVID_Switzerland

Project goal: create a simulation game for Covid vaccinations in Switzerland

Tasks:

# Create 2 classes, BLA (Base logistique de l'armée et) and Canton

-BLA: program received doses feature and distribute doses action
-Canton features: Population, Priority population(2 or 3 categories, perhaps using only age distributions), doses received, doses used(maybe divide into 1st and 2nd doses), usage function(if we limit simulation time we can maybe consider this to be linear until saturation rate) 

# Program rounds/interaction

-Print updated information from previous round or display in interactive interface

-(At least) two distrubtion algorithms and a manual mode

-Completely proportional distribution algorithm

-Optimized distribution algorithm based on usage efficiciency, with a minimal rate for all cantons, and the remainder allocated to the most efficient cantons

-Manual mode, type in manually how much each canton should reveive

# For the report

- Describe all the above steps

- Simulate the process for 12 weeks (March-May) with both of our automatic models

-Write about the results in terms of efficiency, limitations of the paramters we use, how to add complexity to the model, and how it might interact wiht epidemiological elements
