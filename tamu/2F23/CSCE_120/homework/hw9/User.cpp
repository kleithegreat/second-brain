# include <string>
# include <stdexcept>
# include "User.h"

using std::string, std::vector;

User::User(string userName) /* TODO: initialize */ {
    // TODO: implement constructor checks
}

string User::getUserName() {
    // TODO: implement getter
}

vector<Post*>& User::getUserPosts() {
    // TODO: implement getter
}

void User::addUserPost(Post* post) {
    // TODO: add post to user posts
}
