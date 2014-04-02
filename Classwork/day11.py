# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 13:56:37 2014

@author: sophie
"""



class User:
    pass

def print_user_information(u):
    print "User's name:" + u.name
    print "User's hometown:" + u.hometown
    print "Friends:"
    for friend in u.friends:
        print "" + friend.name
def make_friends(u1,u2):
    u1.friends.append(u2)
    u2.friends.append(u1)

if __name__ == "__main__":
    u = User()
    u.name = "Sophie Li"
    u.hometown = "Troy, MI"
    u.friends = []
    u2 = User()
    u2.name = "Bob Someone"
    u2.hometown = "Place, MI"
    u2.friends = []
    make_friends(u,u2)
    print_user_information(u2)
#    print u.name