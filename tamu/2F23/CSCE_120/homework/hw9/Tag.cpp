# include <string>
# include <stdexcept>
# include "Tag.h"

using std::string, std::vector;

Tag::Tag(string tagName) /* TODO: initialize */ {
    // TODO: implement constructor checks
}

string Tag::getTagName() {
    // TODO: implement getter
}

vector<Post*>& Tag::getTagPosts() {
    // TODO: implement getter
}

void Tag::addTagPost(Post* post) {
    // TODO: add post to tag posts
}
