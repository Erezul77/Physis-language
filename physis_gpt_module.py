
from typing import List, Union, Dict
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str

@dataclass
class ASTNode:
    type: str
    value: str
    children: List['ASTNode']

symbol_meanings = {
    "🌱": "growth, potential, emergence",
    "☯": "duality, harmony, balance",
    "🔁": "recursion, reflection, cycle",
    "🔥": "transformation, intensity, passion",
    "💧": "emotion, flow, adaptability",
    "🌀": "evolution, fractal unfolding, self-expansion",
    "👁": "awareness, clarity, perception",
    "∞": "eternity, unbounded recursion, infinite process"
}

def tokenize(code: str) -> List[Token]:
    tokens = []
    for char in code:
        if char == '(':
            tokens.append(Token("GROUP_START", char))
        elif char == ')':
            tokens.append(Token("GROUP_END", char))
        elif char.strip() != '':
            tokens.append(Token("SYMBOL", char))
    return tokens

def build_ast(tokens: List[Token]) -> ASTNode:
    def parse_expression(index: int) -> Union[ASTNode, int]:
        token = tokens[index]
        if token.type == "SYMBOL":
            node = ASTNode(type="Symbol", value=token.value, children=[])
            return node, index + 1
        elif token.type == "GROUP_START":
            node = ASTNode(type="Group", value="()", children=[])
            index += 1
            while tokens[index].type != "GROUP_END":
                child, index = parse_expression(index)
                node.children.append(child)
            return node, index + 1
        else:
            raise SyntaxError(f"Unexpected token: {token.value}")

    root = ASTNode(type="Program", value="Root", children=[])
    index = 0
    while index < len(tokens):
        node, index = parse_expression(index)
        root.children.append(node)

    return root

def reflect_ast(node: ASTNode, depth=0) -> List[Dict]:
    if node.type == "Program":
        return [reflect_ast(child, depth) for child in node.children]
    elif node.type == "Symbol":
        return {
            "symbol": node.value,
            "meaning": symbol_meanings.get(node.value, "unknown concept"),
            "depth": depth
        }
    elif node.type == "Group":
        return {
            "group": [reflect_ast(child, depth + 1) for child in node.children],
            "depth": depth
        }
    else:
        return {
            "error": f"Unknown node: {node.value}"
        }

def physis_reflect(code: str) -> Dict:
    tokens = tokenize(code)
    ast = build_ast(tokens)
    reflection = reflect_ast(ast)
    return {
        "input": code,
        "tokens": [token.value for token in tokens],
        "reflection": reflection
    }
