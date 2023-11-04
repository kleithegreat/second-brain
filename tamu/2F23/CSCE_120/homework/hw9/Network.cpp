# include <iostream>
# include <fstream>
# include <sstream>
# include <stdexcept>
# include "Network.h"

using std::string, std::vector;

Network::Network() : users({}), posts({}), tags({}) {}

void Network::loadFromFile(string fileName) {
    // TODO: load user and post information from file
}

void Network::addUser(string userName) {
    // TODO: create user and add it to network
}

void Network::addPost(unsigned int postId, string userName, string postText) {
    // TODO: create post and add it to network
}

vector<Post*> Network::getPostsByUser(string userName) {
    // TODO: return posts created by the given user
}

vector<Post*> Network::getPostsWithTag(string tagName) {
    // TODO: return posts containing the given tag
}

vector<string> Network::getMostPopularHashtag() {
    // TODO: return the tag occurring in most posts
}

Network::~Network() {
    for (unsigned int i = 0; i < users.size(); ++i) {
        delete users.at(i);
    }

    for (unsigned int i = 0; i < tags.size(); ++i) {
        delete tags.at(i);
    }
    
    for (unsigned int i = 0; i < posts.size(); ++i) {
        delete posts.at(i);
    }
}
