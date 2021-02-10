# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:15:30 2021

@author: Datta
"""
# To install Flask : pip install Flask==0.12.2
# Module 1- Create a Blockchain
# Import the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# part 1 - Building a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0') 
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
        

# part 2 - Mining our Blockchain