"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    #read the text file.
    with open(text_path,'r') as f:
        #get the text from the file.
        text = f.read()
        #make it lower case to avoid confusion.
        text = text.lower()
        #remove the punctuation (we want only the words to avoid confusion).
        text = text.translate(str.maketrans('','',string.punctuation))
        # to remove [verse 1: artist] when doing lyrics.
        #text = re.sub(r'\[(.+)\]', ' ', text)
        #make a list of the words.
        #remove the white spaces.
        words = text.split()

    return words


def make_graph(words):
    #make an instance of the graph.
    g = Graph()
    #initialize a value (in the beginning there is no previous word).
    previous_word = None
    #go through the words.
    for word in words:
        #get the vertex of the word.
        word_vertex = g.get_vertex(word)
        #increase the edge of this word in the previous word.
        if previous_word:
            previous_word.increment_edge(word_vertex)
        #set this word as the previous word.
        previous_word = word_vertex
    #generate the two lists(neighboring verticies,weights)for each vertex.
    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    # pick the first word randomly and get it's vertex..val
    word_vertex = g.get_vertex(random.choice(words))
    #print(word_vertex.neighboring_verticies)
    #initialize a list.
    composition = []
    #get the next word and add it to the composition 'length' times.
    for _ in range(length):
        composition.append(word_vertex.value)
        word_vertex = g.get_next_word(word_vertex)
    return composition

def main():
    #get the list of the words all in lowercase 
    #without whitespaces and punctuation.
    words = get_words_from_text("texts/hp_sorcerer_stone.txt")
    #get the graph.
    g = make_graph(words)
    #get the list of words and print them.
    composition = compose(g,words,100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()