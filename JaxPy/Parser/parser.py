from typing import List
from Lexer.constants import *
from Utils.select_rule import select_rule
from Utils.match_terminal import match_terminal

from Parser.variable_declaration import var_declaration
from Parser.variable_assignment import variable_assignment
from Parser.if_statement import if_statement
from Parser.loop import loop
from Parser.function_definition import function_definition
from Parser.return_statement import return_statement
from Parser.break_continue import break_continue
from Parser.class_definition import class_definition
from Parser.interface_definition import interface_defintion
from Parser.expression import *

i = 0

def check_is_syntax_valid():
    from tokenset import tokens
    if S():
        if tokens[i].token_type == END_MARKER:
            print("Syntax is Valid")
            return True
    print(f'Error at line number {tokens[i].line}')
    return False

def S() -> bool:
    if select_rule([LET_CONST, IF, UNTIL, PROCEDURE, RETURN, ASSIGNMENT, BREAK_CONTINUE, *follow_of_OE]):
        if MST():
            if S():
                return True
    elif select_rule([FINAL, CLASS]):
        if class_definition():
            if S():
                return True 
    elif select_rule([INTERFACE]):
        if interface_defintion():
            if S():
                return True 
    elif select_rule([END_MARKER]):
        return True
    return False

def MST() -> bool: #multiple statements
    if select_rule([LET_CONST, IF, UNTIL, PROCEDURE, RETURN, ASSIGN, BREAK_CONTINUE, THIS, IDENTIFIER, INTEGER_CONSTANT, FLOAT_CONSTANT, STRING_CONSTANT, BOOL_CONSTANT, NOT]):
        if SST():
            if MST():
                return True
    elif select_rule([CLOSING_BRACE, END_MARKER, CLASS, FINAL, INTERFACE]):
        return True
    return False

def SST() -> bool: #single statements
    if select_rule([LET_CONST]):
        if var_declaration():
            if match_terminal(SEMICOLON):
                return True  
    elif select_rule([IF]):
        if if_statement():
            return True
    elif select_rule([UNTIL]):
        if loop():
            return True  
    elif select_rule([PROCEDURE]):
        if function_definition():
            return True 
    elif select_rule([RETURN]):
        if return_statement():
            if match_terminal(SEMICOLON):
                return True  
    elif select_rule([ASSIGN]):
        if variable_assignment():
            if match_terminal(SEMICOLON):
                return True  
    elif select_rule([BREAK_CONTINUE]):
        if break_continue():
            if match_terminal(SEMICOLON):
                return True   
    elif select_rule(first_of_OE):
        if OE():
            if match_terminal(SEMICOLON):
                return True     
    return False