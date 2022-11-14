![maxresdefault](https://user-images.githubusercontent.com/90480106/201592451-dff4c887-5283-4be6-b7aa-7df22e6d98cc.jpeg)

## AzurLane Characters Images Analysis

#### Problem: 

As a 4 four years Azur Lane commander(player) and a game lover, I want to figure out whether the characters' images are similar in the same faction or types and different from other factions and types. If there is some relationship, it may help the game company when designing characters.

#### AzurLane Introduction (from wikipedia):

Azur Lane is a side-scrolling shoot 'em up video game created by Shanghai Manjuu and Xiamen Yongshi. Set in an alternate timeline of World War II, players engage in side-scrolling shooter gameplay, using female moe anthropomorphic characters based on warships from the war's major participants. 

#### Data scources:

1. [Azur Lane Wiki](https://azurlane.koumakan.jp/wiki/Azur_Lane_Wiki)

2. The game itself!

#### Notebooks and files:

1. azurlane_pic.py -> web crawler, download characters' image from Azur Lane Wiki

2. label.csv -> csv file, I label it with characters' faction and type.

3. azurlane_tsne&umap.ipynb -> main notebook, working on tSNE and Umap.

#### Visualization:

tSNE:

![downloadt1](https://user-images.githubusercontent.com/90480106/201591567-a8da8434-0b06-470d-8e74-6b955cbde304.png)

![downloadt2](https://user-images.githubusercontent.com/90480106/201591575-96944d69-f17f-4b61-9095-5e81c991e53d.png)

umap:

![downloadu1](https://user-images.githubusercontent.com/90480106/201591244-b1ada1f8-bd0f-4a1d-a7c3-3ee77d0b8e49.png)

![downloadu2](https://user-images.githubusercontent.com/90480106/201591290-501dbb8f-ac15-42fc-b519-2eff0dfc54bf.png)

#### Conclusion:

No difference between each faction or ship type in the first scatter plot.

However, scatter plots shows that hair and clothes play an important role. The x-axis seems to be hair color, and the y-axis seems to be clothes' color.

#### Future Improvement:

Combine Convolutional Neural Networks to help visualize.



