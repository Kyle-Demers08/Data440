# Homework 4 - Exploring Social Networks
# Kyle Demers
## 11/3/2022

Assignment
You will investigate the split of the Karate Club (Zachary, 1977), described starting on slide 92 in the Module-07 Social Networks lecture slides. You must use a Python or JavaScript library (as discussed in Module-09 Graph Vis) to generate the graphs required in this assignment.

## Q1. Color nodes based on final split 
Draw the original Karate club graph (before the split) and color the nodes according to the factions they belong to (John A or Mr. Hi). This should look similar to the graph on slide 92 - all edges should be present, just indicate the nodes in the eventual split by color.

### Q: How many nodes (students) eventually go with John and how many with Mr. Hi?

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

### Discussion

The friendship paradox is interesting because the mean is almost always going to be skewed by a few of the "popular" people, or at least the ones who care a lot about their social media presence. This can be seen by the high standard deviation. That is a big part og how this theory works however. You are more likely to be friends with people who have a large amount of friends relative to a small amount of friends. That means that sampling bias occurs as poeple with a lot of friends will likely be sampled. 

---

## Q2. Use the Girvan-Newman algorithm to illustrate the split
Determine if the friendship paradox holds for your Twitter account. Since Twitter is a directed graph, use followers as the value you measure (i.e., "do your followers have more followers than you?").

We know the final result of the Karate Club split, which you've colored in Q1. Use the Girvan-Newman algorithm to check if the split could have been predicted by the social interactions expressed by edges. How well does the mathematical model represent reality? Generously document your answer with all supporting equations, code, graphs, arguments, etc.

Keeping the node colors the same as they were in Q1, run multiple iterations of the Girvan-Newman graph partioning algorithm (see Module-07 Social Networks, slides 90-99) on the Karate Club graph until the graph splits into two connected components. Include an image of the graph after each iteration in your report.

### Q:How many iterations did it take to split the graph?

### Answer:

---

## Q3. Compare the actual to the mathematical split 

### Q: Did all of the same colored nodes end up in the same group? If not, what is different?

### Answer

---
### Extra
Link to ipynb where many calculations and graphs were done:
[link](https://github.com/Kyle-Demers08/Data440/blob/main/HW4/Untitled%20(2).ipynb)


### Resources:
programiz, <https://www.programiz.com/python-programming/methods/list/sort>

github; using the twitter api, <https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/6b-labs-code-standard-python.md>

github; twitters user object model, <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user> 
