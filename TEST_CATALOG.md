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
| test578 | `test_578_equivalent_identical_tags` | TEST578: Equivalent URNs with identical tag sets | tests/test_tagged_urn.py:1081 |
| test579 | `test_579_not_equivalent_when_one_more_specific` | TEST579: Non-equivalent URNs where one is more specific | tests/test_tagged_urn.py:1089 |
| test580 | `test_580_comparable_specialization_chain` | TEST580: Comparable URNs on the same specialization chain | tests/test_tagged_urn.py:1097 |
| test581 | `test_581_incomparable_different_branches` | TEST581: Incomparable URNs in different branches of the lattice | tests/test_tagged_urn.py:1108 |
| test582 | `test_582_equivalent_implies_comparable` | TEST582: Equivalent implies comparable but not vice versa | tests/test_tagged_urn.py:1119 |
| test583 | `test_583_prefix_mismatch_errors` | TEST583: Prefix mismatch raises error for both relations | tests/test_tagged_urn.py:1134 |
| test584 | `test_584_empty_tags_comparable_to_all` | TEST584: Empty tag set is comparable to everything with same prefix | tests/test_tagged_urn.py:1144 |
| test585 | `test_585_string_variants` | TEST585: String variants of is_equivalent and is_comparable | tests/test_tagged_urn.py:1157 |
| test586 | `test_586_special_values` | TEST586: Special values (*, !, ?) with is_equivalent and is_comparable | tests/test_tagged_urn.py:1166 |
| test587 | `test_587_builder_fluent_api` | TEST587: Builder fluent API for tag manipulation | tests/test_tagged_urn.py:1196 |
| test588 | `test_588_builder_custom_tags` | TEST588: Builder with custom tags | tests/test_tagged_urn.py:1211 |
| test589 | `test_589_builder_tag_overrides` | TEST589: Builder tag overrides (last value wins) | tests/test_tagged_urn.py:1224 |
| test590 | `test_590_builder_empty_build` | TEST590: Builder empty build raises error (tags required) | tests/test_tagged_urn.py:1235 |
| test591 | `test_591_builder_single_tag` | TEST591: Builder with single tag | tests/test_tagged_urn.py:1242 |
| test592 | `test_592_builder_complex` | TEST592: Builder with complex multi-tag URN | tests/test_tagged_urn.py:1252 |
| test593 | `test_593_builder_wildcards` | TEST593: Builder with wildcards | tests/test_tagged_urn.py:1278 |
| test594 | `test_594_builder_custom_prefix` | TEST594: Builder with custom prefix | tests/test_tagged_urn.py:1299 |
| test595 | `test_595_builder_matching_with_built_urn` | TEST595: Builder matching with built URN | tests/test_tagged_urn.py:1307 |
| | | | |
| unnumbered | `test_best_match` |  | tests/test_tagged_urn.py:361 |
| unnumbered | `test_builder` |  | tests/test_tagged_urn.py:318 |
| unnumbered | `test_builder_preserves_case` |  | tests/test_tagged_urn.py:330 |
| unnumbered | `test_builder_rejects_empty_value` |  | tests/test_tagged_urn.py:512 |
| unnumbered | `test_builder_with_prefix` |  | tests/test_tagged_urn.py:42 |
| unnumbered | `test_canonical_string_format` |  | tests/test_tagged_urn.py:219 |
| unnumbered | `test_compatibility` |  | tests/test_tagged_urn.py:339 |
| unnumbered | `test_compatibility_with_special_values` |  | tests/test_tagged_urn.py:1007 |
| unnumbered | `test_custom_prefix` |  | tests/test_tagged_urn.py:13 |
| unnumbered | `test_duplicate_key_rejection` |  | tests/test_tagged_urn.py:461 |
| unnumbered | `test_empty_tagged_urn` |  | tests/test_tagged_urn.py:409 |
| unnumbered | `test_empty_value_error` |  | tests/test_tagged_urn.py:479 |
| unnumbered | `test_empty_value_still_error` |  | tests/test_tagged_urn.py:781 |
| unnumbered | `test_empty_with_custom_prefix` |  | tests/test_tagged_urn.py:437 |
| unnumbered | `test_extended_character_support` |  | tests/test_tagged_urn.py:444 |
| unnumbered | `test_full_cross_product_matching` |  | tests/test_tagged_urn.py:923 |
| unnumbered | `test_has_tag_case_sensitive` |  | tests/test_tagged_urn.py:486 |
| unnumbered | `test_invalid_escape_sequence_error` |  | tests/test_tagged_urn.py:125 |
| unnumbered | `test_matching_case_sensitive_values` |  | tests/test_tagged_urn.py:246 |
| unnumbered | `test_matching_different_prefixes_error` |  | tests/test_tagged_urn.py:653 |
| unnumbered | `test_matching_semantics_test1_exact_match` | MATCHING SEMANTICS SPECIFICATION TESTS These 9 tests verify the exact matching semantics from RULES.md Sections 12-17 All implementations (Rust, Go, JS, ObjC) must pass these identically | tests/test_tagged_urn.py:535 |
| unnumbered | `test_matching_semantics_test2_instance_missing_tag` |  | tests/test_tagged_urn.py:545 |
| unnumbered | `test_matching_semantics_test3_urn_has_extra_tag` |  | tests/test_tagged_urn.py:562 |
| unnumbered | `test_matching_semantics_test4_request_has_wildcard` |  | tests/test_tagged_urn.py:572 |
| unnumbered | `test_matching_semantics_test5_urn_has_wildcard` |  | tests/test_tagged_urn.py:582 |
| unnumbered | `test_matching_semantics_test6_value_mismatch` |  | tests/test_tagged_urn.py:592 |
| unnumbered | `test_matching_semantics_test7_pattern_has_extra_tag` |  | tests/test_tagged_urn.py:602 |
| unnumbered | `test_matching_semantics_test8_empty_pattern_matches_anything` |  | tests/test_tagged_urn.py:618 |
| unnumbered | `test_matching_semantics_test9_cross_dimension_constraints` |  | tests/test_tagged_urn.py:636 |
| unnumbered | `test_merge_and_subset` |  | tests/test_tagged_urn.py:376 |
| unnumbered | `test_merge_prefix_mismatch` |  | tests/test_tagged_urn.py:388 |
| unnumbered | `test_missing_tag_handling` |  | tests/test_tagged_urn.py:258 |
| unnumbered | `test_mixed_quoted_unquoted` |  | tests/test_tagged_urn.py:114 |
| unnumbered | `test_mixed_special_values` |  | tests/test_tagged_urn.py:970 |
| unnumbered | `test_must_not_have_exclamation_parsing` |  | tests/test_tagged_urn.py:849 |
| unnumbered | `test_must_not_have_in_instance` |  | tests/test_tagged_urn.py:906 |
| unnumbered | `test_must_not_have_pattern_requires_absent` |  | tests/test_tagged_urn.py:891 |
| unnumbered | `test_numeric_key_restriction` |  | tests/test_tagged_urn.py:466 |
| unnumbered | `test_prefix_case_insensitive` |  | tests/test_tagged_urn.py:20 |
| unnumbered | `test_prefix_mismatch_error` |  | tests/test_tagged_urn.py:32 |
| unnumbered | `test_prefix_required` |  | tests/test_tagged_urn.py:186 |
| unnumbered | `test_question_mark_in_instance` |  | tests/test_tagged_urn.py:874 |
| unnumbered | `test_question_mark_pattern_matches_anything` |  | tests/test_tagged_urn.py:857 |
| unnumbered | `test_quoted_value_escape_sequences` |  | tests/test_tagged_urn.py:100 |
| unnumbered | `test_quoted_value_special_chars` |  | tests/test_tagged_urn.py:86 |
| unnumbered | `test_quoted_values_preserve_case` |  | tests/test_tagged_urn.py:69 |
| unnumbered | `test_round_trip_escapes` |  | tests/test_tagged_urn.py:177 |
| unnumbered | `test_round_trip_quoted` |  | tests/test_tagged_urn.py:168 |
| unnumbered | `test_round_trip_simple` |  | tests/test_tagged_urn.py:160 |
| unnumbered | `test_semantic_equivalence` |  | tests/test_tagged_urn.py:518 |
| unnumbered | `test_serialization_round_trip_special_values` |  | tests/test_tagged_urn.py:991 |
| unnumbered | `test_serialization_smart_quoting` |  | tests/test_tagged_urn.py:134 |
| unnumbered | `test_specificity` |  | tests/test_tagged_urn.py:284 |
| unnumbered | `test_specificity_with_special_values` |  | tests/test_tagged_urn.py:1052 |
| unnumbered | `test_tag_matching` |  | tests/test_tagged_urn.py:226 |
| unnumbered | `test_tagged_urn_creation` |  | tests/test_tagged_urn.py:5 |
| unnumbered | `test_trailing_semicolon_equivalence` |  | tests/test_tagged_urn.py:200 |
| unnumbered | `test_unquoted_values_lowercased` |  | tests/test_tagged_urn.py:49 |
| unnumbered | `test_unspecified_question_mark_parsing` | NEW SEMANTICS TESTS: ? (unspecified) and ! (must-not-have) | tests/test_tagged_urn.py:841 |
| unnumbered | `test_unterminated_quote_error` |  | tests/test_tagged_urn.py:120 |
| unnumbered | `test_valueless_numeric_key_still_rejected` |  | tests/test_tagged_urn.py:806 |
| unnumbered | `test_valueless_tag_at_end` |  | tests/test_tagged_urn.py:702 |
| unnumbered | `test_valueless_tag_case_normalization` |  | tests/test_tagged_urn.py:772 |
| unnumbered | `test_valueless_tag_compatibility` |  | tests/test_tagged_urn.py:789 |
| unnumbered | `test_valueless_tag_equivalence_to_wildcard` |  | tests/test_tagged_urn.py:710 |
| unnumbered | `test_valueless_tag_in_pattern` |  | tests/test_tagged_urn.py:733 |
| unnumbered | `test_valueless_tag_matching` |  | tests/test_tagged_urn.py:720 |
| unnumbered | `test_valueless_tag_mixed_with_valued` |  | tests/test_tagged_urn.py:691 |
| unnumbered | `test_valueless_tag_parsing_multiple` |  | tests/test_tagged_urn.py:681 |
| unnumbered | `test_valueless_tag_parsing_single` | VALUE-LESS TAG TESTS Value-less tags are equivalent to wildcard tags (key=*) | tests/test_tagged_urn.py:673 |
| unnumbered | `test_valueless_tag_roundtrip` |  | tests/test_tagged_urn.py:762 |
| unnumbered | `test_valueless_tag_specificity` |  | tests/test_tagged_urn.py:751 |
| unnumbered | `test_whitespace_in_input_rejected` |  | tests/test_tagged_urn.py:814 |
| unnumbered | `test_wildcard_restrictions` |  | tests/test_tagged_urn.py:451 |
| unnumbered | `test_wildcard_tag` |  | tests/test_tagged_urn.py:396 |
| unnumbered | `test_with_tag_preserves_value` |  | tests/test_tagged_urn.py:501 |
| unnumbered | `test_with_tag_rejects_empty_value` |  | tests/test_tagged_urn.py:506 |
---

