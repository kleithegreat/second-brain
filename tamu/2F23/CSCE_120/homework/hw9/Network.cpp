# include <iostream>
# include <fstream>
# include <sstream>
# include <stdexcept>
# include "Network.h"

using std::string, std::vector;

Network::Network() : users({}), posts({}), tags({}) {}

void Network::loadFromFile(string fileName) {
    // TODO: load user and post information from file
    std::ifstream inFile(fileName);
    if (!inFile.is_open()) {
        throw std::invalid_argument("loadFromFile: could not open file");
    }

    string line;
    while (getline(inFile, line)) {
        std::stringstream ss(line);
        string token;
        vector<string> tokens;
        while (getline(ss, token, ',')) {
            tokens.push_back(token);
        }

        if (tokens.at(0) == "User") {
            if (tokens.size() != 2) {
                throw std::runtime_error("loadFromFile: invalid file format");
            }
            addUser(tokens.at(1));
        } else if (tokens.at(0) == "Post") {
            if (tokens.size() != 4) {
                throw std::runtime_error("loadFromFile: invalid file format");
            }
            addPost(stoi(tokens.at(1)), tokens.at(2), tokens.at(3));
        } else {
            throw std::runtime_error("loadFromFile: invalid file format");
        }
    }
}

void Network::addUser(string userName) {
    // TODO: create user and add it to network
    string lowerUserName = "";
    for (int i = 0; i < userName.length(); i++) {
        lowerUserName += tolower(userName.at(i));
    }

    for (int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == lowerUserName) {
            throw std::invalid_argument("addUser: invalid parameter values");
        }
    }

    User* newUser = new User(lowerUserName);
    users.push_back(newUser);
    std::cout << "Added User " << newUser->getUserName() << std::endl;
}

void Network::addPost(unsigned int postId, string userName, string postText) {
    // TODO: create post and add it to network
    for (int i = 0; i < posts.size(); i++) {
        if (posts.at(i)->getPostId() == postId) {
            throw std::invalid_argument("addPost: invalid parameter values");
        }
    }

    bool userExists = false;
    for (int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == userName) {
            userExists = true;
        }
    }
    if (!userExists) {
        throw std::invalid_argument("addPost: invalid parameter values");
    }

    Post post = new Post(postId, userName, postText);
    posts.push_back(post);

    for (int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == userName) {
            users.at(i)->addUserPost(post);
        }
    }

    vector<string> postTags = post.findTags();
    for (int i = 0; i < postTags.size(); i++) {
        bool tagExists = false;
        for (int j = 0; j < tags.size(); j++) {
            if (tags.at(j)->getTagName() == postTags.at(i)) {
                tagExists = true;
            }
        }
        if (!tagExists) {
            Tag newTag = new Tag(postTags.at(i));
            tags.push_back(newTag);
        }
    }

    std::cout << "Added Post " << postId << " by " << userName << std::endl;
}

vector<Post*> Network::getPostsByUser(string userName) {
    // TODO: return posts created by the given user
    if (userName == "") {
        throw std::invalid_argument("getPostsByUser: user name cannot be empty");
    }

    bool userExists = false;
    vector <Post*> userPosts = {};

    for (int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == userName) {
            userExists = true;
            userPosts = users.at(i)->getUserPosts();
        }
    }

    if (!userExists) {
        throw std::invalid_argument("getPostsByUser: user does not exist");
    }

    return userPosts;
}

vector<Post*> Network::getPostsWithTag(string tagName) {
    // TODO: return posts containing the given tag
    if (tagName == "") {
        throw std::invalid_argument("getPostsWithTag: tag name cannot be empty");
    }

    bool tagExists = false;
    vector <Post*> tagPosts = {};

    for (int i = 0; i < tags.size(); i++) {
        if (tags.at(i)->getTagName() == tagName) {
            tagExists = true;
            tagPosts = tags.at(i)->getTagPosts();
        }
    }

    if (!tagExists) {
        throw std::invalid_argument("getPostsWithTag: tag does not exist");
    }

    return tagPosts;
}

vector<string> Network::getMostPopularHashtag() {
    // TODO: return the tag occurring in most posts
    // in case of a tie, return all the tags in the tie
    
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
