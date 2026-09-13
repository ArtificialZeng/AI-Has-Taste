#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

#include "Highs.h"

int main(int argc, char** argv) {
  if (argc != 3) {
    std::cerr << "usage: extract_lp_dual_ray INSTANCE OUTPUT\n";
    return 2;
  }
  std::ifstream in(argv[1]);
  int n, m; in >> n >> m;
  const int ncol = 3 * n, nrow = n + m;
  std::vector<std::vector<int>> col_rows(ncol);
  for (int v = 0; v < n; ++v)
    for (int t = 0; t < 3; ++t) col_rows[3*v+t].push_back(v);
  std::vector<double> row_lower(nrow), row_upper(nrow);
  for (int v = 0; v < n; ++v) row_lower[v] = row_upper[v] = 1.0;
  for (int cid = 0; cid < m; ++cid) {
    int req, len; in >> req >> len;
    row_lower[n+cid] = req;
    row_upper[n+cid] = kHighsInf;
    for (int i = 0; i < len; ++i) {
      int v,t; in >> v >> t;
      col_rows[3*v+t].push_back(n+cid);
    }
  }

  HighsLp lp;
  lp.num_col_ = ncol;
  lp.num_row_ = nrow;
  lp.col_cost_.assign(ncol, 0.0);
  lp.col_lower_.assign(ncol, 0.0);
  lp.col_upper_.assign(ncol, 1.0);
  lp.row_lower_ = row_lower;
  lp.row_upper_ = row_upper;
  lp.a_matrix_.format_ = MatrixFormat::kColwise;
  lp.a_matrix_.start_.reserve(ncol + 1);
  for (int col = 0; col < ncol; ++col) {
    lp.a_matrix_.start_.push_back(lp.a_matrix_.index_.size());
    for (int row : col_rows[col]) {
      lp.a_matrix_.index_.push_back(row);
      lp.a_matrix_.value_.push_back(1.0);
    }
  }
  lp.a_matrix_.start_.push_back(lp.a_matrix_.index_.size());

  Highs highs;
  highs.setOptionValue("output_flag", false);
  highs.setOptionValue("presolve", "off");
  highs.setOptionValue("solver", "simplex");
  if (highs.passModel(std::move(lp)) != HighsStatus::kOk) return 3;
  if (highs.run() == HighsStatus::kError) return 4;
  std::cerr << "model_status " << highs.modelStatusToString(highs.getModelStatus()) << "\n";
  if (highs.getModelStatus() != HighsModelStatus::kInfeasible) return 5;
  bool has_ray = false;
  std::vector<double> ray(nrow);
  if (highs.getDualRay(has_ray, ray.data()) != HighsStatus::kOk || !has_ray) return 6;
  std::ofstream out(argv[2]);
  out << "dual_ray_v1 " << n << ' ' << m << "\n" << std::setprecision(17);
  for (int row = 0; row < nrow; ++row)
    if (ray[row] != 0.0) out << row << ' ' << ray[row] << "\n";
  return 0;
}
