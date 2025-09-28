#include<bits/stdc++.h>
#define st first
#define nd second
#define all(x) x.begin(),x.end()

using namespace std;

int RA(int low, int high){
    assert(low <= high);
	return rand()%(high-low+1)+low;
}

int getSeed(string name){
    assert(name.size() >= 1);
    int ans = 0;
    for(auto i : name){
        ans += i * RA(1,512);
        ans %= (int)1e9;
    }
	return ans;
}

// LIMITS
// to ensure invalid test is not generated
const int NLIM = 1e5;   // number of verticies

class Generator{
    private:
                                                // Test Data:
        int N, M;                               // N            - number of verticies, M - number of edges
        vector<pair<pair<int,int>,int>> Edges;  // Edges        - edges in graph
        
                                                // Other variables
    int edge_exist[MLIM][MLIM];                 // information if edge (i,j) exist, > 0 exist, 0 does'nt exist
    
    public:

        Generator(){}

        void add_edge(int u, int v, int w){
            assert(edge_exist[u][v] == 0);
            edge_exist[u][v] = w;
            edge_exist[v][u] = w;
            Edges.push_back({{u,v},w});
        }

        void make_random_test(int n_lim, int m_lim, int w_lim){
            assert(n_lim <= NLIM);

            N = RA(2,n_lim);
            M = RA(1, (N * (N-1))/2);
            int u = 0,v = 0;
            edge_exist[0][0] = 1;
            for(int i = 0; i < M; i++){
                while(u == v || edge_exist[u][v] > 0){
                    u = RA(1,N);
                    v = RA(1,N);
                }
                w = RA(1,w_lim);
                edge_exist[u][v] = w;
                edge_exist[v][u] = w;
                Edges.push_back({{u,v},w});
            }
        }

        void print_test(){
            assert(N <= NLIM);
            assert(M <= N * (N - 1)/2);

            cout << N << " " << M << "\n";
            for(auto i : Edges){
                cout << i.st.st << " " << i.st.nd << " " << i.nd << "\n";
            }
        }
};

Generator gen;

int main(int argc, const char* argv[]){
    assert(argc==2);
    srand(getSeed(argv[1]));
	// string name=argv[1];
	
    gen.make_random_test(10, 20, 20);
    gen.print_test();
}