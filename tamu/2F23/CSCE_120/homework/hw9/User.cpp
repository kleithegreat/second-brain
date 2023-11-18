# include <string>
# include <stdexcept>
# include "User.h"

using std::string, std::vector;

User::User(string userName) : userName(), userPosts() {
    if (userName.empty()) {
        throw std::invalid_argument("user constructor: username cannot be empty");
    }

    if (userName.at(0) < 'a' || userName.at(0) > 'z') {
        throw std::invalid_argument("user constructor: username must start with a lowercase letter");
    }

    for (unsigned int i = 0; i < userName.length(); i++) {
        if (userName.at(i) >= 'A' && userName.at(i) <= 'Z') {
            throw std::invalid_argument("user constructor: username must be all lowercase");
        }
    }

    this->userName = std::move(userName);
}

string User::getUserName() {
    return userName;
}

vector<Post*>& User::getUserPosts() {
    return userPosts;
}

void User::addUserPost(Post* post) {
    if (post == nullptr) {
        throw std::invalid_argument("user add post: invalid parameter values");
    }

    userPosts.push_back(post);
}
