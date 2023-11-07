# include <iostream>
# include <fstream>
# include <sstream>
# include <stdexcept>
# include "Network.h"

using std::string;
using std::vector;

Network::Network() : users({}), posts({}), tags({}) {}

void Network::loadFromFile(string fileName) {
    std::ifstream inFile(fileName);
    if (!inFile.is_open()) {
        throw std::invalid_argument("loadFromFile: could not open file");
    }

    string line;
    while (getline(inFile, line)) {
        std::stringstream ss(line);
        string userOrPost;
        ss >> userOrPost;
        if (userOrPost == "User") {
            string username;
            ss >> username;
            if (ss.fail()) {
                throw std::invalid_argument("loadFromFile: invalid file format");
            }
            addUser(username);
        } else if (userOrPost == "Post") {
            unsigned int postId;
            string username;
            string postText;
            ss >> postId >> username;
            if (ss.fail()) {
                throw std::invalid_argument("loadFromFile: invalid file format");
            }
            ss >> std::ws;
            getline(ss, postText);
            if (ss.fail()) {
                throw std::invalid_argument("loadFromFile: invalid file format");
            }
            addPost(postId, username, postText);
        } else {
            throw std::invalid_argument("loadFromFile: invalid file format");
        }
    }
}

void Network::addUser(string userName) {
    string lowerUserName = "";
    for (unsigned int i = 0; i < userName.length(); i++) {
        lowerUserName += tolower(userName.at(i));
    }

    for (unsigned int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == lowerUserName) {
            throw std::invalid_argument("addUser: invalid parameter values");
        }
    }

    User* newUser = new User(lowerUserName);
    users.push_back(newUser);
    std::cout << "Added User " << newUser->getUserName() << std::endl;
}

void Network::addPost(unsigned int postId, string userName, string postText) {
    for (unsigned int i = 0; i < posts.size(); i++) {
        if (posts.at(i)->getPostId() == postId) {
            throw std::invalid_argument("addPost: invalid parameter values");
        }
    }

    bool userExists = false;
    for (unsigned int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == userName) {
            userExists = true;
        }
    }
    if (!userExists) {
        throw std::invalid_argument("addPost: invalid parameter values");
    }

    Post* post = new Post(postId, userName, postText);
    posts.push_back(post);

    for (unsigned int i = 0; i < users.size(); i++) {
        if (users.at(i)->getUserName() == userName) {
            users.at(i)->addUserPost(post);
        }
    }

    vector<string> postTags = post->findTags();
    for (unsigned int i = 0; i < postTags.size(); i++) {
        bool tagExists = false;
        for (unsigned int j = 0; j < tags.size(); j++) {
            if (tags.at(j)->getTagName() == postTags.at(i)) {
                tagExists = true;
            }
        }
        if (!tagExists) {
            Tag* newTag = new Tag(postTags.at(i));
            tags.push_back(newTag);
        }
    }

    std::cout << "Added Post " << postId << " by " << userName << std::endl;
}

vector<Post*> Network::getPostsByUser(string userName) {
    if (userName == "") {
        throw std::invalid_argument("getPostsByUser: user name cannot be empty");
    }

    bool userExists = false;
    vector <Post*> userPosts = {};

    for (unsigned int i = 0; i < users.size(); i++) {
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
    if (tagName == "") {
        throw std::invalid_argument("getPostsWithTag: tag name cannot be empty");
    }

    bool tagExists = false;
    vector <Post*> tagPosts = {};

    for (unsigned int i = 0; i < tags.size(); i++) {
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
    struct TagCount {
        Tag tag;
        int count;
    };

    vector<TagCount> tagCounts = {};
    for (unsigned int i = 0; i < tags.size(); i++) {
        int count = 0;
        for (unsigned int j = 0; j < posts.size(); j++) {
            vector<string> postTags = posts.at(j)->findTags();
            for (unsigned int k = 0; k < postTags.size(); k++) {
                if (postTags.at(k) == tags.at(i)->getTagName()) {
                    count++;
                }
            }
        }
        TagCount tagCount = {*(tags.at(i)), count};
        tagCounts.push_back(tagCount);
    }

    vector<string> mostPopularTags = {};
    int maxCount = 0;
    for (unsigned int i = 0; i < tagCounts.size(); i++) {
        if (tagCounts.at(i).count > maxCount) {
            maxCount = tagCounts.at(i).count;
        }
    }
    for (unsigned int i = 0; i < tagCounts.size(); i++) {
        if (tagCounts.at(i).count == maxCount) {
            mostPopularTags.push_back(tagCounts.at(i).tag.getTagName());
        }
    }

    return mostPopularTags;
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
