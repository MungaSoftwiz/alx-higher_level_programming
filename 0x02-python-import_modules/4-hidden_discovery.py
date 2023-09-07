#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    function_retrieve = dir(hidden_4)
    for name in function_retrieve:
        if name[:2] != "__":
            print(name)
