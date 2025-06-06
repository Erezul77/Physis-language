
from typing import List, Union
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

def execute_ast(node: ASTNode, depth=0) -> str:
    indent = "  " * depth
    if node.type == "Program":
        return "\n".join(execute_ast(child, depth) for child in node.children)
    elif node.type == "Symbol":
        return f"{indent}Reflecting symbol: {node.value}"
    elif node.type == "Group":
        result = f"{indent}Entering group:"
        for child in node.children:
            result += "\n" + execute_ast(child, depth + 1)
        return result
    else:
        return f"{indent}Unknown node: {node.value}"

def reflect_meaning(node, depth=0):
    indent = "  " * depth
    if node.type == "Program":
        return "\n".join(reflect_meaning(child, depth) for child in node.children)
    elif node.type == "Symbol":
        meaning = symbol_meanings.get(node.value, "unknown concept")
        return f"{indent}🧠 {node.value}: {meaning}"
    elif node.type == "Group":
        group_meanings = "\n".join(reflect_meaning(child, depth + 1) for child in node.children)
        return f"{indent}🔍 Group reflects:\n{group_meanings}"
    else:
        return f"{indent}❓ Unknown node: {node.value}"

def run_physis_repl():
    print("🌿 Welcome to the Physis Reflective REPL v0.2")
    print("Type symbolic Physis code like (🌱☯) and receive reflection. Type 'exit' to quit.\n")

    while True:
        code = input("PHYSIS > ")
        if code.strip().lower() in ['exit', 'quit']:
            print("👋 Goodbye, stay reflective.")
            break

        tokens = []
        for char in code:
            if char in ['(', ')']:
                tokens.append(Token("GROUP_START" if char == '(' else "GROUP_END", char))
            elif char.strip() != '':
                tokens.append(Token("SYMBOL", char))

        try:
            ast = build_ast(tokens)
            print("\n🔧 Structure:")
            print(execute_ast(ast))
            print("\n✨ Reflection:")
            print(reflect_meaning(ast))
            print()
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_physis_repl()
