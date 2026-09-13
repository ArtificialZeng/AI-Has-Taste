# BigMac1 — local review directory / 本地待确认目录

Prepared 2026-09-13. Nothing has been uploaded or pushed. The original download and research directories remain untouched.

本次只收入当前会话可确认历史投稿门控的 **41 份独立最终文稿、280 页**；同一课题只保留一个合格终版。不是 41 个母题全解，也不是本轮重新进行数学审稿。

## Directory hierarchy / 目录层级

```text
AI-Has-Taste/
├── README.md + five translated editions
├── archive-manifest.json
├── DIRECTORY_STRUCTURE.md
├── assets/BigMac1/
│   ├── catalog.json
│   ├── exclusions.json
│   ├── package-manifest.json
│   ├── gates/<paper-id>/
│   └── file-tree.txt
├── pdfs/
│   ├── smallmac_1/       17 original PDFs, unchanged
│   ├── smallmac_2/       116 original PDFs, unchanged
│   ├── ai-conjectures/   1 original PDF, unchanged
│   └── BigMac1/         41 final PDFs, flat directory
├── latex_source_code/BigMac1/<paper-id>/
│   ├── README.md
│   └── source/
└── reproducible_source_code/BigMac1/<paper-id>/
    ├── README.md
    └── source/
```

