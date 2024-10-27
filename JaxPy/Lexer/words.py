from Lexer.constants import *

valid_words = {
    KEYWORDS: {
        LET_CONST: [
            "let",
            "const",
        ],
        DATA_TYPES: [
            "string",
            "number",
            "boolean",
        ],
        VOID: [
          "void",
        ],
        ASSIGN: [
            "assign"
        ],
        DISPLAY: [
            "display"
        ],
        IF: [
            "if"
        ],
        ELSE: [
            "else"
        ],
        UNTIL: [
            "until"
        ],
        BREAK_CONTINUE: [
            "break",
            "continue"
        ],
        PROCEDURE: [
            "procedure"
        ],
        RETURN: [
            "return"
        ],
        CLASS: [
            "class"
        ],
        CONSTRUCTOR: [
            "constructor"
        ],
        THIS: [
            "this"
        ],
        ATRATE: [
          "@"
        ],
        METHOD: [
            "method"
        ],
        NEW: [
            "new"
        ],
        EXTENDS: [
            "extends"
        ],
        IMPLEMENTS: [
            "implements"
        ],
        SUPER: [
            "super"
        ],
        FINAL: [
            "final"
        ],
        INTERFACE: [
            "interface"
        ],
        BOOL_CONSTANT: [
            "true",
            "false"
        ]
    },

    OPERATORS: {
        PLUS_MINUS: [
            "+",
            "-",
        ],
        MULTIPLY_DIVIDE_MODULUS: [
            "*",
            "/",
            "%",
        ],
        COMPARISON: [
            "==",
            "!=",
            "<",
            "<=",
            ">",
            ">=",
        ],
        AND: [
            "&&",
        ],
        OR: [
            "||",
        ],
        NOT: [
            "!",
        ],
        ASSIGNMENT_OPERATOR: [
            "=",
        ],
        COMPOUND_ASSIGNMENT_OPERATOR: [
            "+=",
            "-=",
            "*=",
            "/=",
            "%="
        ],
        INCREMENT_DECREMENT: [
            "++",
            "--",
        ],
        BITWISE: [
            "&",
            "|"
        ],
    },

    PUNCTUATORS: {
        OPENING_PARENTHESIS: [
            "(",
        ],
        CLOSING_PARENTHESIS: [
            ")",
        ],
        OPENING_BRACKET: [
            "[",
        ],
        CLOSING_BRACKET: [
            "]",
        ],
        OPENING_BRACE: [
            "{",
        ],
        CLOSING_BRACE: [
            "}",
        ],
        SEMICOLON: [
            ";",
        ],
        COMMA: [
            ",",
        ],
        DOT: [
            ".",
        ],
        COLON: [
            ":",
        ],
    }
}