## Unnumbered Tests

The following tests are cataloged but do not currently participate in numeric test indexing.

- `test_best_match` — tests/test_tagged_urn.py:361
- `test_builder` — tests/test_tagged_urn.py:318
- `test_builder_preserves_case` — tests/test_tagged_urn.py:330
- `test_builder_rejects_empty_value` — tests/test_tagged_urn.py:512
- `test_builder_with_prefix` — tests/test_tagged_urn.py:42
- `test_canonical_string_format` — tests/test_tagged_urn.py:219
- `test_compatibility` — tests/test_tagged_urn.py:339
- `test_compatibility_with_special_values` — tests/test_tagged_urn.py:1007
- `test_custom_prefix` — tests/test_tagged_urn.py:13
- `test_duplicate_key_rejection` — tests/test_tagged_urn.py:461
- `test_empty_tagged_urn` — tests/test_tagged_urn.py:409
- `test_empty_value_error` — tests/test_tagged_urn.py:479
- `test_empty_value_still_error` — tests/test_tagged_urn.py:781
- `test_empty_with_custom_prefix` — tests/test_tagged_urn.py:437
- `test_extended_character_support` — tests/test_tagged_urn.py:444
- `test_full_cross_product_matching` — tests/test_tagged_urn.py:923
- `test_has_tag_case_sensitive` — tests/test_tagged_urn.py:486
- `test_invalid_escape_sequence_error` — tests/test_tagged_urn.py:125
- `test_matching_case_sensitive_values` — tests/test_tagged_urn.py:246
- `test_matching_different_prefixes_error` — tests/test_tagged_urn.py:653
- `test_matching_semantics_test1_exact_match` — tests/test_tagged_urn.py:535
- `test_matching_semantics_test2_instance_missing_tag` — tests/test_tagged_urn.py:545
- `test_matching_semantics_test3_urn_has_extra_tag` — tests/test_tagged_urn.py:562
- `test_matching_semantics_test4_request_has_wildcard` — tests/test_tagged_urn.py:572
- `test_matching_semantics_test5_urn_has_wildcard` — tests/test_tagged_urn.py:582
- `test_matching_semantics_test6_value_mismatch` — tests/test_tagged_urn.py:592
- `test_matching_semantics_test7_pattern_has_extra_tag` — tests/test_tagged_urn.py:602
- `test_matching_semantics_test8_empty_pattern_matches_anything` — tests/test_tagged_urn.py:618
- `test_matching_semantics_test9_cross_dimension_constraints` — tests/test_tagged_urn.py:636
- `test_merge_and_subset` — tests/test_tagged_urn.py:376
- `test_merge_prefix_mismatch` — tests/test_tagged_urn.py:388
- `test_missing_tag_handling` — tests/test_tagged_urn.py:258
- `test_mixed_quoted_unquoted` — tests/test_tagged_urn.py:114
- `test_mixed_special_values` — tests/test_tagged_urn.py:970
- `test_must_not_have_exclamation_parsing` — tests/test_tagged_urn.py:849
- `test_must_not_have_in_instance` — tests/test_tagged_urn.py:906
- `test_must_not_have_pattern_requires_absent` — tests/test_tagged_urn.py:891
- `test_numeric_key_restriction` — tests/test_tagged_urn.py:466
- `test_prefix_case_insensitive` — tests/test_tagged_urn.py:20
- `test_prefix_mismatch_error` — tests/test_tagged_urn.py:32
- `test_prefix_required` — tests/test_tagged_urn.py:186
- `test_question_mark_in_instance` — tests/test_tagged_urn.py:874
- `test_question_mark_pattern_matches_anything` — tests/test_tagged_urn.py:857
- `test_quoted_value_escape_sequences` — tests/test_tagged_urn.py:100
- `test_quoted_value_special_chars` — tests/test_tagged_urn.py:86
- `test_quoted_values_preserve_case` — tests/test_tagged_urn.py:69
- `test_round_trip_escapes` — tests/test_tagged_urn.py:177
- `test_round_trip_quoted` — tests/test_tagged_urn.py:168
- `test_round_trip_simple` — tests/test_tagged_urn.py:160
- `test_semantic_equivalence` — tests/test_tagged_urn.py:518
- `test_serialization_round_trip_special_values` — tests/test_tagged_urn.py:991
- `test_serialization_smart_quoting` — tests/test_tagged_urn.py:134
- `test_specificity` — tests/test_tagged_urn.py:284
- `test_specificity_with_special_values` — tests/test_tagged_urn.py:1052
- `test_tag_matching` — tests/test_tagged_urn.py:226
- `test_tagged_urn_creation` — tests/test_tagged_urn.py:5
- `test_trailing_semicolon_equivalence` — tests/test_tagged_urn.py:200
- `test_unquoted_values_lowercased` — tests/test_tagged_urn.py:49
- `test_unspecified_question_mark_parsing` — tests/test_tagged_urn.py:841
- `test_unterminated_quote_error` — tests/test_tagged_urn.py:120
- `test_valueless_numeric_key_still_rejected` — tests/test_tagged_urn.py:806
- `test_valueless_tag_at_end` — tests/test_tagged_urn.py:702
- `test_valueless_tag_case_normalization` — tests/test_tagged_urn.py:772
- `test_valueless_tag_compatibility` — tests/test_tagged_urn.py:789
- `test_valueless_tag_equivalence_to_wildcard` — tests/test_tagged_urn.py:710
- `test_valueless_tag_in_pattern` — tests/test_tagged_urn.py:733
- `test_valueless_tag_matching` — tests/test_tagged_urn.py:720
- `test_valueless_tag_mixed_with_valued` — tests/test_tagged_urn.py:691
- `test_valueless_tag_parsing_multiple` — tests/test_tagged_urn.py:681
- `test_valueless_tag_parsing_single` — tests/test_tagged_urn.py:673
- `test_valueless_tag_roundtrip` — tests/test_tagged_urn.py:762
- `test_valueless_tag_specificity` — tests/test_tagged_urn.py:751
- `test_whitespace_in_input_rejected` — tests/test_tagged_urn.py:814
- `test_wildcard_restrictions` — tests/test_tagged_urn.py:451
- `test_wildcard_tag` — tests/test_tagged_urn.py:396
- `test_with_tag_preserves_value` — tests/test_tagged_urn.py:501
- `test_with_tag_rejects_empty_value` — tests/test_tagged_urn.py:506

---

*Generated from Python source tree*
*Total tests: 95*
*Total numbered tests: 18*
*Total unnumbered tests: 77*
*Total numbered tests missing descriptions: 0*
*Total numbering mismatches: 0*
