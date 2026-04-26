
from interpreter import tokenize, Parser, make_global_env, eval_node, ReturnSignal

def run_repl():
    env = make_global_env()
    print("shart REPL (type 'exit()' to quit)") # i cant stop laughing at ts name

    while True:
        try:
            user_input = input(">>> ")
            if user_input.strip() == "exit()":
                break
            if not user_input.strip():
                continue

            tokens = tokenize(user_input)
            #single expression
            parser = Parser(tokens)
            ast = parser.parse_program() # or parse_expression if we want to eval directly
            
            result = eval_node(ast, env)
            if result is not None:
                print(result)
        except SyntaxError as e:
            print(f"Syntax Error: {e}")
        except NameError as e:
            print(f"Name Error: {e}")
        except RuntimeError as e:
            print(f"Runtime Error: {e}")
        except ReturnSignal as e:
            print(f"Unexpected Return: {e.value}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_repl()
