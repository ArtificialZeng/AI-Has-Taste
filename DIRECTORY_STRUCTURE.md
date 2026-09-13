# Local GitHub staging directory / 本地待确认目录

Prepared 2026-09-13. Nothing has been uploaded, pushed or submitted. The research queue remains paused.

**Local copy versus Git distribution:** This document describes the complete local directory. The pre-existing [.gitignore](.gitignore) and [upload policy](UPLOAD_GUIDE.md) exclude manuscript LaTeX, including `.tex`/`.bib` copies in reproduction bundles. Those rules were not changed by the BigMac2 addition. Local LaTeX links and successful local builds do not mean those files will exist in a Git clone. Review that policy before publishing a source-complete archive; do not force-add ignored files implicitly.

**本地完整包与上传范围不同：** 原有 Git 规则仍排除 LaTeX。本次已在本地配齐55套源码，但没有更改该上传策略。仅按当前规则上传，GitHub 不会包含这些 LaTeX；671个科学复现输入均不受该排除规则影响。完整本地清单与 Git 分发清单的范围不同。

Local review only / 仅本地审阅：[55套 LaTeX 完整源码](latex_source_code/BigMac2/) · [55套复现材料](reproducible_source_code/BigMac2/)。前一链接指向 Git 忽略的本地目录，不是上传承诺。

**230 distinct cataloged manuscripts / 1,250 pages.** This update adds **55 BigMac2 PDFs / 233 pages** and matching source packages to the existing 175-paper repository. It is not a claim that 230 parent problems were solved.

本次核对当前会话60份有效发布稿：55份新增；5份与仓库现有Smallmac结果重复，保留现有规范版本并登记对应关系。43个已派发但未有有效发布稿的项目、219个仅摄取记录不虚构PDF。所有原有175份PDF和BigMac1源码保持原样。

## Complete directory layout / 完整目录层级

```text
AI-Has-Taste/
├── README.md                  current English catalog
├── README.zh-CN.md             current Chinese catalog
├── README.{fr,ru,de,ja}.md     prior 175-paper language snapshot
├── DIRECTORY_STRUCTURE.md
├── archive-manifest.json
├── assets/
│   ├── BigMac1/                existing provenance retained
│   └── BigMac2/                catalog, gates, checks, dedup, hashes
├── pdfs/
│   ├── smallmac_1/             17 existing PDFs
│   ├── smallmac_2/             116 existing PDFs
│   ├── ai-conjectures/         1 existing PDF
│   ├── BigMac1/                41 existing final PDFs
│   └── BigMac2/                55 new final PDFs (flat directory)
├── latex_source_code/
│   ├── BigMac1/                existing local manuscript sources
│   └── BigMac2/
│       ├── build.py
│       └── BM2-BNN-PNN/
│           ├── README.md
│           └── source/        complete declared publication inputs
└── reproducible_source_code/
    ├── BigMac1/                existing sources; concurrent notes retained
    └── BigMac2/
        ├── prepare.py
        ├── REPRODUCTION_NOTES.md
        └── BM2-BNN-PNN/
            ├── README.md
            ├── package.json
            ├── requirements.txt  where external imports were detected
            └── source/           original relative layout; large data .gz
```

