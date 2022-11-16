# Homework 4 - Exploring Social Networks
# Kyle Demers
## 11/3/2022

Assignment
You will investigate the split of the Karate Club (Zachary, 1977), described starting on slide 92 in the Module-07 Social Networks lecture slides. You must use a Python or JavaScript library (as discussed in Module-09 Graph Vis) to generate the graphs required in this assignment.

## Q1. Color nodes based on final split 
Draw the original Karate club graph (before the split) and color the nodes according to the factions they belong to (John A or Mr. Hi). This should look similar to the graph on slide 92 - all edges should be present, just indicate the nodes in the eventual split by color.

### Answer:

To get the colors, I used the matrix from the data set to get connections from either MrHi or John. This was used as a shortcut to labelling each individual node.
Then I cross refrenced my graph with slide 92 in the Module-07 Social Networks lecture slides and changed the colors accordingly. 
```python
g = nx.karate_club_graph()
#get indexes for mr Hi's group
MrHi = [i for i in g[0]]
#get indexes for Johns group
John = [i for i in g[33]]
#small shortcut to get most labels correct
for i in MrHi:
    color[i] = 'green'
for i in John:
    color[i] = 'red'
#adjust other colors
color[0] = 'green'
color[8] = 'green'
color[33] = 'red'
color[24] = 'green'
color[25] = 'green'
color[16] = 'green'
color[13] = 'green'
color[19] = 'green'
color[24] = 'red'
color[25] = 'red'
#create graph
nx.draw(g, with_labels=True, node_color=color)
```

The result of this code lead me to get this graph

<img width="312" alt="image" src="https://user-images.githubusercontent.com/112887807/202014989-fba6951b-37fb-4e22-9cb3-2829b1967064.png">

### Q: How many nodes (students) eventually go with John and how many with Mr. Hi?

### Answer:

16 students will eventually go with Mr Hi (Green).

16 students will eventually go with John (Red).

*Note that these counts do not include the John or Mr. Hi themselves*

### Discussion

I was able to use whether or not they had a connection to the teacher to develop a first step at labeling each student. This correctly classified a third of the 
students and I was able to hard code the rest of the students from the slide.

---

## Q2. Use the Girvan-Newman algorithm to illustrate the split

We know the final result of the Karate Club split, which you've colored in Q1. Use the Girvan-Newman algorithm to check if the split could have been predicted by the social interactions expressed by edges. How well does the mathematical model represent reality? Generously document your answer with all supporting equations, code, graphs, arguments, etc.

Keeping the node colors the same as they were in Q1, run multiple iterations of the Girvan-Newman graph partioning algorithm (see Module-07 Social Networks, slides 90-99) on the Karate Club graph until the graph splits into two connected components. Include an image of the graph after each iteration in your report.

### Answer:

I created this function to eliminate the node with the most betweeness.

```python
def girvnew():
    edgebetweendict = NC.edge_betweenness(g)
    betweenlist = [edgebetweendict[i] for i in edgebetweendict]
    idx = np.argmax(betweenlist)
    rem = list(edgebetweendict)[idx]
    g.remove_edge(rem[0],rem[1])
    nx.draw(g, with_labels=True, node_color=color)
```

I then initialized a counter, called the function, and added one to the counter.
Each graph per iteration is below as well as which edge was removed.

<img width="287" alt="image" src="https://user-images.githubusercontent.com/112887807/202018947-d432f694-c4b7-4777-bb73-b9d8e9895c9f.png">

<img width="326" alt="image" src="https://user-images.githubusercontent.com/112887807/202018997-60eca42a-5bc9-42c3-b073-de6cceb7d73f.png">

<img width="309" alt="image" src="https://user-images.githubusercontent.com/112887807/202064338-ebce10cc-a7eb-4cbb-9f09-f444fa23f5af.png">

<img width="355" alt="image" src="https://user-images.githubusercontent.com/112887807/202064394-b1873775-0673-4f08-9bee-02772ea39ebf.png">

<img width="305" alt="image" src="https://user-images.githubusercontent.com/112887807/202064437-a865bbc5-78c8-447d-b53c-762507295619.png">

<img width="307" alt="image" src="https://user-images.githubusercontent.com/112887807/202064477-be3b4265-c8dd-4ecd-a6ca-b237b6690277.png">

<img width="319" alt="image" src="https://user-images.githubusercontent.com/112887807/202064524-541b717c-3ff5-497a-bbe6-f0aafbde6035.png">

<img width="286" alt="image" src="https://user-images.githubusercontent.com/112887807/202064563-a2ec89e0-7915-4dc8-bf59-9a9de8086031.png">

<img width="312" alt="image" src="https://user-images.githubusercontent.com/112887807/202064634-451d9a60-227f-4621-85c3-febed0d710f7.png">

<img width="281" alt="image" src="https://user-images.githubusercontent.com/112887807/202064704-9ebd6d58-7c8a-4b46-abe6-fafb0a762ee4.png">

<img width="286" alt="image" src="https://user-images.githubusercontent.com/112887807/202064817-5a80a128-0bca-4190-a73e-2c0ab5592c7b.png">

### Q:How many iterations did it take to split the graph?

### Answer:

It took 11 iterations to fully split the graph

### Discussion:

I couldn't find an automatic way to run a loop until there were 2 distinct clusters. I just had to run a block of code calling the function and 
increase the counter by one. It feels weird not automating it, but this was my best solution.

---

## Q3. Compare the actual to the mathematical split 

### Q: Did all of the same colored nodes end up in the same group? If not, what is different?

### Answer:

Not all the nodes in the groups where the same color. There are two nodes in John's group that are not meant to be there. There are two green nodes that are in the
red nodes groups. That means that the girvan newman model misclassified two nodes.

---
### Extra
Link to ipynb where many calculations and graphs were done:
[link](https://github.com/Kyle-Demers08/Data440/blob/main/HW5/HW_5.ipynb)

### Resources:
github; <https://gist.github.com/millionsmile/3682029>

Google Slides, <https://docs.google.com/presentation/d/1Bey47wfUnBEy4O6j-T2X7y_bT0YNM6CN/edit#slide=id.p92>
