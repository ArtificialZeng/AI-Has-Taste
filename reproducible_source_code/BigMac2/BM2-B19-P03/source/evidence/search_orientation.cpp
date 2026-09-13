#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <random>
#include <string>
#include <utility>
#include <vector>

struct Constraint {
  int required = 0;
  std::vector<std::pair<int,int>> items;
  int count = 0;
};

static int penalty(const Constraint& c, int count) {
  int d = c.required - count;
  if (d <= 0) return 0;
  // Squaring prioritizes constraints with a deficit greater than one.
  return d * d;
}

int main(int argc, char** argv) {
  if (argc != 5) {
    std::cerr << "usage: search_orientation INSTANCE SEED RESTARTS STEPS\n";
    return 2;
  }
  std::ifstream in(argv[1]);
  int n, m;
  if (!(in >> n >> m)) return 2;
  std::vector<Constraint> cons(m);
  std::vector<std::array<std::vector<int>,3>> incidence(n);
  for (int cid = 0; cid < m; ++cid) {
    int len;
    in >> cons[cid].required >> len;
    cons[cid].items.resize(len);
    for (int i = 0; i < len; ++i) {
      int v, t; in >> v >> t;
      cons[cid].items[i] = {v,t};
      incidence[v][t].push_back(cid);
    }
  }
  uint64_t seed = std::stoull(argv[2]);
  int restarts = std::stoi(argv[3]);
  int steps = std::stoi(argv[4]);
  std::mt19937_64 rng(seed);
  std::vector<int> choice(n), best_choice;
  int global_best = std::numeric_limits<int>::max();

  auto recompute = [&]() {
    int objective = 0;
    for (auto& c : cons) {
      c.count = 0;
      for (auto [v,t] : c.items) c.count += (choice[v] == t);
      objective += penalty(c, c.count);
    }
    return objective;
  };

  for (int restart = 0; restart < restarts; ++restart) {
    // Bias the start to the two C14-incidence-maximizing types at each vertex.
    for (int v = 0; v < n; ++v) {
      std::array<int,3> c14{};
      for (int t = 0; t < 3; ++t)
        for (int cid : incidence[v][t])
          if (cons[cid].required == 5) ++c14[t];
      int worst = int(std::min_element(c14.begin(), c14.end()) - c14.begin());
      int a = (worst + 1) % 3, b = (worst + 2) % 3;
      choice[v] = (rng() & 1) ? a : b;
    }
    int objective = recompute();
    std::vector<int> violated;
    violated.reserve(m);

    for (int step = 0; step < steps && objective; ++step) {
      violated.clear();
      for (int cid = 0; cid < m; ++cid)
        if (cons[cid].count < cons[cid].required) violated.push_back(cid);
      if (violated.empty()) { objective = 0; break; }
      int cid = violated[rng() % violated.size()];
      const auto& selected = cons[cid];

      struct Move { int delta, v, target; };
      std::vector<Move> moves;
      moves.reserve(selected.items.size());
      int best_delta = std::numeric_limits<int>::max();
      for (auto [v,target] : selected.items) {
        int old = choice[v];
        if (old == target) continue;
        int delta = 0;
        for (int k : incidence[v][old])
          delta += penalty(cons[k], cons[k].count - 1) - penalty(cons[k], cons[k].count);
        for (int k : incidence[v][target])
          delta += penalty(cons[k], cons[k].count + 1) - penalty(cons[k], cons[k].count);
        if (delta < best_delta) { best_delta = delta; moves.clear(); }
        if (delta == best_delta) moves.push_back({delta,v,target});
      }
      Move move;
      // WalkSAT noise: one eighth of the time use a random repairing move.
      if ((rng() & 7) == 0) {
        auto [v,target] = selected.items[rng() % selected.items.size()];
        while (choice[v] == target) {
          auto item = selected.items[rng() % selected.items.size()];
          v = item.first; target = item.second;
        }
        move = {0,v,target};
      } else {
        move = moves[rng() % moves.size()];
      }
      int v = move.v, old = choice[v], target = move.target;
      // Compute the exact delta even for a noisy move.
      int delta = 0;
      for (int k : incidence[v][old])
        delta += penalty(cons[k], cons[k].count - 1) - penalty(cons[k], cons[k].count);
      for (int k : incidence[v][target])
        delta += penalty(cons[k], cons[k].count + 1) - penalty(cons[k], cons[k].count);
      for (int k : incidence[v][old]) --cons[k].count;
      for (int k : incidence[v][target]) ++cons[k].count;
      choice[v] = target;
      objective += delta;

      if (objective < global_best) {
        global_best = objective;
        best_choice = choice;
        std::cerr << "best " << global_best << " restart " << restart
                  << " step " << step << "\n";
      }
    }
    if (objective == 0) {
      std::cout << "s SATISFIABLE\nchoices";
      for (int x : choice) std::cout << ' ' << x;
      std::cout << "\n";
      return 0;
    }
  }
  std::cout << "s UNKNOWN\nbest_penalty " << global_best << "\nchoices";
  for (int x : best_choice) std::cout << ' ' << x;
  std::cout << "\n";
  return 1;
}