[Every repository file / 全部文件路径](assets/BigMac1/file-tree.txt) · [PDF / LaTeX / code links](README.zh-CN.md#bigmac1)

## Stable IDs and counts

| Source batch label | Included PDFs |
|---|---:|
| `BM1-MATH15` | 1 |
| `BM1-AI15` | 10 |
| `BM1-AF03` | 12 |
| `BM1-AF04` | 7 |
| `BM1-DM01` | 2 |
| `BM1-MAN` | 9 |

The original batch identities are preserved; missing problem numbers are intentional exclusions, not missing copies. `BM1-MAN` is a documented manual-topic sequence, not a fabricated original batch.

## All 41 PDF filenames

```text
pdfs/BigMac1/
├── BM1-MATH15-P13_The_small_Ramsey_degree_of_an_edge_in_ordered_split_graphs_is_three.pdf
├── BM1-AI15-P01_A_Rational_Rank_2_2_Hadamard_Factorization_of_a_Proposed_4x4_Real_Counterexample.pdf
├── BM1-AI15-P02_An_Exact_Transfer_Matrix_Proof_of_Barker_s_Order_Ten_Recurrence_for_OEIS_A321614.pdf
├── BM1-AI15-P03_The_proper_three_colouring_zero_set_of_generalized_chorded_cycles_is_7_8_12_16.pdf
├── BM1-AI15-P05_A_Strict_Certified_Search_Extension_for_Erdos_Problem_647.pdf
├── BM1-AI15-P06_Eleven_equilateral_points_in_five_dimensional_ell_one_require_at_least_nineteen_coordinate_gaps.pdf
├── BM1-AI15-P07_A_certified_finite_verification_of_ErdosSzekeres_699_for_i_3_and_n_at_most_100_million.pdf
├── BM1-AI15-P08_The_Sheil_Small_covering_problem_for_self_inversive_polynomials_in_degrees_two_and_three.pdf
├── BM1-AI15-P11_Tree_independence_sequences_are_unimodal_through_order_31.pdf
├── BM1-AI15-P12_The_Rank_Two_Marcus_Permanent_Inequality_for_Real_3_by_3_Matrices.pdf
├── BM1-AI15-P13_A_Fixed_Point_Counterexample_to_Condition_Number_Only_Stability_of_ShermanMorrison_Iterative_Refinement.pdf
├── BM1-AF03-P01_A_Sharp_3_Degree_ErdosKoRado_Theorem_for_4_Uniform_Families.pdf
├── BM1-AF03-P03_The_n_5_case_of_Lentfer_s_1_2_bosonic_fermionic_coinvariant_basis_conjecture.pdf
├── BM1-AF03-P04_The_transitive_array_conjecture_for_the_classical_YangBaxter_equation.pdf
├── BM1-AF03-P05_Exact_finite_certification_of_the_sparse_complement_two_eigenvalue_conjecture_at_order_nine.pdf
├── BM1-AF03-P07_The_K_Knuth_Shape_Interval_Conjecture_Holds_on_Alphabets_of_Size_at_Most_Eight_An_Exact_Finite_Certification.pdf
├── BM1-AF03-P08_The_n_10_Case_of_a_q_Fibonacci_Product_Conjecture_for_KazhdanLusztig_R_Polynomials.pdf
├── BM1-AF03-P10_Generic_LotkaVolterra_Tree_Systems_Determine_Their_Trees.pdf
├── BM1-AF03-P11_A_Certified_n_7_Case_of_a_Generalized_Stack_Sorting_Enumeration_Conjecture.pdf
├── BM1-AF03-P12_Stability_of_3_Packed_Words_in_the_Plactic_Monoid.pdf
├── BM1-AF03-P13_Exact_counterexamples_to_an_Ehrhart_root_disk_conjecture_for_generalized_snake_posets.pdf
├── BM1-AF03-P14_Local_extrema_of_central_hyperplane_sections_of_the_five_dimensional_cube.pdf
├── BM1-AF03-P15_A_certified_normalized_flow_for_the_absolute_order_of_type_D9.pdf
├── BM1-AF04-P01_Proof_of_the_Four_Step_D_Finite_Recurrence_for_OEIS_A278992.pdf
├── BM1-AF04-P02_The_Pasch_switch_quotient_graph_of_STS_15_has_diameter_11.pdf
├── BM1-AF04-P03_The_Largest_Cyclic_3_31_5_1_Packing_Has_Twelve_Base_Block_Orbits.pdf
├── BM1-AF04-P06_Two_weight_twenty_affine_orbits_of_minimal_vanishing_sums_of_distinct_105th_roots.pdf
├── BM1-AF04-P07_A_certified_determination_of_nu3_11_15_for_arc_disjoint_transitive_triples_in_tournaments.pdf
├── BM1-AF04-P10_Certified_radius_seven_exchange_rigidity_for_a_binary_subspace_code.pdf
├── BM1-AF04-P15_A_Certified_Finite_Census_for_Additive_Square_Free_Words_on_Four_Letter_Integer_Alphabets_of_Height_at_Most_Five.pdf
├── BM1-DM01-P13_Proof_of_a_Square_Endpoint_Supercongruence_for_Central_Binomial_Cubes.pdf
├── BM1-DM01-P15_Proved_179_Occurs_in_the_Factorial_GCD_Sequence_of_Harmonic_Numerators.pdf
├── BM1-MAN-P01_The_BapatSunder_Permanental_Minor_Matrix_on_Regular_Real_Projective_Polygons.pdf
├── BM1-MAN-P02_Sharp_RankOrder_Bounds_for_Reduced_Rank_Ten_Graphs_with_Sparse_Nonsingular_Cores.pdf
├── BM1-MAN-P03_Exact_finite_certificates_for_the_four_dimensional_ternary_Borsuk_problem_and_five_dimensional_ternary_kissing_codes.pdf
├── BM1-MAN-P04_Repeated_summands_in_Euler_s_sixth_power_equation.pdf
├── BM1-MAN-P05_An_Exponent_One_Obstruction_and_a_95_102_Local_Sieve_for_a_Lenhart_Attributed_Family_of_Euler_Bricks.pdf
├── BM1-MAN-P06_One_Sided_Parity_Compression_for_Certified_SAT_Attacks_on_the_33_Point_ErdosSzekeres_Problem.pdf
├── BM1-MAN-P07_A_Finite_Prime_Set_Exclusion_and_an_Odd_Modular_Obstruction_in_Lehmer_s_Totient_Problem.pdf
├── BM1-MAN-P08_Integer_Floor_Lifting_for_Frankl_Complete_Uniform_Configurations.pdf
└── BM1-MAN-P09_Exact_stitched_sheet_local_box_and_complex_phase_tube_positivity_for_a_Hermitian_rank_two_scalar_gate.pdf
```

## Topic/version decisions

- Borsuk and kissing records share one joint paper: **BM1-MAN-P03**, included once.
- Fixed crossing lens: **BM1-MAN-P09** is the final 42-page v18 submission manuscript. Later V22 checkpoint labels are research checkpoints, not later PDF versions.
- Reduced rank-ten graphs: **BM1-MAN-P02** is the final sparse-core manuscript, replacing the earlier narrower tree-core version.
- Lehmer: **BM1-MAN-P07** uses the final round-2 manuscript. The similarly named existing “Lehmer-signature” permutation paper is a different problem.
- **BM1-MAN-P08** and existing **SM1-P15** share Frankl’s parent problem, but prove different restricted statements. They are related topics, not duplicate manuscript versions; both are retained with this distinction.
- Existing Smallmac topics and PDF bytes are preserved. Cross-collection parent-problem overlap is not mislabeled as a new global resolution.

## Holds and exclusions

[60 exclusion / merge records](assets/BigMac1/exclusions.json) cover the 101 executed/manual candidate rows. Capture-only problem lists without manuscript assets are not treated as PDF candidates.

- MATH15 P07 and P12: historical submission PASS exists, but an explicit post-final second novelty check could not be confirmed. Held out conservatively; this does not assert mathematical falsity.
- BPSW: only a process/report artifact was cleared, not a submission-ready paper.
- DM02 P10/P11: mathematical records exist but release gates are blocked; no PDF included.
- Open/no-paper projects, unapproved drafts, and superseded duplicates are not included.

## Reproduction limitations to read before publishing

- AI15 P11: omitted old binaries and upstream nauty tarball prevent original aggregate wrappers from running unchanged. Source and census records remain; full reproduction needs pinned upstream acquisition and local compilation/adaptation.
- AF04 P03: 162 stored graphs (about 2.09 GB) and old executable are omitted. Code and branch records are included, but this is not a self-contained immediate replay of the full negative certificate.
- MAN P06 (ES7): small ES5 certificate data are included; about 1.41 GB of ES6 traces and external checker binaries are not. Encoding/count checks differ from full trace verification.
- Other exact computations have not all been rerun in this packaging task. Read each package README and the historical audits.

## Review and merge

This is a complete review copy, including the original 134 PDFs plus the 41 BigMac1 additions (175 total). Review `README.zh-CN.md`, the source-package notes, and exclusions first. On approval, the user can merge `pdfs/BigMac1/`, `latex_source_code/`, `reproducible_source_code/`, `assets/BigMac1/`, all six READMEs, `DIRECTORY_STRUCTURE.md`, and `archive-manifest.json`. No GitHub publication is performed by this task.
