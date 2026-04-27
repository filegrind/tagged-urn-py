# Python Test Catalog

**Total Tests:** 95

**Numbered Tests:** 18

**Unnumbered Tests:** 77

**Numbered Tests Missing Descriptions:** 0

**Numbering Mismatches:** 0

All numbered test numbers are unique.

This catalog lists all tests in the Python codebase.

| Test # | Function Name | Description | File |
|--------|---------------|-------------|------|
| test578 | `test_578_equivalent_identical_tags` | TEST578: Equivalent URNs with identical tag sets | tests/test_tagged_urn.py:1073 |
| test579 | `test_579_not_equivalent_when_one_more_specific` | TEST579: Non-equivalent URNs where one is more specific | tests/test_tagged_urn.py:1081 |
| test580 | `test_580_comparable_specialization_chain` | TEST580: Comparable URNs on the same specialization chain | tests/test_tagged_urn.py:1089 |
| test581 | `test_581_incomparable_different_branches` | TEST581: Incomparable URNs in different branches of the lattice | tests/test_tagged_urn.py:1100 |
| test582 | `test_582_equivalent_implies_comparable` | TEST582: Equivalent implies comparable but not vice versa | tests/test_tagged_urn.py:1111 |
| test583 | `test_583_prefix_mismatch_errors` | TEST583: Prefix mismatch raises error for both relations | tests/test_tagged_urn.py:1126 |
| test584 | `test_584_empty_tags_comparable_to_all` | TEST584: Empty tag set is comparable to everything with same prefix | tests/test_tagged_urn.py:1136 |
| test585 | `test_585_string_variants` | TEST585: String variants of is_equivalent and is_comparable | tests/test_tagged_urn.py:1149 |
| test586 | `test_586_special_values` | TEST586: Special values (*, !, ?) with is_equivalent and is_comparable | tests/test_tagged_urn.py:1158 |
| test587 | `test_587_builder_fluent_api` | TEST587: Builder fluent API for tag manipulation | tests/test_tagged_urn.py:1188 |
| test588 | `test_588_builder_custom_tags` | TEST588: Builder with custom tags | tests/test_tagged_urn.py:1203 |
| test589 | `test_589_builder_tag_overrides` | TEST589: Builder tag overrides (last value wins) | tests/test_tagged_urn.py:1216 |
| test590 | `test_590_builder_empty_build` | TEST590: Builder empty build raises error (tags required) | tests/test_tagged_urn.py:1227 |
| test591 | `test_591_builder_single_tag` | TEST591: Builder with single tag | tests/test_tagged_urn.py:1234 |
| test592 | `test_592_builder_complex` | TEST592: Builder with complex multi-tag URN | tests/test_tagged_urn.py:1244 |
| test593 | `test_593_builder_wildcards` | TEST593: Builder with wildcards | tests/test_tagged_urn.py:1270 |
| test594 | `test_594_builder_custom_prefix` | TEST594: Builder with custom prefix | tests/test_tagged_urn.py:1288 |
| test595 | `test_595_builder_matching_with_built_urn` | TEST595: Builder matching with built URN | tests/test_tagged_urn.py:1296 |
| | | | |
| unnumbered | `test_best_match` |  | tests/test_tagged_urn.py:353 |
| unnumbered | `test_builder` |  | tests/test_tagged_urn.py:310 |
| unnumbered | `test_builder_preserves_case` |  | tests/test_tagged_urn.py:322 |
| unnumbered | `test_builder_rejects_empty_value` |  | tests/test_tagged_urn.py:504 |
| unnumbered | `test_builder_with_prefix` |  | tests/test_tagged_urn.py:42 |
| unnumbered | `test_canonical_string_format` |  | tests/test_tagged_urn.py:218 |
| unnumbered | `test_compatibility` |  | tests/test_tagged_urn.py:331 |
| unnumbered | `test_compatibility_with_special_values` |  | tests/test_tagged_urn.py:1001 |
| unnumbered | `test_custom_prefix` |  | tests/test_tagged_urn.py:13 |
| unnumbered | `test_duplicate_key_rejection` |  | tests/test_tagged_urn.py:453 |
| unnumbered | `test_empty_tagged_urn` |  | tests/test_tagged_urn.py:401 |
| unnumbered | `test_empty_value_error` |  | tests/test_tagged_urn.py:471 |
| unnumbered | `test_empty_value_still_error` |  | tests/test_tagged_urn.py:775 |
| unnumbered | `test_empty_with_custom_prefix` |  | tests/test_tagged_urn.py:429 |
| unnumbered | `test_extended_character_support` |  | tests/test_tagged_urn.py:436 |
| unnumbered | `test_full_cross_product_matching` |  | tests/test_tagged_urn.py:917 |
| unnumbered | `test_has_tag_case_sensitive` |  | tests/test_tagged_urn.py:478 |
| unnumbered | `test_invalid_escape_sequence_error` |  | tests/test_tagged_urn.py:124 |
| unnumbered | `test_matching_case_sensitive_values` |  | tests/test_tagged_urn.py:245 |
| unnumbered | `test_matching_different_prefixes_error` |  | tests/test_tagged_urn.py:645 |
| unnumbered | `test_matching_semantics_test1_exact_match` | MATCHING SEMANTICS SPECIFICATION TESTS These 9 tests verify the exact matching semantics from RULES.md Sections 12-17 All implementations (Rust, Go, JS, ObjC) must pass these identically | tests/test_tagged_urn.py:527 |
| unnumbered | `test_matching_semantics_test2_instance_missing_tag` |  | tests/test_tagged_urn.py:537 |
| unnumbered | `test_matching_semantics_test3_urn_has_extra_tag` |  | tests/test_tagged_urn.py:554 |
| unnumbered | `test_matching_semantics_test4_request_has_wildcard` |  | tests/test_tagged_urn.py:564 |
| unnumbered | `test_matching_semantics_test5_urn_has_wildcard` |  | tests/test_tagged_urn.py:574 |
| unnumbered | `test_matching_semantics_test6_value_mismatch` |  | tests/test_tagged_urn.py:584 |
| unnumbered | `test_matching_semantics_test7_pattern_has_extra_tag` |  | tests/test_tagged_urn.py:594 |
| unnumbered | `test_matching_semantics_test8_empty_pattern_matches_anything` |  | tests/test_tagged_urn.py:610 |
| unnumbered | `test_matching_semantics_test9_cross_dimension_constraints` |  | tests/test_tagged_urn.py:628 |
| unnumbered | `test_merge_and_subset` |  | tests/test_tagged_urn.py:368 |
| unnumbered | `test_merge_prefix_mismatch` |  | tests/test_tagged_urn.py:380 |
| unnumbered | `test_missing_tag_handling` |  | tests/test_tagged_urn.py:257 |
| unnumbered | `test_mixed_quoted_unquoted` |  | tests/test_tagged_urn.py:113 |
| unnumbered | `test_mixed_special_values` |  | tests/test_tagged_urn.py:964 |
| unnumbered | `test_must_not_have_exclamation_parsing` |  | tests/test_tagged_urn.py:843 |
| unnumbered | `test_must_not_have_in_instance` |  | tests/test_tagged_urn.py:900 |
| unnumbered | `test_must_not_have_pattern_requires_absent` |  | tests/test_tagged_urn.py:885 |
| unnumbered | `test_numeric_key_restriction` |  | tests/test_tagged_urn.py:458 |
| unnumbered | `test_prefix_case_insensitive` |  | tests/test_tagged_urn.py:20 |
| unnumbered | `test_prefix_mismatch_error` |  | tests/test_tagged_urn.py:32 |
| unnumbered | `test_prefix_required` |  | tests/test_tagged_urn.py:185 |
| unnumbered | `test_question_mark_in_instance` |  | tests/test_tagged_urn.py:868 |
| unnumbered | `test_question_mark_pattern_matches_anything` |  | tests/test_tagged_urn.py:851 |
| unnumbered | `test_quoted_value_escape_sequences` |  | tests/test_tagged_urn.py:99 |
| unnumbered | `test_quoted_value_special_chars` |  | tests/test_tagged_urn.py:85 |
| unnumbered | `test_quoted_values_preserve_case` |  | tests/test_tagged_urn.py:68 |
| unnumbered | `test_round_trip_escapes` |  | tests/test_tagged_urn.py:176 |
| unnumbered | `test_round_trip_quoted` |  | tests/test_tagged_urn.py:167 |
| unnumbered | `test_round_trip_simple` |  | tests/test_tagged_urn.py:159 |
| unnumbered | `test_semantic_equivalence` |  | tests/test_tagged_urn.py:510 |
| unnumbered | `test_serialization_round_trip_special_values` |  | tests/test_tagged_urn.py:985 |
| unnumbered | `test_serialization_smart_quoting` |  | tests/test_tagged_urn.py:133 |
| unnumbered | `test_specificity` |  | tests/test_tagged_urn.py:283 |
| unnumbered | `test_specificity_with_special_values` |  | tests/test_tagged_urn.py:1046 |
| unnumbered | `test_tag_matching` |  | tests/test_tagged_urn.py:225 |
| unnumbered | `test_tagged_urn_creation` |  | tests/test_tagged_urn.py:5 |
| unnumbered | `test_trailing_semicolon_equivalence` |  | tests/test_tagged_urn.py:199 |
| unnumbered | `test_unquoted_values_lowercased` |  | tests/test_tagged_urn.py:49 |
| unnumbered | `test_unspecified_question_mark_parsing` | NEW SEMANTICS TESTS: ? (unspecified) and ! (must-not-have) | tests/test_tagged_urn.py:835 |
| unnumbered | `test_unterminated_quote_error` |  | tests/test_tagged_urn.py:119 |
| unnumbered | `test_valueless_numeric_key_still_rejected` |  | tests/test_tagged_urn.py:800 |
| unnumbered | `test_valueless_tag_at_end` |  | tests/test_tagged_urn.py:694 |
| unnumbered | `test_valueless_tag_case_normalization` |  | tests/test_tagged_urn.py:766 |
| unnumbered | `test_valueless_tag_compatibility` |  | tests/test_tagged_urn.py:783 |
| unnumbered | `test_valueless_tag_equivalence_to_wildcard` |  | tests/test_tagged_urn.py:702 |
| unnumbered | `test_valueless_tag_in_pattern` |  | tests/test_tagged_urn.py:725 |
| unnumbered | `test_valueless_tag_matching` |  | tests/test_tagged_urn.py:712 |
| unnumbered | `test_valueless_tag_mixed_with_valued` |  | tests/test_tagged_urn.py:683 |
| unnumbered | `test_valueless_tag_parsing_multiple` |  | tests/test_tagged_urn.py:673 |
| unnumbered | `test_valueless_tag_parsing_single` | VALUE-LESS TAG TESTS Value-less tags are equivalent to wildcard tags (key=*) | tests/test_tagged_urn.py:665 |
| unnumbered | `test_valueless_tag_roundtrip` |  | tests/test_tagged_urn.py:756 |
| unnumbered | `test_valueless_tag_specificity` |  | tests/test_tagged_urn.py:743 |
| unnumbered | `test_whitespace_in_input_rejected` |  | tests/test_tagged_urn.py:808 |
| unnumbered | `test_wildcard_restrictions` |  | tests/test_tagged_urn.py:443 |
| unnumbered | `test_wildcard_tag` |  | tests/test_tagged_urn.py:388 |
| unnumbered | `test_with_tag_preserves_value` |  | tests/test_tagged_urn.py:493 |
| unnumbered | `test_with_tag_rejects_empty_value` |  | tests/test_tagged_urn.py:498 |
---

