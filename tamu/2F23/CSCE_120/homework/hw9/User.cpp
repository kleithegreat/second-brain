# include <string>
# include <stdexcept>
# include "User.h"

using std::string, std::vector;

User::User(string userName) /* TODO: initialize */ {
    // TODO: implement constructor checks
    if (userName == "") {
        throw std::invalid_argument("user constructor: invalid parameter values");
    }

    if (userName.at(0) < 'a' || userName.at(0) > 'z') {
        throw std::invalid_argument("user constructor: invalid parameter values");
    }

    // error if userName contains any uppercase letters
    for (int i = 0; i < userName.length(); i++) {
        if (userName.at(i) >= 'A' && userName.at(i) <= 'Z') {
            throw std::invalid_argument("user constructor: invalid parameter values");
        }
    }

    this->userName = userName;
}

string User::getUserName() {
    // TODO: implement getter
    return userName;
}

vector<Post*>& User::getUserPosts() {
    // TODO: implement getter
    return userPosts;
}

void User::addUserPost(Post* post) {
    // TODO: add post to user posts
    if (post == nullptr) {
        throw std::invalid_argument("user add post: invalid parameter values");
    }

    userPosts.push_back(post);
}