[All repository file paths / 全部仓库文件路径](assets/BigMac2/file-tree.txt) · [English catalog](README.md#bigmac2) · [中文目录](README.zh-CN.md#bigmac2) · [Reproduction instructions](reproducible_source_code/BigMac2/REPRODUCTION_NOTES.md)

The existing [BigMac1 directory document](assets/BigMac1/DIRECTORY_STRUCTURE.snapshot.md) and `assets/BigMac1/file-tree.txt` are historical snapshots, not current whole-repository counts.

## Naming and source pairing / 编号与配套关系

`bigMac-00024-p02` → `BM2-B24-P02`. The prefix BM2 identifies this conversation; B24 and P02 retain the actual batch and problem number. Missing numbers are intentional (no release or duplicate), not silently renumbered.

Each PDF has one matching LaTeX package and one source/evidence package. The five excluded BigMac2 drafts are not paired with the LaTeX of a different Smallmac paper. Their release hashes and gate provenance are retained in assets/BigMac2/gates/.

| Batch | New PDFs |
|---|---:|
| B03 | 2 |
| B04 | 3 |
| B05 | 2 |
| B06 | 2 |
| B07 | 3 |
| B08 | 2 |
| B09 | 1 |
| B10 | 2 |
| B11 | 4 |
| B12 | 2 |
| B13 | 1 |
| B14 | 3 |
| B15 | 2 |
| B16 | 1 |
| B17 | 1 |
| B18 | 1 |
| B19 | 2 |
| B20 | 2 |
| B21 | 1 |
| B22 | 3 |
| B23 | 1 |
| B24 | 2 |
| B25 | 2 |
| B26 | 3 |
| B27 | 4 |
| B28 | 1 |
| B29 | 2 |

## All new PDF filenames / 新增PDF完整文件名

```text
pdfs/BigMac2/
BM2-B03-P01_A_Fixed_Periodic_Bound_for_Signed_Affine_Copies_of_0_1_3.pdf
BM2-B03-P02_Attained_Three_Point_Moment_Selection_for_Five_Labels_with_Direction_Multiplicities_3_1_1.pdf
BM2-B04-P01_The_Six_Point_Type_II_Bounded_Ratio_on_Its_Symmetric_Locus_and_Two_Exact_Obstructions.pdf
BM2-B04-P02_Strict_Positive_Square_Energy_for_Two_Connected_Noncycle_Graphs.pdf
BM2-B04-P03_Exact_Maximum_Loneliness_in_the_Family_1_4_5_6_7_m.pdf
BM2-B05-P02_Exact_Fractional_Hamiltonicity_on_the_Branch_J_m_1.pdf
BM2-B05-P04_The_Cohen_Macaulay_Classification_for_Increasing_Injection_Chains_of_Cycle_Edge_Ideals.pdf
BM2-B06-P03_An_Exact_Counterexample_to_a_Modulo_Five_Congruence_for_b24_4.pdf
BM2-B06-P04_A_Product_Formula_and_All_Degree_Positivity_for_the_6_0_1_Core_Bipartition_Series.pdf
BM2-B07-P01_Pure_Periodicity_for_the_Three_Move_Subtraction_Games_2_5_c.pdf
BM2-B07-P02_The_Complete_Two_Weight_Z_5Z_GoemansLinial_Cone.pdf
BM2-B07-P04_Exact_Verification_of_the_Kasami_Cyclic_Additive_Identity_at_n_14.pdf
BM2-B08-P02_Time_Eight_Positive_Sojourn_Classification_for_Arbitrary_Two_State_Unitary_Coins.pdf
BM2-B08-P04_A_Degree_Four_Boundary_for_the_v_Number_under_Integral_Closure.pdf
BM2-B09-P03_The_Exact_Uniform_Scrambling_Horizon_of_the_Order_Four_Almost_Sarymsakov_Class_Is_Eleven.pdf
BM2-B10-P02_Sharp_Consensus_Time_Asymptotics_for_a_Degenerate_Monotone_Aggregation_Rule.pdf
BM2-B10-P03_Inverse_Weight_LinLuYau_Curvature_on_a_Weighted_Triangle_Exact_Interior_Fixed_Points_and_a_Nonuniform_Stationary_Metric.pdf
BM2-B11-P01_Active_Grade_Six_Exclusion_for_Restart_Four_Conjugate_Gradients.pdf
BM2-B11-P02_Polyregular_Classification_of_Additive_Level_Sorts_with_Coprime_Weights_of_Absolute_Value_at_Most_Two.pdf
BM2-B11-P03_The_independent_row_K_2_2_molecular_species_product.pdf
BM2-B11-P04_Sign_Reversal_and_the_Exact_Zero_Set_for_the_Covariance_of_Competing_Bulk_and_Surface_Stopping_in_the_Three_Ball.pdf
BM2-B12-P02_An_Exact_Type_D4_Alternating_Normal_Form_and_Condition_A_for_All_Garside_Powers.pdf
BM2-B12-P04_A_Sharp_Logarithmic_Almost_Sure_Threshold_for_a_Critical_Two_Step_Pearson_Walk.pdf
BM2-B13-P03_The_Exact_Lipschitz_Constant_for_an_Absolute_Value_Exponential_Tilt_of_the_Gaussian.pdf
BM2-B14-P01_Exact_Invertibility_Probability_for_Binary_Matrices_with_Two_Ones_in_Every_Row_and_Column.pdf
BM2-B14-P02_Fixed_Sticky_Refreshing_Preserves_the_Exponent_Two_Degree_Laws_in_Range_Renewal_Networks.pdf
BM2-B14-P04_The_Exact_Relative_Dimension_of_the_Three_Dimensional_Boolean_Lattice.pdf
BM2-B15-P01_Exact_Joint_ANF_Leap_for_Raw_Finite_Field_Inversion.pdf
BM2-B15-P02_Critical_First_Sign_Failure_of_Even_Cumulants_for_the_BlumeCapel_Single_Site_Law.pdf
BM2-B16-P02_Exact_Homological_Invariants_for_Closed_Neighborhood_Ideals_of_Cubes_of_Broom_Graphs.pdf
BM2-B17-P01_The_Grid_Traffic_Threshold_A_Proof_for_Every_n_496.pdf
BM2-B18-P03_The_Three_Halves_Endpoint_Remainder_for_a_Truncated_Gaussian_Heat_Kernel.pdf
BM2-B19-P02_Power_of_Two_Cycles_in_24_Vertex_Graphs_with_Degree_Sequence_5_followed_by_23_threes.pdf
BM2-B19-P03_An_Exact_Weighted_Cycle_Obstruction_for_the_812_Vertex_AGL_1_29_Orientation_Instance.pdf
BM2-B20-P01_A_Three_Dimensional_Counterexample_to_a_Split_Ideal_Question.pdf
BM2-B20-P03_Three_Probes_Suffice_for_Directional_Localization_on_the_Three_Cube.pdf
BM2-B21-P05_The_Majority_C_Chromatic_Number_of_K3_square_K3_square_K3.pdf
BM2-B22-P01_The_Sharp_Queried_Gradient_Constant_of_Nesterov_s_Fast_Gradient_Method_at_Horizon_Two.pdf
BM2-B22-P03_The_d_4_Hypercube_Inequality_on_Supports_of_Size_at_Most_Five.pdf
BM2-B22-P04_Integral_Homology_of_Singleton_Anchor_Configuration_Spaces_of_Finite_Graphs.pdf
BM2-B23-P06_An_Exact_Computer_Assisted_Perfectness_Census_for_Integral_Circulant_Graphs_Through_Order_32.pdf
BM2-B24-P01_Convergence_of_Chebyshevs_Method_for_z_z181.pdf
BM2-B24-P02_The_Exact_Minimax_Two_Step_Schedule_for_Smooth_Convex_Gradient_Descent.pdf
BM2-B25-P01_Nonexistence_of_a_Four_Layer_Balanced_Hamilton_Starter_in_Cay_Z12_1_2_3.pdf
BM2-B25-P03_Cross_part_rainbow_near_perfect_matchings_in_the_nine_element_affine_plane_an_exact_finite_proof.pdf
BM2-B26-P02_Fixed_Start_Cover_Times_Change_Under_Every_Edge_Addition_on_Connected_Cyclic_Graphs_of_Order_Eight.pdf
BM2-B26-P03_The_Weak_EKR_Difference_Set_Condition_for_Irreducible_Subgroups_of_GL_3_2.pdf
BM2-B26-P04_An_Explicit_13_Vertex_Graph_with_No_Edgeless_Five_Vertex_Vertex_Minor.pdf
BM2-B27-P01_Entropy_Concavity_for_All_Three_Bit_Overlap_Bernoulli_Distributions.pdf
BM2-B27-P02_The_Three_Neighbor_Percolation_Number_of_the_8_by_8_Torus.pdf
BM2-B27-P03_No_Weak_Abelian_Square_of_Total_Length_at_Most_2745_in_a_Proposed_Five_Letter_Cyclic_Morphic_Word.pdf
BM2-B27-P04_Regular_Distance_Magic_Graphs_on_Eight_Vertices_and_Generating_F2_Cubed_Magic_Maps.pdf
BM2-B28-P04_The_Exact_Label_Realization_Radius_nu_4_4.pdf
BM2-B29-P01_Exact_Rational_Certificates_for_the_Reverse_LCDLP_Comparison_at_20_8.pdf
BM2-B29-P13_The_Least_Residue_Choice_Incompatibility_Layer_for_Finite_Survivor_Sets_A_Complete_Classification.pdf
```

## Canonical duplicate mapping / 重复稿对应表

| Excluded BigMac2 draft | Existing canonical PDF | Reason |
|---|---|---|
| BM2-B02-P11 | [SM2-P01](pdfs/smallmac_2/SM2-P01_No_Centrally_Symmetric_Hexagon_Attains_the_Planar_L2_RogersShephard_Bound.pdf) | Same strict planar L2 centrally symmetric hexagon theorem; no wider contribution. |
| BM2-B07-P03 | [SM2-P47](pdfs/smallmac_2/SM2-P47_Minimum_order_of_a_connected_cubic_bipartite_graph_with_bondage_number_five.pdf) | Same cubic bipartite bondage census through order 16; the existing paper also checks the order-18 witness. |
| BM2-B09-P01 | [SM2-P81](pdfs/smallmac_2/SM2-P81_A_cubic_graph_on_sixteen_vertices_without_an_equitable_four_total_coloring.pdf) | Same order-16 type-1 cubic total-colouring counterexample; graph6 witnesses are exactly isomorphic. |
| BM2-B09-P02 | [SM2-P84](pdfs/smallmac_2/SM2-P84_Nonexistence_of_invertible_cross_product_twists_for_gl2_F_FI_in_characteristic_two.pdf) | Same characteristic-two rank obstruction to the twisted cross-product model. |
| BM2-B29-P03 | [SM2-P93](pdfs/smallmac_2/SM2-P93_Eulerian_orientations_of_separable_4_regular_graphs_on_sixteen_vertices.pdf) | Same order-16 separable Eulerian-orientation maximum 9216 and unique extremal isomorphism class. |

## Local packaging checks / 本地检查

- All 60 original active releases passed the current installed gate validation against evidence, source, PDF and audit hashes. This reused historical mathematical/visual audits of unchanged PDFs; it is not new peer review.
- Original files, review role IDs and final PDF bytes are not rewritten. Five semantic duplicates are documented; no old PDF was deleted.
- Source preservation, clean LaTeX builds and short computational replays are separate checks. See the per-package README and machine-readable check records for exact scope.
- Gzip is lossless, not an omitted-data placeholder. prepare.py verifies both stored bytes and the restored original digest. Machine-specific executables and environments are not redistributed.
- Only English and Chinese README catalogs were updated. Other language editions retain the previous snapshot and are labeled as such in the current pages.
- Concurrent BigMac1 documentation and Git-distribution metadata changes were preserved, not reverted to the initial packaging snapshot. Existing PDF and scientific-source bytes were not changed by this addition.
- The reported `operatorname` issue is already repaired in the staged EN/ZH original: the permanent uses `\mathrm{per}`. That GitHub-safe expression remains intact; no error text is embedded.

Please review this folder before publishing. This task performs no GitHub mutation.