## Unnumbered Tests

The following tests are cataloged but do not currently participate in numeric test indexing.

- `test_best_match` — tests/test_tagged_urn.py:353
- `test_builder` — tests/test_tagged_urn.py:310
- `test_builder_preserves_case` — tests/test_tagged_urn.py:322
- `test_builder_rejects_empty_value` — tests/test_tagged_urn.py:504
- `test_builder_with_prefix` — tests/test_tagged_urn.py:42
- `test_canonical_string_format` — tests/test_tagged_urn.py:218
- `test_compatibility` — tests/test_tagged_urn.py:331
- `test_compatibility_with_special_values` — tests/test_tagged_urn.py:1001
- `test_custom_prefix` — tests/test_tagged_urn.py:13
- `test_duplicate_key_rejection` — tests/test_tagged_urn.py:453
- `test_empty_tagged_urn` — tests/test_tagged_urn.py:401
- `test_empty_value_error` — tests/test_tagged_urn.py:471
- `test_empty_value_still_error` — tests/test_tagged_urn.py:775
- `test_empty_with_custom_prefix` — tests/test_tagged_urn.py:429
- `test_extended_character_support` — tests/test_tagged_urn.py:436
- `test_full_cross_product_matching` — tests/test_tagged_urn.py:917
- `test_has_tag_case_sensitive` — tests/test_tagged_urn.py:478
- `test_invalid_escape_sequence_error` — tests/test_tagged_urn.py:124
- `test_matching_case_sensitive_values` — tests/test_tagged_urn.py:245
- `test_matching_different_prefixes_error` — tests/test_tagged_urn.py:645
- `test_matching_semantics_test1_exact_match` — tests/test_tagged_urn.py:527
- `test_matching_semantics_test2_instance_missing_tag` — tests/test_tagged_urn.py:537
- `test_matching_semantics_test3_urn_has_extra_tag` — tests/test_tagged_urn.py:554
- `test_matching_semantics_test4_request_has_wildcard` — tests/test_tagged_urn.py:564
- `test_matching_semantics_test5_urn_has_wildcard` — tests/test_tagged_urn.py:574
- `test_matching_semantics_test6_value_mismatch` — tests/test_tagged_urn.py:584
- `test_matching_semantics_test7_pattern_has_extra_tag` — tests/test_tagged_urn.py:594
- `test_matching_semantics_test8_empty_pattern_matches_anything` — tests/test_tagged_urn.py:610
- `test_matching_semantics_test9_cross_dimension_constraints` — tests/test_tagged_urn.py:628
- `test_merge_and_subset` — tests/test_tagged_urn.py:368
- `test_merge_prefix_mismatch` — tests/test_tagged_urn.py:380
- `test_missing_tag_handling` — tests/test_tagged_urn.py:257
- `test_mixed_quoted_unquoted` — tests/test_tagged_urn.py:113
- `test_mixed_special_values` — tests/test_tagged_urn.py:964
- `test_must_not_have_exclamation_parsing` — tests/test_tagged_urn.py:843
- `test_must_not_have_in_instance` — tests/test_tagged_urn.py:900
- `test_must_not_have_pattern_requires_absent` — tests/test_tagged_urn.py:885
- `test_numeric_key_restriction` — tests/test_tagged_urn.py:458
- `test_prefix_case_insensitive` — tests/test_tagged_urn.py:20
- `test_prefix_mismatch_error` — tests/test_tagged_urn.py:32
- `test_prefix_required` — tests/test_tagged_urn.py:185
- `test_question_mark_in_instance` — tests/test_tagged_urn.py:868
- `test_question_mark_pattern_matches_anything` — tests/test_tagged_urn.py:851
- `test_quoted_value_escape_sequences` — tests/test_tagged_urn.py:99
- `test_quoted_value_special_chars` — tests/test_tagged_urn.py:85
- `test_quoted_values_preserve_case` — tests/test_tagged_urn.py:68
- `test_round_trip_escapes` — tests/test_tagged_urn.py:176
- `test_round_trip_quoted` — tests/test_tagged_urn.py:167
- `test_round_trip_simple` — tests/test_tagged_urn.py:159
- `test_semantic_equivalence` — tests/test_tagged_urn.py:510
- `test_serialization_round_trip_special_values` — tests/test_tagged_urn.py:985
- `test_serialization_smart_quoting` — tests/test_tagged_urn.py:133
- `test_specificity` — tests/test_tagged_urn.py:283
- `test_specificity_with_special_values` — tests/test_tagged_urn.py:1046
- `test_tag_matching` — tests/test_tagged_urn.py:225
- `test_tagged_urn_creation` — tests/test_tagged_urn.py:5
- `test_trailing_semicolon_equivalence` — tests/test_tagged_urn.py:199
- `test_unquoted_values_lowercased` — tests/test_tagged_urn.py:49
- `test_unspecified_question_mark_parsing` — tests/test_tagged_urn.py:835
- `test_unterminated_quote_error` — tests/test_tagged_urn.py:119
- `test_valueless_numeric_key_still_rejected` — tests/test_tagged_urn.py:800
- `test_valueless_tag_at_end` — tests/test_tagged_urn.py:694
- `test_valueless_tag_case_normalization` — tests/test_tagged_urn.py:766
- `test_valueless_tag_compatibility` — tests/test_tagged_urn.py:783
- `test_valueless_tag_equivalence_to_wildcard` — tests/test_tagged_urn.py:702
- `test_valueless_tag_in_pattern` — tests/test_tagged_urn.py:725
- `test_valueless_tag_matching` — tests/test_tagged_urn.py:712
- `test_valueless_tag_mixed_with_valued` — tests/test_tagged_urn.py:683
- `test_valueless_tag_parsing_multiple` — tests/test_tagged_urn.py:673
- `test_valueless_tag_parsing_single` — tests/test_tagged_urn.py:665
- `test_valueless_tag_roundtrip` — tests/test_tagged_urn.py:756
- `test_valueless_tag_specificity` — tests/test_tagged_urn.py:743
- `test_whitespace_in_input_rejected` — tests/test_tagged_urn.py:808
- `test_wildcard_restrictions` — tests/test_tagged_urn.py:443
- `test_wildcard_tag` — tests/test_tagged_urn.py:388
- `test_with_tag_preserves_value` — tests/test_tagged_urn.py:493
- `test_with_tag_rejects_empty_value` — tests/test_tagged_urn.py:498

---

*Generated from Python source tree*
*Total tests: 95*
*Total numbered tests: 18*
*Total unnumbered tests: 77*
*Total numbered tests missing descriptions: 0*
*Total numbering mismatches: 0*
