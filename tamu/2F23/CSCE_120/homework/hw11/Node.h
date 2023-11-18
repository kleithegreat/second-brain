# ifndef NODE
# define NODE

# include "TemperatureData.h"

struct Node {
	public:
		TemperatureData data;
		Node* next;

		Node();
		Node(std::string id, int year, int month, double temperature);
		Node(const Node& other);
		Node& operator=(const Node& other);
		bool operator<(const Node& b);
		virtual ~Node() {}
};

# endif
