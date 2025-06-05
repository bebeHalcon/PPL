// Trần Thiện Nhân
// 2111913
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: newline_list? decl_list EOF;													// Program

////////////////////// PARSER //////////////////////

// ---------------------------- DECLARATIONS ---------------------------- //
decl_list: decl_mem decl_list | decl_mem;												// Declaration list
decl_mem: decl newline_list;															// Declaration with newline
decl: var_decl | func_decl;																// Declaration

var_decl: type_decl | v_decl | dyn_decl;												// Variable declaration
dyn_decl: DYNAMIC ID as_expr?;															// Dynamic declaration
v_decl: VAR ID as_expr;																	// Declaration start with 'var'
type_decl: types ID arr_dim? as_expr?;													// Normal declaration

func_decl: FUNC ID LP param_list RP func_body;											// Function declaration
param_list: param_prime | ;																// Parameter list
param_prime: param CM param_prime | param;												// Non-null parameter list
param: types ID arr_dim?;																// Parameter
func_body: newline_list? return_stmt | newline_list? block_stmt | ;						// Function body


// ---------------------------- STATEMENTS ---------------------------- //
stmt_list: stmt_mem stmt_list | ;														// Null-able statement list
stmt_mem: stmt newline_list;															// Statement with newline
stmt: match_stmt | unmatch_stmt;														// Statement
match_stmt: var_decl
	| assign_stmt 
	| match_if_stmt 
	| for_stmt 
	| break_stmt 
	| continue_stmt 
	| return_stmt 
	| func_call_stmt
	| block_stmt;																		// Match Statement

unmatch_stmt: IF cond_expr newline_list? stmt
			| IF cond_expr newline_list? match_stmt elif_match_list elif_stmt
			| IF cond_expr newline_list? match_stmt elif_match_list else_unmatch_stmt;	// Unmatch statement
elif_stmt: newline_list ELIF cond_expr newline_list? stmt;								// Elif statement
else_unmatch_stmt: newline_list ELSE newline_list? unmatch_stmt;						// Unmatch Else statement

lhs: ID | arr_elem;																		// Left hand side
assign_stmt: lhs as_expr;																// Assignment statement
as_expr: ASSIGN expr;																	// Assignment expression

match_if_stmt: IF cond_expr newline_list? match_stmt elif_match_list else_match_stmt;	// Match If statement
elif_match_list: newline_list elif_match_stmt elif_match_list | ;						// Match Elif list
elif_match_stmt: ELIF cond_expr newline_list? match_stmt;								// Match Elif statement
else_match_stmt: newline_list ELSE newline_list? match_stmt;							// Match Else statement
cond_expr: LP expr RP;																	// Condition expression

for_stmt: FOR ID UNTIL expr BY expr newline_list? stmt;									// For statement
break_stmt: BREAK;																		// Break statement
continue_stmt: CONTINUE;																// Continue statement
return_stmt: RETURN expr?;																// Return statement
func_call_stmt: ID LP expr_list RP;														// Function call statement
block_stmt: BEGIN newline_list stmt_list END;											// Block statement


// ---------------------------- NEWLINES ---------------------------- //
newline_list: NEWLINE newline_list | NEWLINE;											// Non-null newline list


// ---------------------------- EXPRESSIONS ---------------------------- //
expr_list: expr_prime | ;																// Null-able expression list
expr_prime: expr CM expr_prime | expr;													// Non-null expression list
expr: rel_expr CONCAT rel_expr | rel_expr;												// Concatenation expression
rel_expr: and_expr (EQ|STR_EQ|NEQ|LESS|GREATER|LEQ|GEQ) and_expr | and_expr;			// Relational expression
and_expr: and_expr (AND|OR) add_expr | add_expr;										// Logical expression (and, or)
add_expr: add_expr (ADD|SUB) mul_expr | mul_expr;										// Adding expression (add, sub)
mul_expr: mul_expr (MUL|DIV|MOD) not_expr | not_expr;									// Multiplying expression (mul, div, mod)
not_expr: NOT not_expr | sign_expr;														// Logical expression (not)
sign_expr: SUB sign_expr | idx_expr;													// Sign expression (-)
idx_expr: elem_expr | operand;															// Index expression
elem_expr: (ID | func_call_expr) LSB idx_op RSB;										// Element expression
operand: ID | literal | func_call_expr | LP expr RP;									// Operands
func_call_expr: ID LP expr_list RP;														// Function call expression
arr_elem: ID LSB idx_op RSB;															// Array element

// ---------------------------- TYPES ---------------------------- //
types: NUMBER | BOOL | STRING; 															// Types
idx_op: expr CM idx_op | expr;															// Index operator
arr_lit: LSB expr_prime RSB;															// Array literal

dim_list: NUM_LIT CM dim_list | NUM_LIT;												// Dimension List
arr_dim: LSB dim_list RSB;																// Dimension of array


////////////////////// LEXER //////////////////////

// ------- KEYWORDS ------- //
fragment TRUE: 'true';
fragment FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';


// ------- OPERATORS ------- //
ADD: '+';		// Addition
SUB: '-';		// Subtraction
MUL: '*';		// Multiplication
DIV: '/';		// Division
MOD: '%';		// Modulo
EQ: '=';		// Equal
ASSIGN: '<-';	// Assign
NEQ: '!=';		// Not Equal
LESS: '<';		// Less than
LEQ: '<=';		// Less than or equal
GREATER: '>';	// Greater than
GEQ: '>=';		// Greater than or equal
CONCAT: '...';	// Concatenate two strings
STR_EQ: '==';	// Compare two same strings


// ------- SEPERATORS ------- //
LP: '(';									// Left Parenthesis
RP: ')';									// Right Parenthesis
LSB: '[';									// Left Square Bracket
RSB: ']';									// Right Square Bracket
CM: ',';									// Comma


// ------- FRAGMENTS ------- //
fragment INT: [0-9]+;											// Integer
fragment DEC: '.' [0-9]*;										// Decimal
fragment EXP: [eE] [+-]? [0-9]+;								// Exponent

fragment ESC_SEQ: '\\' [bfrnt\\'];								// Escape sequences
fragment STR_CHAR: '\'"' | ~[\n\r\f\\"] | ESC_SEQ; 				// String character
fragment ILL_ESC: '\\' (~[bfrnt\\'])?;							// Illegal escape characters


// ------- LITERALS ------- //
literal: NUM_LIT | STR_LIT | BOOL_LIT | arr_lit;				// Literals
NUM_LIT: INT DEC? EXP?;											// Number literal
BOOL_LIT: TRUE | FALSE;											// Boolean literal
STR_LIT: '"' STR_CHAR* '"'
{
	self.text = self.text[1:-1]
}; 																// String literal


// ------- IDENTIFIER ------- //
ID: [a-zA-Z_][a-zA-Z0-9_]*;										// Identifier


// ---------- NEWLINE ----------//
NEWLINE: '\n';													// Newline


// ------- WHITESPACE ------- //
WS: [ \t\b\f]+ -> skip ; 										// Whitespace


// ------- COMMENTS ------- //
COMMENT: '##' ~[\r\f\n]* -> skip;								// Single-line comment


// ------- ERRORS ------- //
UNCLOSE_STRING: '"' STR_CHAR* ('\n'|'\r'|'\f'|EOF)
{
	s = str(self.text)
	if s[-1] in ['\n', '\r', '\f']:
		raise UncloseString(s[1:-1])
	else:
		raise UncloseString(s[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ILL_ESC 
{
	s = str(self.text)
	raise IllegalEscape(s[1:])
};

ERROR_TOKEN: . {raise ErrorToken(self.text)};