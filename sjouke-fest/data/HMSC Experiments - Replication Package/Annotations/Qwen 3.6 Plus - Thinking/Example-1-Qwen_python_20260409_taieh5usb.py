from graphviz import Digraph

def create_lts():
    dot = Digraph(comment='LTS for MSC Example 1')
    dot.attr(rankdir='LR') # Left to Right layout
    dot.attr('node', shape='circle')

    # --- Prefix ---
    # States: s0 -> s1 -> s2 -> s3 -> s4
    dot.node('s0', 's0')
    dot.node('s1', 's1')
    dot.node('s2', 's2')
    dot.node('s3', 's3')
    dot.node('s4', 's4')

    dot.edge('s0', 's1', label='!m0')
    dot.edge('s1', 's2', label='!m1')
    dot.edge('s2', 's3', label='?m1')
    dot.edge('s3', 's4', label='!m2')

    # --- Concurrent Part (Grid) ---
    # Thread 1 events: a, !m4, ?m4
    # Thread 2 events: ?m2, !m3, ?m3
    
    # We create a grid of states starting from s4 (which is grid[0][0])
    # Dimensions: 4x4 (indices 0..3 for both)
    grid_nodes = {}
    
    # Create nodes
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                grid_nodes[(i,j)] = 's4'
            else:
                node_id = f'g{i}_{j}'
                # Label is just the ID for clarity, or we can leave it blank/numbered
                dot.node(node_id, f's{i*4+j+5}') 
                grid_nodes[(i,j)] = node_id

    # Create edges
    # Thread 1 events (moving right in grid logic, let's say x-axis)
    # Events: a, !m4, ?m4
    t1_events = ['a', '!m4', '?m4']
    
    # Thread 2 events (moving down in grid logic, let's say y-axis)
    # Events: ?m2, !m3, ?m3
    t2_events = ['?m2', '!m3', '?m3']

    for i in range(4):
        for j in range(4):
            current_node = grid_nodes[(i,j)]
            
            # Transition for Thread 1 (if not at end of T1)
            if i < 3:
                next_node = grid_nodes[(i+1, j)]
                dot.edge(current_node, next_node, label=t1_events[i])
            
            # Transition for Thread 2 (if not at end of T2)
            if j < 3:
                next_node = grid_nodes[(i, j+1)]
                dot.edge(current_node, next_node, label=t2_events[j])

    return dot

dot_graph = create_lts()
# dot_graph.render('lts_msc', format='png', cleanup=True)
# Since I cannot execute and show the file directly in this text block, 
# I will output the source code that generates it, 
# but the user asked for the picture. I will simulate the "picture" by providing the code 
# and describing the structure clearly, or better, I will assume the environment can render graphviz.
# Wait, I am an AI text model. I cannot "produce" a binary image file directly in the chat 
# unless I use a specific tool or describe it. 
# However, standard practice for these prompts is to provide the code to generate it 
# OR describe it. 
# BUT, looking at the prompt "Please produce one static picture", usually implies I should 
# try to generate it if I have capabilities. 
# I don't have an image generation tool active here that takes graphviz. 
# I will provide the Graphviz DOT code which is the standard way to represent this statically, 
# and explain that it renders to the picture.

print(dot_graph.source)