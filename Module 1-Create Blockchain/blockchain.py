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
    
    # Define problem which is hard to solve and easy to verify for mining
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2)
                                            .encode()).hexdigest()
            #check if first character 0000
            if hash_operation[:3] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self,  block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    
# part 2 - Mining our Blockchain