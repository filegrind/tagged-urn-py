# Python Test Catalog

**Total Tests:** 95

**Numbered Tests:** 95

**Unnumbered Tests:** 0

**Numbered Tests Missing Descriptions:** 0

**Numbering Mismatches:** 0

All numbered test numbers are unique.

This catalog lists all tests in the Python codebase.

| Test # | Function Name | Description | File |
|--------|---------------|-------------|------|
| test0001 | `test_0001_tagged_urn_creation` | TEST0001: Tagged urn creation | tests/test_tagged_urn.py:6 |
| test0002 | `test_0002_custom_prefix` | TEST0002: Custom prefix | tests/test_tagged_urn.py:15 |
| test0003 | `test_0003_prefix_case_insensitive` | TEST0003: Prefix case insensitive | tests/test_tagged_urn.py:23 |
| test0004 | `test_0004_prefix_mismatch_error` | TEST0004: Prefix mismatch error | tests/test_tagged_urn.py:36 |
| test0005 | `test_0005_builder_with_prefix` | TEST0005: Builder with prefix | tests/test_tagged_urn.py:47 |
| test0006 | `test_0006_unquoted_values_lowercased` | TEST0006: Unquoted values lowercased | tests/test_tagged_urn.py:55 |
| test0007 | `test_0007_quoted_values_preserve_case` | TEST0007: Quoted values preserve case | tests/test_tagged_urn.py:76 |
| test0008 | `test_0008_quoted_value_special_chars` | TEST0008: Quoted value special chars | tests/test_tagged_urn.py:94 |
| test0009 | `test_0009_quoted_value_escape_sequences` | TEST0009: Quoted value escape sequences | tests/test_tagged_urn.py:109 |
| test0010 | `test_0010_mixed_quoted_unquoted` | TEST0010: Mixed quoted unquoted | tests/test_tagged_urn.py:124 |
| test0011 | `test_0011_unterminated_quote_error` | TEST0011: Unterminated quote error | tests/test_tagged_urn.py:131 |
| test0012 | `test_0012_invalid_escape_sequence_error` | TEST0012: Invalid escape sequence error | tests/test_tagged_urn.py:137 |
| test0013 | `test_0013_serialization_smart_quoting` | TEST0013: Serialization smart quoting | tests/test_tagged_urn.py:147 |
| test0014 | `test_0014_round_trip_simple` | TEST0014: Round trip simple | tests/test_tagged_urn.py:174 |
| test0015 | `test_0015_round_trip_quoted` | TEST0015: Round trip quoted | tests/test_tagged_urn.py:183 |
| test0016 | `test_0016_round_trip_escapes` | TEST0016: Round trip escapes | tests/test_tagged_urn.py:193 |
| test0017 | `test_0017_prefix_required` | TEST0017: Prefix required | tests/test_tagged_urn.py:203 |
| test0018 | `test_0018_trailing_semicolon_equivalence` | TEST0018: Trailing semicolon equivalence | tests/test_tagged_urn.py:218 |
| test0019 | `test_0019_canonical_string_format` | TEST0019: Canonical string format | tests/test_tagged_urn.py:238 |
| test0020 | `test_0020_tag_matching` | TEST0020: Tag matching | tests/test_tagged_urn.py:246 |
| test0021 | `test_0021_matching_case_sensitive_values` | TEST0021: Matching case sensitive values | tests/test_tagged_urn.py:267 |
| test0022 | `test_0022_missing_tag_handling` | TEST0022: Missing tag handling | tests/test_tagged_urn.py:280 |
| test0023 | `test_0023_specificity` | TEST0023: Specificity | tests/test_tagged_urn.py:307 |
| test0024 | `test_0024_builder` | TEST0024: Builder | tests/test_tagged_urn.py:342 |
| test0025 | `test_0025_builder_preserves_case` | TEST0025: Builder preserves case | tests/test_tagged_urn.py:355 |
| test0026 | `test_0026_compatibility` | TEST0026: Compatibility | tests/test_tagged_urn.py:365 |
| test0027 | `test_0027_best_match` | TEST0027: Best match | tests/test_tagged_urn.py:388 |
| test0028 | `test_0028_merge_and_subset` | TEST0028: Merge and subset | tests/test_tagged_urn.py:404 |
| test0029 | `test_0029_merge_prefix_mismatch` | TEST0029: Merge prefix mismatch | tests/test_tagged_urn.py:417 |
| test0030 | `test_0030_wildcard_tag` | TEST0030: Wildcard tag | tests/test_tagged_urn.py:426 |
| test0031 | `test_0031_empty_tagged_urn` | TEST0031: Empty tagged urn | tests/test_tagged_urn.py:440 |
| test0032 | `test_0032_empty_with_custom_prefix` | TEST0032: Empty with custom prefix | tests/test_tagged_urn.py:469 |
| test0033 | `test_0033_extended_character_support` | TEST0033: Extended character support | tests/test_tagged_urn.py:477 |
| test0034 | `test_0034_wildcard_restrictions` | TEST0034: Wildcard restrictions | tests/test_tagged_urn.py:485 |
| test0035 | `test_0035_duplicate_key_rejection` | TEST0035: Duplicate key rejection | tests/test_tagged_urn.py:496 |
| test0036 | `test_0036_numeric_key_restriction` | TEST0036: Numeric key restriction | tests/test_tagged_urn.py:502 |
| test0037 | `test_0037_empty_value_error` | TEST0037: Empty value error | tests/test_tagged_urn.py:516 |
| test0038 | `test_0038_has_tag_case_sensitive` | TEST0038: Has tag case sensitive | tests/test_tagged_urn.py:524 |
| test0039 | `test_0039_with_tag_preserves_value` | TEST0039: With tag preserves value | tests/test_tagged_urn.py:540 |
| test0040 | `test_0040_with_tag_rejects_empty_value` | TEST0040: With tag rejects empty value | tests/test_tagged_urn.py:546 |
| test0041 | `test_0041_builder_rejects_empty_value` | TEST0041: Builder rejects empty value | tests/test_tagged_urn.py:553 |
| test0042 | `test_0042_semantic_equivalence` | TEST0042: Semantic equivalence | tests/test_tagged_urn.py:560 |
| test0043 | `test_0043_matching_semantics_test1_exact_match` | MATCHING SEMANTICS SPECIFICATION TESTS These 9 tests verify the exact matching semantics from RULES.md Sections 12-17 All implementations (Rust, Go, JS, ObjC) must pass these identically | tests/test_tagged_urn.py:577 |
| test0044 | `test_0044_matching_semantics_test2_instance_missing_tag` | TEST0044: Matching semantics test2 instance missing tag | tests/test_tagged_urn.py:588 |
| test0045 | `test_0045_matching_semantics_test3_urn_has_extra_tag` | TEST0045: Matching semantics test3 urn has extra tag | tests/test_tagged_urn.py:606 |
| test0046 | `test_0046_matching_semantics_test4_request_has_wildcard` | TEST0046: Matching semantics test4 request has wildcard | tests/test_tagged_urn.py:617 |
| test0047 | `test_0047_matching_semantics_test5_urn_has_wildcard` | TEST0047: Matching semantics test5 urn has wildcard | tests/test_tagged_urn.py:628 |
| test0048 | `test_0048_matching_semantics_test6_value_mismatch` | TEST0048: Matching semantics test6 value mismatch | tests/test_tagged_urn.py:639 |
| test0049 | `test_0049_matching_semantics_test7_pattern_has_extra_tag` | TEST0049: Matching semantics test7 pattern has extra tag | tests/test_tagged_urn.py:650 |
| test0050 | `test_0050_matching_semantics_test8_empty_pattern_matches_anything` | TEST0050: Matching semantics test8 empty pattern matches anything | tests/test_tagged_urn.py:667 |
| test0051 | `test_0051_matching_semantics_test9_cross_dimension_constraints` | TEST0051: Matching semantics test9 cross dimension constraints | tests/test_tagged_urn.py:686 |
| test0052 | `test_0052_matching_different_prefixes_error` | TEST0052: Matching different prefixes error | tests/test_tagged_urn.py:704 |
| test0053 | `test_0053_valueless_tag_parsing_single` | VALUE-LESS TAG TESTS Value-less tags are equivalent to wildcard tags (key=*) | tests/test_tagged_urn.py:724 |
| test0054 | `test_0054_valueless_tag_parsing_multiple` | TEST0054: Valueless tag parsing multiple | tests/test_tagged_urn.py:733 |
| test0055 | `test_0055_valueless_tag_mixed_with_valued` | TEST0055: Valueless tag mixed with valued | tests/test_tagged_urn.py:744 |
| test0056 | `test_0056_valueless_tag_at_end` | TEST0056: Valueless tag at end | tests/test_tagged_urn.py:756 |
| test0057 | `test_0057_valueless_tag_equivalence_to_wildcard` | TEST0057: Valueless tag equivalence to wildcard | tests/test_tagged_urn.py:765 |
| test0058 | `test_0058_valueless_tag_matching` | TEST0058: Valueless tag matching | tests/test_tagged_urn.py:776 |
| test0059 | `test_0059_valueless_tag_in_pattern` | TEST0059: Valueless tag in pattern | tests/test_tagged_urn.py:790 |
| test0060 | `test_0060_valueless_tag_specificity` | TEST0060: Valueless tag specificity | tests/test_tagged_urn.py:809 |
| test0061 | `test_0061_valueless_tag_roundtrip` | TEST0061: Valueless tag roundtrip | tests/test_tagged_urn.py:821 |
| test0062 | `test_0062_valueless_tag_case_normalization` | TEST0062: Valueless tag case normalization | tests/test_tagged_urn.py:832 |
| test0063 | `test_0063_empty_value_still_error` | TEST0063: Empty value still error | tests/test_tagged_urn.py:842 |
| test0064 | `test_0064_valueless_tag_compatibility` | TEST0064: Valueless tag compatibility | tests/test_tagged_urn.py:851 |
| test0065 | `test_0065_valueless_numeric_key_still_rejected` | TEST0065: Valueless numeric key still rejected | tests/test_tagged_urn.py:869 |
| test0066 | `test_0066_whitespace_in_input_rejected` | TEST0066: Whitespace in input rejected | tests/test_tagged_urn.py:878 |
| test0067 | `test_0067_unspecified_question_mark_parsing` | NEW SEMANTICS TESTS: ? (unspecified) and ! (must-not-have) | tests/test_tagged_urn.py:905 |
| test0068 | `test_0068_must_not_have_exclamation_parsing` | TEST0068: Must not have exclamation parsing | tests/test_tagged_urn.py:914 |
| test0069 | `test_0069_question_mark_pattern_matches_anything` | TEST0069: Question mark pattern matches anything | tests/test_tagged_urn.py:923 |
| test0070 | `test_0070_question_mark_in_instance` | TEST0070: Question mark in instance | tests/test_tagged_urn.py:941 |
| test0071 | `test_0071_must_not_have_pattern_requires_absent` | TEST0071: Must not have pattern requires absent | tests/test_tagged_urn.py:959 |
| test0072 | `test_0072_must_not_have_in_instance` | TEST0072: Must not have in instance | tests/test_tagged_urn.py:975 |
| test0073 | `test_0073_full_cross_product_matching` | TEST0073: Full cross product matching | tests/test_tagged_urn.py:993 |
| test0074 | `test_0074_mixed_special_values` | TEST0074: Mixed special values | tests/test_tagged_urn.py:1041 |
| test0075 | `test_0075_serialization_round_trip_special_values` | TEST0075: Serialization round trip special values | tests/test_tagged_urn.py:1063 |
| test0076 | `test_0076_compatibility_with_special_values` | TEST0076: Compatibility with special values | tests/test_tagged_urn.py:1080 |
| test0077 | `test_0077_specificity_with_special_values` | TEST0077: Specificity with special values | tests/test_tagged_urn.py:1126 |
| test578 | `test_578_equivalent_identical_tags` | TEST578: Equivalent URNs with identical tag sets | tests/test_tagged_urn.py:1155 |
| test579 | `test_579_not_equivalent_when_one_more_specific` | TEST579: Non-equivalent URNs where one is more specific | tests/test_tagged_urn.py:1163 |
| test580 | `test_580_comparable_specialization_chain` | TEST580: Comparable URNs on the same specialization chain | tests/test_tagged_urn.py:1171 |
| test581 | `test_581_incomparable_different_branches` | TEST581: Incomparable URNs in different branches of the lattice | tests/test_tagged_urn.py:1182 |
| test582 | `test_582_equivalent_implies_comparable` | TEST582: Equivalent implies comparable but not vice versa | tests/test_tagged_urn.py:1193 |
| test583 | `test_583_prefix_mismatch_errors` | TEST583: Prefix mismatch raises error for both relations | tests/test_tagged_urn.py:1208 |
| test584 | `test_584_empty_tags_comparable_to_all` | TEST584: Empty tag set is comparable to everything with same prefix | tests/test_tagged_urn.py:1218 |
| test585 | `test_585_string_variants` | TEST585: String variants of is_equivalent and is_comparable | tests/test_tagged_urn.py:1231 |
| test586 | `test_586_special_values` | TEST586: Special values (*, !, ?) with is_equivalent and is_comparable | tests/test_tagged_urn.py:1240 |
| test587 | `test_587_builder_fluent_api` | TEST587: Builder fluent API for tag manipulation | tests/test_tagged_urn.py:1270 |
| test588 | `test_588_builder_custom_tags` | TEST588: Builder with custom tags | tests/test_tagged_urn.py:1285 |
| test589 | `test_589_builder_tag_overrides` | TEST589: Builder tag overrides (last value wins) | tests/test_tagged_urn.py:1298 |
| test590 | `test_590_builder_empty_build` | TEST590: Builder empty build raises error (tags required) | tests/test_tagged_urn.py:1309 |
| test591 | `test_591_builder_single_tag` | TEST591: Builder with single tag | tests/test_tagged_urn.py:1316 |
| test592 | `test_592_builder_complex` | TEST592: Builder with complex multi-tag URN | tests/test_tagged_urn.py:1326 |
| test593 | `test_593_builder_wildcards` | TEST593: Builder with wildcards | tests/test_tagged_urn.py:1352 |
| test594 | `test_594_builder_custom_prefix` | TEST594: Builder with custom prefix | tests/test_tagged_urn.py:1373 |
| test595 | `test_595_builder_matching_with_built_urn` | TEST595: Builder matching with built URN | tests/test_tagged_urn.py:1381 |
---

*Generated from Python source tree*
*Total tests: 95*
*Total numbered tests: 95*
*Total unnumbered tests: 0*
*Total numbered tests missing descriptions: 0*
*Total numbering mismatches: 0*
