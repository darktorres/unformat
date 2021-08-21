from random import choice, random, randrange
from sys import stderr


def make_choice(*choices):
    return lambda value, mutation_rate: choice(choices)


def make_delta_sq(factor, minimum=0):
    return lambda value, mutation_rate: max(minimum,
                                            int(value) + randrange(-factor, factor + 1) * randrange(factor + 1))


def make_range(start, stop):
    return lambda value, mutation_rate: randrange(start, stop)


mutation_rules = {
    "AccessModifierOffset": make_range(-8, 9),
    "AfterControlStatement": make_choice("Never", "MultiLine", "Always"),
    "AlignAfterOpenBracket": make_choice("Align", "DontAlign", "AlwaysBreak"),
    "AlignConsecutiveAssignments": make_choice("None", "Consecutive", "AcrossEmptyLines", "AcrossComments", "AcrossEmptyLinesAndComments"),
    "AlignConsecutiveBitFields": make_choice("None", "Consecutive", "AcrossEmptyLines", "AcrossComments", "AcrossEmptyLinesAndComments"),
    "AlignConsecutiveDeclarations": make_choice("None", "Consecutive", "AcrossEmptyLines", "AcrossComments", "AcrossEmptyLinesAndComments"),
    "AlignConsecutiveMacros": make_choice("None", "Consecutive", "AcrossEmptyLines", "AcrossComments", "AcrossEmptyLinesAndComments"),
    "AlignEscapedNewlines": make_choice("DontAlign", "Left", "Right"),
    "AlignOperands": make_choice("DontAlign", "Align", "AlignAfterOperator"),
    "AllowShortBlocksOnASingleLine": make_choice("Never", "Empty", "Always"),
    "AllowShortFunctionsOnASingleLine": make_choice("None", "Empty", "Inline", "All"),
    "AllowShortIfStatementsOnASingleLine": make_choice("Never", "WithoutElse", "OnlyFirstIf", "AllIfsAndElse"),
    "AllowShortLambdasOnASingleLine": make_choice("None", "Empty", "Inline", "All"),
    "AlwaysBreakAfterDefinitionReturnType": make_choice("None", "All", "TopLevel"),
    "AlwaysBreakAfterReturnType": make_choice("None", "All", "TopLevel", "AllDefinitions", "TopLevelDefinitions"),
    "AlwaysBreakTemplateDeclarations": make_choice("No", "MultiLine", "Yes"),
    "AttributeMacros": lambda value, mutation_rate: value,
    "BasedOnStyle": make_choice("LLVM", "Google", "Chromium", "Mozilla", "WebKit", "Microsoft", "GNU"),
    "BitFieldColonSpacing": make_choice("Both", "None", "Before", "After"),
    "BraceWrapping": lambda value, mutation_rate: mutate(value, mutation_rate),
    "BreakBeforeBinaryOperators": make_choice("None", "NonAssignment", "All"),
    "BreakBeforeBraces": make_choice("Attach", "Linux", "Mozilla", "Stroustrup", "Allman", "GNU", "WebKit", "Custom"),
    "BreakConstructorInitializers": make_choice("BeforeColon", "BeforeComma", "AfterColon"),
    "BreakInheritanceList": make_choice("BeforeColon", "BeforeComma", "AfterColon", "AfterComma"),
    "ColumnLimit": make_delta_sq(5, 1),
    "CommentPragmas": lambda value, mutation_rate: value,
    "ConstructorInitializerIndentWidth": make_delta_sq(4),
    "ContinuationIndentWidth": make_delta_sq(3),
    "DisableFormat": lambda value, mutation_rate: False,
    "EmptyLineBeforeAccessModifier": make_choice("Never", "Leave", "LogicalBlock", "Always"),
    "ForEachMacros": lambda value, mutation_rate: value,
    "IncludeBlocks": make_choice("Preserve", "Merge", "Regroup"),
    "IncludeCategories": lambda value, mutation_rate: [mutate(item, mutation_rate) for item in value],
    "IncludeIsMainRegex": lambda value, mutation_rate: value,
    "IncludeIsMainSourceRegex": lambda value, mutation_rate: value,
    "IndentExternBlock": make_choice("AfterExternBlock", "NoIndent", "Indent"),
    "IndentPPDirectives": make_choice("None", "AfterHash", "BeforeHash"),
    "IndentWidth": make_delta_sq(4),
    "InsertTrailingCommas": make_choice("None", "Wrapped"),
    "JavaScriptQuotes": make_choice("Leave", "Single", "Double"),
    "Language": make_choice("None", "Cpp", "Java", "JavaScript", "Proto", "TableGen"),
    "MacroBlockBegin": lambda value, mutation_rate: value,
    "MacroBlockEnd": lambda value, mutation_rate: value,
    "MaxEmptyLinesToKeep": make_delta_sq(1),
    "NamespaceIndentation": make_choice("None", "Inner", "All"),
    "ObjCBinPackProtocolList": make_choice("Auto", "Always", "Never"),
    "ObjCBlockIndentWidth": make_range(0, 8),
    "PenaltyBreakAssignment": make_delta_sq(2),
    "PenaltyBreakBeforeFirstCallParameter": make_delta_sq(2),
    "PenaltyBreakComment": make_delta_sq(10),
    "PenaltyBreakFirstLessLess": make_delta_sq(10),
    "PenaltyBreakString": make_delta_sq(25),
    "PenaltyBreakTemplateDeclaration": make_delta_sq(10),
    "PenaltyExcessCharacter": make_delta_sq(1000),
    "PenaltyIndentedWhitespace": make_delta_sq(1),
    "PenaltyReturnTypeOnItsOwnLine": make_delta_sq(10),
    "PointerAlignment": make_choice("Left", "Right", "Middle"),
    "Priority": lambda value, mutation_rate: value,
    "RawStringFormats": lambda value, mutation_rate: [mutate(item, mutation_rate) for item in value],
    "Regex": lambda value, mutation_rate: value,
    "SortJavaStaticImport": make_choice("Before", "After"),
    "SortPriority": lambda value, mutation_rate: value,
    "SpaceAroundPointerQualifiers": make_choice("Default", "Before", "After", "Both"),
    "SpaceBeforeParens": make_choice("Never", "ControlStatements", "Always"),
    "SpacesBeforeTrailingComments": make_delta_sq(3),
    "Standard": make_choice("c++03", "c++11", "c++14", "c++17", "c++20", "Latest", "Auto"),
    "StatementAttributeLikeMacros": lambda value, mutation_rate: value,
    "StatementMacros": lambda value, mutation_rate: value,
    "TabWidth": make_delta_sq(3),
    "UseTab": make_choice("Never", "ForIndentation", "Always"),	
    "WhitespaceSensitiveMacros": lambda value, mutation_rate: value,
    "EmptyLineAfterAccessModifier": make_choice("Never", "Leave", "Always"),
    "SpacesInAngles": make_choice("Never", "Always", "Leave"),
    "ReferenceAlignment": make_choice("Pointer", "Left", "Right", "Middle"),
    "AlignArrayOfStructures": make_choice("Left", "Right", "None"),
    "LambdaBodyIndentation": make_choice("Signature", "OuterScope"),
    "SortIncludes": make_choice("Never", "CaseSensitive", "CaseInsensitive"),
    "ShortNamespaceLines": make_delta_sq(3),
    "PPIndentWidth": make_range(-1, 9),
    "IfMacros": lambda value, mutation_rate: value,
    "SpacesInLineCommentPrefix": lambda value, mutation_rate: mutate(value, mutation_rate),
    "Minimum": make_range(-1, 9),
    "Maximum": make_range(-1, 9),
}


def mutate_value(key, value, mutation_rate):
    if key in mutation_rules:
        mutation_rule = mutation_rules[key]
        return mutation_rule(value, mutation_rate)

    if isinstance(value, bool):
        return not value

    print("Unrecognized setting, '{}: {}', in .clang-format configuration.".format(key, value), file=stderr)
    return value


def visit_line(key, value, mutation_rate):
    return mutate_value(key, value, mutation_rate) if random() < mutation_rate else value


def mutate(config, mutation_rate):
    return {key: visit_line(key, value, mutation_rate) for key, value in config.items()}


def recombine(scored_parents, args):
    ranked = sorted(scored_parents, key=lambda scored_parent: scored_parent[0])

    fittest = ranked[0]
    (fittest_score, fittest_config) = fittest

    # rank-based selection with elitism
    elite_configs = [fittest_config]
    recombined_configs = [mutate(ranked[int(random() * random() * len(ranked))][1], args.mutation) for _ in
                          range(args.population - 1)]
    recombination = elite_configs + recombined_configs

    return (fittest, recombination)
