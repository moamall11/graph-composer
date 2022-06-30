
"""
Empty Graph Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

class Vertex(object):
    def __init__(self, value):
        #the value is the word.
        self.value = value
        #make a dictionary that includes all the words 
        #that have an edge from this vertex. 
        self.adjacent = {}
        self.neighboring_verticies = []
        self.neighboring_weights = []

    def add_edge_to(self, vertex, weight=0):
        #assign an edge to a vertex.
        self.adjacent[vertex] = weight
 
    def increment_edge(self, vertex):
        #increase the edge of a vertex.
        self.adjacent[vertex] = self.adjacent.get(vertex,0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        #make two lists from the dictionary.
        for vertex,weight in self.adjacent.items():
            self.neighboring_verticies.append(vertex)
            self.neighboring_weights.append(weight)


    def next_word(self):
        #returns the most probable vertex depending on the weights.
        # return random.choices(self.neighboring_verticies,
            # weights = self.neighboring_weights)[0]
        #go through all the neighboring verticies 
        #until u find the one with the highest weight and return it.
        score=0
        for i,vertex in enumerate(self.neighboring_verticies):
            if self.neighboring_weights[i] >= score:
                next_word_vertex = vertex
                score = self.neighboring_weights[i]
        return next_word_vertex

class Graph(object):
    def __init__(self):
        #make a dictionary of all the words and their verticies objects.
        self.verticies = {}

    def get_vertex_values(self):
        #return all the possible words to be used.
        return self.verticies.keys()

    def add_vertex(self, value):
        #take a value(word) and convert it into a vertex object 
        #and add them to the dictionary.
        self.verticies[value]=Vertex(value)


    def get_vertex(self, value):
        #return the vertex object of a value(word) 
        #and if it doesn't exist add one.
        if value not in self.verticies:
            self.add_vertex(value)
        return self.verticies[value]

    def get_next_word(self, current_vertex):
        #returns the next vertex.
        return current_vertex.next_word()

    def generate_probability_mappings(self):
        for vertex in self.verticies.values():
            vertex.get_probability_map()
